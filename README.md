# Naukri.com — Resume Library & Smart Apply
### Product Teardown, Primary User Research & Interactive UX Prototype

🌐 **Live Interactive Presentation (GitHub Pages)**
- 🖥️ [Interactive 11-Slide Presentation & Live Smart Apply Prototype](https://gopalmahere.github.io/Naukri.com-Resume-Library-Application-Experience-Enhancement/)

---

## 1. Project Mission & Business Context

This repository presents a **problem-first Product Management case study** built for **Naukri.com (Info Edge India Ltd.)** to resolve a high-friction gap in the candidate job-application journey: how to give multi-role job seekers full control over **resume selection during Apply** and **resume tracking post-application**—without adding latency for single-CV users or disrupting B2B recruiter search on **Resdex**.

Rather than a static slide deck, this project delivers a **self-contained 11-slide interactive web presentation** with a **live clickable Smart Apply prototype**, grounded in Info Edge's public disclosures, primary survey data from **100+ Indian college students**, and an automated DOM verification suite.

### The Strategic Disconnect on Naukri.com
- **Massive Platform & AI Resume Scale:** Naukri holds **106 million resumes** (22,000 added daily in Q4FY25 — [Info Edge Q4FY25 Presentation](https://www.infoedge.in/pdfs/corporatePresentations_pdfs/Info-Edge-May25-Presentation.pdf)), generates **270,000 monthly AI-powered resume downloads** ([Info Edge 31st AGM, Aug 2026](https://www.infoedge.in/pdfs/Report_filings/AGM-proceedings-31.pdf)), and reached an **~₹240 Cr annualized AI Recruitment billings run rate** in Q2FY27 ([Info Edge Q2FY27 Presentation](https://www.infoedge.in/pdfs/corporatePresentations_pdfs/Info-Edge-Oct26-Presentation.pdf)).
- **The Internal Product Gap:** [Naukri Career Guidance](https://www.naukri.com/campus/career-guidance/how-to-tailor-resume-for-job-applications) advises candidates to tailor resumes for each application, and [Naukri Campus Resume Maker](https://www.naukri.com/campus/career-guidance/how-to-write-a-resume-for-freshers) lets students build multiple CVs—yet the core **Apply** flow submits only the single resume stored on the main profile without asking which version to send.

---

## 2. Problem Architecture & Journey Comparison

### Current Flow (6 Steps · High Friction & Drop-Off Risk)
```text
Spot Role-Specific Job (e.g., Consulting while PM CV is active)
  │
  ├── 1. Abandon Job Listing (Apply submits active profile CV without asking)
  ├── 2. Open Naukri Profile → Resume Section
  ├── 3. Overwrite Existing Profile CV (hurts inbound continuity)
  ├── 4. Return to Job Search (lose filters & scroll position)
  ├── 5. Re-find the Exact Same Job (risk of listing disappearing)
  └── 6. Apply → No Application-Wise Record of Which CV Was Sent
```

### Proposed Flow (2 Steps · Zero Context Switch)
```text
Click "Apply Now" on Job Card
  │
  ├── 1. In-Flow Smart Apply Picker Opens Over Listing
  │     ├── Option A: Pick from Saved Resume Library (up to 5 role-tagged CVs; Resdex Default stays intact)
  │     └── Option B: Upload a Fresh / New CV on the Spot
  │           └── Dynamic Checkbox: "Save this new CV in main Resume Library?"
  │                 ├── Checked   → Stored in Resume Library + Submitted
  │                 └── Unchecked → One-time submission (not added to main library)
  │
  └── 2. Submit → Immutable CV Snapshot Logged Automatically in "Applied Jobs"
```

---

## 3. Primary User Research & Competitive Benchmark

### Primary Survey Findings (`n = 100+` Indian College Students)

| Survey Metric | Reported Result |
| :--- | :---: |
| Recently applied for jobs | **90%** |
| Apply across **3+ role categories** (`60%` apply to 4+ roles · `20%` apply to 3 roles) | **80%** |
| Maintain multiple resume versions | **90%** |
| Frequently need an alternative CV while applying | **90%** |
| Rated multi-resume selection "extremely useful" & "very likely to use" | **90%** |

> **Honest PM Caveat:** This survey measures self-reported experiences and interest among 100+ college students. It validates that the problem is worth investigating, but does not prove universal adoption across all Naukri cohorts—motivating the controlled 4-week A/B test defined in `docs/metrics-and-ab-experiment.md`.

### Competitive Benchmark Summary

| Capability | Naukri.com (Current) | Indeed India | LinkedIn Easy Apply | Naukri.com (Proposed) |
| :--- | :--- | :--- | :--- | :--- |
| **Saved Resume Versions** | 1 profile resume | 1 file at a time ([Indeed Help](https://in.indeed.com/help/job-seekers/articles/11314976176141-faqs-creating-uploading-and-managing-a-resume-file)) | Up to 4 recent CVs ([Guide](https://www.cvchapchap.com/blog/upload-cv-to-linkedin)) | **Up to 5 role-tagged CVs + Resdex default** |
| **In-Flow Apply Picker** | No (exits to profile) | Upload different file from device | Pick saved or upload in modal | **1-click picker + instant fresh upload** |
| **Save-to-Library Choice** | N/A | Overwrites profile if replaced | Auto-saves last 4 (FIFO) | **Explicit user tickbox after fresh upload** |
| **Application-Wise CV Record** | Not surfaced per job | No historical version storage | Limited post-apply visibility | **Immutable CV snapshot per Applied Job** |

*Note: While Naukri FastForward documents up to 5 separate profiles (1 resume each), that is a distinct service rather than an integrated multi-resume picker inside standard Naukri job applications.*

---

## 4. Project Deliverables & Repository Map

```text
naukri-resume-library-case-study/
│
├── index.html                           # 11-Slide Interactive Digital Presentation & Live Prototype
├── README.md                            # Master Case Study Documentation & Executive Summary
├── validate_presentation.py             # Automated DOM, Slide & Link Integrity Audit Script
├── .gitignore                           # Clean repository exclusions
│
└── docs/
    ├── problem-definition.md            # Strict Problem-vs-Solution Framing & Detour Audit
    ├── user-research-and-benchmarks.md  # 100+ Student Survey Findings, Caveats & Competitor Matrix
    ├── product-requirements-prd.md      # Concise PRD: Library, Instant Upload, Resdex Guardrails & Rollout
    └── metrics-and-ab-experiment.md     # North Star KPI, Guardrails & 4-Week A/B Experiment Design
```

---

## 5. How to Run & Demonstrate the Deliverables

### Interactive Digital Presentation & Prototype (`index.html`)
- **Local Run:** Double-click `index.html` in any modern browser. Zero build step or server required.
- **Navigation Controls:** Use `←` / `→` keyboard arrows, the top slide indicator bar, or click **Live Prototype** to jump straight to Slide 7.
- **Key Prototype Workflows to Test (Slide 7):**
  1. **Pick a Saved CV:** Click **Apply Now** on any job card, notice the highlighted role-track match, and submit without leaving the job feed.
  2. **Instant Fresh Upload + Save Toggle:** Click **Apply Now** → select **Upload a Fresh / New Resume** → choose a PDF/DOCX (or click **Simulate Instant Upload**) → test submitting both *with* and *without* ticking **"Would you like to save this new CV in your main Resume Library?"**.
  3. **Resdex Default Isolation:** Open the **Resume Library** tab to add/delete CVs or switch which resume is marked **Resdex Default**.
  4. **Immutable CV Tracking:** Open the **Applied Jobs** tab and click **View Snapshot** to verify every application preserves the exact CV sent—even for one-time uploads or deleted library files.

---

## 6. Automated Verification & Quality Audit

Run the included Python audit script to verify slide sequencing, DOM/JavaScript ID coverage, and grounded external citations:

```bash
python3 validate_presentation.py
```

- **Result:** 100% PASS — confirms all 11 slides are sequentially indexed (`0..10`), 100% of JavaScript `getElementById` hooks map to unique static DOM IDs with zero broken references or duplicates, and all external references use verified HTTPS links.

---

## 7. Evidence Classification Standard

Every claim and metric in this repository is explicitly categorized by source reliability:
- **`[Published Filing]`** — Official Info Edge investor presentations & 31st AGM proceedings (106M resumes, 22K daily additions, 270K monthly AI resumes, ~₹240 Cr AI run rate).
- **`[Primary Research]`** — Direct survey of 100+ Indian college students conducted by the author (explicitly paired with self-reporting caveats).
- **`[Competitor Docs]`** — Public help documentation and guides for Indeed India, LinkedIn Easy Apply, and Naukri Campus.
- **`[Proposed Hypothesis]`** — Product architecture, 3-phase rollout, and A/B test KPIs framed strictly as proposals to validate in production.

---

## 8. Author & Contact

- **Author:** Aditya Sharma
- **Email:** `adityapandat2002@gmail.com`
- **Focus:** Product Management, User Research, Marketplace UX & Prototyping
- **Stack:** HTML5, Tailwind CSS, Vanilla JavaScript (ES6+), Lucide Icons, Python 3
