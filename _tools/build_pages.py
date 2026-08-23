#!/usr/bin/env python3
"""Regenerate the workshop pages from _data/.

The site is hand-authored HTML inside .md files, which is how it was built and how
GitHub Pages serves it. This script keeps that, but drives the repetitive pages from
one data file so a talk, a speaker or a material link is edited in exactly one place.

  python3 _tools/build_pages.py

Reads   _data/schedule.json, _data/manuscripts.json
Writes  index.md
        workshop/schedule.md
        workshop/tutorials.md
        workshop/student-work.md
        workshop/ignition.md     (redirect)
        workshop/synthesis.md    (redirect)

workshop/method.md and workshop/gallery.md are hand-written and are NOT touched.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCHED = json.load(open(os.path.join(ROOT, "_data/schedule.json"), encoding="utf-8"))
PAPERS = json.load(open(os.path.join(ROOT, "_data/manuscripts.json"), encoding="utf-8"))
DAYS = SCHED["days"]

KIND_LABEL = {"lecture": "Lecture", "tutorial": "Tutorial", "method": "Research method"}

PHASES = [
    ("questions", "Week one", "Ignition: five questions",
     "Each day opens a live question in quantitative biology, with research talks in the "
     "morning and a hands-on studio in the afternoon."),
    ("sprint", "Week two", "Synthesis: research sprint",
     "Expert talk drops away almost entirely. Students work on their own questions, and "
     "the hours go to producing something."),
    ("finale", "Finale", "Demo day",
     "Final presentation. Team talks in the morning, posters after lunch, then the "
     "closing ceremony."),
]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def plural(n, suffix="s"):
    return "" if n == 1 else suffix


def hosted(talk):
    """Materials that are real files on this site: not dead links, not external URLs."""
    return [m for m in talk["materials"]
            if m["href"].strip() != "#" and not m["href"].startswith("http")]


def cal_label(day, n_files):
    """The small grey line under a day on the homepage calendar."""
    n = len(day["talks"])
    if not n:
        return day.get("cal_label", "No sessions")
    out = f"{n} talk{plural(n)}"
    if n_files:
        out += f" &middot; {n_files} file{plural(n_files)}"
    return out


def counts():
    talks = [t for d in DAYS for t in d["talks"]]
    return {
        "days": len(DAYS),
        "talks": len(talks),
        "lectures": sum(1 for t in talks if t["kind"] == "lecture"),
        "tutorials": sum(1 for t in talks if t["kind"] == "tutorial"),
        "files": sum(len(hosted(t)) for t in talks),
        "tutorial_files": sum(len(hosted(t)) for t in talks if t["kind"] == "tutorial"),
        "papers": len(PAPERS),
        "authors": len({a for p in PAPERS for a in p["authors"]}),
    }


C = counts()

# --------------------------------------------------------------------------- css
SHARED_CSS = """
  :root {
    --accent: #FF6C0C;
    --ink: #1f2937;
    --muted: #6b7280;
    --line: #e5e7eb;
    --soft: #f9fafb;
  }
  .wrap { max-width: 980px; margin: 0 auto; padding: 0 1.5rem; }
  .page-head { margin: 0 0 2.5rem; }
  .page-head h1 { font-size: 2rem; font-weight: 650; color: var(--ink); letter-spacing: -0.02em; }
  .page-head .lede { margin-top: 0.6rem; color: var(--muted); font-size: 1.05rem; max-width: 62ch; }
  .page-head .tally { margin-top: 1rem; font-size: 0.85rem; color: var(--muted); }
  .page-head .tally b { color: var(--ink); font-weight: 600; }

  .phase { margin: 0 0 3rem; }
  .phase-head { display: flex; align-items: baseline; gap: 0.75rem; flex-wrap: wrap;
                padding-bottom: 0.6rem; border-bottom: 2px solid var(--line); margin-bottom: 1.5rem; }
  .phase-head .tag { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.09em;
                     text-transform: uppercase; color: var(--accent); }
  .phase-head h2 { font-size: 1.3rem; font-weight: 620; color: var(--ink); }
  .phase-head p { flex-basis: 100%; margin: 0.35rem 0 0; color: var(--muted); font-size: 0.92rem; max-width: 68ch; }

  .day { display: grid; grid-template-columns: 8.5rem 1fr; gap: 1.5rem;
         padding: 1.4rem 0; border-bottom: 1px solid var(--line); }
  .day:last-child { border-bottom: 0; }
  .day-when { position: sticky; top: 1rem; align-self: start; }
  .day-when .d { font-size: 1.25rem; font-weight: 650; color: var(--ink); line-height: 1.15; }
  .day-when .wd { font-size: 0.8rem; color: var(--muted); }
  .day-theme { font-size: 1rem; font-weight: 600; color: var(--ink); }
  .day-desc { font-size: 0.88rem; color: var(--muted); margin: 0.3rem 0 0.9rem; max-width: 70ch; }
  .day-note { font-size: 0.88rem; color: var(--muted); background: var(--soft);
              border: 1px dashed var(--line); border-radius: 7px; padding: 0.7rem 0.9rem; }

  .item { padding: 0.6rem 0; border-top: 1px dashed var(--line); }
  .item:first-of-type { border-top: 0; padding-top: 0; }
  .item-head { display: flex; align-items: baseline; gap: 0.6rem; flex-wrap: wrap; }
  .item-title { font-weight: 550; color: var(--ink); }
  .item-by { font-size: 0.85rem; color: var(--muted); }
  .item-by a { color: var(--muted); text-decoration: none; border-bottom: 1px solid var(--line); }
  .item-by a:hover { color: var(--accent); border-color: var(--accent); }
  .kind { font-size: 0.63rem; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase;
          padding: 0.13rem 0.42rem; border-radius: 3px; white-space: nowrap; }
  .kind.lecture { background: #eef2ff; color: #4338ca; }
  .kind.tutorial { background: #ecfdf5; color: #047857; }
  .kind.method { background: #fff1e7; color: #c2410c; }

  .files { list-style: none; margin: 0.5rem 0 0; padding: 0;
           display: flex; flex-wrap: wrap; gap: 0.35rem; }
  .files li { margin: 0; }
  .files a { display: inline-block; font-size: 0.78rem; color: #374151; text-decoration: none;
             background: var(--soft); border: 1px solid var(--line); border-radius: 5px;
             padding: 0.22rem 0.5rem; transition: all 0.15s; word-break: break-word; }
  .files a:hover { border-color: var(--accent); color: var(--accent); background: #fff; }
  .files a.dead { opacity: 0.45; pointer-events: none; text-decoration: line-through; }
  .nofiles { font-size: 0.78rem; color: #9ca3af; margin-top: 0.35rem; }

  @media (max-width: 720px) {
    .day { grid-template-columns: 1fr; gap: 0.5rem; }
    .day-when { position: static; display: flex; align-items: baseline; gap: 0.5rem; }
  }
"""


def front(title, permalink, layout="page"):
    return f'---\nlayout: {layout}\ntitle: "{title}"\npermalink: {permalink}\n---\n\n'


def render_materials(talk):
    if not talk["materials"]:
        return '        <div class="nofiles">No materials posted.</div>\n'
    out = '        <ul class="files">\n'
    for m in talk["materials"]:
        href = m["href"]
        dead = href.strip() == "#"
        cls = ' class="dead"' if dead else ""
        label = esc(m["name"]) + (" (not uploaded)" if dead else "")
        out += f'          <li><a href="{href}"{cls}>{label}</a></li>\n'
    out += "        </ul>\n"
    return out


def render_talk(talk):
    by = ""
    if talk["speaker"]:
        if talk["speaker_url"]:
            by = (f'<span class="item-by">'
                  f'<a href="{talk["speaker_url"]}" target="_blank" rel="noopener">'
                  f'{esc(talk["speaker"])}</a></span>')
        else:
            by = f'<span class="item-by">{esc(talk["speaker"])}</span>'
    return (
        '      <div class="item">\n'
        '        <div class="item-head">\n'
        f'          <span class="kind {talk["kind"]}">{KIND_LABEL[talk["kind"]]}</span>\n'
        f'          <span class="item-title">{esc(talk["title"])}</span>\n'
        f'          {by}\n'
        '        </div>\n'
        + render_materials(talk) +
        '      </div>\n'
    )


def render_day(day):
    mm, dd = day["date"].split(".")
    out = (
        '    <section class="day" id="d' + day["date"].replace(".", "") + '">\n'
        '      <div class="day-when">\n'
        f'        <div class="d">{mm}.{dd}</div>\n'
        f'        <div class="wd">{day["weekday"]}</div>\n'
        '      </div>\n'
        '      <div class="day-body">\n'
        f'        <div class="day-theme">{esc(day["theme"])}</div>\n'
    )
    if day.get("description"):
        out += f'        <p class="day-desc">{esc(day["description"])}</p>\n'
    for t in day["talks"]:
        out += render_talk(t)
    if not day["talks"] and day.get("note"):
        out += f'        <div class="day-note">{esc(day["note"])}</div>\n'
    out += "      </div>\n    </section>\n"
    return out


# ------------------------------------------------------------------- schedule.md
def build_schedule():
    s = front("Schedule", "/workshop/schedule/")
    s += '<div class="wrap">\n\n'
    s += (
        '  <header class="page-head">\n'
        '    <h1>Schedule</h1>\n'
        '    <p class="lede">Every day of PEBBLE BioFusion 2026, in order, with the talks given '
        'and every file that goes with them. Week one asks five questions. Week two spends the '
        'hours on student work instead.</p>\n'
        f'    <p class="tally"><b>{C["days"]}</b> days &middot; <b>{C["talks"]}</b> talks &middot; '
        f'<b>{C["files"]}</b> downloadable files</p>\n'
        '  </header>\n\n'
    )
    for key, tag, name, blurb in PHASES:
        ds = [d for d in DAYS if d["phase"] == key]
        if not ds:
            continue
        s += ('  <div class="phase">\n'
              '    <div class="phase-head">\n'
              f'      <span class="tag">{tag}</span>\n'
              f'      <h2>{name}</h2>\n'
              f'      <p>{blurb}</p>\n'
              '    </div>\n')
        for d in ds:
            s += render_day(d)
        s += "  </div>\n\n"
    s += "</div>\n\n<style>\n" + SHARED_CSS + "</style>\n"
    return s


# ------------------------------------------------------------------ tutorials.md
def build_tutorials():
    tuts = [(d, t) for d in DAYS for t in d["talks"] if t["kind"] == "tutorial"]
    s = front("Tutorials", "/workshop/tutorials/")
    s += '<div class="wrap">\n\n'
    s += (
        '  <header class="page-head">\n'
        '    <h1>Tutorials &amp; materials</h1>\n'
        '    <p class="lede">The hands-on studio sessions, one card each. Slides, notebooks, data and '
        'worksheets, written by the teaching assistants and used during the camp. Everything here '
        'is downloadable and runs on its own.</p>\n'
        f'    <p class="tally"><b>{len(tuts)}</b> session{plural(len(tuts))} &middot; '
        f'<b>{sum(len(hosted(t)) for _, t in tuts)}</b> files</p>\n'
        '  </header>\n\n'
    )
    s += '  <div class="tut-grid">\n'
    for d, t in tuts:
        s += ('    <section class="tut">\n'
              '      <div class="tut-head">\n'
              f'        <h2>{esc(t["title"])}</h2>\n'
              f'        <div class="tut-meta">{esc(t["speaker"])} '
              f'<span class="dot">&middot;</span> '
              f'<a href="{{{{ site.baseurl }}}}/workshop/schedule/#d{d["date"].replace(".", "")}">'
              f'{d["date"]} {esc(d["theme"].split(":")[0])}</a></div>\n'
              '      </div>\n')
        s += render_materials(t).replace("        ", "      ")
        s += "    </section>\n"
    s += "  </div>\n\n</div>\n\n<style>\n" + SHARED_CSS + """
  .tut-grid { display: grid; gap: 1.1rem; }
  .tut { border: 1px solid var(--line); border-radius: 9px; padding: 1.1rem 1.25rem;
         transition: border-color 0.15s; }
  .tut:hover { border-color: #d1d5db; }
  .tut-head h2 { font-size: 1.02rem; font-weight: 600; color: var(--ink); margin: 0; }
  .tut-meta { font-size: 0.82rem; color: var(--muted); margin-top: 0.2rem; }
  .tut-meta a { color: var(--muted); text-decoration: none; border-bottom: 1px solid var(--line); }
  .tut-meta a:hover { color: var(--accent); border-color: var(--accent); }
  .tut-meta .dot { margin: 0 0.35rem; color: #d1d5db; }
</style>
"""
    return s


# --------------------------------------------------------------- student-work.md
def build_student_work():
    s = front("Student work", "/workshop/student-work/")
    s += '<div class="wrap">\n\n'
    s += (
        '  <header class="page-head">\n'
        '    <h1>Student work</h1>\n'
        '    <p class="lede">What the teams produced during the camp. Each entry is a manuscript '
        'written from scratch over the sprint week, with the poster or graphical abstract that '
        'went with it. Click a title for the PDF, or the image for the full-resolution version.</p>\n'
        f'    <p class="tally"><b>{C["papers"]}</b> manuscripts &middot; '
        f'<b>{C["authors"]}</b> student authors</p>\n'
        '  </header>\n\n'
        '  <div class="synthesis">\n'
    )
    for p in PAPERS:
        s += ('    <article class="paper-row">\n'
              '      <div class="paper-info">\n'
              f'        <a href="{p["pdf"]}" class="paper-title">{esc(p["title"])}</a>\n'
              f'        <div class="paper-meta">{esc(", ".join(p["authors"]))}</div>\n'
              '      </div>\n'
              f'      <a href="{p["image"]}" class="paper-poster" target="_blank">\n'
              f'        <img src="{p["image"]}" alt="{esc(p["title"])}" loading="lazy">\n'
              '      </a>\n'
              '    </article>\n')
    s += "  </div>\n\n</div>\n\n<style>\n" + SHARED_CSS + """
  .synthesis { display: grid; gap: 0; }
  .paper-row { display: grid; grid-template-columns: 1fr 190px; gap: 1.75rem;
               align-items: center; padding: 1.35rem 0; border-bottom: 1px solid var(--line); }
  .paper-row:last-child { border-bottom: 0; }
  .paper-title { display: block; font-size: 1.02rem; font-weight: 600; color: var(--ink);
                 text-decoration: none; line-height: 1.4; }
  .paper-title:hover { color: var(--accent); }
  .paper-meta { margin-top: 0.4rem; font-size: 0.85rem; color: var(--muted); }
  .paper-poster { display: block; border: 1px solid var(--line); border-radius: 7px;
                  overflow: hidden; background: var(--soft); transition: border-color 0.15s; }
  .paper-poster:hover { border-color: var(--accent); }
  .paper-poster img { width: 100%; height: 130px; object-fit: cover; display: block; }
  @media (max-width: 720px) {
    .paper-row { grid-template-columns: 1fr; gap: 0.85rem; }
    .paper-poster img { height: 170px; }
  }
</style>
"""
    return s


# --------------------------------------------------------------------- redirects
def build_redirect(title, old, new, note):
    return (
        f'---\nlayout: page\ntitle: "{title}"\npermalink: {old}\n---\n\n'
        f'<div class="wrap redirect-note">\n'
        f'  <h1>This page has moved</h1>\n'
        f'  <p>{note}</p>\n'
        f'  <p><a class="go" href="{{{{ site.baseurl }}}}{new}">Continue &rarr;</a></p>\n'
        f'</div>\n\n'
        f'<meta http-equiv="refresh" content="0; url={{{{ site.baseurl }}}}{new}">\n'
        f'<link rel="canonical" href="{{{{ site.baseurl }}}}{new}">\n\n'
        '<style>\n'
        '  .redirect-note { max-width: 640px; margin: 4rem auto; padding: 0 1.5rem; text-align: center; }\n'
        '  .redirect-note h1 { font-size: 1.5rem; font-weight: 620; color: #1f2937; }\n'
        '  .redirect-note p { margin-top: 0.85rem; color: #6b7280; }\n'
        '  .redirect-note .go { display: inline-block; margin-top: 0.5rem; padding: 0.55rem 1.1rem;\n'
        '    background: #FF6C0C; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 550; }\n'
        '</style>\n'
    )



# ------------------------------------------------------------------- index.md
def partial(name):
    with open(os.path.join(ROOT, "_tools/partials", name), encoding="utf-8") as fh:
        return fh.read()


HOME_INTRO = """
  <section class="about-section">

    <p class="intro">
      <strong>PEBBLE BioFusion 2026</strong> is designed from the ground up for the age of AI. We are
      not adding AI as a tool on top of a traditional curriculum. Instead, we are rethinking what a
      workshop should train when AI makes tutorials, literature review, coding, and draft generation
      available on demand. In this new landscape, three things become critically important:
    </p>

    <ul class="skills">
      <li>
        <span class="skill-name">Taste</span>
        <span class="skill-desc">the ability to ask deep, well-chosen questions. Which problems are alive? Which framings reveal new structure?</span>
      </li>
      <li>
        <span class="skill-name">Rigor</span>
        <span class="skill-desc">the ability to develop a full, in-depth chain of logic that tells a complete, convincing story.</span>
      </li>
      <li>
        <span class="skill-name">Courage</span>
        <span class="skill-desc">the willingness to ask bold questions, and the determination to pursue them all the way through.</span>
      </li>
    </ul>

    <p class="closing">
      These are precisely what AI does not reliably provide. They are what <strong>PEBBLE BioFusion</strong> trains.
    </p>

  </section>
"""


def build_index():
    s = "---\nlayout: default\n---\n\n"
    s += '<div class="pebble-home">\n\n'
    s += partial("carousel.html")
    s += HOME_INTRO

    # ---- what the camp produced, in real numbers
    s += '''
  <section class="stats" id="numbers">
    <a class="stat" href="{{ site.baseurl }}/workshop/schedule/">
      <div class="stat-number">%(talks)d</div><div class="stat-label">talks over %(days)d days</div></a>
    <a class="stat" href="{{ site.baseurl }}/workshop/tutorials/">
      <div class="stat-number">%(tutorials)d</div><div class="stat-label">tutorial sessions</div></a>
    <a class="stat" href="{{ site.baseurl }}/workshop/student-work/">
      <div class="stat-number">%(papers)d</div><div class="stat-label">student manuscripts</div></a>
    <a class="stat" href="{{ site.baseurl }}/workshop/student-work/">
      <div class="stat-number">%(authors)d</div><div class="stat-label">student authors</div></a>
  </section>
''' % C

    # ---- the calendar
    s += '''
  <section class="home-section" id="schedule">
    <div class="sec-head">
      <h2>The camp, day by day</h2>
      <a class="more" href="{{ site.baseurl }}/workshop/schedule/">Full schedule &rarr;</a>
    </div>
    <p class="sec-lede">Week one opens five live questions. Week two hands the hours over to the
    students. The last day is theirs to present. Every day below links to its talks and the files
    that go with them.</p>
    <div class="cal">
'''
    for key, tag, name, _ in PHASES:
        ds = [d for d in DAYS if d["phase"] == key]
        s += f'      <div class="cal-phase"><span>{tag}</span><b>{name}</b></div>\n'
        s += '      <div class="cal-row">\n'
        for d in ds:
            n_files = sum(len(hosted(t)) for t in d["talks"])
            mm, dd = d["date"].split(".")
            anchor = d["date"].replace(".", "")
            s += (f'        <a class="cal-day {key}" href="{{{{ site.baseurl }}}}/workshop/schedule/#d{anchor}">\n'
                  f'          <span class="cd">{mm}.{dd}</span>\n'
                  f'          <span class="cw">{d["weekday"][:3]}</span>\n'
                  f'          <span class="ct">{esc(d["theme"])}</span>\n'
                  f'          <span class="cn">{cal_label(d, n_files)}</span>\n        </a>\n')
        s += '      </div>\n'
    s += "    </div>\n  </section>\n"

    # ---- section cards
    s += '''
  <section class="home-section" id="explore">
    <div class="sec-head"><h2>Explore</h2></div>
    <div class="cards">
      <a class="card" href="{{ site.baseurl }}/workshop/method/">
        <span class="card-tag">Research with AI</span>
        <span class="card-title">The method we taught</span>
        <span class="card-desc">The four commandments for working with an AI agent, the PCAPS chain
        of logic, and a worked example carrying one idea from a sentence to a manuscript.</span>
      </a>
      <a class="card" href="{{ site.baseurl }}/workshop/tutorials/">
        <span class="card-tag">Tutorials</span>
        <span class="card-title">%(tutorials)d sessions, %(tutorial_files)d files</span>
        <span class="card-desc">Slides, notebooks, data and worksheets from the hands-on studios,
        written by the teaching assistants. Every file downloadable, each one runs on its own.</span>
      </a>
      <a class="card" href="{{ site.baseurl }}/workshop/student-work/">
        <span class="card-tag">Student work</span>
        <span class="card-title">%(papers)d manuscripts</span>
        <span class="card-desc">What the teams produced during the sprint week, with the posters and
        graphical abstracts that went with them.</span>
      </a>
      <a class="card" href="{{ site.baseurl }}/workshop/gallery/">
        <span class="card-tag">Gallery</span>
        <span class="card-title">The camp itself</span>
        <span class="card-desc">Photographs from the two weeks in Hangzhou.</span>
      </a>
    </div>
  </section>
''' % C

    s += "\n</div>\n\n<style>\n" + partial("carousel.css") + HOME_CSS + "</style>\n\n<script>\n" + partial("carousel.js") + "</script>\n"
    return s


HOME_CSS = """
  /* ===== Homepage sections ===== */
  .pebble-home { max-width: 980px; margin: 0 auto; padding: 0 1.5rem; }

  .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin: 2.5rem 0 0; }
  .stats .stat { display: block; text-align: center; padding: 1.1rem 0.6rem; border: 1px solid #e5e7eb;
    border-radius: 9px; text-decoration: none; transition: border-color 0.15s, transform 0.15s; }
  .stats .stat:hover { border-color: #FF6C0C; transform: translateY(-2px); }
  .stats .stat-number { font-size: 1.85rem; font-weight: 680; color: #1f2937; line-height: 1.1; }
  .stats .stat-label { font-size: 0.78rem; color: #6b7280; margin-top: 0.25rem; }

  .home-section { margin: 3.5rem 0 0; }
  .sec-head { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem;
    border-bottom: 2px solid #e5e7eb; padding-bottom: 0.55rem; }
  .sec-head h2 { font-size: 1.35rem; font-weight: 640; color: #1f2937; letter-spacing: -0.01em; }
  .sec-head .more { font-size: 0.86rem; color: #FF6C0C; text-decoration: none; font-weight: 550;
    white-space: nowrap; }
  .sec-head .more:hover { text-decoration: underline; }
  .sec-lede { margin-top: 0.85rem; color: #6b7280; font-size: 0.95rem; max-width: 66ch; }

  .cal { margin-top: 1.4rem; }
  .cal-phase { display: flex; align-items: baseline; gap: 0.6rem; margin: 1.3rem 0 0.7rem; }
  .cal-phase span { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.09em;
    text-transform: uppercase; color: #FF6C0C; }
  .cal-phase b { font-size: 0.95rem; font-weight: 600; color: #1f2937; }
  .cal-row { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 0.7rem; }
  .cal-day { display: flex; flex-direction: column; gap: 0.1rem; padding: 0.85rem 0.9rem;
    border: 1px solid #e5e7eb; border-radius: 8px; text-decoration: none; background: #fff;
    transition: border-color 0.15s, transform 0.15s, box-shadow 0.15s; }
  .cal-day:hover { border-color: #FF6C0C; transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 108, 12, 0.10); }
  .cal-day.sprint { background: #fffaf6; }
  .cal-day.finale { background: #fff3e9; border-color: #fbd5b5; }
  .cal-day .cd { font-size: 1.05rem; font-weight: 660; color: #1f2937; line-height: 1.15; }
  .cal-day .cw { font-size: 0.72rem; color: #9ca3af; }
  .cal-day .ct { font-size: 0.83rem; color: #374151; margin-top: 0.35rem; line-height: 1.35; }
  .cal-day .cn { font-size: 0.72rem; color: #9ca3af; margin-top: 0.4rem; }

  .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 0.9rem; margin-top: 1.4rem; }
  .card { display: flex; flex-direction: column; padding: 1.2rem; border: 1px solid #e5e7eb;
    border-radius: 9px; text-decoration: none; transition: border-color 0.15s, transform 0.15s; }
  .card:hover { border-color: #FF6C0C; transform: translateY(-2px); }
  .card-tag { font-size: 0.67rem; font-weight: 700; letter-spacing: 0.09em; text-transform: uppercase;
    color: #FF6C0C; }
  .card-title { font-size: 1.02rem; font-weight: 620; color: #1f2937; margin-top: 0.3rem; }
  .card-desc { font-size: 0.86rem; color: #6b7280; margin-top: 0.45rem; line-height: 1.55; }

  @media (max-width: 720px) {
    .stats { grid-template-columns: repeat(2, 1fr); }
  }
"""


def main():
    out = {
        "index.md": build_index(),
        "workshop/schedule.md": build_schedule(),
        "workshop/tutorials.md": build_tutorials(),
        "workshop/student-work.md": build_student_work(),
        "workshop/ignition.md": build_redirect(
            "Ignition", "/workshop/ignition/", "/workshop/schedule/",
            "Ignition is now <strong>Schedule</strong>: the same days and materials, "
            "in order, with everything visible."),
        "workshop/synthesis.md": build_redirect(
            "Synthesis", "/workshop/synthesis/", "/workshop/student-work/",
            "Synthesis is now <strong>Student work</strong>."),
    }
    for path, text in out.items():
        full = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {path}  ({len(text):,} bytes)")


if __name__ == "__main__":
    main()
