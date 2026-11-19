# slides_strategy.py - Slides 13 to 16 (MVP & Validation, Appendix A, Appendix B, Appendix C)

SLIDES_STRATEGY = [
    # SLIDE 13: MVP, EXPERIMENTATION & FINAL RECOMMENDATION (Consolidates old Slides 17, 18, 19, 20)
    {
        "id": "slide-13",
        "number": "13",
        "stage": "Deliver",
        "tag": "MVP, Validation & Recommendation",
        "evidenceType": "Proposed Solution",
        "title": "From Product Proposal to Product Validation",
        "subtitle": "Compact MVP scope, controlled experiment design, rollout plan, and recommendation for Naukri PMs",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 10px;">
          <!-- 3-Column Structured Grid: A (MVP), B (Experiment), C (Rollout) -->
          <div style="display: grid; grid-template-columns: 1fr 1.05fr 0.95fr; gap: 14px; flex: 1;">
            
            <!-- Column A: What Should Be Built First? (MVP Prioritization) -->
            <div class="card card-blue" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-blue">A. MVP Prioritization</span>
                  <span style="font-size: 11px; font-weight: 700; color: var(--naukri-blue);">Scope</span>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  What Should Be Built First?
                </div>
                
                <!-- Must-Have Scope -->
                <div style="background: white; border: 1.5px solid #BFDBFE; border-radius: 6px; padding: 8px 10px; margin-bottom: 6px;">
                  <div style="font-size: 10.5px; font-weight: 800; color: #1E3A8A; text-transform: uppercase; margin-bottom: 3px;">
                    ✓ Must-Have Core (MVP)
                  </div>
                  <ul style="font-size: 10.5px; color: var(--slate-700); padding-left: 14px; line-height: 1.35; margin: 0;">
                    <li>Store up to 5 independent resumes in library</li>
                    <li>Mandatory custom naming (e.g. PM CV)</li>
                    <li>Application-time resume selector modal</li>
                    <li>In-flow upload of fresh resume document</li>
                    <li><strong>Conditional save checkbox</strong> (post-upload)</li>
                    <li>Strict non-destructive saving (no overwrites)</li>
                    <li>Pre-submission review and confirmation</li>
                    <li>Immutable document reference in history</li>
                  </ul>
                </div>

                <!-- Future Scope -->
                <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 6px 10px;">
                  <div style="font-size: 10.5px; font-weight: 700; color: var(--slate-600); text-transform: uppercase; margin-bottom: 2px;">
                    ⏳ Future Scope (Post-MVP)
                  </div>
                  <div style="font-size: 10px; color: var(--slate-500); line-height: 1.35;">
                    • In-library rename & delete controls<br>
                    • Explicit document replacement flows<br>
                    • Candidate-designated default preference
                  </div>
                </div>
              </div>

              <div style="font-size: 10px; color: var(--naukri-blue); margin-top: 4px; font-weight: 600;">
                Detailed Given/When/Then acceptance criteria in Appendix C.
              </div>
            </div>

            <!-- Column B: How Would We Know It Works? (A/B Experiment) -->
            <div class="card card-teal" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-teal">B. Experiment Design</span>
                  <span style="font-size: 11px; font-weight: 700; color: var(--teal-accent);">Evaluation</span>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  How Would We Know It Works?
                </div>

                <!-- A/B Experiment Setup -->
                <div style="background: white; border: 1.5px solid #99F6E4; border-radius: 6px; padding: 8px 10px; margin-bottom: 6px;">
                  <div style="display: flex; justify-content: space-between; font-size: 10.5px; font-weight: 700; margin-bottom: 3px;">
                    <span style="color: var(--slate-600);">Control: Existing Flow</span>
                    <span style="color: #0F766E;">Test: Resume Library Flow</span>
                  </div>
                  <div style="font-size: 11px; font-weight: 800; color: #115E59; margin-top: 2px;">
                    Primary Metric: Application Completion Rate
                  </div>
                  <div style="background: #F0FDFA; padding: 3px 6px; border-radius: 4px; font-size: 10.5px; font-weight: 700; color: #0D9488; margin-top: 2px;">
                    Completion Rate = Completed Applications / Starts
                  </div>
                </div>

                <!-- Secondary & Guardrails -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
                  <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10px; font-weight: 700; color: var(--teal-accent); text-transform: uppercase;">Secondary</div>
                    <div style="font-size: 9.5px; color: var(--slate-600); line-height: 1.3; margin-top: 2px;">
                      • Feature adoption<br>
                      • Save-to-library rate<br>
                      • Time to apply<br>
                      • Upload success rate
                    </div>
                  </div>

                  <div style="background: #FFF1F2; border: 1px solid #FECDD3; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10px; font-weight: 700; color: var(--rose-accent); text-transform: uppercase;">Guardrails</div>
                    <div style="font-size: 9.5px; color: #9F1239; line-height: 1.3; margin-top: 2px;">
                      • Wrong CV reports<br>
                      • Accidental overwrites<br>
                      • Application errors<br>
                      • Data/privacy leaks
                    </div>
                  </div>
                </div>
              </div>

              <div style="font-size: 10px; color: var(--slate-500); margin-top: 4px;">
                *Sample size and power analysis to be sized by Naukri analytics.
              </div>
            </div>

            <!-- Column C: What Should Happen Next? (Rollout Plan) -->
            <div class="card card-emerald" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-teal">C. Rollout Strategy</span>
                  <span style="font-size: 11px; font-weight: 700; color: var(--emerald-accent);">Execution</span>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  What Should Happen Next?
                </div>

                <div style="display: flex; flex-direction: column; gap: 5px;">
                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">1. Telemetry Audit:</div>
                    <div style="font-size: 10px; color: var(--slate-600);">Validate current drop-off rates on Path B vs Path A flows.</div>
                  </div>

                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">2. Technical Feasibility:</div>
                    <div style="font-size: 10px; color: var(--slate-600);">Review schema storage models for up to 5 CV references.</div>
                  </div>

                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">3. Usability Testing:</div>
                    <div style="font-size: 10px; color: var(--slate-600);">Test prototype flows with 10–15 multi-role candidates.</div>
                  </div>

                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">4. Controlled Pilot:</div>
                    <div style="font-size: 10px; color: var(--slate-600);">5% production traffic pilot on direct native application flows.</div>
                  </div>

                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">5. Evaluate & Iterate:</div>
                    <div style="font-size: 10px; color: var(--slate-600);">Assess completion lift and candidate feedback before 100% rollout.</div>
                  </div>
                </div>
              </div>

              <div style="font-size: 10px; color: #166534; margin-top: 4px; font-weight: 600;">
                Low-risk staged deployment minimizing platform disruption.
              </div>
            </div>

          </div>

          <!-- Bottom: Closing Statement & Invitation for Feedback -->
          <div style="background: linear-gradient(135deg, #0B1B3D 0%, #13274F 100%); color: white; border-radius: 8px; padding: 12px 18px; box-shadow: 0 4px 14px rgba(11,27,61,0.2);">
            <div style="font-size: 12.5px; line-height: 1.5; color: #E2E8F0; margin-bottom: 6px;">
              <strong style="color: #93C5FD;">Closing Recommendation:</strong> "Candidates may maintain different resume versions for different opportunities. This proposal explores a simpler way to manage those documents and choose the appropriate one when applying, without silently replacing previously saved files."
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.12); padding-top: 6px; font-size: 11.5px;">
              <span style="color: #38BDF8; font-weight: 600;">
                "I would welcome feedback from Naukri's Product team on the problem definition, current application behaviour and suitability of this proposed improvement."
              </span>
              <span style="color: #CBD5E1; font-weight: 500;">
                Aditya Sharma • Independent PM Case Study
              </span>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 13 — MVP, Validation & Recommendation (Suggested Duration: ~90 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To conclude the main presentation, this slide articulates the practical transition from product proposal to empirical validation across three pillars:</p>
        <ul>
          <li><strong>A. What should be built first?</strong> We establish a disciplined MVP scope: store up to 5 resumes, custom naming, apply-time selector, in-flow upload, conditional save checkbox, review screen, and history reference. Secondary items like in-library renaming and delete tools can follow post-MVP.</li>
          <li><strong>B. How would we know it works?</strong> We propose a controlled A/B experiment where the Control is the existing Naukri application experience and the Test is the Resume Library flow. The primary metric is <strong>Application Completion Rate (Completed Applications / Starts)</strong>, tracked alongside secondary adoption metrics and guardrails against wrong-CV submissions.</li>
          <li><strong>C. What should happen next?</strong> A 5-stage rollout: internal telemetry audit, technical review, usability tests with 10–15 students, a 5% pilot on native applications, and iterative evaluation.</li>
        </ul>
        <p><strong>Closing Statement:</strong> Candidates maintain different resume versions for different opportunities. This proposal explores a simpler way to manage those documents and choose the appropriate one when applying, without silently replacing previously saved files.</p>
        <p>I warmly welcome feedback from Naukri's Product team on this problem definition, current platform behaviour, and proposed solution. Thank you."</p>
        <div class='cue-box'><strong>Q&A / Reference:</strong> Slides 14, 15, and 16 contain comprehensive appendices covering full survey data, competitor citations, and technical PRD specifications.</div>
        """
    },

    # SLIDE 14: APPENDIX A: COMPLETE USER RESEARCH & METHODOLOGY
    {
        "id": "slide-14",
        "number": "14",
        "stage": "Appendix",
        "tag": "Appendix A: User Research",
        "evidenceType": "Survey Evidence N=45",
        "title": "Appendix A: Complete User Research & Methodology",
        "subtitle": "Detailed Q1–Q13 survey responses, respondent profiles, workarounds, and research constraints",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 10px;">
          <!-- Top Row: Survey Context & Respondent Profile -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div class="card card-blue" style="padding: 10px 14px;">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue); margin-bottom: 2px;">Research Methodology & Sample</div>
              <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.45;">
                • <strong>Cohort Size:</strong> 45 respondents, surveyed via Google Forms & direct interview outreach.<br>
                • <strong>Target Profile:</strong> Undergraduate and postgraduate college students in India.<br>
                • <strong>Timing:</strong> September – October 2024 (Campus placement & internship cycle).<br>
                • <strong>Goal:</strong> Validate resume versioning frequency, management tools, and application friction.
              </div>
            </div>

            <div class="card card-teal" style="padding: 10px 14px;">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--teal-accent); margin-bottom: 2px;">Methodological Boundaries & Caveats</div>
              <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.45;">
                • <strong>Sample Skew:</strong> Predominantly college students; does not represent all Naukri demographics.<br>
                • <strong>Exploratory Finding:</strong> Demonstrates high student demand, not platform-wide volume.<br>
                • <strong>Self-Reported Data:</strong> Stated intent (90%) often exceeds realized behavioral adoption.<br>
                • <strong>Platform Verification:</strong> Actual drop-offs must be validated via Naukri telemetry.
              </div>
            </div>
          </div>

          <!-- Middle: Complete Q1–Q13 Survey Results Catalog -->
          <div class="card" style="padding: 10px 14px; flex: 1; border: 1.5px solid var(--slate-200); overflow-y: auto;">
            <div style="font-size: 11.5px; font-weight: 800; text-transform: uppercase; color: var(--navy-dark); margin-bottom: 6px;">
              Complete Survey Data Catalog (Q1 to Q13)
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; font-size: 11px; color: var(--slate-700);">
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q1: Current Search Status</strong><br>
                90% actively applying in last 90 days.
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q2: Target Opportunity</strong><br>
                80% Full-time / Placements; 20% Internships.
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q3: Role Categories Applied</strong><br>
                60% (4+ roles), 20% (3 roles), 15% (2), 5% (1).
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q4: Multiple CVs Maintained?</strong><br>
                90% maintain distinct resume versions.
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q5: Stored Versions Count</strong><br>
                Average 3.2 versions (range 2 to 5 resumes).
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q6: Alternate CV Frequency</strong><br>
                90% frequently need alternate CV in-flow.
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q7: Document Storage Tools</strong><br>
                65% Google Drive, 25% Local, 10% Email drafts.
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q8: Experienced Overwrite Fear?</strong><br>
                75% worried about submitting wrong CV.
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q9: Navigated Away from Flow?</strong><br>
                60% exited an application to swap resume file.
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q10: Feature Usefulness Rating</strong><br>
                90% rated 4 or 5 out of 5 (Extremely useful).
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q11: Intent to Use Resume Library</strong><br>
                90% reported very likely / likely to adopt.
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 8px;">
                <strong>Q12: Willingness to Test Demo</strong><br>
                70% volunteered for interactive UX prototype testing.
              </div>
            </div>
          </div>

          <!-- Bottom: Qualitative Insights Summary -->
          <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px 14px; font-size: 11px; color: var(--slate-600);">
            <strong>Qualitative Workaround Pattern:</strong> Candidates currently maintain complex folder hierarchies (e.g. <code>Aditya_PM_2024.pdf</code>, <code>Aditya_Consulting.pdf</code>) on Google Drive and must download/re-upload files repeatedly during campus drives.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 14 — Appendix A: User Research (Reference Material)</h4>
        <p><strong>Note for Presenter:</strong> This slide serves as supporting evidence during Q&A when evaluators inquire about sample size, question wording, or methodology:</p>
        <ul>
          <li><strong>Sample:</strong> 45 college students in placement cycles (September–October 2024).</li>
          <li><strong>Key Metrics:</strong> 90% active applicants, 80% applying to 3+ roles, 90% maintaining multiple resumes, 90% rated feature extremely useful.</li>
          <li><strong>Caveats:</strong> We openly state the exploratory nature and student bias. It justifies pilot experimentation rather than immediate platform-wide rollout.</li>
        </ul>
        """
    },

    # SLIDE 15: APPENDIX B: COMPETITOR EVIDENCE & OFFICIAL DOCUMENTATION
    {
        "id": "slide-15",
        "number": "15",
        "stage": "Appendix",
        "tag": "Appendix B: Competitor Evidence",
        "evidenceType": "Official Documentation",
        "title": "Appendix B: Official Competitor Documentation & Links",
        "subtitle": "Public platform documentation, verified URLs, retrieval dates, and scoping boundaries",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 10px;">
          <!-- 3 Platform Evidence Panels -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; flex: 1;">
            
            <!-- Naukri.com Platform Audit -->
            <div class="card card-blue" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-blue">Naukri.com</span>
                  <span style="font-size: 10px; color: var(--slate-500);">Verified Nov 2026</span>
                </div>
                <div style="font-size: 13.5px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  Public FAQs & Documentation
                </div>
                <div style="font-size: 11px; color: var(--slate-700); line-height: 1.45;">
                  • <strong>FastForward Profile FAQs:</strong> Specifies up to 5 profiles per username with 1 resume per profile, strictly in text/visual CV context.<br>
                  • <strong>Direct Apply Flow:</strong> Ties job applications to the single profile resume attached to candidate record.<br>
                  • <strong>Builder Tools:</strong> Separate standalone builder tools exist with independent resume management.
                </div>
              </div>
              <div style="background: #EFF6FF; border-radius: 4px; padding: 6px 8px; font-size: 10px; color: var(--naukri-blue); margin-top: 6px;">
                <strong>Source:</strong> <code>https://resume.naukri.com/faqs</code>
              </div>
            </div>

            <!-- LinkedIn Platform Audit -->
            <div class="card card-indigo" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge" style="background:#EDE9FE; color:#4F46E5;">LinkedIn</span>
                  <span style="font-size: 10px; color: var(--slate-500);">Verified Nov 2026</span>
                </div>
                <div style="font-size: 13.5px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  Official Help Documentation
                </div>
                <div style="font-size: 11px; color: var(--slate-700); line-height: 1.45;">
                  • <strong>Manage Your Resumes:</strong> Stores up to 4 recently uploaded resumes in candidate job settings.<br>
                  • <strong>Easy Apply Selector:</strong> Candidates select from stored resumes inside the application modal.<br>
                  • <strong>Audit History:</strong> Logs exact submitted document in candidate's application history.<br>
                  • <strong>Scope Boundary:</strong> Bypassed when application redirects to external company ATS.
                </div>
              </div>
              <div style="background: #EEF2FF; border-radius: 4px; padding: 6px 8px; font-size: 10px; color: #4F46E5; margin-top: 6px;">
                <strong>Source:</strong> <code>https://www.linkedin.com/help/linkedin/answer/a511339</code>
              </div>
            </div>

            <!-- Indeed India Audit -->
            <div class="card card-teal" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-teal">Indeed India</span>
                  <span style="font-size: 10px; color: var(--slate-500);">Verified Nov 2026</span>
                </div>
                <div style="font-size: 13.5px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  Official Help Articles
                </div>
                <div style="font-size: 11px; color: var(--slate-700); line-height: 1.45;">
                  • <strong>Profile Resume:</strong> Maintains 1 stored resume file on profile; uploading a new file replaces the prior one.<br>
                  • <strong>Application-Time Upload:</strong> Candidates can upload a different document during job application without updating profile file.<br>
                  • <strong>Scope Boundary:</strong> Stored profile file remains distinct from application-time document upload.
                </div>
              </div>
              <div style="background: #F0FDFA; border-radius: 4px; padding: 6px 8px; font-size: 10px; color: var(--teal-accent); margin-top: 6px;">
                <strong>Source:</strong> <code>https://indeed.force.com/clearinghouse/s/article/How-to-Upload-and-Edit-Resume</code>
              </div>
            </div>

          </div>

          <!-- Bottom: Analytical Commentary -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 10px 16px; font-size: 11.5px; color: var(--slate-700); line-height: 1.45;">
            <strong style="color: var(--navy-dark);">Benchmarking Synthesis:</strong> Across modern employment platforms, the industry standard has converged on separating the candidate's master profile from job-specific application documents. LinkedIn's 4-resume model in Easy Apply validates the usability of a small, candidate-controlled library.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 15 — Appendix B: Competitor Evidence (Reference Material)</h4>
        <p><strong>Note for Presenter:</strong> Use this slide if the evaluator questions our competitor claims or asks for source URLs:</p>
        <ul>
          <li><strong>Naukri FastForward:</strong> Up to 5 profiles per username, 1 resume per profile, strictly in text/visual CV context.</li>
          <li><strong>LinkedIn:</strong> Verified 4-resume limit in Easy Apply flows, with application history tracking.</li>
          <li><strong>Indeed India:</strong> Confirmed 1-stored-profile CV model with application-time upload separation.</li>
        </ul>
        """
    },

    # SLIDE 16: APPENDIX C: PRODUCT SPECIFICATION & TECHNICAL CONSIDERATIONS
    {
        "id": "slide-16",
        "number": "16",
        "stage": "Appendix",
        "tag": "Appendix C: Product Specification",
        "evidenceType": "Proposed Solution",
        "title": "Appendix C: Product Specification & Technical Considerations",
        "subtitle": "PRD requirements, acceptance criteria, data integrity, security, and technical dependencies",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 10px;">
          <!-- Top Grid: Functional Requirements & Acceptance Criteria -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; flex: 1;">
            
            <!-- Left: Functional Requirements Table -->
            <div class="card" style="padding: 10px 14px; display: flex; flex-direction: column; justify-content: space-between; border: 1.5px solid var(--slate-200);">
              <div>
                <div style="font-size: 11.5px; font-weight: 800; text-transform: uppercase; color: var(--navy-dark); margin-bottom: 6px;">
                  Functional Requirements Prioritization
                </div>
                
                <table class="deck-table" style="font-size: 10.5px; width: 100%;">
                  <thead>
                    <tr style="background: #F1F5F9; color: var(--slate-700);">
                      <th style="width: 15%; padding: 4px 6px;">Priority</th>
                      <th style="width: 35%; padding: 4px 6px;">Feature</th>
                      <th style="width: 50%; padding: 4px 6px;">Requirement Scope</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><span class="badge badge-must" style="font-size: 9px;">MUST</span></td>
                      <td>Resume Storage</td>
                      <td>Store up to 5 independent resumes in candidate library</td>
                    </tr>
                    <tr>
                      <td><span class="badge badge-must" style="font-size: 9px;">MUST</span></td>
                      <td>Apply Selector</td>
                      <td>Modal resume picker in direct application flows</td>
                    </tr>
                    <tr>
                      <td><span class="badge badge-must" style="font-size: 9px;">MUST</span></td>
                      <td>Conditional Save</td>
                      <td>Checkbox strictly hidden until upload success</td>
                    </tr>
                    <tr>
                      <td><span class="badge badge-must" style="font-size: 9px;">MUST</span></td>
                      <td>Audit History</td>
                      <td>Exact immutable document snapshot reference</td>
                    </tr>
                    <tr>
                      <td><span class="badge badge-should" style="font-size: 9px;">SHOULD</span></td>
                      <td>Default CV</td>
                      <td>Set default resume for quick preselection</td>
                    </tr>
                    <tr>
                      <td><span class="badge badge-could" style="font-size: 9px;">COULD</span></td>
                      <td>Rename/Delete</td>
                      <td>In-library document management controls</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div style="font-size: 10px; color: var(--slate-500); margin-top: 4px;">
                MoSCoW framework ensures lean MVP delivery for pilot validation.
              </div>
            </div>

            <!-- Right: Given/When/Then Acceptance Criteria -->
            <div class="card card-indigo" style="padding: 10px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="font-size: 11.5px; font-weight: 800; text-transform: uppercase; color: #4F46E5; margin-bottom: 6px;">
                  Core Acceptance Criteria (Given / When / Then)
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 5px; font-size: 10.5px; color: var(--slate-700);">
                  <div style="background: white; border: 1px solid #C7D2FE; border-radius: 4px; padding: 5px 8px;">
                    <strong style="color: #3730A3;">AC1: Conditional Save Gate</strong><br>
                    <em>Given</em> an in-flow upload, <em>When</em> upload is in progress, <em>Then</em> save checkbox is hidden. Checkbox renders only upon 100% upload success.
                  </div>

                  <div style="background: white; border: 1px solid #C7D2FE; border-radius: 4px; padding: 5px 8px;">
                    <strong style="color: #3730A3;">AC2: Mandatory Naming Validation</strong><br>
                    <em>Given</em> candidate checks 'Save to Library', <em>When</em> custom name is blank or whitespace, <em>Then</em> submission is blocked with inline error.
                  </div>

                  <div style="background: white; border: 1px solid #C7D2FE; border-radius: 4px; padding: 5px 8px;">
                    <strong style="color: #3730A3;">AC3: Duplicate Filename Isolation</strong><br>
                    <em>Given</em> candidate uploads file named <code>Resume.pdf</code>, <em>When</em> existing file has same name, <em>Then</em> system generates unique internal UUID.
                  </div>

                  <div style="background: white; border: 1px solid #C7D2FE; border-radius: 4px; padding: 5px 8px;">
                    <strong style="color: #3730A3;">AC4: Historical Integrity</strong><br>
                    <em>Given</em> candidate deletes a resume from library post-apply, <em>When</em> reviewing past applications, <em>Then</em> submitted snapshot remains intact.
                  </div>
                </div>
              </div>

              <div style="font-size: 10px; color: #4F46E5; margin-top: 4px;">
                Guarantees zero data loss, unambiguous candidate intent, and legal compliance.
              </div>
            </div>

          </div>

          <!-- Bottom: Technical Architecture & Glossary -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 8px 14px; display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 12px; font-size: 10.5px; color: var(--slate-600);">
            <div>
              <strong style="color: var(--navy-dark);">Technical Architecture:</strong> Resumes stored in S3-compatible cloud object store with SHA-256 hash validation. Metadata stored in relational candidate schema. Recruiter search indexing (Resdex) remains mapped to the candidate's master profile record.
            </div>
            <div>
              <strong style="color: var(--navy-dark);">Privacy Guarantee:</strong> Only the specific resume file attached to an application is exposed to the prospective employer. Library files remain strictly private.
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 16 — Appendix C: Product Specification (Reference Material)</h4>
        <p><strong>Note for Presenter:</strong> Refer to this slide if technical, engineering, or design stakeholders ask for implementation specifications:</p>
        <ul>
          <li><strong>Acceptance Criteria:</strong> Enforces conditional checkbox rendering, mandatory custom naming validation, duplicate filename isolation via UUIDs, and immutable application logs.</li>
          <li><strong>Architecture:</strong> Explains how document storage operates via object stores while candidate profile metadata remains unified, and confirms library privacy boundaries.</li>
        </ul>
        """
    }
]
