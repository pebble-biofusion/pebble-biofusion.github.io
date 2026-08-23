---
layout: page
title: "Research with AI"
permalink: /workshop/method/
---

<div class="wrap">

  <header class="page-head">
    <h1>Research with AI</h1>
    <p class="lede">PEBBLE BioFusion is built for a world where AI writes the tutorial, finds the
    paper, drafts the code and produces a first draft on demand. That changes what a research
    workshop should teach. This page collects what we taught about the practice itself: the stance
    to take toward an agent, the scaffold for telling it what you want, and a worked example of
    carrying one idea from a sentence to a manuscript.</p>
    <p class="tally">All materials below were delivered during the 2026 camp. Dates are the session
    they were given in.</p>
  </header>

  <!-- ============================================================ stance -->
  <section class="method-block">
    <div class="method-head">
      <span class="tag">The stance</span>
      <h2>Commandments of Research-with-AI</h2>
      <div class="when">Delivered <a href="{{ site.baseurl }}/workshop/schedule/#d0726">07.26, Q2 night</a> &middot; Fangzhou Xiao</div>
    </div>

    <p>An agent output is not research. It becomes research when a human can understand it, defend
    it and communicate it. Four rules fix how a researcher stands relative to an AI agent.</p>

    <ol class="commandments">
      <li>
        <b>AI is our minion, not our peer.</b>
        <span>Own every claim, or do not use it. If you cannot explain it, it is vapor.</span>
      </li>
      <li>
        <b>AI is a cyber-arm.</b>
        <span>Attach it to the work you care about most, not the chores you dislike. If an idea is
        active in your mind, put it into the loop before it cools.</span>
      </li>
      <li>
        <b>Your input&ndash;output bandwidth is the bottleneck.</b>
        <span>Not the model's power. Specification in, comprehension out. If the channel is narrow,
        widen the channel.</span>
      </li>
      <li>
        <b>Be above AI on everything you think about.</b>
        <span>Generic AI output is the floor, not the ceiling. Know the generic answer before
        claiming your own expertise.</span>
      </li>
    </ol>

    <p>Seven working habits sit under the four rules: keep files at three zoom levels, give feedback
    on the spine rather than the details, never fear a fresh start, ask for figure snippets rather
    than finished slides, fix one palette and plot style, keep a local library of full texts, and
    keep the context window fresh.</p>

    <ul class="files">
      <li><a href="{{ site.baseurl }}/workshop/materials/Commandments_of_Research_with_AI_v8-improved.pdf">Commandments_of_Research_with_AI_v8-improved.pdf</a></li>
    </ul>
  </section>

  <!-- ============================================================ scaffold -->
  <section class="method-block">
    <div class="method-head">
      <span class="tag">The scaffold</span>
      <h2>PCAPS, and a story that spreads</h2>
      <div class="when">Delivered <a href="{{ site.baseurl }}/workshop/schedule/#d0725">07.25, Q1</a> &middot; Fangzhou Xiao</div>
    </div>

    <p>A specification an agent can act on has the same shape as a scientific story worth hearing.
    PCAPS is that shape, five links in one chain of logic.</p>

    <dl class="pcaps">
      <dt>P<span>roblem</span></dt><dd>What are you tackling?</dd>
      <dt>C<span>hallenge</span></dt><dd>Why is it not solved yet?</dd>
      <dt>A<span>pproach</span></dt><dd>What is your take, and why?</dd>
      <dt>P<span>roof</span></dt><dd>What evidence shows it works?</dd>
      <dt>S<span>ignificance</span></dt><dd>What is the contribution, and who cares?</dd>
    </dl>

    <ul class="files">
      <li><a href="{{ site.baseurl }}/workshop/materials/202607-PEBBLE-PCAPS-seed.pdf">202607-PEBBLE-PCAPS-seed.pdf</a></li>
    </ul>
  </section>

  <!-- ============================================================ worked example -->
  <section class="method-block">
    <div class="method-head">
      <span class="tag">The worked example</span>
      <h2>From a story to a publishable paper</h2>
      <div class="when">Delivered <a href="{{ site.baseurl }}/workshop/schedule/#d0725">07.25, Q1</a> &middot; Fangzhou Xiao</div>
    </div>

    <p>A deep dive into AI-native research, run as a live demonstration rather than a lecture. One
    hypothesis in one sentence, carried round by round to a manuscript with simulations and figures,
    with the whole trajectory kept rather than tidied away. Every round in the public repository
    records the prompts that drove it, so the process is visible and not just the result.</p>

    <p class="aside">The idea: the composition of a microbial community is set in large part by a
    parameter almost everyone treats as a fixed protocol detail, the serial-dilution interval.</p>

    <ul class="files">
      <li><a href="https://github.com/chemaoxfz/pebble-from-story-to-paper" target="_blank" rel="noopener">github.com/chemaoxfz/pebble-from-story-to-paper</a></li>
      <li><a href="https://github.com/chemaoxfz/idea-to-essay" target="_blank" rel="noopener">github.com/chemaoxfz/idea-to-essay &mdash; the literature-to-essay procedure, as an open skill</a></li>
    </ul>
  </section>

  <!-- ============================================================ design -->
  <section class="method-block design">
    <div class="method-head">
      <span class="tag">The design</span>
      <h2>Why the camp is shaped this way</h2>
    </div>

    <p>AI has made expert explanation cheap and available on demand. A camp in 2026 that spends its
    hours transmitting explanation is selling something its students can already get. So the
    schedule moves the hours: week one opens five live questions with research talks and hands-on
    studios, and week two hands the time over to the students to work on questions of their own.
    <a href="{{ site.baseurl }}/workshop/schedule/">The schedule</a> shows the shift, and
    <a href="{{ site.baseurl }}/workshop/student-work/">Student work</a> shows what came out of it.</p>

    <p>What AI does not reliably supply is what the camp trains: <b>taste</b>, the ability to ask a
    deep and well-chosen question; <b>rigor</b>, the ability to build a chain of logic that holds;
    and <b>courage</b>, the willingness to pursue a bold question all the way through.</p>
  </section>

</div>

<style>
  :root {
    --accent: #FF6C0C;
    --ink: #1f2937;
    --muted: #6b7280;
    --line: #e5e7eb;
    --soft: #f9fafb;
  }
  .wrap { max-width: 820px; margin: 0 auto; padding: 0 1.5rem; }
  .page-head { margin: 0 0 3rem; }
  .page-head h1 { font-size: 2rem; font-weight: 650; color: var(--ink); letter-spacing: -0.02em; }
  .page-head .lede { margin-top: 0.7rem; color: #4b5563; font-size: 1.05rem; line-height: 1.65; }
  .page-head .tally { margin-top: 1rem; font-size: 0.85rem; color: var(--muted); }

  .method-block { padding: 1.9rem 0; border-top: 1px solid var(--line); }
  .method-block p { margin-top: 0.9rem; color: #374151; line-height: 1.7; }
  .method-head { margin-bottom: 0.4rem; }
  .method-head .tag { display: inline-block; font-size: 0.68rem; font-weight: 700;
    letter-spacing: 0.09em; text-transform: uppercase; color: var(--accent); }
  .method-head h2 { font-size: 1.4rem; font-weight: 620; color: var(--ink); margin-top: 0.25rem;
    letter-spacing: -0.01em; }
  .method-head .when { font-size: 0.83rem; color: var(--muted); margin-top: 0.3rem; }
  .method-head .when a { color: var(--muted); border-bottom: 1px solid var(--line); text-decoration: none; }
  .method-head .when a:hover { color: var(--accent); border-color: var(--accent); }

  .commandments { list-style: none; counter-reset: c; margin: 1.3rem 0 0; padding: 0; }
  .commandments li { counter-increment: c; position: relative; padding: 0.75rem 0 0.75rem 2.6rem;
    border-top: 1px dashed var(--line); }
  .commandments li:first-child { border-top: 0; }
  .commandments li::before { content: counter(c, upper-roman); position: absolute; left: 0; top: 0.78rem;
    font-size: 0.8rem; font-weight: 700; color: var(--accent); letter-spacing: 0.04em; }
  .commandments b { display: block; color: var(--ink); font-weight: 600; }
  .commandments span { display: block; margin-top: 0.15rem; color: var(--muted); font-size: 0.93rem; }

  .pcaps { display: grid; grid-template-columns: auto 1fr; gap: 0.45rem 1.1rem; margin: 1.3rem 0 0;
    align-items: baseline; }
  .pcaps dt { font-weight: 700; color: var(--accent); font-size: 1.02rem; }
  .pcaps dt span { color: var(--ink); font-weight: 600; font-size: 0.9rem; }
  .pcaps dd { margin: 0; color: var(--muted); font-size: 0.93rem; }

  .aside { border-left: 3px solid var(--line); padding-left: 1rem; color: var(--muted) !important;
    font-size: 0.93rem; }

  .files { list-style: none; margin: 1.2rem 0 0; padding: 0; display: flex; flex-wrap: wrap; gap: 0.4rem; }
  .files a { display: inline-block; font-size: 0.8rem; color: #374151; text-decoration: none;
    background: var(--soft); border: 1px solid var(--line); border-radius: 5px;
    padding: 0.3rem 0.6rem; transition: all 0.15s; word-break: break-word; }
  .files a:hover { border-color: var(--accent); color: var(--accent); background: #fff; }

  .design { border-bottom: 1px solid var(--line); }
  .design a { color: var(--accent); text-decoration: none; border-bottom: 1px solid #fcd9c0; }
  .design a:hover { border-color: var(--accent); }
</style>
