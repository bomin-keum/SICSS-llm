import json

with open("/sessions/lucid-epic-goodall/mnt/outputs/report_data.json") as f:
    D = json.load(f)

S = D["summary"]
DIMS = D["dims"]
POSTS = D["posts"]

data_json = json.dumps({"posts": POSTS, "summary": S, "dims": DIMS})

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Measuring...the Unmeasurable? | SICSS 2026</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/plotly.js/2.35.2/plotly.min.js"></script>
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
    font-size: 2.6rem;
    line-height: 1.15;
    margin: 14px auto 12px;
    max-width: 780px;
    font-weight: 700;
    letter-spacing: -0.01em;
  }
  .subtitle { color: var(--muted); font-size: 1.05rem; max-width: 640px; margin: 0 auto; }
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
  .cmp-tags { display:flex; gap:6px; margin: 2px 0 12px; flex-wrap:wrap; }
  .cmp-tag {
    font-size: 10.5px; text-transform: uppercase; letter-spacing: .05em; font-weight: 700;
    color: #a9c6f5; background: rgba(56,189,248,.08); border: 1px solid rgba(56,189,248,.28);
    padding: 3px 10px; border-radius: 6px;
  }
  h2 { font-size: 1.6rem; margin: 0 0 8px; font-weight: 700; }
  .section-desc { color: var(--muted); max-width: 760px; font-size: .97rem; }
  .why-copy { max-width: 760px; }
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

  .panel { background: var(--panel); border: 1px solid var(--border); border-radius: 16px; padding: 24px; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }

  .callout {
    background: linear-gradient(135deg, rgba(37,99,235,.16), rgba(56,189,248,.07));
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 26px 28px;
    margin-top: 28px;
  }
  .callout h3 { margin: 0 0 8px; font-size: 1.15rem; }
  .callout p { margin: 0; color: var(--muted); font-size: .95rem; }

  .toggle-row { display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }
  .toggle-btn {
    background: var(--panel2); border: 1px solid var(--border); color: var(--muted);
    padding: 8px 16px; border-radius: 999px; font-size: 12.5px; cursor: pointer; font-family: var(--font);
  }
  .toggle-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); font-weight: 700; }
  .legend-note { color: var(--muted); font-size: 12px; margin-top: 10px; }

  .fail-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 24px; }
  .fail-card { background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 20px; }
  .fail-card .n { color: var(--accent2); font-weight: 800; font-size: 12.5px; letter-spacing: .08em; }
  .fail-card h4 { margin: 6px 0 8px; font-size: 1.02rem; }
  .fail-card p { margin: 0; color: var(--muted); font-size: .89rem; }
  .fail-card .ex { margin-top: 10px; font-size: .82rem; color: #c7cbe0; background: var(--panel2); border-radius: 8px; padding: 8px 10px; border-left: 3px solid var(--accent); }

  footer { border-top: 1px solid var(--border); padding-top: 30px; color: var(--muted); font-size: .85rem; text-align:center; }
  footer a { color: var(--accent2); }

  @media (max-width: 860px) {
    .stat-grid { grid-template-columns: repeat(2,1fr); }
    .grid-2 { grid-template-columns: 1fr; }
    .fail-grid { grid-template-columns: 1fr; }
    h1.title { font-size: 1.9rem; }
  }
</style>
</head>
<body>

<header class="hero">
  <div class="kicker">SICSS 2026 &middot; University of Washington</div>
  <h1 class="title">Measuring&hellip;the Unmeasurable?</h1>
  <div class="subtitle">An iterative framework for using LLMs to study nuance in text.</div>
  <div class="authors">
    <span><span class="who">Bo Min Keum</span> &middot; <span class="aff">International CyberCrime Research Institute, SFU</span></span>
    <span><span class="who">Roman Pomeshchikov</span> &middot; <span class="aff">Near and Middle Eastern Studies (NMES) Interdisciplinary Program, University of Washington</span></span>
  </div>
</header>

<div class="wrap">

  <section id="why">
    <div class="section-head">
      <div class="eyebrow">01 &middot; First: Why?</div>
      <h2>&ldquo;Nuance&rdquo; is hard to measure.</h2>
    </div>
    <div class="why-copy">
      <p>Masculinity, populism, humiliation, identity threat, sarcasm, humour&hellip; concepts like these aren't directly measurable. They're theory-dependent, context-dependent, interpretive, and highly contested in the social sciences. There's no agreement on what they even mean.</p>
      <p>LLMs are increasingly used to classify text. Human coders read nuance, but they don't scale to hundreds of thousands of posts &mdash; a struggle we've found in our own PhD research on online radicalization discourse (Bo Min Keum) and political discourse (Roman Pomeshchikov). But while LLMs scale, LLM-generated labels require human validation to make sure downstream analysis isn't affected &mdash; which requires considering construct validity: whether, through LLMs, we're measuring what we think we're measuring. If prompting changes what gets measured, prompt design becomes part of that validity question: are we actually measuring the thing we claim to measure?</p>
      <p><strong>So we made the prompt itself the object of study.</strong> We started with a sample of 1.7K posts made on StormFront (a web forum associated with white-supremacist and far-right movements) on which gemma-3-27B and xai-grok-3.1 gave polar opposite scores &mdash; one model saw no conspiratorial content (0), the other saw conspiratorial rhetoric as the core of the message (3). That kind of disagreement was an indication to us that something about the post, or about how each model read it, was producing two entirely different readings. We randomly sampled 500 of these high-disagreement posts and ran them through four experiments &mdash; using gemma-3-27B and xai-grok-3.4 &mdash; testing whether refining the prompt changes what the two models "see" in the same text.</p>
    </div>
  </section>

  <section id="table">
    <div class="section-head">
      <div class="eyebrow">02 &middot; Descriptive Overview</div>
      <p class="section-desc">All four experiments re-score the same 500 posts, so results are comparable across experiments. Exp0, Exp1, and Exp3 use a 0&ndash;3 Likert scale, so change is reported as mean absolute shift from baseline. Exp2 is a binary label, so change is reported as the share of posts that flipped away from their original baseline extreme (0&rarr;1 or 3&rarr;0).</p>
    </div>

    <div class="stat-grid">
      <div class="stat-card"><div class="exp-tag">Exp 0</div><div class="num">0%</div><div class="lbl">cross-model agreement (baseline)</div></div>
      <div class="stat-card"><div class="exp-tag">Exp 1</div><div class="num">%%exp1_agree%%%</div><div class="lbl">agreement after requiring justification</div></div>
      <div class="stat-card"><div class="exp-tag">Exp 2</div><div class="num">%%exp2_agree%%%</div><div class="lbl">agreement after decomposing into 11 dimensions</div></div>
      <div class="stat-card"><div class="exp-tag">Exp 3</div><div class="num">%%exp3_agree%%%</div><div class="lbl">agreement with a more specific Likert scale</div></div>
    </div>

    <table class="desc-table">
      <thead>
        <tr><th>Experiment</th><th class="tag-gemma">GEMMA</th><th class="tag-grok">GROK</th><th>Cross-model agreement</th></tr>
      </thead>
      <tbody>
        <tr>
          <td class="rowlabel">Exp 0 &middot; Baseline<span class="sub">0&ndash;3 Likert, no justification</span></td>
          <td>mean %%e0_gemma_mean%%<span class="sub">250 posts @ 0, 250 @ 3 (by design)</span></td>
          <td>mean %%e0_grok_mean%%<span class="sub">250 posts @ 0, 250 @ 3 (by design)</span></td>
          <td>0.0%<span class="sub">avg. distance 3.0 / 3</span></td>
        </tr>
        <tr>
          <td class="rowlabel">Exp 1 &middot; Justification<span class="sub">same prompt + required reasoning</span></td>
          <td>&Delta; %%e1_gemma_absdiff%%<span class="sub">%%e1_gemma_changed%%% of posts changed score</span></td>
          <td>&Delta; %%e1_grok_absdiff%%<span class="sub">%%e1_grok_changed%%% of posts changed score</span></td>
          <td>%%exp1_agree%%%<span class="sub">avg. distance %%e1_dist%%</span></td>
        </tr>
        <tr>
          <td class="rowlabel">Exp 2 &middot; Decomposition<span class="sub">11 dims &rarr; binary label</span></td>
          <td>%%e2_gemma_flip%%% flipped<span class="sub">%%e2_gemma_pos%%% labeled positive overall</span></td>
          <td>%%e2_grok_flip%%% flipped<span class="sub">%%e2_grok_pos%%% labeled positive overall</span></td>
          <td>%%exp2_agree%%%<span class="sub">%%e2_gemma_unc%%/%%e2_grok_unc%% marked uncertain (G/R)</span></td>
        </tr>
        <tr>
          <td class="rowlabel">Exp 3 &middot; More Specific Likert<span class="sub">rewritten scale, no justification</span></td>
          <td>&Delta; %%e3_gemma_absdiff%%<span class="sub">%%e3_gemma_changed%%% of posts changed score</span></td>
          <td>&Delta; %%e3_grok_absdiff%%<span class="sub">%%e3_grok_changed%%% of posts changed score</span></td>
          <td>%%exp3_agree%%%<span class="sub">avg. distance %%e3_dist%%</span></td>
        </tr>
      </tbody>
    </table>

    <div class="callout">
      <h3>Our Observations</h3>
      <p>Cross-model agreement climbed steadily from justification (Exp 1: %%exp1_agree%%%) to decomposition (Exp 2: %%exp2_agree%%%) &mdash; then <strong>dropped</strong> under the more specific Likert scale (Exp 3: %%exp3_agree%%%), below even Exp 1. Breaking the construct into checkable sub-dimensions did more for cross-model agreement than writing a more careful version of the same holistic scale. GEMMA's scores also moved more than GROK's at every stage: its mean absolute shift from baseline was %%e1_gemma_absdiff%% in Exp 1 and %%e3_gemma_absdiff%% in Exp 3 &mdash; roughly %%vol_ratio1%%&times; and %%vol_ratio3%%&times; GROK's.</p>
    </div>
  </section>

  <section id="agreement-chart">
    <div class="section-head">
      <div class="eyebrow">03 &middot; Model Agreement Across Experiments</div>
      <div class="cmp-tags"><span class="cmp-tag">Across-experiment</span></div>
      <h2>Agreement rose, then fell</h2>
      <p class="section-desc">Decomposition (Exp 2) produced the highest cross-model agreement of any prompting strategy tested &mdash; higher than either Likert variant.</p>
    </div>
    <div class="panel"><div id="agreementChart" style="height:360px;"></div></div>
  </section>

  <section id="volatility-chart">
    <div class="grid-2">
      <div>
        <div class="section-head">
          <div class="eyebrow">04 &middot; Score Movement</div>
          <div class="cmp-tags"><span class="cmp-tag">Model vs. model</span><span class="cmp-tag">Across-experiment</span></div>
          <h2>Which model moved more?</h2>
          <p class="section-desc">Mean absolute change from the Exp 0 baseline score, by model and experiment.</p>
        </div>
        <div class="panel"><div id="volatilityChart" style="height:340px;"></div></div>
      </div>
      <div>
        <div class="section-head">
          <div class="eyebrow">05 &middot; Label Breakdown</div>
          <div class="cmp-tags"><span class="cmp-tag">Model vs. model</span><span class="cmp-tag">Within Exp 2</span></div>
          <h2>Exp 2: positive, negative, or uncertain?</h2>
          <p class="section-desc">Full breakdown of how each model labeled the 500 posts once conspiracy was decomposed into 11 checkable dimensions: positive (conspiratorial), negative (not conspiratorial), or uncertain.</p>
        </div>
        <div class="panel"><div id="posrateChart" style="height:340px;"></div></div>
      </div>
    </div>
  </section>

  <section id="dims">
    <div class="section-head">
      <div class="eyebrow">06 &middot; Where the Models Diverge</div>
      <div class="cmp-tags"><span class="cmp-tag">Model vs. model</span><span class="cmp-tag">Within Exp 2</span></div>
      <h2>Dimension-level (dis)agreement, Experiment 2</h2>
      <p class="section-desc">Endorsement rate per dimension (% of 500 posts each model flagged "yes"), plus how often the two models agreed on that dimension specifically. Hidden truth shows the widest gap.</p>
    </div>
    <div class="panel"><div id="dimChart" style="height:460px;"></div></div>
  </section>

  <section id="heatmap">
    <div class="section-head">
      <div class="eyebrow">07 &middot; Post-Level Trajectories</div>
      <h2>Which posts stayed stable, which stayed contested</h2>
      <p class="section-desc">Each row is one post; each column is a model's score at a given experiment (Exp 2 is binary, rescaled 0/3 for display &mdash; hover shows the real 0/1 label). Rows are sorted by the final gap between GEMMA and GROK at Exp 3.</p>
    </div>
    <div class="toggle-row">
      <button class="toggle-btn active" data-view="persist">Most persistent disagreement (40)</button>
      <button class="toggle-btn" data-view="resolved">Most resolved (40)</button>
      <button class="toggle-btn" data-view="all">Full sample (500, scroll)</button>
    </div>
    <div class="panel">
      <div id="heatmapDiv" style="overflow-y:auto; max-height:760px;"></div>
      <div class="legend-note">Grey cells = uncertain / not classified. Color scale: dark blue (0, absent) &rarr; bright cyan (3, central). * Exp 2 columns show a binary label rescaled onto the same 0/3 axis for visual comparison only.</div>
    </div>
  </section>

  <section id="failures">
    <div class="section-head">
      <div class="eyebrow">08 &middot; Useful &ldquo;Failures&rdquo;</div>
      <h2>What to check before trusting an LLM label</h2>
      <p class="section-desc">We found three patterns across iterations that could be useful as a checklist for anyone building a similar measurement prompt.</p>
    </div>
    <div class="fail-grid">
      <div class="fail-card">
        <div class="n">01</div>
        <h4>Interchangeability</h4>
        <p>The model substitutes one construct for another, and has inconsistent conceptual scope.</p>
        <div class="ex">Example: ideology read as conspiracy, conspiracy read as generalized distrust, grievance read as anger.</div>
      </div>
      <div class="fail-card">
        <div class="n">02</div>
        <h4>Over-picking / under-picking</h4>
        <p>The model accepts weak evidence too readily (inflated false positives), or misses implicit/contextual evidence (false negatives).</p>
        <div class="ex">Example: GEMMA treated a belief the author explicitly rejected as evidence of coordination &mdash; mistaking a quoted, debunked claim for the author's own.</div>
      </div>
      <div class="fail-card">
        <div class="n">03</div>
        <h4>Inconsistent thresholds</h4>
        <p>Different models apply different thresholds to the same prompt. This becomes visible once justification is required &mdash; useful for researchers assessing whether a model's interpretation of text aligns with their research interests, and if not, how the prompt should be iteratively refined.</p>
        <div class="ex">Example: GROK was more conservative than GEMMA in satisfying the criteria required to label a post "conspiratorial." GEMMA made more inferences and drew that boundary more broadly than intended. Which is preferable depends on context (e.g. white-supremacist vs. anti-vaccine conspiratorial rhetoric) and on what the researcher needs to measure &mdash; conspiracy as a gradient, or as a binary.</div>
      </div>
    </div>
  </section>

  <footer>
    Measuring&hellip;the Unmeasurable? &middot; SICSS 2026 project deliverable &middot; prompt library, comparative reasoning, and failure catalogue in the accompanying repository.
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

/* ---- 03 Agreement line chart ---- */
safeDraw('agreementChart', () => {
Plotly.newPlot('agreementChart', [{
  x: ['Exp 0<br>Baseline','Exp 1<br>Justification','Exp 2<br>Decomposition','Exp 3<br>More Specific Likert'],
  y: [DATA.summary.exp0.cross_agree_pct, DATA.summary.exp1.cross_agree_pct, DATA.summary.exp2.cross_agree_pct, DATA.summary.exp3.cross_agree_pct],
  type: 'scatter', mode: 'lines+markers+text',
  text: [DATA.summary.exp0.cross_agree_pct+'%', DATA.summary.exp1.cross_agree_pct+'%', DATA.summary.exp2.cross_agree_pct+'%', DATA.summary.exp3.cross_agree_pct+'%'],
  textposition: 'top center',
  line: {color: '#2563eb', width: 3, shape: 'spline'},
  marker: {color: '#38bdf8', size: 11},
  fill: 'tozeroy', fillcolor: 'rgba(37,99,235,0.10)'
}], Object.assign({}, baseLayout, {
  yaxis: {title: 'Cross-model agreement (%)', range: [0,90], gridcolor: gridColor, zeroline:false},
  xaxis: {gridcolor: gridColor}
}), plotlyConfig);
});

/* ---- 04 Volatility bar chart ---- */
safeDraw('volatilityChart', () => {
Plotly.newPlot('volatilityChart', [
  {x: ['Exp 1','Exp 3'], y: [DATA.summary.exp1.gemma_mean_absdiff, DATA.summary.exp3.gemma_mean_absdiff],
   type:'bar', name:'GEMMA', marker:{color:'#38bdf8'}},
  {x: ['Exp 1','Exp 3'], y: [DATA.summary.exp1.grok_mean_absdiff, DATA.summary.exp3.grok_mean_absdiff],
   type:'bar', name:'GROK', marker:{color:'#6366f1'}}
], Object.assign({}, baseLayout, {
  barmode: 'group',
  yaxis: {title:'Mean |change| from baseline', gridcolor: gridColor, zeroline:false},
  xaxis: {gridcolor: gridColor},
  legend: {orientation:'h', y:1.15}
}), plotlyConfig);
});

/* ---- 05 Positive / negative / uncertain stacked bar ---- */
safeDraw('posrateChart', () => {
Plotly.newPlot('posrateChart', [
  {x: [DATA.summary.exp2.gemma_positive_pct, DATA.summary.exp2.grok_positive_pct], y: ['GEMMA','GROK'],
   type:'bar', orientation:'h', name:'Positive', marker:{color:'#38bdf8'},
   text: [DATA.summary.exp2.gemma_positive_pct+'%', DATA.summary.exp2.grok_positive_pct+'%'], textposition:'inside', insidetextanchor:'middle'},
  {x: [DATA.summary.exp2.gemma_negative_pct, DATA.summary.exp2.grok_negative_pct], y: ['GEMMA','GROK'],
   type:'bar', orientation:'h', name:'Negative', marker:{color:'#1d4ed8'},
   text: [DATA.summary.exp2.gemma_negative_pct+'%', DATA.summary.exp2.grok_negative_pct+'%'], textposition:'inside', insidetextanchor:'middle'},
  {x: [DATA.summary.exp2.gemma_uncertain_pct, DATA.summary.exp2.grok_uncertain_pct], y: ['GEMMA','GROK'],
   type:'bar', orientation:'h', name:'Uncertain', marker:{color:'#3a3f52'},
   text: [DATA.summary.exp2.gemma_uncertain_pct+'%', DATA.summary.exp2.grok_uncertain_pct+'%'], textposition:'inside', insidetextanchor:'middle'}
], Object.assign({}, baseLayout, {
  barmode: 'stack',
  xaxis: {title:'% of 500 posts', range:[0,100], gridcolor: gridColor},
  yaxis: {gridcolor: gridColor},
  legend: {orientation:'h', y:1.2},
  margin: {t:20,r:20,b:44,l:70}
}), plotlyConfig);
});

/* ---- 06 Dimension grouped bar ---- */
safeDraw('dimChart', () => {
const dims = DATA.dims;
Plotly.newPlot('dimChart', [
  {x: dims.map(d=>d.dim), y: dims.map(d=>d.gemma_pct), type:'bar', name:'GEMMA', marker:{color:'#38bdf8'}},
  {x: dims.map(d=>d.dim), y: dims.map(d=>d.grok_pct), type:'bar', name:'GROK', marker:{color:'#6366f1'}},
  {x: dims.map(d=>d.dim), y: dims.map(d=>d.agree_pct), type:'scatter', mode:'lines+markers', name:'Agreement %',
   yaxis:'y2', line:{color:'#eef1f8', width:2, dash:'dot'}, marker:{size:6, color:'#eef1f8'}}
], Object.assign({}, baseLayout, {
  barmode: 'group',
  yaxis: {title:'% posts endorsed', gridcolor: gridColor, zeroline:false},
  yaxis2: {title:'Agreement %', overlaying:'y', side:'right', range:[0,100], gridcolor:'rgba(0,0,0,0)'},
  xaxis: {tickangle: -30, gridcolor: gridColor},
  legend: {orientation:'h', y:1.15},
  margin: {t:20,r:60,b:110,l:56}
}), plotlyConfig);
});

/* ---- 07 Heatmap ---- */
const cols = ['e0g','e0r','e1g','e1r','e2g','e2r','e3g','e3r'];
const colLabels = ['Exp0 GEMMA','Exp0 GROK','Exp1 GEMMA','Exp1 GROK','Exp2 GEMMA*','Exp2 GROK*','Exp3 GEMMA','Exp3 GROK'];

function cellVal(post, key){
  const v = post[key];
  if (v === null || v === undefined) return -1;
  if (key === 'e2g' || key === 'e2r') return v * 3;
  return v;
}
function cellText(post, key, idx){
  const v = post[key];
  if (v === null || v === undefined) return 'n/a';
  if (key === 'e2g' || key === 'e2r') return v === 1 ? 'label: 1 (yes)' : 'label: 0 (no)';
  return 'score: ' + v;
}

function buildMatrix(postList){
  const z = [], text = [], rowLabels = [];
  postList.forEach(p => {
    z.push(cols.map(c => cellVal(p, c)));
    text.push(cols.map((c, i) => 'Post ' + p.id + ' (' + p.grp + ')<br>' + colLabels[i] + '<br>' + cellText(p, c, i)));
    rowLabels.push('#' + p.id);
  });
  return {z, text, rowLabels};
}

const colorscale = [
  [0, '#2a3040'],
  [0.001, '#0b2545'],
  [0.33, '#1d4ed8'],
  [0.66, '#38bdf8'],
  [1, '#a7f3ff']
];

function drawHeatmap(postList, height){
  safeDraw('heatmapDiv', () => {
    const m = buildMatrix(postList);
    Plotly.newPlot('heatmapDiv', [{
      z: m.z, x: colLabels, y: m.rowLabels, text: m.text, hoverinfo: 'text',
      type: 'heatmap', colorscale: colorscale, zmin: -1, zmax: 3, showscale: true,
      xgap: 3, ygap: postList.length > 100 ? 0 : 2,
      colorbar: {title:'score', tickvals:[-1,0,1,2,3], ticktext:['n/a','0','1','2','3'], thickness: 14}
    }], Object.assign({}, baseLayout, {
      height: height,
      margin: {t:10, r:20, b:70, l:70},
      xaxis: {tickangle: -30, gridcolor: gridColor, side:'bottom'},
      yaxis: {gridcolor: gridColor, autorange: 'reversed', tickfont:{size: postList.length>100?7:10}}
    }), plotlyConfig);
  });
}

function finalGap(p){
  if (p.e3g === null || p.e3r === null) return null;
  return Math.abs(p.e3g - p.e3r);
}

let byGapDesc = [], byGapAsc = [];
try {
  const allPosts = DATA.posts.slice();
  const validGap = allPosts.filter(p => finalGap(p) !== null);
  const missingGap = allPosts.filter(p => finalGap(p) === null);
  byGapDesc = validGap.slice().sort((a,b) => finalGap(b) - finalGap(a)).concat(missingGap);
  byGapAsc = validGap.slice().sort((a,b) => finalGap(a) - finalGap(b));
} catch (e) {
  console.error('Post data processing failed:', e);
  chartFallback('heatmapDiv', 'Post data could not be processed. Open the browser console for details.');
}

function render(view){
  if (view === 'persist') drawHeatmap(byGapDesc.slice(0,40), 620);
  else if (view === 'resolved') drawHeatmap(byGapAsc.slice(0,40), 620);
  else drawHeatmap(byGapDesc, 5200);
}
if (byGapDesc.length) render('persist');

document.querySelectorAll('.toggle-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    render(btn.dataset.view);
  });
});
</script>
</body>
</html>
"""

vals = {
    "exp1_agree": S["exp1"]["cross_agree_pct"],
    "exp2_agree": S["exp2"]["cross_agree_pct"],
    "exp3_agree": S["exp3"]["cross_agree_pct"],
    "e0_gemma_mean": S["exp0"]["gemma_mean"],
    "e0_grok_mean": S["exp0"]["grok_mean"],
    "e1_gemma_absdiff": S["exp1"]["gemma_mean_absdiff"],
    "e1_grok_absdiff": S["exp1"]["grok_mean_absdiff"],
    "e1_gemma_changed": S["exp1"]["gemma_pct_changed"],
    "e1_grok_changed": S["exp1"]["grok_pct_changed"],
    "e1_dist": S["exp1"]["cross_dist"],
    "e2_gemma_flip": S["exp2"]["gemma_flip_pct"],
    "e2_grok_flip": S["exp2"]["grok_flip_pct"],
    "e2_gemma_pos": S["exp2"]["gemma_positive_pct"],
    "e2_grok_pos": S["exp2"]["grok_positive_pct"],
    "e2_gemma_unc": S["exp2"]["gemma_uncertain_n"],
    "e2_grok_unc": S["exp2"]["grok_uncertain_n"],
    "e3_gemma_absdiff": S["exp3"]["gemma_mean_absdiff"],
    "e3_grok_absdiff": S["exp3"]["grok_mean_absdiff"],
    "e3_gemma_changed": S["exp3"]["gemma_pct_changed"],
    "e3_grok_changed": S["exp3"]["grok_pct_changed"],
    "e3_dist": S["exp3"]["cross_dist"],
    "vol_ratio1": round(S["exp1"]["gemma_mean_absdiff"]/S["exp1"]["grok_mean_absdiff"],1),
    "vol_ratio3": round(S["exp3"]["gemma_mean_absdiff"]/S["exp3"]["grok_mean_absdiff"],1),
}

for _k, _v in vals.items():
    html = html.replace('%%' + _k + '%%', str(_v))
html = html.replace("__DATA_JSON__", data_json)

with open("/sessions/lucid-epic-goodall/mnt/outputs/report.html", "w") as f:
    f.write(html)

print("written, length:", len(html))
