# slides_research.py - Slides 05 to 08 (User Research, Current Journey, Validation & Root Causes, Competitor Benchmarking)

SLIDES_RESEARCH = [
    # SLIDE 05: USER RESEARCH & FINDINGS (Merges old Slides 7 & 8)
    {
        "id": "slide-5",
        "number": "05",
        "stage": "Research",
        "tag": "User Research & Findings",
        "evidenceType": "Survey Evidence N=100+",
        "title": "What We Learned from the Respondents",
        "subtitle": "Exploratory survey findings from 100+ college students applying across role categories",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 12px;">
          <!-- Top Row: 4 Separate Key Survey Finding Cards -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;">
            
            <div class="card card-blue" style="padding: 10px 12px; text-align: center;">
              <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue); letter-spacing: 0.5px; margin-bottom: 2px;">Maintain Multiple Resumes (Q4)</div>
              <div style="font-size: 34px; font-weight: 800; color: #1E3A8A; line-height: 1.1; margin: 4px 0;">90%</div>
              <div style="font-size: 11px; color: var(--slate-700); line-height: 1.35;">
                Maintain multiple tailored resume versions
              </div>
            </div>

            <div class="card card-indigo" style="padding: 10px 12px; text-align: center;">
              <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: #4F46E5; letter-spacing: 0.5px; margin-bottom: 2px;">Frequently Need Alternate (Q7)</div>
              <div style="font-size: 34px; font-weight: 800; color: #3730A3; line-height: 1.1; margin: 4px 0;">90%</div>
              <div style="font-size: 11px; color: var(--slate-700); line-height: 1.35;">
                Frequently need a different resume while applying
              </div>
            </div>

            <div class="card card-amber" style="padding: 10px 12px; text-align: center;">
              <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--amber-accent); letter-spacing: 0.5px; margin-bottom: 2px;">Rate Feature Useful (Q11)</div>
              <div style="font-size: 34px; font-weight: 800; color: #92400E; line-height: 1.1; margin: 4px 0;">90%</div>
              <div style="font-size: 11px; color: var(--slate-700); line-height: 1.35;">
                Rate the proposed feature extremely useful
              </div>
            </div>

            <div class="card card-emerald" style="padding: 10px 12px; text-align: center;">
              <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--emerald-accent); letter-spacing: 0.5px; margin-bottom: 2px;">Very Likely to Use (Q12)</div>
              <div style="font-size: 34px; font-weight: 800; color: #065F46; line-height: 1.1; margin: 4px 0;">90%</div>
              <div style="font-size: 11px; color: var(--slate-700); line-height: 1.35;">
                Report being very likely to adopt the feature
              </div>
            </div>

          </div>

          <!-- Middle Row: Role Distribution Chart + Motivations & Workarounds -->
          <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 16px; flex: 1;">
            
            <!-- Left: Visual Bar Chart of Role Categories -->
            <div class="card" style="padding: 14px 18px; display: flex; flex-direction: column; justify-content: space-between;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 12px; font-weight: 800; text-transform: uppercase; color: var(--navy-dark); letter-spacing: 0.5px;">
                  Role Categories Applied To (N=100+)
                </span>
                <span class="badge badge-blue" style="font-size: 10px;">80% across 3+ roles</span>
              </div>
              
              <!-- Custom Visual CSS Horizontal Bar Chart (Rounded percentages without fabricated exact counts) -->
              <div style="display: flex; flex-direction: column; gap: 8px; flex: 1; justify-content: center;">
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 600; color: var(--slate-700); margin-bottom: 3px;">
                    <span>4 or more distinct role types</span>
                    <strong style="color: #1E3A8A;">60%</strong>
                  </div>
                  <div style="width: 100%; height: 14px; background: #E2E8F0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 60%; height: 100%; background: linear-gradient(90deg, #1856EA, #3B82F6); border-radius: 4px;"></div>
                  </div>
                </div>

                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 600; color: var(--slate-700); margin-bottom: 3px;">
                    <span>3 distinct role types</span>
                    <strong style="color: #4F46E5;">20%</strong>
                  </div>
                  <div style="width: 100%; height: 14px; background: #E2E8F0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 20%; height: 100%; background: linear-gradient(90deg, #6366F1, #818CF8); border-radius: 4px;"></div>
                  </div>
                </div>

                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 600; color: var(--slate-700); margin-bottom: 3px;">
                    <span>2 distinct role types</span>
                    <strong style="color: #0D9488;">15%</strong>
                  </div>
                  <div style="width: 100%; height: 14px; background: #E2E8F0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 15%; height: 100%; background: linear-gradient(90deg, #0D9488, #14B8A6); border-radius: 4px;"></div>
                  </div>
                </div>

                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 600; color: var(--slate-700); margin-bottom: 3px;">
                    <span>1 role type only</span>
                    <strong style="color: var(--slate-600);">5%</strong>
                  </div>
                  <div style="width: 100%; height: 14px; background: #E2E8F0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 5%; height: 100%; background: #94A3B8; border-radius: 4px;"></div>
                  </div>
                </div>
              </div>

              <div style="font-size: 11px; color: var(--slate-500); margin-top: 6px; padding-top: 6px; border-top: 1px solid var(--slate-100);">
                Key Insight: Only 5% of early-career applicants rely on a single narrow role category.
              </div>
            </div>

            <!-- Right: Motivations & Workarounds Panels -->
            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div class="card card-teal" style="padding: 10px 14px; flex: 1;">
                <div style="font-size: 11.5px; font-weight: 700; color: #115E59; margin-bottom: 4px;">
                  💡 Reported Candidate Motivations (Q5)
                </div>
                <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.4;">
                  Candidates report maintaining multiple resumes to:<br>
                  • Highlight <strong>different skills</strong> relevant to each role<br>
                  • Apply to <strong>different industries</strong> simultaneously<br>
                  • Pursue <strong>different career paths</strong> in parallel<br>
                  • Tailor documents to <strong>specific job descriptions</strong>
                </div>
              </div>

              <div class="card card-amber" style="padding: 10px 14px; flex: 1;">
                <div style="font-size: 11.5px; font-weight: 700; color: #92400E; margin-bottom: 4px;">
                  📁 Reported Workarounds (Q6, Q8)
                </div>
                <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.4;">
                  Reported behaviors when a different resume is needed:<br>
                  • Maintaining separate storage locations (drives, local folders)<br>
                  • Uploading a different document within the portal<br>
                  • Leaving or pausing the application and returning later<br>
                  • Skipping the application or postponing submission
                </div>
              </div>
            </div>

          </div>

          <!-- Bottom: Methodological Limitation Disclaimer -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 8px 16px; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 11.5px; color: var(--slate-600);">
              <strong style="color: var(--navy-dark);">Research Boundary:</strong> Exploratory survey based on personal outreach with 100+ college-student respondents. Does not establish market-wide demand or prove that the same issue affects all Naukri users.
            </div>
            <span style="font-size: 11px; color: var(--naukri-blue); font-weight: 700; white-space: nowrap; margin-left: 10px;">
              Full Q1–Q13 Data in Appendix A →
            </span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 05 — User Research & Findings (Suggested Duration: ~75 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To investigate candidate behavior, I conducted an exploratory survey with 100+ college job seekers. Here are the core empirical findings:</p>
        <ul>
          <li><strong>90%</strong> were actively applying in the last 90 days—80% seeking full-time placements and 20% seeking internships.</li>
          <li><strong>80%</strong> applied across three or more distinct role categories. In fact, 60% applied to four or more roles. Only 5% applied to a single role.</li>
          <li><strong>90%</strong> maintain multiple resume versions, frequently needing an alternate version during active applications.</li>
          <li><strong>90%</strong> rated the proposed Resume Library extremely useful and expressed very high intent to use it.</li>
        </ul>
        <p>Candidates reported tailoring documents to highlight relevant skills and projects across roles, and managing separate documents independently. We avoid treating rounded percentages as exact respondent counts and note that exact open-ended counts were not recorded.</p>
        <p>We clearly state the research boundary: this exploratory cohort is student-focused; complete Q1 to Q13 responses are cataloged in Appendix A."</p>
        <div class='cue-box'><strong>Transition:</strong> Let's see how this plays out in the candidate's actual application journey on the platform.</div>
        """
    },

    # SLIDE 06: CURRENT CANDIDATE JOURNEY & FRICTION (Preserves old Slide 9)
    {
        "id": "slide-6",
        "number": "06",
        "stage": "Validate",
        "tag": "Current Candidate Journey",
        "evidenceType": "User-Reported Journey",
        "title": "Where Resume Management Can Interrupt the Application Journey",
        "subtitle": "Examining common application paths and candidate-reported friction points",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 12px;">
          <!-- Top: Linear Candidate Journey Flow -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 12px 16px;">
            <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); letter-spacing: 0.6px; margin-bottom: 8px;">
              Common Candidate Journey Sequence
            </div>
            <div style="display: flex; align-items: center; justify-content: space-between;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background: var(--navy-dark); color: white; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700;">1</span>
                <span style="font-size: 12.5px; font-weight: 700; color: var(--navy-dark);">Maintain Profile</span>
              </div>
              <span style="color: var(--slate-400); font-weight: 700;">→</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background: var(--navy-dark); color: white; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700;">2</span>
                <span style="font-size: 12.5px; font-weight: 700; color: var(--navy-dark);">Search & Find Job</span>
              </div>
              <span style="color: var(--slate-400); font-weight: 700;">→</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background: var(--navy-dark); color: white; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700;">3</span>
                <span style="font-size: 12.5px; font-weight: 700; color: var(--navy-dark);">Click Apply</span>
              </div>
              <span style="color: var(--slate-400); font-weight: 700;">→</span>
              <div style="display: flex; align-items: center; gap: 8px; background: #FFF1F2; border: 1.5px solid #FECDD3; padding: 4px 10px; border-radius: 6px;">
                <span style="background: var(--rose-accent); color: white; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700;">4</span>
                <span style="font-size: 12.5px; font-weight: 700; color: var(--rose-accent);">Decide Resume to Submit</span>
              </div>
            </div>
          </div>

          <!-- Middle: 3 Application Paths Comparison -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; flex: 1;">
            
            <!-- Path A: Direct In-Flow Upload -->
            <div class="card card-emerald" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-teal">Path A</span>
                  <span style="font-size: 11px; color: #166534; font-weight: 600;">Seamless</span>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  In-Flow Alternate Upload
                </div>
                <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  Application flow permits candidate to attach an alternate document directly within the application modal without leaving the flow.
                </div>
              </div>
              <div style="background: #ECFDF5; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: #166534; margin-top: 8px;">
                ✓ Low friction; document submitted directly.
              </div>
            </div>

            <!-- Path B: Profile-Attached Workflow -->
            <div class="card card-rose" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-red">Path B</span>
                  <span style="font-size: 11px; color: #9F1239; font-weight: 700;">User-Reported Friction</span>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  Profile-Attached Workflow
                </div>
                <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  Candidate encounters an application flow tied to the profile resume. Reported workaround involves leaving or pausing the application, updating the resume associated with the profile, and returning to complete the application.
                </div>
              </div>
              <div style="background: #FFF1F2; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: #9F1239; margin-top: 8px;">
                ⚠️ Reported friction: context-switching, overwrite risk, and drop-off.
              </div>
            </div>

            <!-- Path C: External ATS Redirect -->
            <div class="card" style="display: flex; flex-direction: column; justify-content: space-between; border-top: 4px solid var(--slate-500);">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-gray">Path C</span>
                  <span style="font-size: 11px; color: var(--slate-500); font-weight: 600;">Third-Party</span>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  External ATS Portal
                </div>
                <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  Application redirects out of Naukri to company career site (e.g. Workday, Greenhouse). Document handling is governed by the external employer portal.
                </div>
              </div>
              <div style="background: #F1F5F9; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: var(--slate-600); margin-top: 8px;">
                ℹ️ Outside Naukri native UI boundary.
              </div>
            </div>

          </div>

          <!-- Bottom: Reported Candidate Friction & Validation Boundary -->
          <div style="background: #FFFFFF; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 10px 16px; display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 14px; align-items: center;">
            <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
              <strong style="color: var(--navy-dark);">Reported Workarounds & Validation Boundary:</strong>
              Candidates reported pausing or leaving applications to adjust their resume, or postponing submission. The exact proportion of Naukri postings following Path A vs Path B vs Path C requires internal platform telemetry validation.
            </div>
            <div style="font-size: 11px; color: var(--slate-500); border-left: 2px solid var(--amber-accent); padding-left: 10px;">
              *Labelled as user-reported experience. Exact platform workflow behaviors require Naukri telemetry validation.
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 06 — Current Candidate Journey & Friction (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "When we examine candidate application journeys, friction surfaces right at step 4: deciding which resume to submit.</p>
        <p>Depending on the specific posting, candidates encounter three distinct paths:</p>
        <ul>
          <li><strong>Path A:</strong> In-flow upload allows attaching an alternate document. This works smoothly when available.</li>
          <li><strong>Path B (Reported Friction):</strong> The candidate encounters a flow tied strictly to the profile resume. Reported candidate workarounds involve pausing or leaving the application, navigating to profile settings to update the file, and returning to finish applying. This context-switching risks application drop-off and file replacement.</li>
          <li><strong>Path C:</strong> External ATS redirects out to third-party employer sites, where document handling is outside Naukri's native controls.</li>
        </ul>
        <p>We specifically label Path B as candidate-reported friction, noting that the exact distribution of flows across Naukri requires platform telemetry validation."</p>
        <div class='cue-box'><strong>Transition:</strong> Let's separate what our evidence firmly supports from what still requires internal Naukri validation.</div>
        """
    },

    # SLIDE 07: PROBLEM VALIDATION & ROOT-CAUSE ANALYSIS (Merges old Slides 10 & 11)
    {
        "id": "slide-7",
        "number": "07",
        "stage": "Diagnose",
        "tag": "Validation & Root Causes",
        "evidenceType": "Requires Naukri Validation",
        "title": "What the Evidence Supports — and What We Still Need to Investigate",
        "subtitle": "Auditing our current research boundaries and diagnosing underlying structural hypotheses",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 12px;">
          <!-- Two Main Columns: Section A (Evidence Audit) & Section B (Root-Cause Hypotheses) -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; flex: 1;">
            
            <!-- Section A: Evidence Audit (Supported vs Requires Validation) -->
            <div class="card" style="padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; color: var(--navy-dark); letter-spacing: 0.5px; margin-bottom: 8px;">
                  Section A: Evidence Audit
                </div>
                
                <!-- Supported by Data -->
                <div style="background: #ECFDF5; border: 1.5px solid #A7F3D0; border-radius: 6px; padding: 10px 12px; margin-bottom: 10px;">
                  <div style="font-size: 11.5px; font-weight: 700; color: #166534; display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
                    <span>✓ SUPPORTED BY CURRENT EVIDENCE (N=100+)</span>
                  </div>
                  <ul style="font-size: 11.5px; color: #14532D; padding-left: 16px; line-height: 1.45; margin: 0;">
                    <li>Multi-role applications are standard practice (80% across 3+ roles).</li>
                    <li>Maintaining multiple resume versions is normal candidate behavior (90%).</li>
                    <li>Strong candidate intent and appetite for a dedicated library (90%).</li>
                    <li>Competitors offer different resume-management capabilities, including reusable resume storage on LinkedIn and alternate application-time uploads on Indeed.</li>
                  </ul>
                </div>

                <!-- Requires Validation -->
                <div style="background: #FFFBEB; border: 1.5px solid #FDE68A; border-radius: 6px; padding: 10px 12px;">
                  <div style="font-size: 11.5px; font-weight: 700; color: #92400E; display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
                    <span>⚠️ REQUIRES NAUKRI INTERNAL VALIDATION</span>
                  </div>
                  <ul style="font-size: 11.5px; color: #78350F; padding-left: 16px; line-height: 1.45; margin: 0;">
                    <li>Exact percentage of candidates who experience Path B profile redirects.</li>
                    <li>Telemetry on application start-to-completion drop-offs correlated with resume edits.</li>
                    <li>Ratio of native applications vs external ATS redirects across listings.</li>
                    <li>Engineering assessment of candidate document storage models and indexing.</li>
                  </ul>
                </div>
              </div>

              <div style="font-size: 10.5px; color: var(--slate-500); margin-top: 6px;">
                Maintains strict objectivity by separating sample findings from platform truths.
              </div>
            </div>

            <!-- Section B: 5 Root-Cause Hypotheses -->
            <div class="card card-purple" style="padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <span style="font-size: 12px; font-weight: 800; text-transform: uppercase; color: #6D28D9; letter-spacing: 0.5px;">
                    Section B: Root-Cause Hypotheses
                  </span>
                  <span class="badge" style="background:#EDE9FE; color:#6D28D9;">Hypotheses Only</span>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 7px;">
                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H1. Selection & Storage Integration:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Hypothesis: Resume selection options and persistent document storage may not be unified in certain application workflows.
                    </div>
                  </div>

                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H2. In-Flow Reusability:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Hypothesis: Alternate documents uploaded in some flows may not automatically save to candidate accounts for future applications.
                    </div>
                  </div>

                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H3. Document Model Architecture:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Hypothesis: The candidate data schema may center primarily on a single master profile resume rather than a candidate-managed document library.
                    </div>
                  </div>

                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H4. Version Traceability:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Hypothesis: Candidates may lack visible audit records of the exact document version submitted to past applications.
                    </div>
                  </div>

                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H5. Recruiter Search Indexing Considerations:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Hypothesis: How candidate profiles are indexed for recruiter search when multiple documents exist remains an open architectural question for engineering review.
                    </div>
                  </div>
                </div>
              </div>

              <div style="font-size: 10.5px; color: #7C3AED; margin-top: 6px;">
                *These are analytical hypotheses for engineering investigation, not confirmed internal architecture.
              </div>
            </div>

          </div>

          <!-- Bottom: Transition Banner -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 8px 16px; font-size: 11.5px; color: var(--slate-700);">
            <strong style="color: var(--navy-dark);">PM Assessment:</strong> We treat these potential root causes as hypotheses to be evaluated with Naukri engineering and analytics teams, rather than confirmed technical defects.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 07 — Problem Validation & Root Causes (Suggested Duration: ~75 seconds)</h4>
        <p><strong>Speaker Script:</strong> "A disciplined PM distinguishes firmly between verified sample data and unverified hypotheses.</p>
        <p>In <strong>Section A</strong>, our evidence confirms that multi-role applications are widespread (80%), multiple resumes are common (90%), and candidates express strong desire for a library. However, what <em>requires Naukri validation</em> is the internal telemetry: how many candidates abandon applications during resume edits, and what percentage of applications flow through Path A vs Path B vs Path C?</p>
        <p>In <strong>Section B</strong>, we examine five structural hypotheses behind the friction: decoupled selection in certain flows, lack of reusability, single-resume legacy profile models, version traceability questions, and recruiter indexing considerations. We explicitly frame these as hypotheses for engineering evaluation rather than known internal facts."</p>
        <div class='cue-box'><strong>Transition:</strong> How do other leading talent platforms solve this multi-resume challenge? Let's benchmark the competition.</div>
        """
    },

    # SLIDE 08: COMPETITOR BENCHMARKING (Preserves old Slide 12)
    {
        "id": "slide-8",
        "number": "08",
        "stage": "Assess",
        "tag": "Competitor Benchmarking",
        "evidenceType": "Official Documentation",
        "title": "How Existing Platforms Handle Resume Selection",
        "subtitle": "Benchmarking resume management approaches across Naukri, LinkedIn, and Indeed India",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 12px;">
          <!-- 3-Platform Benchmark Grid -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; flex: 1;">
            
            <!-- Naukri.com Platform -->
            <div class="card card-blue" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <span class="badge badge-blue">Naukri.com</span>
                  <span style="font-size: 10.5px; color: var(--slate-500);">Current Platform</span>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
                  Profile & Application Handling
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  <div>
                    <strong>• FastForward Documented Limit:</strong> FastForward FAQ specifically documents creating up to 5 profiles per username with 1 resume per profile in text/visual CV packages.
                  </div>
                  <div>
                    <strong>• Application Experience:</strong> The author encountered a profile-associated resume workflow in the application journey. Whether alternate resume selection is supported across other direct application flows requires hands-on and internal Naukri validation.
                  </div>
                  <div>
                    <strong>• Builder Capabilities:</strong> Standalone resume builder tools exist with tool-specific limits distinct from general profile applications.
                  </div>
                </div>
              </div>
              <div style="background: #EFF6FF; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: var(--naukri-blue); margin-top: 8px; font-weight: 600;">
                Opportunity: Explore persistent in-profile resume library.
              </div>
            </div>

            <!-- LinkedIn Platform -->
            <div class="card card-indigo" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <span class="badge" style="background:#EDE9FE; color:#4F46E5;">LinkedIn</span>
                  <span style="font-size: 10.5px; color: var(--slate-500);">Documented</span>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
                  Up to 4 Reusable Resumes
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  <div>
                    <strong>• Reusable Storage:</strong> Stores up to 4 recently uploaded resumes in candidate job settings for Easy Apply.
                  </div>
                  <div>
                    <strong>• In-Flow Selection:</strong> Allows candidate to select from stored resumes inside the application modal.
                  </div>
                  <div>
                    <strong>• Document History:</strong> Logs which specific resume was submitted to past Easy Apply applications.
                  </div>
                </div>
              </div>
              <div style="background: #EEF2FF; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: #4F46E5; margin-top: 8px; font-weight: 600;">
                Validated model: 4 persistent resumes in Easy Apply.
              </div>
            </div>

            <!-- Indeed India Platform -->
            <div class="card card-teal" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <span class="badge badge-teal">Indeed India</span>
                  <span style="font-size: 10.5px; color: var(--slate-500);">Documented</span>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
                  1 Stored File & Apply-Time Upload
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  <div>
                    <strong>• Stored Account Resume:</strong> Allows 1 stored resume file on account; uploading a new stored file replaces the prior file.
                  </div>
                  <div>
                    <strong>• Application Instructions:</strong> Application instructions permit uploading a different document from device during an application.
                  </div>
                  <div>
                    <strong>• Documentation Boundary:</strong> Documentation does not explicitly establish whether an apply-time upload updates the stored account resume file.
                  </div>
                </div>
              </div>
              <div style="background: #F0FDFA; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: var(--teal-accent); margin-top: 8px; font-weight: 600;">
                Validated model: Separation of apply-time upload capability.
              </div>
            </div>

          </div>

          <!-- Bottom: Strategic Takeaway Callout -->
          <div style="background: #FFFFFF; border: 1.5px solid var(--naukri-blue); border-left: 5px solid var(--naukri-blue); border-radius: 8px; padding: 12px 18px; box-shadow: 0 4px 12px rgba(24,86,234,0.06);">
            <div style="font-size: 11.5px; font-weight: 800; text-transform: uppercase; color: var(--naukri-blue); letter-spacing: 0.6px; margin-bottom: 3px;">
              Strategic Product Conclusion
            </div>
            <div style="font-size: 13px; color: var(--navy-dark); line-height: 1.5; font-weight: 600;">
              "The opportunity is not simply to introduce multiple resume uploads. It is to explore persistent, independent resume management within one comprehensive candidate profile, with application-time selection and non-destructive saving."
            </div>
          </div>

          <!-- Footnote Citation -->
          <div style="font-size: 10.5px; color: var(--slate-500); display: flex; justify-content: space-between;">
            <span>*Sources: Official Public Help Centers (Naukri FastForward FAQs, LinkedIn Help, Indeed India Support). Verified Nov 2026.</span>
            <span style="color: var(--naukri-blue); font-weight: 600;">Detailed documentation links in Appendix B →</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 08 — Competitor Benchmarking (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To understand market norms, we benchmarked official documentation across Naukri, LinkedIn, and Indeed India:</p>
        <ul>
          <li><strong>Naukri.com:</strong> We do not describe Naukri universally as a single-resume platform. Its cited FastForward FAQ specifically documents creating up to 5 profiles per username with 1 resume per profile in text/visual CV packages. However, in standard candidate job applications, candidates typically reference their active profile resume without an in-flow library selector.</li>
          <li><strong>LinkedIn:</strong> Offers up to 4 reusable uploaded resumes directly accessible in Easy Apply, and logs submitted versions in application history.</li>
          <li><strong>Indeed India:</strong> Maintains 1 stored profile CV, and application instructions permit uploading a different document from device during an application. The documentation does not explicitly establish whether that upload overwrites the stored file.</li>
        </ul>
        <p>The strategic takeaway: the opportunity is exploring a <strong>persistent, candidate-controlled Resume Library inside a single profile</strong>, with application-time selection and non-destructive saving."</p>
        <div class='cue-box'><strong>Transition:</strong> Which product approach best solves this challenge? Let's evaluate five strategic alternatives.</div>
        """
    }
]
