# Success Metrics, Guardrails & A/B Experiment Plan

## 1. Proposed KPI Framework

### North Star Metric
- **Multi-Role Application Completion Rate:** Percentage of *Apply* clicks resulting in completed submissions among job seekers who browse ≥2 distinct job categories in a 14-day window.

### Secondary Adoption & Engagement Metrics
- **Resume Library Adoption:** % of active job seekers saving ≥2 resume versions.
- **Active CV Switching Rate:** % of applications submitted using a non-default or freshly uploaded CV.
- **Instant Upload Save-Through Rate:** % of fresh in-flow uploads where candidates opt in to save the CV to their main library.
- **Tracker Utility:** Click-through rate on *"View Submitted CV"* inside Applied Jobs.

### Guardrail Metrics (Zero Regression Required)
- **Single-CV Apply Latency & Conversion:** Zero increase in time-to-apply or drop-off for candidates with 1 resume.
- **Recruiter Signal Quality (Resdex & Responses):** Maintain or improve recruiter shortlist and CV download rates.
- **Profile Overwrite Churn:** Measurable reduction in repeated same-day profile resume replacements.

## 2. Proposed A/B Experiment Design
- **Cohort:** Randomized split of active job seekers searching across ≥2 role categories (Web + Android/iOS).
- **Duration:** 4 weeks to capture full apply-to-recruiter-response cycles.
- **Decision Gate:** Ship to 100% if multi-role apply completion improves with zero statistically significant regression on single-CV apply conversion or recruiter shortlist rates.
