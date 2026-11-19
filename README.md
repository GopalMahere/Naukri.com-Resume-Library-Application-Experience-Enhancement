# Naukri.com – Apply with the Right Resume
### A candidate-controlled Resume Library proposal for improving the job application experience.

[![Live Presentation](https://img.shields.io/badge/Live_Presentation-GitHub_Pages-1856EA?style=for-the-badge&logo=github)](https://gopalmahere.github.io/Naukri.com-Resume-Library-Application-Experience-Enhancement/)
[![Author](https://img.shields.io/badge/Prepared_by-Aditya_Sharma-0B1B3D?style=for-the-badge)](https://github.com/GopalMahere)
[![Project](https://img.shields.io/badge/Type-Independent_PM_Investigation-059669?style=for-the-badge)](#)
[![Deck](https://img.shields.io/badge/Slides-16_Interactive_Screens-D97706?style=for-the-badge)](#)

---

## 🌐 Live Presentation & Shareable Link

> **Open the Interactive Presentation:**  
> 🔗 **[https://gopalmahere.github.io/Naukri.com-Resume-Library-Application-Experience-Enhancement/](https://gopalmahere.github.io/Naukri.com-Resume-Library-Application-Experience-Enhancement/)**

*This presentation is self-contained in `index.html`. It runs directly in any modern desktop, laptop, tablet, or mobile browser with zero external framework dependencies.*

---

## 📌 Project Overview & Origin

This project began with a candidate-side problem encountered during job applications. While applying across different role categories (such as Product Management, Consulting, Operations, and Core Tech), the author maintained tailored resume versions for different opportunities. However, when the document to be submitted differed from the resume associated with the candidate's profile, managing that change could add extra steps or disrupt the application flow.

Rather than jumping directly to an assumed solution, this project follows an **investigation-first Product Management lifecycle**: examining candidate behaviour, collecting exploratory survey data, auditing competitor capabilities, separating established facts from unanswered questions, evaluating alternatives, and developing a structured product proposal for Naukri.com.

> **Independent Project Disclaimer:**  
> This is an independent Product Management case study prepared by Aditya Sharma. It is not an official Naukri.com project, and Info Edge / Naukri.com has neither endorsed nor validated this proposal. The proposed solution is designed as a candidate-side improvement for discussion with Naukri's product team.

---

## 🔄 Product Management Process Followed

The presentation communicates the complete product argument in **10–12 minutes** across **13 core slides + 3 comprehensive appendices (16 total slides)**:

```
[Discover]  ──▶  [Define]    ──▶  [Research]  ──▶  [Validate]  ──▶  [Diagnose]
Problem Signal   JTBD & Scope     N=45 Survey     Evidence Audit   Root Causes
      │
      ▼
   [Assess]  ──▶  [Design]    ──▶  [Test]      ──▶  [Deliver]
5 Options         3 Pillars        Prototype        MVP Scope, Controlled A/B
Competitors       Workflow Gate    Simulation       Metrics & Feedback Request
```

### 16-Slide Structure (13 Core + 3 Appendices)
1. **Slide 01 (Cover):** *Naukri.com – Apply with the Right Resume* (Hero hook, Aditya Sharma metadata, conceptual flow illustration).
2. **Slide 02 (Executive Summary):** *What This Investigation Is About* (6-part structured summary: Origin, Friction, Survey N=45, Validation limits, Opportunity, Recommendation).
3. **Slide 03 (Origin & Target Users):** *Where the Idea Started — Understanding the Candidate* (`[PERSONAL OBSERVATION]` grounding, multi-role reality for PM/Consulting/Ops/Tech, student & career-changer segmentation).
4. **Slide 04 (Problem Definition):** *Defining the Actual Candidate Problem* (Core JTBD, 4-box framing: User/Situation/Need/Outcome, Resume Management vs Writing boundary).
5. **Slide 05 (User Research Findings):** *What We Learned from the Respondents* (N=45 survey data, role-category distribution chart, qualitative motivations & workarounds, explicit research limits).
6. **Slide 06 (Current Journey):** *Where Resume Management Can Interrupt the Application Journey* (Common journey, Path A in-flow upload, Path B profile redirect friction, Path C external ATS).
7. **Slide 07 (Validation & Root Causes):** *What the Evidence Supports — and What We Still Need to Investigate* (Section A: Evidence Audit [Supported vs Requires Validation]; Section B: 5 Root-Cause Hypotheses).
8. **Slide 08 (Competitor Benchmarking):** *How Existing Platforms Handle Resume Selection* (Naukri FastForward CV vs builder nuances, LinkedIn 4 reusable CVs, Indeed India 1 stored CV + apply-time upload).
9. **Slide 09 (Strategic Alternatives):** *Which Product Approach Best Addresses the Problem?* (Qualitative matrix of Options A–E; justification for Option D Resume Library; AI matching out of scope for MVP).
10. **Slide 10 (Proposed Solution):** *A Resume Library Built Around Candidate Choice* (3 Pillars: Comprehensive Profile, Dedicated Library, Apply-Time Selector; 5 Principles: Control, Privacy, Independence, No Overwrite, History).
11. **Slide 11 (Future Workflow & Logic):** *How the Proposed Experience Would Work* (11-step pipeline, prominent conditional save gate post-upload, quick-apply path, default preselection with review, duplicate filename handling).
12. **Slide 12 (UX Design & Interactive Prototype):** *From Product Concept to Candidate Experience* (6 desktop UI screens, embedded interactive candidate simulator with 4 scenario presets, set default, reset, and sanitized demo data).
13. **Slide 13 (MVP, Experimentation & Recommendation):** *From Product Proposal to Product Validation* (Consolidated closing slide: A. Compact MVP Must vs Future; B. Controlled A/B Experiment & Completion Rate formula; C. 5-Stage Rollout Plan; Closing recommendation & PM feedback invitation).
14. **Appendix A (Slide 14):** *Appendix A: Complete User Research & Methodology* (Full Q1–Q13 survey data catalog, respondent profile, motivations, workarounds, stated preferences, limitations).
15. **Appendix B (Slide 15):** *Appendix B: Official Competitor Documentation & Links* (Naukri, LinkedIn, Indeed India official URLs, verified retrieval dates, supported claims, scope limitations).
16. **Appendix C (Slide 16):** *Appendix C: Product Specification & Technical Considerations* (Detailed functional requirements, Must/Should/Could priorities, Given/When/Then acceptance criteria, conditional save logic, duplicate filename handling, upload failure behaviour, privacy/security, technical dependencies, terms & assumptions glossary).

---

## 🎯 Candidate Problem & Job-to-be-Done (JTBD)

### The Job-to-be-Done
> *"When I apply to different types of roles, I want to choose the resume that best represents my relevant experience while keeping my other versions intact, so I can submit the document I intend without repeatedly managing profile files."*

### Formal Problem Statement
> *"Candidates who maintain multiple role-specific resumes need a simple and reliable way to select the intended document during supported job application flows, without repeatedly replacing or losing access to other versions."*

* **In Scope:** Document management, custom version naming, apply-time selection, post-upload conditional saving, and immutable submitted history tracking.
* **Explicitly Out of Scope:** AI resume generation, automated bullet point rewriting, and algorithmic matching.

---

## 📊 Exploratory User Research (N=45)

We conducted an exploratory survey of **45 college students** to investigate candidate habits:

| Research Signal | Reported Survey Finding | Context & Limitations |
| :--- | :--- | :--- |
| **Recent Activity (Q1)** | **90%** applied for jobs/internships in last 90 days | Active applicant pool |
| **Cohort Profile (Q2)** | **80%** full-time / placements; **20%** internships | Student-focused sample; does not represent working professionals |
| **Role Breadth (Q3)** | **80%** apply across $\ge 3$ distinct role categories | 60% apply to 4+ roles; 20% to 3 roles; 15% to 2 roles; 5% to 1 role |
| **Multiple Versions (Q4)** | **90%** maintain tailored resume versions | High prevalence of role-specific documents |
| **Friction Frequency (Q7)** | **90%** frequently need alternate CV while applying | Demonstrates frequent divergence between profile CV and job target |
| **Feature Valuation (Q11)** | **90%** rated the concept *"Extremely useful"* | Stated candidate preference (exploratory indicator, not observed adoption) |
| **Adoption Likelihood (Q12)** | **90%** reported being *"Very likely"* to use it | Stated intent |

* **Research Integrity Note:** These percentages reflect the exploratory student cohort. They do not prove platform-wide demand, nor do they establish that 90% of all Naukri users experience this problem.

---

## ⚖️ Evidence Audit: Established vs. Unverified

| Supported by Current Evidence | Requires Naukri Validation |
| :--- | :--- |
| • Multiple resume versions are common in surveyed student cohort (90%).<br>• Candidates frequently need an alternate resume when applying (90%).<br>• Multi-category job searching is high (80% apply to 3+ roles).<br>• Competitor platforms document resume reuse and apply-time uploading.<br>• Firsthand observation confirmed application-time friction in studied flows. | • Exactly how widespread this problem is across Naukri's full candidate base.<br>• What proportion of applications on Naukri follow direct vs. external redirect flows.<br>• Which specific application types already support alternate file uploads.<br>• Whether candidates actually abandon applications due to this issue.<br>• Whether a Resume Library measurably lifts application completion rates.<br>• Technical constraints governing document versioning in Naukri's backend. |

---

## 🔍 Competitor Benchmarking (Official Documentation)

* **Naukri.com:** FastForward FAQ documents up to 5 profiles per username (1 resume per profile) specifically for text/visual CV packages. Separate tools have specific limits (AI maker creates 1 CV; Online Builder FAQ notes up to 50). *We do not treat tool-specific limits as universal application profile rules.*
* **LinkedIn:** Official documentation confirms storing up to 4 recently uploaded reusable resumes for *Easy Apply* flows, and viewing submitted resumes in history. *Does not carry over to external employer redirects.*
* **Indeed India:** Official documentation confirms storing 1 resume file on an account (uploading replaces existing), but allows uploading an alternate resume during the application process.

---

## 💡 The Proposed Feature: Resume Library

The proposed solution consists of three complementary pillars:

```
                  ┌──────────────────────────────────────────────┐
                  │          Comprehensive Naukri Profile        │
                  │       (Education, Experience, Skills)        │
                  └──────────────────────┬───────────────────────┘
                                         │
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │            Dedicated Resume Library          │
                  │  ┌──────────────┐ ┌──────────────┐ ┌───────┐ │
                  │  │ PM Resume.pdf│ │Consulting.pdf│ │ ...   │ │
                  │  └──────────────┘ └──────────────┘ └───────┘ │
                  └──────────────────────┬───────────────────────┘
                                         │
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │      Moment-of-Application Selector          │
                  │  🔘 Preselects Default (Explicit Review Req) │
                  │  ⚪ Select Alternate Saved Resume            │
                  │  ➕ Upload New Resume                        │
                  └──────────────────────┬───────────────────────┘
                                         │
                        ┌────────────────┴────────────────┐
                        ▼                                 ▼
              [Unchecked: App-Only]            [Checked: Save to Library]
              Used for current job only        Prompt mandatory custom name
              Zero changes to library          Saved as new independent entry
```

> **Data Architecture Note:**  
> The proposed design keeps the candidate's structured profile conceptually separate from independently managed resume documents. Integration with Naukri's recruiter-search architecture requires product and engineering validation.

---

## 🛠️ Interactive Prototype & Scenarios

Slide 12 embeds a complete client-side candidate simulator testing key candidate flows:

* **Single-Resume Quick Apply:** Preserves existing quick-apply speed by pre-attaching the single resume, with inline "Change Resume" and "+ Upload New Resume" options.
* **Multi-Resume Selector:** Displays saved documents with custom names, dates, and preselects the designated default. *Strictly requires explicit candidate review before submission.*
* **Scenario A (Apply-Only Upload):** Candidate uploads a new document. The save checkbox appears **only post-upload**. Left unchecked, it applies to this job only; library count remains at 4.
* **Scenario B (Upload & Save):** Candidate checks the save box. Mandatory custom name validation is enforced. Saved as a 5th independent entry without modifying existing files.
* **Duplicate Filenames:** Two files named `Resume.pdf` receive distinct internal UUIDs; duplicate filenames never trigger silent overwrites.
* **Submitted History:** The *Application History Log* retains an immutable version snapshot independently of future library edits or deletions.

---

## 📈 Experimentation & Metrics Framework

To establish whether the feature improves candidate conversion:

* **Primary Metric:**
  $$\text{Application Completion Rate} = \frac{\text{Completed Applications}}{\text{Application Starts}}$$
* **Secondary Diagnostic Metrics:** Resume Library adoption (% managing $\ge 2$ CVs), selection distribution (existing vs. new upload), save adoption rate, time-to-apply, abandonment rate, CSAT.
* **Guardrail Metrics:** Accidental overwrite incidents (**strictly zero tolerance**), wrong-resume support tickets, technical upload failures, funnel deterioration.
* **Statistical Parameters:** Minimum Detectable Effect (MDE), statistical power, required sample size, and duration must be defined by internal analytics based on baseline traffic and variance.

---

## 📂 Repository File Structure

```
├── index.html           # Compiled, self-contained 16-slide interactive presentation (13 core + 3 appendices)
├── build_deck.py        # Python build script compiling modular source files into index.html
├── styles.py            # CSS design system, responsive breakpoints, lifecycle tracks, cards & badges
├── slides_discovery.py  # Slides 01–04: Cover, Executive Summary, Origin & Target Users, Problem Definition & JTBD
├── slides_research.py   # Slides 05–08: User Research (N=45), Current Journey, Validation & Root Causes, Competitors
├── slides_solution.py   # Slides 09–12: Alternatives, Solution Pillars, Workflow & Logic, UX & Interactive Prototype
├── slides_strategy.py   # Slides 13–16: MVP & Validation, Appendix A, Appendix B, Appendix C
├── scripts_js.py        # Presentation controls, keyboard navigation & interactive prototype engine
├── test_verify.py       # Automated QA verification script
├── .gitignore           # Git ignore rules for build artifacts
└── README.md            # Investigation documentation and product proposal
```

### 💻 Running Locally

Simply open `index.html` in your web browser:
```bash
# Optional: recompile the deck from source Python modules
python build_deck.py
```

### ⌨️ Presentation Keyboard Shortcuts

* **`→` / `Space` / `Page Down`**: Next slide
* **`←` / `Page Up`**: Previous slide
* **`N`**: Toggle Speaker Notes drawer (detailed speaking guidance & suggested times)
* **`G`**: Open Slide Overview Grid (jump to any of the 16 slides)
* **`O` / `E`**: Open Evaluator Guide & Executive Brief
* **`F`**: Toggle Fullscreen presentation mode
* **`Esc`**: Close active modals

---

## 👤 Author & Invitation for Product Review

* **Prepared by:** Aditya Sharma
* **Project Type:** Independent Product Discovery & Improvement Proposal
* **Platform:** Naukri.com — Candidate Experience
* **Contact & Feedback:**  
  *"I would welcome feedback from Naukri's Product Management team on the problem definition, current application behaviour, and suitability of this proposed improvement."*
