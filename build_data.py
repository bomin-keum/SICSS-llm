import pandas as pd, numpy as np, json, re

df = pd.read_pickle('merged500.pkl')

g0 = pd.to_numeric(df['exp0_conspiracy_GEMMA']); r0 = pd.to_numeric(df['exp0_conspiracy_GROK'])
g1 = pd.to_numeric(df['exp1_GEMMA_score'], errors='coerce'); r1 = pd.to_numeric(df['exp1_GROK_score'], errors='coerce')
g2 = pd.to_numeric(df['GEMMA-experiment 3-score'], errors='coerce'); r2 = pd.to_numeric(df['GROK-experiment 3-score'], errors='coerce')
g3 = pd.to_numeric(df['exp3_GEMMA_score'], errors='coerce'); r3 = pd.to_numeric(df['exp3_GROK_score'], errors='coerce')

def likert_stats(g, r, base_g, base_r):
    shift_g = round((g-base_g).abs().mean(), 2)
    shift_r = round((r-base_r).abs().mean(), 2)
    changed_g = round((g!=base_g).mean()*100, 1)
    changed_r = round((r!=base_r).mean()*100, 1)
    valid = g.notna() & r.notna()
    agree = round((g[valid]==r[valid]).mean()*100, 1)
    dist = round((g[valid]-r[valid]).abs().mean(), 2)
    return dict(gemma_mean_absdiff=shift_g, grok_mean_absdiff=shift_r,
                gemma_pct_changed=changed_g, grok_pct_changed=changed_r,
                cross_agree_pct=agree, cross_dist=dist, n=int(valid.sum()))

exp0_stats = dict(gemma_mean=1.5, grok_mean=1.5, cross_agree_pct=0.0, cross_dist=3.0)
exp1_stats = dict(gemma_mean_absdiff=2.14, grok_mean_absdiff=0.64, gemma_pct_changed=85.0, grok_pct_changed=43.4, cross_agree_pct=56.6, cross_dist=0.59)
exp2_stats = dict(gemma_mean_absdiff=1.8, grok_mean_absdiff=0.67, gemma_pct_changed=69.4, grok_pct_changed=44.6, cross_agree_pct=35.4, cross_dist=1.2)
exp3_stats = likert_stats(g3, r3, g0, r0)
print("exp3 (new) stats:", exp3_stats)

exp4_stats = dict(gemma_flip_pct=62.6, grok_flip_pct=36.2, cross_agree_pct=77.8, gemma_positive_pct=25.0, grok_positive_pct=17.4,
                   gemma_negative_pct=73.8, grok_negative_pct=78.4, gemma_uncertain_pct=0.8, grok_uncertain_pct=2.6)

vol_ratio1 = round(exp1_stats['gemma_mean_absdiff']/exp1_stats['grok_mean_absdiff'],2)
vol_ratio2 = round(exp2_stats['gemma_mean_absdiff']/exp2_stats['grok_mean_absdiff'],2)
vol_ratio3 = round(exp3_stats['gemma_mean_absdiff']/exp3_stats['grok_mean_absdiff'],2)
print("vol ratios:", vol_ratio1, vol_ratio2, vol_ratio3)

dims = json.load(open('report_data.json'))['dims']

# persistent disagreement across NEW exp0,1,2,3 (all four must show gap>=1)
gap0=(g0-r0).abs(); gap1=(g1-r1).abs(); gap2=(g2-r2).abs(); gap3=(g3-r3).abs()
valid4 = gap0.notna() & gap1.notna() & gap2.notna() & gap3.notna()
persistent = valid4 & (gap0>=1) & (gap1>=1) & (gap2>=1) & (gap3>=1)
n_persistent = int(persistent.sum())
pct_persistent = round(n_persistent/500*100,1)
print("persistent:", n_persistent, pct_persistent)

out = dict(
    exp0=exp0_stats, exp1=exp1_stats, exp2=exp2_stats, exp3=exp3_stats, exp4=exp4_stats,
    vol_ratio1=vol_ratio1, vol_ratio2=vol_ratio2, vol_ratio3=vol_ratio3,
    dims=dims, n_persistent=n_persistent, pct_persistent=pct_persistent,
)
json.dump(out, open('report_data_v2.json','w'), indent=1)
print("saved report_data_v2.json")
