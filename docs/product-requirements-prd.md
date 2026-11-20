# Product Requirements Document (PRD): Resume Library & Smart Apply

## 1. Objective
Give Naukri.com job seekers full control over **resume selection at apply time** and **resume tracking post-application**, while preserving 1-click speed for single-CV users and protecting B2B recruiter search quality on **Resdex**.

## 2. Core Capabilities

### A. Multi-Resume Library (Profile)
- Store up to **5 labeled resume versions** (PDF/DOCX) tagged by target role track (e.g., Product Management, Consulting, Analytics).
- **Resdex Default Toggle:** Exactly one resume is marked as the **Primary Profile Resume** indexed by Resdex for inbound recruiter searches. Secondary CVs stay private to outbound applications.

### B. In-Flow Smart Apply Picker + Instant Fresh Upload
- **1-CV Fast Path:** Users with only 1 saved resume experience zero extra clicks (no modal).
- **Multi-CV Picker:** Users with ≥2 resumes see a lightweight in-flow modal/bottom sheet on *Apply* highlighting the best role-tag match.
- **Upload Fresh / New Resume:** Candidates can upload a tailored CV on the spot without leaving the job listing.
  - Immediately after uploading, a checkbox appears: *"Would you like to save this new CV in your main Resume Library?"*
  - **Checked:** Saved to the main Resume Library (up to 5 slots) and submitted.
  - **Unchecked:** Submitted for this single job only without cluttering the main Resume Library.

### C. Application-Wise Immutable CV Tracker
- Every submitted application logs an immutable snapshot (`resume_version_id` + file copy) under **Applied Jobs**.
- Editing or deleting a file from the Resume Library later never alters or breaks historical application records.

### D. Naukri 360 / AI Resume Maker Sync
- Adds a one-click **"Save to Resume Library"** action inside Naukri's AI Resume Builder (270K monthly AI resume downloads per Info Edge's 31st AGM), closing the loop between AI resume creation and core job applications.

## 3. Phased Rollout Plan
1. **Phase 1 (MVP — Weeks 1–6):** 5-CV Resume Library, Resdex Default isolation, In-Flow Apply Picker + Instant Fresh Upload with save-to-library checkbox.
2. **Phase 2 (Retention — Weeks 7–12):** Immutable Application CV Ledger in Applied Jobs + Naukri 360 / Campus AI Resume Maker sync.
3. **Phase 3 (AI Differentiation — Q2+):** Automated JD-to-CV match scoring inside the Apply picker.
