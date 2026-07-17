#!/usr/bin/env python3
"""Build a static, file://-friendly HTML navigator for reports/*.md."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
OUT = REPORTS / "index.html"

DOMAIN_LABELS = {
    "frontier-watch": "Frontier Watch",
    "agentic-coding": "Agentic Coding",
    "production-ai-eng": "Production AI Eng",
    "ai-economics": "AI Economics",
}

CSS = """
:root {
  --bg: #f3f1ec;
  --panel: #1c2430;
  --panel-2: #243041;
  --panel-border: #2f3d52;
  --text: #1a1f27;
  --muted: #6b7380;
  --panel-text: #d7dee8;
  --panel-muted: #8b96a8;
  --accent-soft: rgba(47, 111, 237, 0.14);
  --link: #1d5fd0;
  --rule: #ddd6cb;
  --shadow: 0 18px 50px rgba(28, 36, 48, 0.12);
}
* { box-sizing: border-box; }
html, body { height: 100%; }
body {
  margin: 0;
  font-family: "IBM Plex Sans", "Segoe UI", sans-serif;
  background:
    radial-gradient(1200px 500px at 10% -10%, #e8eef9 0%, transparent 55%),
    radial-gradient(900px 400px at 100% 0%, #efe8dc 0%, transparent 50%),
    var(--bg);
  color: var(--text);
}
.app { display: grid; grid-template-columns: 300px 1fr; min-height: 100%; }
.sidebar {
  position: sticky; top: 0; height: 100vh; overflow: auto;
  background: linear-gradient(180deg, var(--panel) 0%, #161d27 100%);
  color: var(--panel-text); padding: 1.4rem 1rem 2rem;
  border-right: 1px solid var(--panel-border);
}
.brand {
  display: flex; flex-direction: column; gap: 0.2rem;
  padding: 0.35rem 0.55rem 1.1rem; margin-bottom: 0.5rem;
  border-bottom: 1px solid var(--panel-border);
}
.brand strong { font-size: 1.15rem; letter-spacing: 0.02em; font-weight: 600; }
.brand span { color: var(--panel-muted); font-size: 0.8rem; }
.nav-section { margin-top: 1.15rem; }
.nav-section h2 {
  margin: 0 0 0.45rem; padding: 0 0.55rem;
  font-size: 0.68rem; font-weight: 600; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--panel-muted);
}
.nav-list { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 0.2rem; }
.nav-list a {
  display: block; padding: 0.55rem 0.65rem; border-radius: 8px;
  color: var(--panel-text); text-decoration: none; font-size: 0.9rem;
  line-height: 1.3; border: 1px solid transparent;
}
.nav-list a:hover { background: var(--panel-2); border-color: var(--panel-border); }
.nav-list a.active {
  background: var(--accent-soft); border-color: rgba(47, 111, 237, 0.35); color: #fff;
}
.nav-list .meta { display: block; margin-top: 0.15rem; color: var(--panel-muted); font-size: 0.72rem; }
.main { min-width: 0; display: flex; flex-direction: column; }
.toolbar {
  position: sticky; top: 0; z-index: 2;
  display: flex; align-items: center; justify-content: space-between; gap: 1rem;
  padding: 0.85rem 1.5rem;
  background: rgba(243, 241, 236, 0.88); backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--rule);
}
.toolbar-title {
  min-width: 0; font-size: 0.92rem; font-weight: 500; color: var(--muted);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.toolbar-actions { display: flex; gap: 0.5rem; flex-shrink: 0; }
.btn {
  appearance: none; border: 1px solid #cfc7ba; background: #fff; color: var(--text);
  border-radius: 8px; padding: 0.4rem 0.7rem; font: inherit; font-size: 0.82rem;
  text-decoration: none; display: inline-block;
}
.btn:hover { border-color: #a9b0bb; }
.btn.disabled { opacity: 0.45; pointer-events: none; }
.reader-wrap { padding: 1.25rem 1.5rem 3rem; }
.reader {
  max-width: 820px; margin: 0 auto; background: #fffdf9;
  border: 1px solid #e4ddd2; border-radius: 16px; box-shadow: var(--shadow);
  padding: 2rem 2.25rem 2.5rem;
}
.content {
  font-family: "Source Serif 4", "Iowan Old Style", Georgia, serif;
  font-size: 1.05rem; line-height: 1.7; color: #222831;
}
.content > *:first-child { margin-top: 0; }
.content h1, .content h2, .content h3, .content h4 {
  font-family: "IBM Plex Sans", "Segoe UI", sans-serif;
  line-height: 1.25; color: #141a22;
}
.content h1 { font-size: 1.85rem; margin: 0 0 1rem; }
.content h2 {
  font-size: 1.25rem; margin: 2rem 0 0.75rem; padding-top: 0.4rem;
  border-top: 1px solid var(--rule);
}
.content h2:first-of-type { border-top: 0; padding-top: 0; }
.content h3 { font-size: 1.05rem; margin: 1.4rem 0 0.5rem; }
.content p { margin: 0.85rem 0; }
.content ul, .content ol { padding-left: 1.3rem; }
.content li { margin: 0.35rem 0; }
.content a { color: var(--link); }
.content hr { border: 0; border-top: 1px solid var(--rule); margin: 1.5rem 0; }
.content code {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.86em; background: #f1ece3; padding: 0.1em 0.35em; border-radius: 4px;
}
.content pre {
  overflow: auto; background: #1c2430; color: #e8eef7;
  padding: 1rem; border-radius: 10px;
}
.content pre code { background: transparent; color: inherit; padding: 0; }
.content blockquote {
  margin: 1rem 0; padding: 0.2rem 0 0.2rem 1rem;
  border-left: 3px solid #c9d7f5; color: #4a5563;
}
.content table {
  width: 100%; border-collapse: collapse;
  font-family: "IBM Plex Sans", "Segoe UI", sans-serif;
  font-size: 0.92rem; margin: 1rem 0;
}
.content th, .content td {
  border: 1px solid var(--rule); padding: 0.5rem 0.65rem;
  text-align: left; vertical-align: top;
}
.content th { background: #f6f2ea; }
.menu-toggle {
  display: none; appearance: none; border: 1px solid #cfc7ba; background: #fff;
  border-radius: 8px; padding: 0.4rem 0.7rem; font: inherit; font-size: 0.82rem; cursor: pointer;
}
.panel { display: none; }
.panel.active { display: block; }
@media (max-width: 900px) {
  .app { grid-template-columns: 1fr; }
  .sidebar {
    position: fixed; inset: 0 auto 0 0; width: min(86vw, 320px); z-index: 5;
    transform: translateX(-105%); transition: transform 0.2s ease; box-shadow: var(--shadow);
  }
  body.nav-open .sidebar { transform: translateX(0); }
  .menu-toggle { display: inline-block; }
  .reader { padding: 1.35rem 1.15rem 1.75rem; border-radius: 12px; }
  .reader-wrap { padding: 1rem 0.85rem 2rem; }
  .toolbar { padding-left: 0.85rem; padding-right: 0.85rem; }
}
""".strip()


def strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


def inline_md(text: str) -> str:
    # Escape first, then re-introduce intentional markup via placeholders.
    text = html.escape(text)

    def code_span(m: re.Match[str]) -> str:
        return f"<code>{m.group(1)}</code>"

    text = re.sub(r"`([^`]+)`", code_span, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def md_to_html(md: str) -> str:
    lines = strip_front_matter(md).splitlines()
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False
    in_blockquote = False
    para: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def close_quote() -> None:
        nonlocal in_blockquote
        if in_blockquote:
            out.append("</blockquote>")
            in_blockquote = False

    def flush_para() -> None:
        nonlocal para
        if para:
            out.append("<p>" + inline_md(" ".join(para)) + "</p>")
            para = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # fenced code
        if stripped.startswith("```"):
            flush_para()
            close_lists()
            close_quote()
            lang = stripped[3:].strip()
            i += 1
            code_lines: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            code = html.escape("\n".join(code_lines))
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{code}</code></pre>")
            i += 1
            continue

        # blank
        if not stripped:
            flush_para()
            close_lists()
            close_quote()
            i += 1
            continue

        # horizontal rule
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            flush_para()
            close_lists()
            close_quote()
            out.append("<hr />")
            i += 1
            continue

        # headings
        hm = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if hm:
            flush_para()
            close_lists()
            close_quote()
            level = len(hm.group(1))
            out.append(f"<h{level}>{inline_md(hm.group(2))}</h{level}>")
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            flush_para()
            close_lists()
            quote_text = stripped.lstrip("> ").strip()
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append("<p>" + inline_md(quote_text) + "</p>")
            i += 1
            continue
        else:
            close_quote()

        # unordered list
        um = re.match(r"^[-*+]\s+(.*)$", stripped)
        if um:
            flush_para()
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append("<li>" + inline_md(um.group(1)) + "</li>")
            i += 1
            continue

        # ordered list
        om = re.match(r"^\d+\.\s+(.*)$", stripped)
        if om:
            flush_para()
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append("<li>" + inline_md(om.group(1)) + "</li>")
            i += 1
            continue

        # table (simple GFM)
        if "|" in stripped and i + 1 < len(lines) and re.match(
            r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[i + 1]
        ):
            flush_para()
            close_lists()
            close_quote()

            def split_row(row: str) -> list[str]:
                row = row.strip().strip("|")
                return [c.strip() for c in row.split("|")]

            header = split_row(stripped)
            i += 2
            body_rows: list[list[str]] = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                body_rows.append(split_row(lines[i]))
                i += 1
            out.append("<table><thead><tr>")
            for cell in header:
                out.append(f"<th>{inline_md(cell)}</th>")
            out.append("</tr></thead><tbody>")
            for row in body_rows:
                out.append("<tr>")
                for cell in row:
                    out.append(f"<td>{inline_md(cell)}</td>")
                out.append("</tr>")
            out.append("</tbody></table>")
            continue

        # continuation / paragraph
        if in_ul or in_ol:
            # treat as new paragraph outside list
            close_lists()
        para.append(stripped)
        i += 1

    flush_para()
    close_lists()
    close_quote()
    return "\n".join(out)


def rewrite_md_links(fragment: str, current_path: str, slug_for: dict[str, str]) -> str:
    """Point relative .md hrefs at in-page anchors."""

    def repl(m: re.Match[str]) -> str:
        href = m.group(1)
        if re.match(r"^(https?:|mailto:|#)", href, re.I):
            return m.group(0)
        if not href.endswith(".md"):
            return m.group(0)
        base = current_path.rsplit("/", 1)[0] + "/" if "/" in current_path else ""
        # resolve relative path
        parts: list[str] = []
        for p in (base + href).split("/"):
            if p in ("", "."):
                continue
            if p == "..":
                if parts:
                    parts.pop()
            else:
                parts.append(p)
        target = "/".join(parts)
        slug = slug_for.get(target)
        if not slug:
            return m.group(0)
        return f'href="#{slug}"'

    return re.sub(r'href="([^"]+)"', repl, fragment)


def collect_catalog() -> list[tuple[str, list[tuple[str, str, str]]]]:
    sections: list[tuple[str, list[tuple[str, str, str]]]] = [
        ("Start here", [("weekly-digest.md", "Weekly digest", "All domains")])
    ]

    for domain, label in DOMAIN_LABELS.items():
        d = REPORTS / domain
        if not d.is_dir():
            continue
        items: list[tuple[str, str, str]] = []
        for p in sorted(d.glob("*-news-*.md"), reverse=True):
            date = p.stem.split("-news-")[-1]
            items.append((f"{domain}/{p.name}", f"News — {date}", "Delta report"))
        for p in d.glob("*-state-of-the-art.md"):
            items.append((f"{domain}/{p.name}", "State of the art", "Standing briefing"))
        if items:
            sections.append((label, items))

    extra = []
    for p in sorted(REPORTS.glob("*.md")):
        if p.name == "weekly-digest.md":
            continue
        extra.append((p.name, p.stem.replace("-", " ").title(), "Report"))
    if extra:
        sections.append(("Other", extra))

    audits = REPORTS / "source-audits"
    if audits.is_dir():
        audit_items = [
            (f"source-audits/{p.name}", p.stem, "Source audit")
            for p in sorted(audits.glob("*.md"), reverse=True)
        ]
        if audit_items:
            sections.append(("Source audits", audit_items))

    return sections


def slugify(path: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", path).strip("-").lower()


def build() -> None:
    sections = collect_catalog()
    flat = [item for _, items in sections for item in items]
    slug_for = {path: slugify(path) for path, _, _ in flat}

    panels: list[str] = []
    for idx, (path, label, _meta) in enumerate(flat):
        md_path = REPORTS / path
        if not md_path.exists():
            body = f"<p>Missing file: <code>{html.escape(path)}</code></p>"
        else:
            body = md_to_html(md_path.read_text(encoding="utf-8"))
            body = rewrite_md_links(body, path, slug_for)

        slug = slug_for[path]
        prev_slug = slug_for[flat[idx - 1][0]] if idx > 0 else ""
        next_slug = slug_for[flat[idx + 1][0]] if idx < len(flat) - 1 else ""
        panels.append(
            f'<section class="panel" id="{html.escape(slug)}" '
            f'data-path="{html.escape(path)}" data-label="{html.escape(label)}" '
            f'data-prev="{html.escape(prev_slug)}" data-next="{html.escape(next_slug)}">'
            f'<div class="content">{body}</div></section>'
        )

    nav_bits: list[str] = []
    for section, items in sections:
        links = []
        for path, label, meta in items:
            slug = slug_for[path]
            links.append(
                f'<li><a href="#{slug}" data-slug="{slug}">'
                f"{html.escape(label)}"
                f'<span class="meta">{html.escape(meta)}</span></a></li>'
            )
        nav_bits.append(
            f'<div class="nav-section"><h2>{html.escape(section)}</h2>'
            f'<ul class="nav-list">{"".join(links)}</ul></div>'
        )

    default_slug = slug_for[flat[0][0]] if flat else ""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Radar Reports</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet" />
  <style>
{CSS}
  </style>
</head>
<body>
  <div class="app">
    <aside class="sidebar" id="sidebar">
      <div class="brand">
        <strong>Radar</strong>
        <span>Report browser · open this file directly</span>
      </div>
      <nav id="nav">
{"".join(nav_bits)}
      </nav>
    </aside>
    <main class="main">
      <div class="toolbar">
        <div style="display:flex; align-items:center; gap:0.6rem; min-width:0;">
          <button class="menu-toggle" id="menuToggle" type="button">Menu</button>
          <div class="toolbar-title" id="toolbarTitle">Radar Reports</div>
        </div>
        <div class="toolbar-actions">
          <a class="btn disabled" id="prevBtn" href="#">← Prev</a>
          <a class="btn disabled" id="nextBtn" href="#">Next →</a>
        </div>
      </div>
      <div class="reader-wrap">
        <article class="reader" id="reader">
{"".join(panels)}
        </article>
      </div>
    </main>
  </div>
  <script>
    const defaultSlug = {default_slug!r};
    const titleEl = document.getElementById("toolbarTitle");
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");
    const menuToggle = document.getElementById("menuToggle");

    function currentSlug() {{
      return decodeURIComponent(location.hash.replace(/^#/, "")) || defaultSlug;
    }}

    function show(slug) {{
      const panels = document.querySelectorAll(".panel");
      let active = null;
      panels.forEach((p) => {{
        const on = p.id === slug;
        p.classList.toggle("active", on);
        if (on) active = p;
      }});
      if (!active && panels.length) {{
        active = panels[0];
        active.classList.add("active");
        slug = active.id;
      }}
      document.querySelectorAll(".nav-list a").forEach((a) => {{
        a.classList.toggle("active", a.getAttribute("data-slug") === slug);
      }});
      if (active) {{
        titleEl.textContent = active.dataset.label + " · " + active.dataset.path;
        const prev = active.dataset.prev;
        const next = active.dataset.next;
        prevBtn.href = prev ? "#" + prev : "#";
        nextBtn.href = next ? "#" + next : "#";
        prevBtn.classList.toggle("disabled", !prev);
        nextBtn.classList.toggle("disabled", !next);
      }}
      document.body.classList.remove("nav-open");
      window.scrollTo(0, 0);
    }}

    menuToggle.addEventListener("click", () => {{
      document.body.classList.toggle("nav-open");
    }});

    document.addEventListener("keydown", (e) => {{
      if (e.target.matches("input, textarea")) return;
      if (e.key === "ArrowLeft" && !prevBtn.classList.contains("disabled")) prevBtn.click();
      if (e.key === "ArrowRight" && !nextBtn.classList.contains("disabled")) nextBtn.click();
    }});

    window.addEventListener("hashchange", () => show(currentSlug()));
    show(currentSlug());
  </script>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(flat)} reports, no server needed)")


if __name__ == "__main__":
    build()
