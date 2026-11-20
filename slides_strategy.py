# slides_strategy.py - Slides 13 to 16 (MVP & Validation, Appendix A, Appendix B, Appendix C)

SLIDES_STRATEGY = [
    # SLIDE 13: MVP, EXPERIMENTATION & FINAL RECOMMENDATION
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
                    <li>Store up to 5 resumes (proposed MVP capacity assumption requiring validation)</li>
                    <li>Mandatory custom naming (e.g. PM CV)</li>
                    <li>Application-time resume selector modal</li>
                    <li>In-flow upload of fresh resume document</li>
                    <li><strong>Conditional save checkbox</strong> (post-upload)</li>
                    <li>Strict non-destructive saving (no overwrites)</li>
                    <li>Pre-submission review and confirmation</li>
                    <li>Audit reference to submitted document version in history</li>
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
                    <span style="color: var(--slate-600);">Control: Current Application Flow (incl. any existing alternate-upload options)</span>
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
                    <div style="font-size: 10px; color: var(--slate-600);">Validate current drop-off rates on in-flow upload vs standard apply paths.</div>
                  </div>

                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">2. Technical Feasibility:</div>
                    <div style="font-size: 10px; color: var(--slate-600);">Review schema and storage models for up to 5 CV references with engineering.</div>
                  </div>

                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">3. Usability Testing (Illustrative Proposal):</div>
                    <div style="font-size: 10px; color: var(--slate-600);">Test prototype flows with 10–15 candidates (illustrative proposal; final sample size to be determined by Naukri research team).</div>
                  </div>

                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">4. Controlled Pilot (Illustrative Proposal):</div>
                    <div style="font-size: 10px; color: var(--slate-600);">5% production traffic pilot on direct native application flows (illustrative proposal; rollout percentages to be determined by Naukri analytics team).</div>
                  </div>

                  <div style="background: white; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">5. Evaluate & Iterate:</div>
                    <div style="font-size: 10px; color: var(--slate-600);">Assess completion lift, save-to-library adoption, and candidate feedback before broader rollout.</div>
                  </div>
                </div>
              </div>

              <div style="font-size: 9.5px; color: #166534; margin-top: 4px; font-weight: 600;">
                *Illustrative proposal: Usability sample sizes and pilot rollout percentages subject to formal determination by Naukri research and analytics teams.
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
          <li><strong>A. What should be built first?</strong> We establish a disciplined MVP scope: store up to 5 resumes (a proposed MVP capacity assumption requiring validation), custom naming, apply-time selector, in-flow upload, conditional save checkbox, review screen, and history reference. Secondary items like in-library renaming and delete tools can follow post-MVP.</li>
          <li><strong>B. How would we know it works?</strong> We propose a controlled A/B experiment where the Control is the existing Naukri application experience and the Test is the Resume Library flow. The primary metric is <strong>Application Completion Rate (Completed Applications / Starts)</strong>, tracked alongside secondary adoption metrics and guardrails against wrong-CV submissions.</li>
          <li><strong>C. What should happen next?</strong> A 5-stage rollout: internal telemetry audit, technical review, usability tests with 10–15 candidates (illustrative proposal; final sample size to be determined by Naukri research team), a 5% pilot on native applications (illustrative proposal; rollout percentages to be determined by Naukri analytics team), and iterative evaluation.</li>
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
        "evidenceType": "Survey Evidence N=100+",
        "title": "Appendix A: Complete User Research & Methodology",
        "subtitle": "Restored Q1–Q13 survey responses, respondent profiles, reported behaviors, and research boundaries",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 8px;">
          <!-- Top Row: Survey Context & Respondent Profile -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
            <div class="card card-blue" style="padding: 9px 12px;">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue); margin-bottom: 2px;">Research Methodology & Sample</div>
              <div style="font-size: 11px; color: var(--slate-700); line-height: 1.4;">
                • <strong>Cohort Size:</strong> 100+ college-student respondents.<br>
                • <strong>Outreach Method:</strong> Personal outreach to undergraduate and postgraduate college students in India.<br>
                • <strong>Context:</strong> Active job and campus internship application period.<br>
                • <strong>Primary Focus:</strong> Multi-role job search, resume versioning frequency, and in-flow friction.
              </div>
            </div>

            <div class="card card-teal" style="padding: 9px 12px;">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--teal-accent); margin-bottom: 2px;">Methodological Boundaries & Caveats</div>
              <div style="font-size: 11px; color: var(--slate-700); line-height: 1.4;">
                • <strong>Target Demographic Boundary:</strong> Cohort comprised 100+ college students; does not represent full Naukri demographic spectrum (experienced hires, CXOs).<br>
                • <strong>Outreach Limitation:</strong> Sample acquired via personal outreach rather than randomized platform-wide sampling.<br>
                • <strong>Exploratory Evidence:</strong> Demonstrates high multi-role application demand in campus cohort; platform-wide behavior requires internal telemetry validation.<br>
                • <strong>Self-Reported Intent:</strong> Stated survey enthusiasm (90%) reflects perceived utility, which must be calibrated against behavioral conversion in A/B testing.
              </div>
            </div>
          </div>

          <!-- Middle: Complete Restored Q1–Q13 Survey Results Catalog -->
          <div class="card" style="padding: 8px 12px; flex: 1; border: 1.5px solid var(--slate-200); overflow-y: auto;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--navy-dark);">
                Complete Survey Data Catalog (Restored Q1 to Q13 Findings)
              </div>
              <span class="badge badge-blue" style="font-size: 9.5px;">N=100+ College Students</span>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 7px; font-size: 10px; color: var(--slate-700);">
              <!-- Q1 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q1: Current Search Status</div>
                <div style="color: #1E3A8A; font-weight: 700;">90% recent job applicants</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">Actively applied for opportunities within the last 90 days.</div>
              </div>

              <!-- Q2 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q2: Target Opportunities</div>
                <div style="color: #1E3A8A; font-weight: 700;">80% Full-Time / Placements; 20% Internships</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">Primary focus on immediate post-graduation career placement.</div>
              </div>

              <!-- Q3 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q3: Role Categories Applied</div>
                <div style="color: #1E3A8A; font-weight: 700;">60% (4+ roles), 20% (3), 15% (2), 5% (1)</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">80% simultaneously apply across 3 or more distinct job tracks.</div>
              </div>

              <!-- Q4 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q4: Multiple Resumes Maintained</div>
                <div style="color: #1E3A8A; font-weight: 700;">90% maintain multiple resumes</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">Maintain distinct versions tailored to different role profiles.</div>
              </div>

              <!-- Q5 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q5: Reasons for Multiple Resumes</div>
                <div style="color: #0F766E; font-weight: 600;">Different skills, industries, career paths & JD tailoring</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">*Qualitative response; exact counts unavailable.</div>
              </div>

              <!-- Q6 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q6: Storage & Management Methods</div>
                <div style="color: #0F766E; font-weight: 600;">Separate storage, portal uploads & pre-apply editing</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">*Qualitative response; exact counts unavailable.</div>
              </div>

              <!-- Q7 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q7: Need for Alternate Resume in Flow</div>
                <div style="color: #1E3A8A; font-weight: 700;">90% frequently need alternate CV</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">Encounter jobs requiring a different document than profile resume.</div>
              </div>

              <!-- Q8 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q8: Behavior When Alternate Needed</div>
                <div style="color: #0F766E; font-weight: 600;">Replacing files, uploading another, pause/return, skip</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">*Reported workarounds; exact counts unavailable.</div>
              </div>

              <!-- Q9 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q9: Inconvenience / Drop-off Friction</div>
                <div style="color: #78350F; font-weight: 600;">Reported inconvenience & flow friction</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">*Suggested friction, but no reliable numerical result.</div>
              </div>

              <!-- Q10 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q10: Specific Application Incident</div>
                <div style="color: var(--slate-600); font-weight: 600;">No detailed written examples provided</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">*Open-ended field yielded no verifiable written case detail.</div>
              </div>

              <!-- Q11 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q11: Feature Usefulness Rating</div>
                <div style="color: #1E3A8A; font-weight: 700;">90% rated 4 or 5 out of 5</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">Rated 4 or 5 out of 5 for potential value to job search.</div>
              </div>

              <!-- Q12 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q12: Likelihood to Adopt</div>
                <div style="color: #1E3A8A; font-weight: 700;">90% very likely to use</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">Expressed strong positive willingness to utilize resume library.</div>
              </div>

              <!-- Q13 -->
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 5px 7px; grid-column: span 3;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">Q13: Desired Feature Capabilities (Qualitative Feedback)</div>
                <div style="color: #0F766E; font-weight: 600;">Multiple resumes, custom naming, application-time selection, application history, and resume management</div>
                <div style="color: var(--slate-500); font-size: 9.5px; margin-top: 1px;">*Candidate feature wishlist; exact category counts unavailable.</div>
              </div>
            </div>
          </div>

          <!-- Bottom: Qualitative Insights Summary -->
          <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 7px 12px; font-size: 10.5px; color: var(--slate-600); line-height: 1.4;">
            <strong style="color: var(--navy-dark);">Research Data Transparency:</strong> Primary response data collected via personal outreach across 100+ college students in India. Numerical metrics are reported only for structured questions with verified response tallies (Q1–Q4, Q7, Q11, Q12). For qualitative or open-ended questions (Q5, Q6, Q8, Q9, Q10, Q13), observed themes are documented without unverified numerical extrapolations.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 14 — Appendix A: User Research (Reference Material)</h4>
        <p><strong>Note for Presenter:</strong> This slide serves as supporting evidence during Q&A when evaluators inquire about sample size, question wording, or methodology:</p>
        <ul>
          <li><strong>Sample & Outreach:</strong> 100+ college-student respondents in India reached via personal outreach during active recruitment and internship cycles.</li>
          <li><strong>Verified Quantitative Findings:</strong> 90% recent applicants (Q1), 80% full-time/placements vs 20% internships (Q2), 80% applying across 3+ roles (Q3), 90% maintain multiple resumes (Q4), 90% frequently need alternate resume in-flow (Q7), 90% rated feature 4 or 5 out of 5 (Q11), and 90% reported very likely to adopt (Q12).</li>
          <li><strong>Qualitative Scope (Exact Counts Unavailable):</strong> Q5 (skills/industries/JD tailoring reasons), Q6 (external storage and pre-application editing methods), Q8 (leaving/pausing flows or uploading alternate files), Q9 (reported friction without reliable numerical tallies), Q10 (no detailed written examples), and Q13 (feature desires: multiple CVs, custom naming, selector, history).</li>
          <li><strong>Methodological Caveats:</strong> We transparently note the exploratory nature and student demographic boundaries. This data justifies pilot experimentation rather than immediate platform-wide assumptions.</li>
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
                  Public FAQs & Service Documentation
                </div>
                <div style="font-size: 11px; color: var(--slate-700); line-height: 1.45;">
                  • <strong>FastForward Resume Service FAQs:</strong> Naukri's FastForward documentation specifies that a single username can hold up to 5 profiles, with 1 resume attached per profile (in the context of visual/text CV packages).<br>
                  • <strong>General Application Flow:</strong> The author encountered a profile-associated resume workflow. The availability of alternate resume selection across Naukri's application types requires further validation.<br>
                  • <strong>Service Boundary:</strong> Paid FastForward profile packages represent a distinct service from the core free job application experience.
                </div>
              </div>
              <div style="background: #EFF6FF; border-radius: 4px; padding: 6px 8px; font-size: 9.5px; color: var(--naukri-blue); margin-top: 6px; word-break: break-all;">
                <strong>Official Source:</strong><br>
                <a href="https://resume.naukri.com/faqs" target="_blank" style="color: var(--naukri-blue); text-decoration: underline;">https://resume.naukri.com/faqs</a>
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
                  • <strong>Easy Apply Four-Resume Reuse:</strong> LinkedIn allows job seekers to store up to 4 recently uploaded resumes within Easy Apply settings for immediate selection and reuse.<br>
                  • <strong>Submitted Resume History:</strong> LinkedIn allows candidates to view the resume submitted for an Easy Apply application through Job Tracker.<br>
                  • <strong>Scope Boundary:</strong> Applies to native Easy Apply applications; external ATS redirects bypass LinkedIn's resume selector.
                </div>
              </div>
              <div style="background: #EEF2FF; border-radius: 4px; padding: 6px 8px; font-size: 9.5px; color: #4F46E5; margin-top: 6px; word-break: break-all;">
                <strong>Official Sources:</strong><br>
                • <a href="https://www.linkedin.com/help/linkedin/answer/a512405" target="_blank" style="color: #4F46E5; text-decoration: underline;">Four-Resume Reuse FAQ</a><br>
                • <a href="https://www.linkedin.com/help/linkedin/answer/a506680" target="_blank" style="color: #4F46E5; text-decoration: underline;">Submitted Resume History FAQ</a>
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
                  • <strong>Stored Profile Resume File:</strong> Candidates can upload and maintain 1 stored resume file on their Indeed profile.<br>
                  • <strong>Alternate Application Upload:</strong> Indeed's application instructions state that candidates can upload a different resume file while applying for a specific position.<br>
                  • <strong>Documentation Boundary:</strong> Public Indeed documentation does not establish whether uploading an alternate resume during an application updates the candidate's stored resume file on their profile.
                </div>
              </div>
              <div style="background: #F0FDFA; border-radius: 4px; padding: 6px 8px; font-size: 9.5px; color: var(--teal-accent); margin-top: 6px; word-break: break-all;">
                <strong>Official Sources:</strong><br>
                • <a href="https://in.indeed.com/help/job-seekers/articles/11314976176141-faqs-creating-uploading-and-managing-a-resume-file?co=IN&hl=en" target="_blank" style="color: var(--teal-accent); text-decoration: underline;">Stored Resume File FAQ</a><br>
                • <a href="https://in.indeed.com/help/job-seekers/articles/204652920-applying-for-a-job-on-indeed?co=IN&hl=en" target="_blank" style="color: var(--teal-accent); text-decoration: underline;">Applying with Alternate Resume</a>
              </div>
            </div>

          </div>

          <!-- Bottom: Analytical Commentary -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 10px 16px; font-size: 11px; color: var(--slate-700); line-height: 1.45;">
            <strong style="color: var(--navy-dark);">Benchmarking Synthesis & Documentation Boundaries:</strong> Public help documentation from LinkedIn confirms support for up to 4 reusable resumes in native Easy Apply and allows candidates to view the resume submitted for an Easy Apply application through Job Tracker. Indeed India confirms application-time upload capability, though public documentation does not establish whether uploading an alternate file updates the candidate's stored profile resume. Naukri FastForward FAQs establish multi-profile packages (up to 5 profiles, 1 resume each in the documented text/visual CV context), while the availability of alternate resume selection across Naukri's application types requires further validation.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 15 — Appendix B: Competitor Evidence (Reference Material)</h4>
        <p><strong>Note for Presenter:</strong> Use this slide if the evaluator questions competitor citations or asks for verified source URLs:</p>
        <ul>
          <li><strong>Naukri.com:</strong> FastForward FAQs document up to 5 profiles per username with 1 resume per profile in text/visual CV packages (<a href='https://resume.naukri.com/faqs' target='_blank'>resume.naukri.com/faqs</a>). In core job search applications, the author encountered a profile-associated resume workflow; the availability of alternate resume selection across Naukri's application types requires further validation.</li>
          <li><strong>LinkedIn:</strong> Verified 4-resume reuse capability in Easy Apply (<a href='https://www.linkedin.com/help/linkedin/answer/a512405' target='_blank'>a512405</a>); LinkedIn allows candidates to view the resume submitted for an Easy Apply application through Job Tracker (<a href='https://www.linkedin.com/help/linkedin/answer/a506680' target='_blank'>a506680</a>).</li>
          <li><strong>Indeed India:</strong> Confirmed 1-stored profile resume (<a href='https://in.indeed.com/help/job-seekers/articles/11314976176141-faqs-creating-uploading-and-managing-a-resume-file?co=IN&hl=en' target='_blank'>article 11314976176141</a>) and alternate application upload (<a href='https://in.indeed.com/help/job-seekers/articles/204652920-applying-for-a-job-on-indeed?co=IN&hl=en' target='_blank'>article 204652920</a>). Documented capability allows uploading a different resume during an application, though public documentation does not establish its effect on stored profile files.</li>
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
        "subtitle": "PRD requirements, acceptance criteria, data integrity, technical boundaries, and governance review",
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
                      <td>Store up to 5 resumes (proposed MVP capacity assumption requiring validation)</td>
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
                      <td>Submitted document version reference in application logs</td>
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
                    <strong style="color: #3730A3;">AC3: Duplicate Filename Handling</strong><br>
                    <em>Given</em> candidate uploads file named <code>Resume.pdf</code>, <em>When</em> existing file has same name, <em>Then</em> system assigns unique internal document identifier without overwriting.
                  </div>

                  <div style="background: white; border: 1px solid #C7D2FE; border-radius: 4px; padding: 5px 8px;">
                    <strong style="color: #3730A3;">AC4: Historical Submission Integrity</strong><br>
                    <em>Given</em> candidate modifies or removes a resume post-apply, <em>When</em> reviewing past applications, <em>Then</em> submitted record retains reference to the document version sent.
                  </div>
                </div>
              </div>

              <div style="font-size: 10px; color: #4F46E5; margin-top: 4px;">
                Proposed specifications for engineering review to prevent data collisions and ensure candidate control.
              </div>
            </div>

          </div>

          <!-- Bottom: Technical Requirements & Governance Review -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 8px 14px; display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 12px; font-size: 10.5px; color: var(--slate-600);">
            <div>
              <strong style="color: var(--navy-dark);">Technical Requirements for Engineering Evaluation:</strong> Document storage requires secure object/blob storage with unique document identifiers to prevent collisions. Candidate metadata requires relational mapping between candidate profile ID, library resume entities, and application submission logs. Search indexing integration (e.g. recruiter Resdex discovery) and synchronisation behavior must be formally evaluated by Naukri engineering.
            </div>
            <div>
              <strong style="color: var(--navy-dark);">Data Retention, Privacy & Legal Review:</strong> Document retention and deletion policies require formal review by Naukri engineering and legal teams to establish statutory compliance, storage lifecycles, and candidate data erasure protocols. Employer document access must remain strictly restricted to the specific resume selected for that application.
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 16 — Appendix C: Product Specification (Reference Material)</h4>
        <p><strong>Note for Presenter:</strong> Refer to this slide if technical, engineering, or design stakeholders ask for implementation specifications:</p>
        <ul>
          <li><strong>Acceptance Criteria:</strong> Enforces conditional checkbox rendering, mandatory custom naming validation, duplicate filename isolation via unique document IDs, and submitted document reference preservation in application logs.</li>
          <li><strong>Engineering Evaluation:</strong> Replaces assumptions about specific cloud vendors or database schemas with general technical requirements for Naukri engineering to evaluate (object storage, metadata mapping, Resdex synchronisation behavior).</li>
          <li><strong>Governance & Privacy:</strong> States clearly that document retention, deletion lifecycles, and privacy rules require formal review by Naukri engineering and legal teams.</li>
        </ul>
        """
    }
]
