# Problem Definition & User Journey Audit

> **Core Discipline:** This document strictly defines the user problem encountered on Naukri.com. Proposed solutions live separately in `product-requirements-prd.md` so the problem is never confused with a feature pitch.

## 1. The Actual Problem Faced on Naukri.com
Job seekers frequently apply to opportunities across multiple role tracks that require distinct, tailored resumes (for example, a **Product Management CV** vs. a **Consulting CV**).

In the standard Naukri.com application experience encountered by the candidate:
1. Only **one resume** can be uploaded to the main profile at a time.
2. Clicking **Apply** immediately submits that active profile resume without asking which version the candidate wants to send.

## 2. The 5-Step Friction Detour
To apply to a role that requires a different CV version, a candidate must:
1. Leave the job application and navigate to their Naukri profile.
2. Replace their currently uploaded resume with the alternative version.
3. Return to the job search page.
4. Search for and locate the same job listing again.
5. Restart the application process.

**Consequences:**
- The job listing may disappear, expire, or become difficult to find again.
- The loop repeats every time the candidate switches between role tracks during a job search session.

## 3. Secondary Connected Problem: Post-Application Resume Blindness
When candidates overwrite their profile resume repeatedly to apply for different roles, they lose track of which CV version was sent to which employer. Without an **application-wise resume record**, candidates struggle to prepare accurately once recruiters reach out for interviews.

## 4. Core Problem Statement
> **Candidates do not have sufficient flexibility and control over resume selection and resume tracking throughout their job application journey.**
