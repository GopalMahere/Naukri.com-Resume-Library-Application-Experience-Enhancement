# One Profile, Multiple Resumes
### A Candidate-Controlled Resume Library for Naukri.com

[![Live Presentation](https://img.shields.io/badge/Live_Presentation-GitHub_Pages-1856EA?style=for-the-badge&logo=github)](https://gopalmahere.github.io/Naukri.com-Resume-Library-Application-Experience-Enhancement/)
[![Author](https://img.shields.io/badge/Prepared_by-Aditya_Sharma-0B1B3D?style=for-the-badge)](https://github.com/GopalMahere)
[![Format](https://img.shields.io/badge/Format-Interactive_Digital_Presentation-059669?style=for-the-badge)](#)
[![Deck](https://img.shields.io/badge/Slides-15_Interactive_Screens-D97706?style=for-the-badge)](#)

---

## 🌐 Live Presentation & Shareable Link

> **View the Live Interactive Deck:**  
> 🔗 **[https://gopalmahere.github.io/Naukri.com-Resume-Library-Application-Experience-Enhancement/](https://gopalmahere.github.io/Naukri.com-Resume-Library-Application-Experience-Enhancement/)**

*Tip: You can also clone this repository and open `index.html` directly in any desktop or mobile browser. It is 100% self-contained with zero external dependencies.*

---

## 📌 Executive Summary

Candidates frequently apply across diverse career paths (e.g., Product Management, Consulting, Operations, and Core Tech). Today, candidates maintain different tailored resumes, but switching or managing them during the portal application journey can introduce friction: candidates often have to leave an active application flow, navigate to profile settings, and overwrite their current profile document.

**"One Profile, Multiple Resumes"** solves this by establishing a dedicated, candidate-controlled **Resume Library** inside Naukri.com:
1. **One Central Profile:** Preserves the candidate's single structured profile as the master source of truth for recruiter search (Resdex).
2. **Dedicated Resume Library:** Stores independent, user-named resume versions (e.g., *Product Management CV*, *Consulting CV*).
3. **Application-Time Selection:** Job seekers can pick an existing resume or upload a new one at the moment of application.
4. **Non-Destructive Saving:** An optional save checkbox appears **only after** an upload succeeds, allowing candidates to save the document as an independent library entry without overwriting existing files.
5. **Candidate Agency:** The system preselects the candidate's designated default resume for convenience, but **never submits without explicit review and confirmation**.

---

## 🔍 Problem Discovery & Research Signals

* **Multi-Role Job Search Reality:** Based on our exploratory survey of **45 college students**:
  * **90%** applied for jobs, internships, or placements in the last 90 days.
  * **80%** were looking for placements/full-time roles; **20%** were looking for internships.
  * **80%** applied across **3 or more distinct role types** simultaneously (60% applied to 4+ role tracks).
  * **90%** actively maintain multiple resume versions.
  * **90%** frequently need a resume different from their current profile document when applying.
* **Observed User Friction:** When a candidate clicks *Apply* and realizes an alternate resume is needed, they are forced to leave the flow or risk overwriting active profile files.
* **Competitive Benchmarking:**
  * **Naukri.com:** Official FastForward FAQ documents up to 5 profiles per username (1 resume per profile) for text/visual CV packages. Separate tools have specific limits (AI maker: 1 CV; online builder FAQ: up to 50 drafts).
  * **LinkedIn:** Stores up to 4 recently uploaded reusable resumes for *Easy Apply* flows; allows viewing submitted versions in history.
  * **Indeed India:** Stores 1 profile resume file on the account (replacing previous uploads), while allowing candidates to upload an alternate file during the application process.

---

## 💡 The Proposed Architecture

```
                  ┌──────────────────────────────────────────────┐
                  │          Comprehensive Naukri Profile        │
                  │   (Single Master Record: Education, Skills)  │
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

---

## 🛠️ Interactive Prototype & Scenarios

The presentation includes an embedded, client-side interactive prototype (Slide 11) demonstrating end-to-end user flows with zero backend required:

| Preset Scenario | Key User Experience Tested |
| :--- | :--- |
| **1. Single-Resume Quick Apply** | If a candidate has only 1 saved resume, the interface preserves existing streamlined quick-apply with an inline "Upload New Resume" option. |
| **2. Multi-Resume Selector** | When multiple resumes exist, dynamically displays saved CVs with their custom names, filenames, update timestamps, and designated default preselection. |
| **3. Scenario A: Apply-Only Upload** | Candidate uploads a new file (`Product_Analyst_v2.pdf`). The save checkbox appears only post-upload. Left **unchecked**, it applies to the current job only; the library count remains at 4. |
| **4. Scenario B: Upload & Save** | Candidate checks the save box. Mandatory custom naming validation is enforced. Upon submission, the document is saved as a 5th independent entry without overwriting existing files. |
| **⭐ Default Preference & History** | Candidates can designate any library item as default. The simulated *Application History Log* records immutable version snapshots. |

---

## 📊 Experimentation & Measurement Framework

To validate whether reducing resume-switching friction improves application conversion without compromising user trust:

* **Primary Success Metric:**
  $$\text{Application Completion Rate} = \frac{\text{Completed Applications}}{\text{Application Starts}}$$
* **Secondary Diagnostic Metrics:**
  * Multi-resume adoption (% managing $\ge 2$ resumes)
  * Selection distribution (existing vs. on-the-fly upload)
  * Save adoption rate (% saving new uploads)
  * Funnel abandonment rate & Time-to-apply
* **Guardrail Metrics:**
  * Accidental overwrite incidents (**strictly zero tolerance**)
  * Wrong-resume submission support tickets
  * Upload failure rates & external redirect drop-off
* **Rollout Roadmap:**
  * **Phase 1:** Internal Alpha & Document Reference QA
  * **Phase 2:** Limited Closed Beta (eligible multi-track applicants)
  * **Phase 3:** Controlled A/B Experiment
  * **Phase 4 & 5:** Iteration & Gradual Production Scale

---

## 📂 Repository File Structure

```
├── index.html          # Compiled, single-file interactive HTML presentation
├── build_deck.py       # Python compiler script assembling modules into index.html
├── styles.py           # CSS styling system, responsive grid & prototype UI styles
├── slides_part1.py     # Slides 01–05: Cover, Exec Summary, Problem, Journey, Survey
├── slides_part2.py     # Slides 06–10: Benchmarking, Solution, Workflow, UI Mockups, PRD
├── slides_part3.py     # Slides 11–15: Prototype, Experimentation, Business Model, Closing, Appendix
├── scripts_js.py       # Client-side presentation controls & interactive prototype logic
├── .gitignore          # Git ignore rules for temporary build artifacts
└── README.md           # Project documentation and product overview
```

### 💻 Running Locally

Simply double-click `index.html` or open it in your browser:
```bash
# Optional: recompile the deck from source files
python build_deck.py
```

### ⌨️ Presentation Keyboard Shortcuts

* **`→` / `Space` / `Page Down`**: Next slide
* **`←` / `Page Up`**: Previous slide
* **`N`**: Toggle Speaker Notes panel
* **`G`**: Open Slide Grid modal (jump to any slide)
* **`O` / `E`**: Open Evaluator & Review Guide
* **`F`**: Toggle Fullscreen
* **`Esc`**: Close any active modal

---

## 👤 Author & Project Scope

* **Prepared by:** Aditya Sharma
* **Format:** Independent Product Management Case Study
* **Scope:** Problem Discovery, Primary Survey Analysis (N=45), Competitive Benchmarking, UX/UI Specifications, Product Requirements Document (PRD), Interactive Prototype & Controlled Experiment Design.
* **Target Platform:** Naukri.com (Desktop Web & Mobile Web)
