# slides_strategy.py - Slides 18 to 23 (Experimentation, Risks/Implementation, Final Recommendation, Appendices A, B, C)

SLIDES_STRATEGY = [
    # SLIDE 18: PRODUCT VALIDATION AND EXPERIMENTATION
    {
        "id": "slide-18",
        "number": "18",
        "stage": "Test",
        "tag": "Experiment & Metrics",
        "evidenceType": "Product Hypothesis",
        "title": "How Would We Know Whether It Works?",
        "subtitle": "Controlled A/B pilot design, metric hierarchy, guardrails, and statistical rigor",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Top: Controlled Experiment Setup -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div class="card card-tinted" style="border-left: 4px solid var(--slate-400); padding: 10px 14px;">
              <div class="card-header-sm">
                <span>Cohort A: Control Group</span>
                <span class="badge badge-gray">Baseline Experience</span>
              </div>
              <div style="font-size: 13px; font-weight: 700; color: var(--navy-dark); margin: 2px 0;">Existing Application Experience</div>
              <p class="card-text" style="font-size: 11px;">
                Candidates encounter the existing application journey for eligible on-platform postings, relying on their profile-attached resume.
              </p>
            </div>
            
            <div class="card card-blue" style="border-left: 4px solid var(--naukri-blue); padding: 10px 14px;">
              <div class="card-header-sm">
                <span style="color: var(--naukri-blue); font-weight: 800;">Cohort B: Test Group</span>
                <span class="badge badge-blue">Proposed Pilot</span>
              </div>
              <div style="font-size: 13px; font-weight: 700; color: var(--navy-dark); margin: 2px 0;">Resume Library Experience</div>
              <p class="card-text" style="font-size: 11px; color: var(--slate-700);">
                Candidates receive the dedicated Resume Library, moment-of-apply resume selector, in-flow upload, and optional non-destructive saving.
              </p>
            </div>
          </div>
          
          <!-- Middle: Metric Hierarchy Grid -->
          <div style="display: grid; grid-template-columns: 1.1fr 1.3fr 1fr; gap: 12px; flex: 1;">
            <!-- Primary Metric -->
            <div class="card" style="border: 2px solid var(--naukri-blue); background: var(--naukri-blue-light); display: flex; flex-direction: column; padding: 12px 14px;">
              <div class="card-header-sm">
                <span style="color: var(--naukri-blue); font-weight: 800;">Primary Metric</span>
                <span class="badge badge-blue">Conversion</span>
              </div>
              <div style="font-size: 14.5px; font-weight: 800; color: var(--navy-dark); margin: 2px 0;">
                Application Completion Rate
              </div>
              <div style="background: white; border: 1px solid var(--naukri-blue-border); padding: 6px 8px; border-radius: 6px; font-size: 11px; font-family: monospace; color: var(--naukri-blue); text-align: center; margin: 4px 0;">
                Completed Applications ÷ Application Starts
              </div>
              <p class="card-text" style="font-size: 10.5px; color: var(--slate-700);">
                Measures whether candidates are genuinely more likely to complete applications when resume-switching friction is mitigated.
              </p>
            </div>
            
            <!-- Secondary Metrics -->
            <div class="card" style="display: flex; flex-direction: column; padding: 12px 14px;">
              <div class="card-header-sm">
                <span>Secondary Diagnostic Metrics</span>
                <span class="badge badge-teal">Diagnostics</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 4px; font-size: 10.5px; color: var(--slate-700); margin-top: 2px;">
                <div><strong>• Library Adoption:</strong> % of eligible candidates managing ≥2 resumes.</div>
                <div><strong>• Selection Ratio:</strong> % selecting existing CV vs. uploading new.</div>
                <div><strong>• Save Adoption Rate:</strong> % saving newly uploaded resumes to library.</div>
                <div><strong>• Time-to-Apply:</strong> Time taken to complete the application journey.</div>
                <div><strong>• Application Abandonment:</strong> Drop-off points within the flow.</div>
                <div><strong>• Candidate Satisfaction (CSAT):</strong> Self-reported experience rating.</div>
              </div>
            </div>
            
            <!-- Guardrail Metrics -->
            <div class="card" style="border-left: 3px solid var(--rose-accent); background: #FFFBFB; display: flex; flex-direction: column; padding: 12px 14px;">
              <div class="card-header-sm">
                <span style="color: var(--rose-accent); font-weight: 800;">Guardrail Metrics</span>
                <span class="badge badge-red">Protection</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 4px; font-size: 10.5px; color: #4C0519; margin-top: 2px;">
                <div><strong>• Accidental Overwrites:</strong> Strictly zero tolerance.</div>
                <div><strong>• Wrong-Resume Tickets:</strong> Candidate support complaint rates.</div>
                <div><strong>• Technical Failures:</strong> Upload or submission error frequency.</div>
                <div><strong>• Funnel Deterioration:</strong> Any negative impact on overall apply rates.</div>
                <div><strong>• Privacy Exposure:</strong> Unintended recruiter document access.</div>
              </div>
            </div>
          </div>
          
          <div style="background: var(--slate-100); padding: 7px 12px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 6px;">
            <span><strong>Statistical Rigor:</strong> Minimum Detectable Effect (MDE), statistical power, required sample size, and duration must be defined by Naukri's analytics team based on baseline application volume and variance. Any potential lift remains a hypothesis until tested.</span>
            <span class="badge badge-gray">Analytics-Led Power Calculation</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 18 — Experimentation & Metrics Framework</h4>
        <p>To establish whether the feature improves the candidate experience, we propose a controlled A/B experiment:</p>
        <ul>
          <li><strong>Eligible Cohorts:</strong> Cohort A experiences the baseline application flow; Cohort B receives the Resume Library and application-time selector.</li>
          <li><strong>Primary Metric:</strong> Application Completion Rate (Completed Applications / Application Starts). This measures whether candidates are more likely to finish applying when resume-switching friction is mitigated.</li>
          <li><strong>Secondary Metrics:</strong> We track adoption—how many candidates store multiple resumes, the ratio of existing selection vs. fresh uploads, and save adoption.</li>
          <li><strong>Guardrail Metrics:</strong> Accidental overwrite incidents must strictly remain zero. We also monitor wrong-resume support tickets and upload failures.</li>
          <li><strong>Statistical Parameters:</strong> We do not invent arbitrary conversion numbers or guaranteed lifts. The analytics team must determine sample size, MDE, and duration based on Naukri's actual volume.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's examine implementation risks, technical dependencies, and rollout planning.</div>
        """
    },

    # SLIDE 19: RISKS, DEPENDENCIES AND IMPLEMENTATION PLAN
    {
        "id": "slide-19",
        "number": "19",
        "stage": "Deliver",
        "tag": "Rollout & Governance",
        "evidenceType": "Requires Naukri Validation",
        "title": "What Would Naukri Need to Validate Before Building?",
        "subtitle": "Risk mitigation matrix, phased implementation stages, and open technical questions for Naukri",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Top Row: Risk Matrix & Open Questions -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; flex: 1;">
            <!-- Risk & Mitigation Table -->
            <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
              <div style="padding: 7px 12px; background: var(--slate-100); border-bottom: 1px solid var(--slate-200); font-weight: 700; font-size: 10.5px; text-transform: uppercase; color: var(--navy-dark);">
                Risk Mitigation Matrix
              </div>
              <div class="table-scroll-wrap" style="flex: 1;">
                <table class="deck-table" style="font-size: 10px;">
                  <thead>
                    <tr>
                      <th style="width: 44%;">Risk</th>
                      <th style="width: 56%;">Mitigation Strategy</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Candidate submits wrong resume</strong></td>
                      <td>Show selected file and review screen before submission.</td>
                    </tr>
                    <tr>
                      <td><strong>New upload overwrites old file</strong></td>
                      <td>Store new uploads as independent records with distinct IDs.</td>
                    </tr>
                    <tr>
                      <td><strong>Duplicate filenames cause confusion</strong></td>
                      <td>Treat duplicate filenames as separate records with unique IDs.</td>
                    </tr>
                    <tr>
                      <td><strong>Upload fails</strong></td>
                      <td>Show error message and retry; withhold save checkbox.</td>
                    </tr>
                    <tr>
                      <td><strong>Resume deleted after applying</strong></td>
                      <td>Preserve historical application document/version snapshot.</td>
                    </tr>
                    <tr>
                      <td><strong>Too many selection choices</strong></td>
                      <td>Preselect designated default without silent submission.</td>
                    </tr>
                    <tr>
                      <td><strong>Privacy concerns</strong></td>
                      <td>Make library private; submit only the chosen document.</td>
                    </tr>
                    <tr>
                      <td><strong>Third-party application limitations</strong></td>
                      <td>Clearly communicate external redirects to candidates.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            
            <!-- Open Questions for Naukri Product Team -->
            <div class="card card-tinted" style="padding: 12px 14px; display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Open Questions for Naukri Team</span>
                <span class="evidence-tag evidence-tag-val">Requires Naukri Input</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 5px; font-size: 10.5px; color: var(--slate-700); flex: 1;">
                <div><strong>1. Flow Capabilities:</strong> Which current application flows already permit alternate resume uploads?</div>
                <div><strong>2. Attachment Architecture:</strong> How do profile documents and application attachments interact in existing services?</div>
                <div><strong>3. Version Immutability:</strong> Can the backend associate an immutable document version UUID with each application?</div>
                <div><strong>4. Retention Policy:</strong> What document retention and deletion policies apply to stored files?</div>
                <div><strong>5. Recruiter Visibility:</strong> Would this feature require modifications to recruiter-side document viewing?</div>
                <div><strong>6. Cross-Platform Scope:</strong> Which desktop and mobile web flows should be prioritized for initial release?</div>
              </div>
              <div style="background: white; border: 1px solid var(--slate-200); padding: 6px 10px; border-radius: 4px; font-size: 10px; color: var(--slate-600); margin-top: 6px;">
                These open questions illustrate why dialogue with Naukri's actual product team is essential.
              </div>
            </div>
          </div>
          
          <!-- Bottom Row: 6 Phased Implementation Stages -->
          <div class="card card-tinted" style="padding: 10px 14px;">
            <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 6px;">Phased Rollout Plan</div>
            <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 6px;">
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px; text-align: center;">
                <div style="font-size: 9.5px; font-weight: 700; color: var(--naukri-blue);">1. Flow Mapping</div>
                <div style="font-size: 9px; color: var(--slate-500); margin-top: 2px;">Audit eligible flows</div>
              </div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px; text-align: center;">
                <div style="font-size: 9.5px; font-weight: 700; color: var(--naukri-blue);">2. Technical Review</div>
                <div style="font-size: 9px; color: var(--slate-500); margin-top: 2px;">Storage & UUIDs</div>
              </div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px; text-align: center;">
                <div style="font-size: 9.5px; font-weight: 700; color: var(--naukri-blue);">3. Usability Tests</div>
                <div style="font-size: 9px; color: var(--slate-500); margin-top: 2px;">Test with job seekers</div>
              </div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px; text-align: center;">
                <div style="font-size: 9.5px; font-weight: 700; color: var(--emerald-accent);">4. Limited Beta</div>
                <div style="font-size: 9px; color: var(--slate-500); margin-top: 2px;">Eligible segment pilot</div>
              </div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px; text-align: center;">
                <div style="font-size: 9.5px; font-weight: 700; color: var(--emerald-accent);">5. Controlled A/B</div>
                <div style="font-size: 9px; color: var(--slate-500); margin-top: 2px;">Evaluate conversion</div>
              </div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px; text-align: center;">
                <div style="font-size: 9.5px; font-weight: 700; color: var(--navy-dark);">6. Phased Scale</div>
                <div style="font-size: 9px; color: var(--slate-500); margin-top: 2px;">Expand if validated</div>
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 19 — Risks, Implementation & Open Questions</h4>
        <p>A realistic proposal anticipates operational risks and engineering dependencies:</p>
        <ul>
          <li><strong>Risk Governance:</strong> We have mapped mitigations for wrong-resume submission, overwriting, duplicate filenames, and third-party redirects.</li>
          <li><strong>Open Questions for Naukri:</strong> We explicitly identify key questions that only Naukri's engineering and product teams can answer—such as flow eligibility, attachment architecture, and retention rules.</li>
          <li><strong>Phased Delivery:</strong> We propose a 6-stage rollout: Flow Mapping, Technical Feasibility, Usability Testing, Limited Beta, Controlled A/B Testing, and Phased Production Scaling.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's conclude with our final recommendation and request for feedback.</div>
        """
    },

    # SLIDE 20: FINAL RECOMMENDATION
    {
        "id": "slide-20",
        "number": "20",
        "stage": "Deliver",
        "tag": "Product Recommendation",
        "evidenceType": "Proposed Solution",
        "title": "A Better Way to Choose the Resume You Submit",
        "subtitle": "Summary of findings, proposed next steps, and professional request for feedback from Naukri PMs",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; padding: 6px 0;">
          <!-- Core Takeaway Card -->
          <div class="card card-blue" style="padding: 18px 22px; border: 2px solid var(--naukri-blue-border); background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);">
            <div style="font-size: 10.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: var(--naukri-blue); margin-bottom: 4px;">
              Closing Strategic Recommendation
            </div>
            <div style="font-size: 17px; font-weight: 800; color: var(--navy-dark); line-height: 1.4; margin-bottom: 8px;">
              "Candidates may maintain different resume versions for different opportunities. This proposal explores a simpler way to manage those documents and choose the appropriate one when applying, without silently replacing previously saved files."
            </div>
            <div style="font-size: 12px; color: var(--slate-700); line-height: 1.5;">
              The feature is designed to reduce unnecessary navigation and resume-management effort within supported Naukri application flows. Its actual effect on application completion and candidate satisfaction should be established through a controlled pilot.
            </div>
          </div>
          
          <!-- Three Strategic Benefit Pillars -->
          <div class="grid-3" style="gap: 12px;">
            <div class="card card-tinted" style="text-align: center; padding: 12px;">
              <div style="font-size: 20px; margin-bottom: 3px;">🎯</div>
              <div style="font-weight: 800; font-size: 12.5px; color: var(--navy-dark); margin-bottom: 2px;">Fewer Application Steps</div>
              <p style="font-size: 11px; color: var(--slate-600); line-height: 1.35;">
                Select or upload the appropriate resume at the moment of apply without navigating away from active applications.
              </p>
            </div>
            
            <div class="card card-tinted" style="text-align: center; padding: 12px;">
              <div style="font-size: 20px; margin-bottom: 3px;">🛡️</div>
              <div style="font-weight: 800; font-size: 12.5px; color: var(--navy-dark); margin-bottom: 2px;">Independent Resume Management</div>
              <p style="font-size: 11px; color: var(--slate-600); line-height: 1.35;">
                Maintain versioned documents with custom naming, separate from master profile data, with zero accidental overwriting.
              </p>
            </div>
            
            <div class="card card-tinted" style="text-align: center; padding: 12px;">
              <div style="font-size: 20px; margin-bottom: 3px;">🤝</div>
              <div style="font-weight: 800; font-size: 12.5px; color: var(--navy-dark); margin-bottom: 2px;">Candidate-Controlled Submission</div>
              <p style="font-size: 11px; color: var(--slate-600); line-height: 1.35;">
                Preselects designated default for convenience; strictly requires explicit candidate review before submission.
              </p>
            </div>
          </div>
          
          <!-- Recommendation Next Steps Box -->
          <div style="background: var(--slate-50); border: 1.5px solid var(--slate-200); border-radius: var(--radius-md); padding: 10px 14px; font-size: 11.5px; color: var(--slate-700); line-height: 1.45;">
            <strong>Recommended Next Step:</strong> Validate the current candidate journey across Naukri's supported application flows, assess the proposed Resume Library against existing capabilities, and explore a small usability pilot before considering a broader rollout.
          </div>
          
          <!-- Professional Invitation for Feedback -->
          <div style="text-align: center; padding: 12px 16px; background: var(--navy-dark); border-radius: var(--radius-md); color: white;">
            <div style="font-size: 14.5px; font-weight: 800; letter-spacing: -0.2px;">
              "I would welcome feedback from Naukri's Product team on the problem definition, current application behaviour, and suitability of this proposed improvement."
            </div>
            <div style="font-size: 11px; color: #93C5FD; margin-top: 3px;">
              Prepared by Aditya Sharma • Independent Product Management Case Study
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 20 — Final Recommendation & Invitation for Dialogue</h4>
        <p>In conclusion:</p>
        <ul>
          <li><strong>Core Proposal:</strong> Giving candidates a dedicated Resume Library within their single profile offers a practical, candidate-controlled solution to a real observed friction point in the job search journey.</li>
          <li><strong>The Three Strategic Benefits:</strong> Fewer application steps, independent resume management without accidental overwrites, and candidate-controlled submission with explicit review.</li>
          <li><strong>Our Recommended Next Step:</strong> Validate the current candidate journey across Naukri's supported flows, assess this concept against internal data, and run a small usability pilot.</li>
          <li><strong>Professional Ask:</strong> We conclude with a professional invitation to Naukri's Product Management team for feedback on our problem framing, assumptions, and proposal suitability.</li>
        </ul>
        <div class='cue-box'><strong>Appendix:</strong> Detailed survey results, verified competitor citations, and technical glossaries follow on Slides 21 to 23.</div>
        """
    },

    # SLIDE 21: APPENDIX A: DETAILED SURVEY RESULTS & METHODOLOGY
    {
        "id": "slide-21",
        "number": "21",
        "stage": "Appendix",
        "tag": "Appendix A",
        "evidenceType": "Survey Finding",
        "title": "Appendix A: Detailed Survey Data & Limitations",
        "subtitle": "Complete Q1–Q13 data catalog, respondent profile, and research integrity boundaries",
        "content": """
        <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 16px; height: 100%;">
          <!-- Left: Complete Q1-Q13 Data Catalog -->
          <div class="card" style="padding: 12px 16px; overflow-y: auto;">
            <div class="card-header-sm">
              <span>Complete Exploratory Survey Catalog</span>
              <span class="badge badge-blue">N=45 Student Sample</span>
            </div>
            <div style="display: flex; flex-direction: column; gap: 5px; font-size: 10.5px; color: var(--slate-700); margin-top: 4px;">
              <div><strong>Q1. Recent Activity:</strong> 90% applied for a job, internship, or placement in the last 90 days.</div>
              <div><strong>Q2. Cohort Breakdown:</strong> 80% college students looking for placements/full-time; 20% looking for internships.</div>
              <div><strong>Q3. Role Categories:</strong> 5% (1 role), 15% (2 roles), 20% (3 roles), 60% (4+ roles) -> 80% apply to 3+ roles.</div>
              <div><strong>Q4. Multiple Versions:</strong> 90% maintain different resume versions for different role tracks.</div>
              <div><strong>Q5. Motivations:</strong> Highlighting distinct skills, multiple industries, varied career pathways, JD tailoring.</div>
              <div><strong>Q6. Storage Methods:</strong> Local folders on PC/phone, separate portal uploads, editing before apply.</div>
              <div><strong>Q7. Friction Frequency:</strong> 90% frequently need a resume different from profile resume while applying.</div>
              <div><strong>Q8. Workarounds:</strong> Replacing uploaded profile CV, uploading during apply, postponing, skipping.</div>
              <div><strong>Q9 & Q10:</strong> Suggested inconvenience; exact counts and written examples omitted to avoid fabrication.</div>
              <div><strong>Q11. Feature Valuation:</strong> 90% rated the proposed feature <em>'Extremely useful'</em>.</div>
              <div><strong>Q12. Stated Adoption:</strong> 90% reported being <em>'Very likely'</em> to use the feature.</div>
              <div><strong>Q13. Desired Features:</strong> Custom names, apply-time selection, submitted history, document management.</div>
            </div>
          </div>
          
          <!-- Right: Methodology & Research Integrity Disclosures -->
          <div class="card card-tinted" style="padding: 12px 16px; overflow-y: auto;">
            <div class="card-header-sm">
              <span>Methodological Disclosures</span>
              <span class="badge badge-amber">Research Integrity</span>
            </div>
            <div style="display: flex; flex-direction: column; gap: 6px; font-size: 10.5px; color: var(--slate-700); margin-top: 4px;">
              <div><strong>1. Student-Focused Cohort:</strong> Respondents were recruited via direct outreach to college students. Working professionals were not represented in this sample.</div>
              <div><strong>2. No Inferred Counts:</strong> Where exact counts were not recorded, we report qualitative summaries rather than inferring counts from rounded percentages.</div>
              <div><strong>3. Stated vs. Observed:</strong> Q11 and Q12 measure stated intent, which is a directional signal, not proof of production conversion.</div>
              <div><strong>4. Platform Attribution:</strong> The survey captured general job-seeking behaviour across platforms and did not measure portal-specific market shares.</div>
            </div>
            
            <div style="margin-top: 10px; background: var(--amber-light); border: 1px solid var(--amber-border); padding: 6px 10px; border-radius: 4px; font-size: 10px; color: #92400E;">
              <strong>Rigor Guarantee:</strong> No unsupported counts, fabricated quotations, or unverified statistical generalizations have been included.
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 21 — Appendix A: Survey Catalog & Research Integrity</h4>
        <p>This appendix documents our complete exploratory survey dataset from Q1 through Q13:</p>
        <ul>
          <li>We transparently document the exact responses collected and explain why Q9 and Q10 counts were omitted to prevent fabricating data.</li>
          <li>We reinforce that this student cohort provides an exploratory directional signal rather than a company-wide statistical sample.</li>
        </ul>
        """
    },

    # SLIDE 22: APPENDIX B: OFFICIAL COMPETITOR SOURCES & REFERENCES
    {
        "id": "slide-22",
        "number": "22",
        "stage": "Appendix",
        "tag": "Appendix B",
        "evidenceType": "Official Public Documentation",
        "title": "Appendix B: Official Competitor Documentation & Links",
        "subtitle": "Full URLs, retrieval dates, and context for Naukri, LinkedIn, and Indeed India documentation",
        "content": """
        <div class="card" style="padding: 14px 18px; height: 100%; overflow-y: auto;">
          <div class="card-header-sm">
            <span>Verified Public Documentation Sources</span>
            <span class="badge badge-gray">Verified November 2026</span>
          </div>
          
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 10.5px; color: var(--slate-700); margin-top: 6px;">
            <!-- Ref 1 -->
            <div id="ref-1" style="background: var(--slate-50); padding: 8px 10px; border-radius: 4px; border-left: 3px solid var(--naukri-blue);">
              <div style="font-weight: 700; color: var(--navy-dark);">[1] Naukri FastForward Official FAQ: Multiple Profiles & CVs</div>
              <div style="color: var(--slate-600); margin: 2px 0;">
                "One Naukri username can have up to five profiles. Each profile can have only one resume attached to it." (Context: text and visual CV packages).
              </div>
              <a href="https://resume.naukri.com/frequently-asked-questions-faq/i-already-have-got-a-text-cv-developed-through-naukri-after-getting-a-visual-cv-developed-can-i-upload-both-the-text-cv-and-the-visual-cv-on-my-same-naukri-profile-which-i-have/" target="_blank" style="color: var(--naukri-blue); word-break: break-all; font-size: 9.5px;">
                resume.naukri.com/frequently-asked-questions-faq/...
              </a>
            </div>
            
            <!-- Ref 2a -->
            <div id="ref-2a" style="background: var(--slate-50); padding: 8px 10px; border-radius: 4px; border-left: 3px solid var(--naukri-blue);">
              <div style="font-weight: 700; color: var(--navy-dark);">[2a] Naukri AI Resume Maker Tool</div>
              <div style="color: var(--slate-600); margin: 2px 0;">
                Tool-specific creation of single resume documents from user profile credentials.
              </div>
              <a href="https://www.naukri.com/resume-maker" target="_blank" style="color: var(--naukri-blue); word-break: break-all; font-size: 9.5px;">
                www.naukri.com/resume-maker
              </a>
            </div>
            
            <!-- Ref 2b -->
            <div id="ref-2b" style="background: var(--slate-50); padding: 8px 10px; border-radius: 4px; border-left: 3px solid var(--naukri-blue);">
              <div style="font-weight: 700; color: var(--navy-dark);">[2b] Naukri Online Resume Builder FAQ (Tool Limits)</div>
              <div style="color: var(--slate-600); margin: 2px 0;">
                Tool FAQ documenting retention of up to 50 resumes/drafts within that specific builder.
              </div>
              <a href="https://resume.naukri.com/frequently-asked-questions-faq/how-many-resumes-can-i-create-using-online-resume-builder-tool/" target="_blank" style="color: var(--naukri-blue); word-break: break-all; font-size: 9.5px;">
                resume.naukri.com/frequently-asked-questions-faq/how-many-resumes-can-i-create...
              </a>
            </div>
            
            <!-- Ref 3 -->
            <div id="ref-3" style="background: var(--slate-50); padding: 8px 10px; border-radius: 4px; border-left: 3px solid #0077B5;">
              <div style="font-weight: 700; color: var(--navy-dark);">[3] LinkedIn Official Help: Manage Your Resumes</div>
              <div style="color: var(--slate-600); margin: 2px 0;">
                Documents storing up to 4 recently uploaded reusable resumes for Easy Apply flows.
              </div>
              <a href="https://www.linkedin.com/help/linkedin/answer/a512405/reusing-a-recently-used-resume-for-a-job-application-on-linkedin?lang=en" target="_blank" style="color: #0077B5; word-break: break-all; font-size: 9.5px;">
                www.linkedin.com/help/linkedin/answer/a512405/...
              </a>
            </div>
            
            <!-- Ref 3b -->
            <div id="ref-3b" style="background: var(--slate-50); padding: 8px 10px; border-radius: 4px; border-left: 3px solid #0077B5;">
              <div style="font-weight: 700; color: var(--navy-dark);">[3b] LinkedIn Official Help: View Resume Used in Application</div>
              <div style="color: var(--slate-600); margin: 2px 0;">
                Documents viewing the specific resume submitted for Easy Apply jobs.
              </div>
              <a href="https://www.linkedin.com/help/linkedin/answer/a513477" target="_blank" style="color: #0077B5; word-break: break-all; font-size: 9.5px;">
                www.linkedin.com/help/linkedin/answer/a513477
              </a>
            </div>
            
            <!-- Ref 4 -->
            <div id="ref-4" style="background: var(--slate-50); padding: 8px 10px; border-radius: 4px; border-left: 3px solid #003A9B;">
              <div style="font-weight: 700; color: var(--navy-dark);">[4] Indeed Official Help: Applying for a Job on Indeed</div>
              <div style="color: var(--slate-600); margin: 2px 0;">
                Confirms candidates can select existing uploaded resume or upload a different file during apply.
              </div>
              <a href="https://in.indeed.com/help/job-seekers/articles/204652920-applying-for-a-job-on-indeed?co=IN&hl=en" target="_blank" style="color: #003A9B; word-break: break-all; font-size: 9.5px;">
                in.indeed.com/help/.../applying-for-a-job-on-indeed
              </a>
            </div>
            
            <!-- Ref 5 -->
            <div id="ref-5" style="background: var(--slate-50); padding: 8px 10px; border-radius: 4px; border-left: 3px solid #003A9B;">
              <div style="font-weight: 700; color: var(--navy-dark);">[5] Indeed India Official Help: Managing Resume Files</div>
              <div style="color: var(--slate-600); margin: 2px 0;">
                Confirms only 1 resume file is stored on the account; new uploads replace existing.
              </div>
              <a href="https://in.indeed.com/help/job-seekers/articles/11314976176141-faqs-creating-uploading-and-managing-a-resume-file?co=IN&hl=en" target="_blank" style="color: #003A9B; word-break: break-all; font-size: 9.5px;">
                in.indeed.com/help/.../faqs-creating-uploading-and-managing-a-resume-file
              </a>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 22 — Appendix B: Competitor Help Centers & Citations</h4>
        <p>This appendix lists direct links, verification dates, and exact contextual notes for all competitor citations referenced across the presentation.</p>
        """
    },

    # SLIDE 23: APPENDIX C: TERMS, ASSUMPTIONS & GLOSSARY
    {
        "id": "slide-23",
        "number": "23",
        "stage": "Appendix",
        "tag": "Appendix C",
        "evidenceType": "Proposed Solution",
        "title": "Appendix C: Product Terms, Assumptions & Technical Glossary",
        "subtitle": "Definitions of core product concepts, technical hypotheses, and integration considerations",
        "content": """
        <div class="card" style="padding: 14px 18px; height: 100%; overflow-y: auto;">
          <div class="card-header-sm">
            <span>Product Glossary & Assumptions</span>
            <span class="badge badge-gray">Terminology</span>
          </div>
          
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 11px; color: var(--slate-700); margin-top: 6px;">
            <div style="background: var(--slate-50); padding: 8px 12px; border-radius: 4px; border-left: 3px solid var(--navy-dark);">
              <strong>Resume Library:</strong> A candidate-controlled collection of versioned resume documents with custom user-defined names, stored within the candidate's account.
            </div>
            
            <div style="background: var(--slate-50); padding: 8px 12px; border-radius: 4px; border-left: 3px solid var(--navy-dark);">
              <strong>Master Profile Record:</strong> Structured candidate career information (education, work history, skills) that remains the central record for recruiter search.
            </div>
            
            <div style="background: var(--slate-50); padding: 8px 12px; border-radius: 4px; border-left: 3px solid var(--naukri-blue);">
              <strong>Application-Time Selection:</strong> The user interaction allowing a candidate to choose which resume document to attach at the moment of applying for a specific job.
            </div>
            
            <div style="background: var(--slate-50); padding: 8px 12px; border-radius: 4px; border-left: 3px solid var(--emerald-accent);">
              <strong>Non-Destructive Saving:</strong> An architecture where newly uploaded documents do not overwrite or replace existing files unless explicitly confirmed by the candidate.
            </div>
            
            <div style="background: var(--slate-50); padding: 8px 12px; border-radius: 4px; border-left: 3px solid var(--teal-accent);">
              <strong>Document Version UUID:</strong> An immutable reference snapshot associated with an application submission so past records remain preserved.
            </div>
            
            <div style="background: var(--slate-50); padding: 8px 12px; border-radius: 4px; border-left: 3px solid var(--slate-400);">
              <strong>Supported vs. External Flows:</strong> On-platform applications hosted directly on Naukri vs. applications redirected to third-party employer ATS platforms.
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 23 — Appendix C: Glossary & Assumptions</h4>
        <p>This appendix clarifies the technical and product definitions used throughout the proposal, ensuring shared vocabulary between candidate UX and backend engineering.</p>
        """
    }
]
