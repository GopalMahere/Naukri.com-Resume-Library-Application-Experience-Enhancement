# Naukri.com – Apply with the Right Resume
### A candidate-controlled Resume Library proposal for improving the job application experience.

[![Live Presentation](https://img.shields.io/badge/Live_Presentation-GitHub_Pages-1856EA?style=for-the-badge&logo=github)](https://gopalmahere.github.io/Naukri.com-Resume-Library-Application-Experience-Enhancement/)
[![Author](https://img.shields.io/badge/Prepared_by-Aditya_Sharma-0B1B3D?style=for-the-badge)](https://github.com/GopalMahere)
[![Project](https://img.shields.io/badge/Type-Independent_PM_Investigation-059669?style=for-the-badge)](#)
[![Deck](https://img.shields.io/badge/Slides-23_Interactive_Screens-D97706?style=for-the-badge)](#)

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

The investigation follows an iterative 9-stage Product Management lifecycle:

```
[Discover]  ──▶  [Define]    ──▶  [Research]  ──▶  [Validate]  ──▶  [Diagnose]
Problem Signal   JTBD & Scope     N=45 Survey     Evidence Audit   Root Causes
      │
      ▼
  [Assess]   ──▶  [Design]    ──▶  [Test]      ──▶  [Deliver]
5 Options         3 Pillars        Controlled A/B   Risks, Stages
Competitors       PRD & Prototype  Metrics Hierarchy & Feedback Request
```

1. **Problem Discovery:** Capturing firsthand candidate observations during multi-track job applications.
2. **Problem Definition:** Establishing the Job-to-be-Done (JTBD), user needs, and scoping boundaries.
3. **User Research:** Formulating 7 research questions and running an exploratory survey (N=45).
4. **Problem Validation:** Auditing supported evidence against unverified platform-side questions.
5. **Root-Cause Diagnosis:** Separating surface symptoms from 5 underlying structural hypotheses.
6. **Market & Competitor Analysis:** Benchmarking official documentation from Naukri, LinkedIn, and Indeed India.
7. **Opportunity Assessment:** Evaluating 5 strategic alternatives (Options A–E) on feasibility and candidate control.
8. **Solution Design & PRD:** Specifying the Resume Library, decision logic, MoSCoW requirements, and testable acceptance criteria.
9. **Testing & Recommendation:** Designing a controlled A/B pilot, metric hierarchy, risk mitigations, and request for Naukri PM review.

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

Slide 16 embeds a complete client-side candidate simulator testing six key flows:

* **Flow A (One Saved Resume):** Preserves existing quick-apply speed by pre-attaching the single resume, with inline "Change Resume" and "+ Upload New Resume" options.
* **Flow B (Multiple Resumes):** Displays saved documents with custom names, dates, and preselects the designated default. *Strictly requires explicit candidate review before submission.*
* **Flow C (Apply-Only Upload):** Candidate uploads a new document. The save checkbox appears **only post-upload**. Left unchecked, it applies to this job only; library count remains at 4.
* **Flow D (Upload & Save):** Candidate checks the save box. Mandatory custom name validation is enforced. Saved as a 5th independent entry without modifying existing files.
* **Flow E (Duplicate Filenames):** Two files named `Resume.pdf` receive distinct internal UUIDs; duplicate filenames never trigger silent overwrites.
* **Flow F (Submitted History):** The *Application History Log* retains an immutable version snapshot independently of future library edits or deletions.

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
├── index.html           # Compiled, self-contained 23-slide interactive presentation
├── build_deck.py        # Python build script compiling modular source files into index.html
├── styles.py            # CSS design system, responsive breakpoints, lifecycle tracks & badges
├── slides_discovery.py  # Slides 01–06: Cover, Overview, PM Approach, Origin, Users, JTBD/Definition
├── slides_research.py   # Slides 07–12: Research Methodology, Survey Data, Journey, Validation, Root Causes, Competitors
├── slides_solution.py   # Slides 13–17: Alternatives, 3 Pillars, 11-Step Logic, Interactive Prototype, PRD & MVP
├── slides_strategy.py   # Slides 18–23: A/B Testing, Risks/Roadmap, Recommendation, Appendices A, B & C
├── scripts_js.py        # Presentation controls, keyboard navigation & interactive prototype engine
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
* **`N`**: Toggle Speaker Notes drawer (detailed speaking guidance)
* **`G`**: Open Slide Overview Grid (jump to any of the 23 slides)
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
