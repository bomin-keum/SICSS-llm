import json

with open("/sessions/lucid-epic-goodall/mnt/outputs/report_data_v2.json") as f:
    D = json.load(f)

exp0 = D["exp0"]; exp1 = D["exp1"]; exp2 = D["exp2"]; exp3 = D["exp3"]; exp4 = D["exp4"]
DIMS = D["dims"]

data_json = json.dumps({"exp0": exp0, "exp1": exp1, "exp2": exp2, "exp3": exp3, "exp4": exp4, "dims": DIMS})

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Measuring the Unmeasurable? | SICSS 2026</title>
<script src="https://cdn.jsdelivr.net/npm/plotly.js-dist-min@2.35.2/plotly.min.js"></script>
<style>
  :root {
    --bg: #000000;
    --panel: #0a0d16;
    --panel2: #0e1220;
    --border: #1b2436;
    --text: #eef1f8;
    --muted: #7d8699;
    --accent: #2563eb;
    --accent2: #38bdf8;
    --gemma: #38bdf8;
    --grok: #6366f1;
    --font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: radial-gradient(circle at 10% 0%, #0a0d18 0%, #000000 55%);
    color: var(--text);
    font-family: var(--font);
    line-height: 1.55;
  }
  .wrap { max-width: 1180px; margin: 0 auto; padding: 0 28px 100px; }
  header.hero {
    padding: 72px 28px 40px;
    text-align: center;
    border-bottom: 1px solid var(--border);
    margin-bottom: 56px;
  }
  .kicker {
    text-transform: uppercase;
    letter-spacing: .18em;
    font-size: 12.5px;
    color: var(--accent2);
    font-weight: 600;
  }
  h1.title {
    font-size: 2.4rem;
    line-height: 1.2;
    margin: 14px auto 12px;
    max-width: 820px;
    font-weight: 700;
    letter-spacing: -0.01em;
  }
  .subtitle { color: var(--muted); font-size: 1.05rem; max-width: 720px; margin: 0 auto; }
  .authors {
    margin-top: 26px;
    display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 26px;
    font-size: 13px; color: var(--muted);
  }
  .authors .who { color: var(--text); font-weight: 600; }
  .authors .aff { color: var(--muted); }
  section { margin-bottom: 64px; }
  .section-head { margin-bottom: 22px; }
  .eyebrow {
    font-size: 12.5px; text-transform: uppercase; letter-spacing: .14em;
    color: var(--accent2); font-weight: 700; margin-bottom: 8px;
  }
  h2 { font-size: 1.6rem; margin: 0 0 8px; font-weight: 700; }
  .section-desc { color: var(--muted); font-size: .97rem; }
  .why-copy p { color: #c7cdde; font-size: 1rem; margin: 0 0 16px; }
  .why-copy p:last-child { margin-bottom: 0; }
  .why-copy strong { color: var(--text); }

  .stat-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-top: 28px;
  }
  .stat-card {
    background: var(--panel); border: 1px solid var(--border); border-radius: 14px;
    padding: 18px 20px; text-align: left;
  }
  .stat-card .exp-tag {
    font-size: 11px; text-transform: uppercase; letter-spacing: .1em; font-weight: 700;
    color: var(--accent2); margin-bottom: 8px;
  }
  .stat-card .num { font-size: 1.9rem; font-weight: 700; color: var(--text); }
  .stat-card .lbl { color: var(--muted); font-size: 12.5px; margin-top: 4px; }

  table.desc-table { width: 100%; border-collapse: collapse; background: var(--panel); border-radius: 14px; overflow: hidden; border: 1px solid var(--border); margin-top: 28px; }
  table.desc-table th, table.desc-table td { padding: 14px 16px; text-align: left; border-bottom: 1px solid var(--border); font-size: .92rem; }
  table.desc-table th { background: var(--panel2); color: var(--muted); font-weight: 600; text-transform: uppercase; font-size: 11.5px; letter-spacing: .06em;}
  table.desc-table tr:last-child td { border-bottom: none; }
  table.desc-table td.rowlabel { font-weight: 700; color: var(--text); }
  table.desc-table td .sub { color: var(--muted); font-size: 12px; display:block; margin-top:2px; }
  .tag-gemma { color: var(--gemma); font-weight: 700; }
  .tag-grok { color: var(--grok); font-weight: 700; }
  .mdl-gemma { color: var(--gemma); font-weight: 700; }
  .mdl-grok { color: var(--grok); font-weight: 700; }

  .panel { background: var(--panel); border: 1px solid var(--border); border-radius: 16px; padding: 24px; }

  .callout {
    background: linear-gradient(135deg, rgba(37,99,235,.2), rgba(56,189,248,.09));
    border: 1px solid var(--border);
    border-left: 4px solid var(--accent2);
    border-radius: 0 16px 16px 0;
    padding: 24px 28px;
    margin-top: 28px;
  }
  .callout-mark { font-size: 1.15rem; font-weight: 800; color: var(--accent2); line-height: 1; margin-bottom: 12px; letter-spacing: .02em; }
  .callout h3 { margin: 0 0 12px; font-size: 1.15rem; }
  .callout ol, .callout ul { margin: 0; padding-left: 20px; color: var(--text); font-size: 1rem; font-weight: 500; }
  .callout li { margin-bottom: 10px; }
  .callout li:last-child { margin-bottom: 0; }
  .callout p { margin: 0; color: var(--text); font-size: 1rem; font-weight: 500; }
  .callout p + p { margin-top: 10px; }

  .subsection {
    margin-top: 40px;
    padding-top: 32px;
    border-top: 1px solid var(--border);
  }
  .mini-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }

  h3.sub-title { font-size: 1.15rem; margin: 0 0 12px; font-weight: 700; }

  .tendency-block { margin-top: 16px; }
  .tendency { font-size: .92rem; margin: 6px 0; }
  .tendency strong { font-weight: 700; }
  .legend-note { color: var(--muted); font-size: 12px; margin-bottom: 14px; }

  /* Pipeline / sample provenance visualization */
  .pipeline { display: flex; align-items: center; gap: 10px; margin-top: 28px; flex-wrap: wrap; }
  .pipe-box {
    background: var(--panel); border: 1px solid var(--border); border-radius: 14px;
    padding: 18px 20px; flex: 1 1 200px; min-width: 190px;
  }
  .pipe-box .big { font-size: 1.5rem; font-weight: 700; color: var(--accent2); }
  .pipe-box .lbl { color: var(--muted); font-size: 12.5px; margin-top: 6px; line-height: 1.45; }
  .pipe-box .lbl .sub { display: block; margin-top: 4px; color: #8b93a8; }
  .pipe-arrow { color: var(--muted); font-size: 1.3rem; flex: 0 0 auto; }
  .pipe-box.wide { flex: 1.4 1 260px; }
  .pipe-exps { list-style: none; margin: 6px 0 0; padding: 0; color: var(--muted); font-size: 11.5px; line-height: 1.7; }
  .pipe-exps li span { color: var(--accent2); font-weight: 700; }

  /* Exp 4 dimension groups */
  .dim-groups { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 22px; }
  .dim-group h4 { font-size: .76rem; text-transform: uppercase; letter-spacing: .08em; color: var(--accent2); margin: 0 0 10px; }
  .dim-group ol { margin: 0; padding-left: 18px; color: var(--muted); font-size: .84rem; }
  .dim-group li { margin-bottom: 7px; color: var(--text); }
  .decision-rule { color: var(--muted); font-size: .9rem; margin-top: 20px; }
  .decision-rule strong { color: var(--text); }

  table.sample-table { width: 100%; border-collapse: collapse; background: var(--panel); border-radius: 14px; overflow: hidden; border: 1px solid var(--border); table-layout: fixed; }
  table.sample-table th, table.sample-table td { padding: 12px 14px; text-align: left; border-bottom: 1px solid var(--border); font-size: .84rem; vertical-align: top; overflow-wrap: anywhere; word-break: break-word; }
  table.sample-table th { background: var(--panel2); color: var(--muted); font-weight: 600; text-transform: uppercase; font-size: 10.5px; letter-spacing: .05em; }
  table.sample-table tr:last-child td { border-bottom: none; }
  table.sample-table td.excerpt { color: #c7cdde; font-style: italic; }
  table.sample-table td.score { font-weight: 700; text-align: center; white-space: nowrap; }
  table.sample-table td.just { color: var(--muted); }

  .fail-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-top: 24px; }
  .fail-card { background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 20px; }
  .fail-card.wide { grid-column: 1 / -1; }
  .fail-card .n { color: var(--accent2); font-weight: 800; font-size: 12.5px; letter-spacing: .08em; }
  .fail-card h4 { margin: 6px 0 8px; font-size: 1.02rem; }
  .fail-card p { margin: 0; color: var(--muted); font-size: .89rem; }
  .fail-card .ex { margin-top: 10px; font-size: .82rem; color: #c7cbe0; background: var(--panel2); border-radius: 8px; padding: 8px 10px; border-left: 3px solid var(--accent); }
  .fail-card .ex + .ex { margin-top: 8px; }

  footer { border-top: 1px solid var(--border); padding-top: 30px; color: var(--muted); font-size: .85rem; text-align:center; }
  footer a { color: var(--accent2); }

  @media (max-width: 860px) {
    .stat-grid { grid-template-columns: repeat(2,1fr); }
    .mini-grid { grid-template-columns: 1fr; }
    .fail-grid { grid-template-columns: 1fr; }
    .fail-card.wide { grid-column: auto; }
    .dim-groups { grid-template-columns: 1fr; }
    table.sample-table { display: block; overflow-x: auto; }
    .pipeline { flex-direction: column; align-items: stretch; }
    .pipe-arrow { transform: rotate(90deg); text-align: center; }
    h1.title { font-size: 1.9rem; }
  }
</style>
</head>
<body>

<header class="hero">
  <div class="kicker">SICSS 2026 &middot; University of Washington</div>
  <h1 class="title">Measuring the Unmeasurable?</h1>
  <div class="subtitle">Auditing and Optimization of LLM-Based Text Classification in the Social Sciences.</div>
  <div class="authors">
    <span><span class="who">Bo Min Keum</span> &middot; <span class="aff">International CyberCrime Research Institute, SFU</span></span>
    <span><span class="who">Roman Pomeshchikov</span> &middot; <span class="aff">Near and Middle Eastern Studies (NMES) Interdisciplinary Program, UW</span></span>
  </div>
</header>

<div class="wrap">

  <section id="why">
    <div class="section-head">
      <div class="eyebrow">01 &middot; First: Why?</div>
      <h2>&ldquo;Nuance&rdquo; is hard to measure.</h2>
    </div>
    <div class="why-copy">
      <p>Generative LLMs are increasingly used to classify text. In the social sciences, this may involve very abstract concepts like masculinity, populism, and grievance. Human coders can read nuance, but they don't scale to hundreds of thousands of posts: a struggle we experience in our own PhD research on online radicalization discourse (Bo Min Keum) and political discourse (Roman Pomeshchikov). But while LLMs scale, we don't know how good LLMs are for such tasks. LLM-generated labels require extensive human validation, which is time-consuming and resource-heavy. Given this, we come up with a strategy for auditing LLM-labelling in ways that could inform <strong>how best we can use LLMs for measuring nuance in text</strong>.</p>
      <p>Given that the generative LLM labeling process inherently works on prompting, and prompting affects measurement, <strong>we made the prompting itself the object of our study</strong>. Further, <strong>we propose a high-disagreement sampling and analysis approach as an audit-optimization strategy:</strong> rather than validating every label across hundreds of thousands of texts by hand, we focus on the texts where the models disagree most.</p>
    </div>
  </section>

  <section id="overview">
    <div class="section-head">
      <div class="eyebrow">02 &middot; Overview</div>
    </div>
    <div class="pipeline">
      <div class="pipe-box"><div class="big">383K</div><div class="lbl">StormFront.org posts<span class="sub">LLM-labeled on 6 radicalization signals, 0&ndash;3 scale each</span></div></div>
      <div class="pipe-arrow">&rarr;</div>
      <div class="pipe-box"><div class="big">1.7K</div><div class="lbl">High-disagreement posts, in how &ldquo;conspiratorial&rdquo;<span class="sub">gemma-3-27B scored 3 while xai-grok-3.4 scored 0 (or the reverse), on the same 0&ndash;3 scale</span></div></div>
      <div class="pipe-arrow">&rarr;</div>
      <div class="pipe-box wide"><div class="big">500</div><div class="lbl">Randomly sampled<span class="sub">250 gemma-3-27B-3 / xai-grok-3.4-0 + 250 gemma-3-27B-0 / xai-grok-3.4-3 posts</span></div></div>
      <div class="pipe-arrow">&rarr;</div>
      <div class="pipe-box wide">
        <div class="big">5 experiments</div>
        <div class="lbl">Same 500 posts re-scored for</div>
        <ul class="pipe-exps">
          <li><span>Exp 0</span> &middot; baseline 0&ndash;3 Likert</li>
          <li><span>Exp 1</span> &middot; 0&ndash;3 Likert + justification</li>
          <li><span>Exp 2</span> &middot; detailed 0&ndash;3 Likert</li>
          <li><span>Exp 3</span> &middot; detailed 0&ndash;3 Likert + justification</li>
          <li><span>Exp 4</span> &middot; binary (11-dimensional criteria)</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="likert-results">
    <div class="section-head">
      <div class="eyebrow">03 &middot; Results: Likert (Exp 0&ndash;3)</div>
      <h2>Does the score change, when the prompting changes?</h2>
      <p class="section-desc">&ldquo;Change&rdquo; is reported as mean absolute change from baseline.</p>
    </div>

    <div class="stat-grid">
      <div class="stat-card"><div class="exp-tag">Exp 0</div><div class="num">0%</div><div class="lbl">cross-model agreement (baseline)</div></div>
      <div class="stat-card"><div class="exp-tag">Exp 1</div><div class="num">%%exp1_agree%%%</div><div class="lbl">agreement after requiring justification</div></div>
      <div class="stat-card"><div class="exp-tag">Exp 2</div><div class="num">%%exp2_agree%%%</div><div class="lbl">agreement with a more detailed Likert scale</div></div>
      <div class="stat-card"><div class="exp-tag">Exp 3</div><div class="num">%%exp3_agree%%%</div><div class="lbl">agreement with detailed Likert + justification</div></div>
    </div>

    <table class="desc-table">
      <thead>
        <tr><th>Experiment</th><th class="tag-gemma">gemma-3-27B</th><th class="tag-grok">xai-grok-3.4</th><th>Cross-model agreement</th></tr>
      </thead>
      <tbody>
        <tr>
          <td class="rowlabel">Exp 0 &middot; 0&ndash;3 Likert<span class="sub">no justification</span></td>
          <td>mean %%e0_gemma_mean%%<span class="sub">250 posts @ 0, 250 @ 3 (by design)</span></td>
          <td>mean %%e0_grok_mean%%<span class="sub">250 posts @ 0, 250 @ 3 (by design)</span></td>
          <td>0.0%<span class="sub">avg. distance 3.0 / 3</span></td>
        </tr>
        <tr>
          <td class="rowlabel">Exp 1 &middot; 0&ndash;3 Likert + justification<span class="sub">same prompt + required reasoning</span></td>
          <td>&Delta; %%e1_gemma_absdiff%%<span class="sub">%%e1_gemma_changed%%% of posts changed score</span></td>
          <td>&Delta; %%e1_grok_absdiff%%<span class="sub">%%e1_grok_changed%%% of posts changed score</span></td>
          <td>%%exp1_agree%%%<span class="sub">avg. distance %%e1_dist%%</span></td>
        </tr>
        <tr>
          <td class="rowlabel">Exp 2 &middot; 0&ndash;3 detailed Likert<span class="sub">rewritten scale, no justification</span></td>
          <td>&Delta; %%e2_gemma_absdiff%%<span class="sub">%%e2_gemma_changed%%% of posts changed score</span></td>
          <td>&Delta; %%e2_grok_absdiff%%<span class="sub">%%e2_grok_changed%%% of posts changed score</span></td>
          <td>%%exp2_agree%%%<span class="sub">avg. distance %%e2_dist%%</span></td>
        </tr>
        <tr>
          <td class="rowlabel">Exp 3 &middot; 0&ndash;3 detailed Likert + justification<span class="sub">rewritten scale + required reasoning</span></td>
          <td>&Delta; %%e3_gemma_absdiff%%<span class="sub">%%e3_gemma_changed%%% of posts changed score</span></td>
          <td>&Delta; %%e3_grok_absdiff%%<span class="sub">%%e3_grok_changed%%% of posts changed score</span></td>
          <td>%%exp3_agree%%%<span class="sub">avg. distance %%e3_dist%%</span></td>
        </tr>
      </tbody>
    </table>

    <div class="callout">
      <div class="callout-mark">&rarr; Thus&hellip;</div>
      <ol>
        <li><strong>Requiring justification (Exp 1)</strong> roughly doubled cross-model agreement, from 0% to %%exp1_agree%%%.</li>
        <li><strong>Detailing the 0-3 Likert (Exp 2)</strong> did not do as much: agreement only reached %%exp2_agree%%%.</li>
        <li><strong>Combining both</strong> led to highest agreement at %%exp3_agree%%%.</li>
      </ol>
    </div>
  </section>

  <section id="binary-results">
    <div class="section-head">
      <div class="eyebrow">04 &middot; Results: Binary (Exp 4)</div>
      <h2>What happens when conspiracy is made into checkable dimensions?</h2>
      <p class="section-desc">Exp 4 breaks conspiracy into 11 binary dimensions, grouped into three categories that cannot be interchangeable:</p>
    </div>

    <div class="dim-groups">
      <div class="dim-group">
        <h4>Claim structure</h4>
        <ol>
          <li>Causal simplicity</li>
          <li>Certainty</li>
          <li>Us vs. them</li>
          <li>Hidden truth</li>
        </ol>
      </div>
      <div class="dim-group">
        <h4>Actors &amp; threat</h4>
        <ol start="5">
          <li>Hidden actor</li>
          <li>Coordination</li>
          <li>Target</li>
          <li>Urgency</li>
        </ol>
      </div>
      <div class="dim-group">
        <h4>Tonal cues (scored separately)</h4>
        <ol start="9">
          <li>Sarcasm/irony</li>
          <li>Mockery/ridicule</li>
          <li>Coded language</li>
        </ol>
      </div>
    </div>
    <p class="decision-rule">A post was labeled <strong>&ldquo;yes&rdquo;</strong> if dimensions 5 (hidden actor) and 6 (coordination) were both present. If only one of the two was present, at least one of dimensions 1, 2, 3, 4, 7, or 8 was required. A post was labeled <strong>&ldquo;no&rdquo;</strong> if both 5 and 6 were absent. Dimensions 9&ndash;11 (tonal cues) were scored as factors relevant for considering how other dimensions were communicated.</p>

    <div class="mini-grid" style="margin-top:28px;">
      <div class="stat-card"><div class="num">%%e4_gemma_flip%%% / %%e4_grok_flip%%%</div><div class="lbl">gemma-3-27B / xai-grok-3.4 flipped from their baseline extreme</div></div>
      <div class="stat-card"><div class="num">%%exp4_agree%%%</div><div class="lbl">models agreed on the binary yes or no</div></div>
      <div class="stat-card"><div class="num">%%e4_gemma_pos%%% / %%e4_grok_pos%%%</div><div class="lbl">gemma-3-27B / xai-grok-3.4 labeled the post conspiratorial overall</div></div>
    </div>
    <div class="callout">
      <div class="callout-mark">&rarr; Thus&hellip;</div>
      <ol>
        <li><span class="mdl-gemma">gemma-3-27B</span> changed from its baseline of 0 or 3 more often than <span class="mdl-grok">xai-grok-3.4</span>.</li>
        <li><span class="mdl-gemma">gemma-3-27B</span> labeled posts conspiratorial nearly 1.5&times; as often as <span class="mdl-grok">xai-grok-3.4</span>. Parsing-out conspiracy into dimensional criteria narrowed the gap, but the gap still exists.</li>
      </ol>
    </div>
  </section>

  <section id="posrate-chart">
    <div class="section-head">
      <div class="eyebrow">05 &middot; Label Breakdown</div>
      <h2>Exp 4: yes, no, or uncertain?</h2>
    </div>
    <div class="panel"><div id="posrateChart" style="height:280px;"></div></div>
    <div class="tendency-block">
      <p class="tendency" style="color:var(--gemma);"><strong>gemma-3-27B:</strong> more likely to make inferences beyond what's explicitly stated.</p>
      <p class="tendency" style="color:var(--grok);"><strong>xai-grok-3.4:</strong> more likely to require an explicit, literal hidden-actor or coordination claim for satisfying criteria before labeling.</p>
    </div>
    <div class="callout">
      <div class="callout-mark">&rarr; Thus&hellip;</div>
      <ol>
        <li>46.4% of <span class="mdl-gemma">gemma-3-27B</span>'s baseline score-3 posts (116 of 250) switched to 0 for both models. These 116 posts would be a relevant sample for human coding, to understand <span class="mdl-gemma">gemma-3-27B</span>'s possible &ldquo;over-picking&rdquo; and how it tends to do so.</li>
        <li>Only 2.8% of <span class="mdl-grok">xai-grok-3.4</span>'s baseline score-3 posts (7 of 250) switched to 0, meaning, <span class="mdl-grok">xai-grok-3.4</span> seems more stable (though not necessarily more accurate). These 7 posts could be another sample for the researcher to review, as a comparison case against the other 116.</li>
      </ol>
    </div>
  </section>

  <section id="dims">
    <div class="section-head">
      <div class="eyebrow">06 &middot; Where the Models Disagree</div>
      <h2>Exp 4: Dimension-level disagreement</h2>
      <p class="section-desc">% of the 500 posts each model flagged &ldquo;yes&rdquo; on, per dimension. Hidden truth shows the widest gap, followed by sarcasm/irony and causal simplicity.</p>
    </div>
    <div class="panel"><div id="dimChart" style="height:420px;"></div></div>
  </section>

  <section id="samples">
    <div class="section-head">
      <div class="eyebrow">07 &middot; Consistent Disagreements</div>
      <h2>Which posts stayed contested</h2>
      <p class="section-desc">These four are drawn from the %%n_persistent%% posts (%%pct_persistent%%% of the 500) that stayed high-disagreement across Exp 0, Exp 1, Exp 2, and Exp 3.</p>
    </div>

    <div class="panel">
      <table class="sample-table">
        <thead>
          <tr><th style="width:20%;">Post excerpt</th><th style="width:6%;">gemma-3-27B</th><th style="width:26%;">Justification (direct quote)</th><th style="width:6%;">xai-grok-3.4</th><th style="width:26%;">Justification (direct quote)</th></tr>
        </thead>
        <tbody>
          <tr>
            <td class="excerpt">"The problems of faking a mass media moon landing are nothing compared with faking the multiple traces of the landing in the scientific literature."</td>
            <td class="score">3</td>
            <td class="just">"The message is centrally organized around the conspiracy theory that the moon landings were faked. It explicitly posits that both the media coverage and the scientific record are fabrications, making the conspiracy claim the core premise of the text."</td>
            <td class="score">0</td>
            <td class="just">"The post contains no attribution of events or evidence to hidden actors, coordinated deception, or concealed forces... It instead highlights the practical implausibility of sustaining a hoax across scientific literature, directly countering rather than advancing conspiracy claims."</td>
          </tr>
          <tr>
            <td class="excerpt">"No kidding. Only a total moron would believe a missle hit the Pentagon, and explosives brought down the WTC."</td>
            <td class="score">3</td>
            <td class="just">"It explicitly rejects the official narrative... and frames those who believe the official account as 'morons,' making the conspiracy rhetoric the primary purpose of the post."</td>
            <td class="score">0</td>
            <td class="just">"The post explicitly rejects 9/11 conspiracy claims... by labeling believers 'total morons,' with no suspicion, implication, or coded reference to hidden actors, coordination, or concealment."</td>
          </tr>
          <tr>
            <td class="excerpt">"He has got a big, big nose ... and he is a homosexual activist. He fits right in with our Jewish enemies. Judaism &amp; Homosexuality: A Marriage Made In Hell"</td>
            <td class="score">3</td>
            <td class="just">"The message is organized around a central conspiracy narrative that links Judaism and homosexuality as coordinated 'enemies.' It employs classic antisemitic tropes... to frame a perceived systemic threat, making conspiracy rhetoric the core of the post."</td>
            <td class="score">2</td>
            <td class="just">"...directly asserting coordinated enmity and deception rather than vague suspicion (ruling out 1), yet the short declarative post does not organize all content around a central explanatory conspiracy for specific events or outcomes (ruling out 3)."</td>
          </tr>
          <tr>
            <td class="excerpt">"Stalin's Jews. We mustn't forget that some of greatest murderers of modern times were Jewish... Written by Sver Plocker, a Jewish journalist..."</td>
            <td class="score">2</td>
            <td class="just">"While the bulk of the text provides a historical overview of Soviet state security, the framing is designed to link these systemic crimes to a specific ethnic/religious group, which is a hallmark of conspiracy-driven narratives regarding Jewish influence in global revolutions."</td>
            <td class="score">3</td>
            <td class="just">"The post is explicitly organized around the claim that Jews were central perpetrators of Soviet mass murder (via the Cheka/NKVD), using the title, opening sentence, and framing of a Jewish author to advance this as the core point."</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="callout">
      <div class="callout-mark">&rarr; Thus&hellip;</div>
      <ol>
        <li><span class="mdl-gemma">gemma-3-27B</span> tends to read and infer conspiracy claims, whether sarcastic or referencing another user's thoughts, as though the author endorsed them.</li>
        <li><span class="mdl-grok">xai-grok-3.4</span> tracks users' stance more reliably, yet requires an explicit hidden-actor or coordination claim, even on posts that are supportive of a conspiratorial worldview.</li>
        <li>For researchers auditing LLM labels: these instances indicate opportunity for checking <span class="mdl-gemma">gemma-3-27B</span>'s &ldquo;yes&rdquo; for missed sarcasm, and potential &ldquo;over-picking&rdquo;, and <span class="mdl-grok">xai-grok-3.4</span>'s &ldquo;no&rdquo; for cases where its bar was simply too high.</li>
      </ol>
    </div>
  </section>

  <section id="failures">
    <div class="section-head">
      <div class="eyebrow">08 &middot; Takeaways</div>
      <h2>What to check before using an LLM label</h2>
      <p class="section-desc">We found five patterns across iterations that could be useful as a checklist for anyone building a similar measurement prompt.</p>
    </div>
    <div class="fail-grid">
      <div class="fail-card">
        <div class="n">01</div>
        <h4>Interchangeability</h4>
        <p>The model could substitute one construct for another, and apply inconsistent conceptual scopes to what's being measured.</p>
        <div class="ex">To-do: In the prompt, add some focus of not letting the presence of one dimension imply another (for criteria-based) and that each is clearly distinguished (for 0-3 Likert) in how the model is instructed to consider "what counts".</div>
        <div class="ex">Example: ideology can be at risk of being read as conspiracy, conspiracy being read as generalized distrust, or grievance being read as anger.</div>
      </div>
      <div class="fail-card">
        <div class="n">02</div>
        <h4>Over-picking / under-picking</h4>
        <p>The model accepts weak evidence too readily (inflated false positives), or misses implicit/contextual evidence (false negatives).</p>
        <div class="ex">To-do: Sample high-disagreement posts and read models' justifications for their labels, being attentive to what models see as relevant.</div>
        <div class="ex">Example: gemma-3-27B tended to mistake an author's reference to another user's conspiratorial claim as the author's own.</div>
      </div>
      <div class="fail-card">
        <div class="n">03</div>
        <h4>Inconsistent thresholds</h4>
        <p>Different models apply different thresholds to the same prompt. These matter for researchers to consider whether a model's interpretation of text aligns with their research focus and interests, and if not, how the prompt should be iteratively refined (e.g. more specific set of criteria to meet).</p>
        <div class="ex">To-do: Require the model to produce justifications, which can provide opportunities for researchers to gain some context for the high-disagreement posts, and determine how they compare with the researchers' approach to measuring the concept of interest.</div>
        <div class="ex">Example: xai-grok-3.4 was more conservative than gemma-3-27B in satisfying the criteria required to label a post "conspiratorial." gemma-3-27B made more inferences and drew that boundary more broadly than intended. Which is preferable depends on the domain, and what the researcher needs to measure (e.g. intending to be able to pick up not yet widely known, newly emerging anti-vaccine conspiracies) as well as how they need to measure it (e.g. in gradients, or as present and not present).</div>
      </div>
      <div class="fail-card">
        <div class="n">04</div>
        <h4>Per Model Justifications</h4>
        <p>Prompting can change LLM-generated labels, in different ways. This requires being attentive to justifications, in how models respond to the criteria specified in the prompt.</p>
        <div class="ex">To-do: consider which model's default behavior is closer to what the task needs: recall-heavy detectability (wider-scope inclusivity) or precision-heavy accuracy (strictly rule-based).</div>
        <div class="ex">Example: gemma-3-27B tended to infer beyond what was explicitly stated in text, while xai-grok-3.4 was more conservative and cited specific parts of text that met/not met the criteria.</div>
      </div>
      <div class="fail-card wide">
        <div class="n">05</div>
        <h4>Dataset &amp; domain</h4>
        <p>Iterations we've done here were adapted to this dataset: short, informal StormFront.org posts about white-supremacist conspiracy narratives. A different domain (e.g. anti-vaccine forums) or a different content type (lengthy, formal documents vs. short, informal user posts) might influence where models over- or under-detect, and would require auditing based on how well the researcher understands their data and domain well.</p>
        <div class="ex">To-do: Revisit and adjust the prompt's criteria for the new domain's characteristic rhetoric (e.g., anti-vaccine posts may rely more on misrepresented studies than on "hidden actor" framing) rather than reusing the same criteria unchanged.</div>
        <div class="ex">Example: a prompt tuned to catch explicit tropes in one-line StormFront posts may under-perform on multi-paragraph anti-vaccine essays, where conspiratorial claims are spread across paragraphs rather than concentrated in a single sentence.</div>
      </div>
    </div>
  </section>

  <footer>
    Measuring the Unmeasurable? &middot; SICSS 2026 project deliverable &middot; prompt library, comparative reasoning, and failure catalogue in the accompanying repository.
  </footer>

</div>

<script>
const DATA = __DATA_JSON__;

const plotlyConfig = {displayModeBar: false, responsive: true};

const paperBg = 'rgba(0,0,0,0)';
const fontColor = '#eef1f8';
const gridColor = '#1b2436';
const baseLayout = {
  paper_bgcolor: paperBg, plot_bgcolor: paperBg,
  font: {color: fontColor, family: 'inherit', size: 12.5},
  margin: {t:20, r:20, b:44, l:56},
};

function chartFallback(id, msg){
  const el = document.getElementById(id);
  if (el) el.innerHTML = '<p style="color:#7d8699;font-size:13px;margin:0;padding:12px 4px;">' + msg + '</p>';
}
function safeDraw(id, fn){
  try { fn(); }
  catch (e) {
    console.error('Chart failed to render:', id, e);
    const isLoadError = typeof Plotly === 'undefined';
    chartFallback(id, isLoadError
      ? 'Chart library failed to load from the CDN. Check your internet connection and reload this page.'
      : 'This chart hit an error (' + (e && e.message ? e.message : 'unknown') + '). Open the browser console for details.');
  }
}

/* ---- Exp4 yes / no / uncertain stacked bar ---- */
safeDraw('posrateChart', () => {
Plotly.newPlot('posrateChart', [
  {x: [DATA.exp4.gemma_positive_pct, DATA.exp4.grok_positive_pct], y: ['gemma-3-27B','xai-grok-3.4'],
   type:'bar', orientation:'h', name:'Yes', marker:{color:'#38bdf8'},
   text: [DATA.exp4.gemma_positive_pct+'%', DATA.exp4.grok_positive_pct+'%'], textposition:'inside', insidetextanchor:'middle'},
  {x: [DATA.exp4.gemma_negative_pct, DATA.exp4.grok_negative_pct], y: ['gemma-3-27B','xai-grok-3.4'],
   type:'bar', orientation:'h', name:'No', marker:{color:'#1d4ed8'},
   text: [DATA.exp4.gemma_negative_pct+'%', DATA.exp4.grok_negative_pct+'%'], textposition:'inside', insidetextanchor:'middle'},
  {x: [DATA.exp4.gemma_uncertain_pct, DATA.exp4.grok_uncertain_pct], y: ['gemma-3-27B','xai-grok-3.4'],
   type:'bar', orientation:'h', name:'Uncertain', marker:{color:'#3a3f52'},
   text: [DATA.exp4.gemma_uncertain_pct+'%', DATA.exp4.grok_uncertain_pct+'%'], textposition:'inside', insidetextanchor:'middle'}
], Object.assign({}, baseLayout, {
  barmode: 'stack',
  xaxis: {title:'% of 500 posts', range:[0,100], gridcolor: gridColor},
  yaxis: {gridcolor: gridColor},
  legend: {orientation:'h', y:1.25},
  margin: {t:20,r:20,b:44,l:90}
}), plotlyConfig);
});

/* ---- Exp4 dimension grouped bar: single axis scaled to the data, model vs model only ---- */
safeDraw('dimChart', () => {
const dims = DATA.dims;
Plotly.newPlot('dimChart', [
  {x: dims.map(d=>d.dim), y: dims.map(d=>d.gemma_pct), type:'bar', name:'gemma-3-27B', marker:{color:'#38bdf8'}},
  {x: dims.map(d=>d.dim), y: dims.map(d=>d.grok_pct), type:'bar', name:'xai-grok-3.4', marker:{color:'#6366f1'}}
], Object.assign({}, baseLayout, {
  barmode: 'group',
  yaxis: {title:'% of 500 posts scored "yes"', range:[0,65], gridcolor: gridColor, zeroline:false},
  xaxis: {tickangle: -30, gridcolor: gridColor},
  legend: {orientation:'h', y:1.15, x:0, xanchor:'left'},
  margin: {t:20,r:40,b:110,l:56}
}), plotlyConfig);
});
</script>
</body>
</html>
"""

vals = {
    "exp1_agree": exp1["cross_agree_pct"],
    "exp2_agree": exp2["cross_agree_pct"],
    "exp3_agree": exp3["cross_agree_pct"],
    "exp4_agree": exp4["cross_agree_pct"],
    "e0_gemma_mean": exp0["gemma_mean"],
    "e0_grok_mean": exp0["grok_mean"],
    "e1_gemma_absdiff": exp1["gemma_mean_absdiff"],
    "e1_grok_absdiff": exp1["grok_mean_absdiff"],
    "e1_gemma_changed": exp1["gemma_pct_changed"],
    "e1_grok_changed": exp1["grok_pct_changed"],
    "e1_dist": exp1["cross_dist"],
    "e2_gemma_absdiff": exp2["gemma_mean_absdiff"],
    "e2_grok_absdiff": exp2["grok_mean_absdiff"],
    "e2_gemma_changed": exp2["gemma_pct_changed"],
    "e2_grok_changed": exp2["grok_pct_changed"],
    "e2_dist": exp2["cross_dist"],
    "e3_gemma_absdiff": exp3["gemma_mean_absdiff"],
    "e3_grok_absdiff": exp3["grok_mean_absdiff"],
    "e3_gemma_changed": exp3["gemma_pct_changed"],
    "e3_grok_changed": exp3["grok_pct_changed"],
    "e3_dist": exp3["cross_dist"],
    "e4_gemma_flip": exp4["gemma_flip_pct"],
    "e4_grok_flip": exp4["grok_flip_pct"],
    "e4_gemma_pos": exp4["gemma_positive_pct"],
    "e4_grok_pos": exp4["grok_positive_pct"],
    "n_persistent": D["n_persistent"],
    "pct_persistent": D["pct_persistent"],
}

for _k, _v in vals.items():
    html = html.replace('%%' + _k + '%%', str(_v))
html = html.replace("__DATA_JSON__", data_json)

with open("/sessions/lucid-epic-goodall/mnt/outputs/report.html", "w") as f:
    f.write(html)

print("written, length:", len(html))
