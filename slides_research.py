# slides_research.py - Slides 05 to 08 (User Research, Current Journey, Validation & Root Causes, Competitor Benchmarking)

SLIDES_RESEARCH = [
    # SLIDE 05: USER RESEARCH & FINDINGS (Merges old Slides 7 & 8)
    {
        "id": "slide-5",
        "number": "05",
        "stage": "Research",
        "tag": "User Research & Findings",
        "evidenceType": "Survey Evidence N=45",
        "title": "What We Learned from the Respondents",
        "subtitle": "Exploratory survey findings from 45 college students applying across role categories",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 12px;">
          <!-- Top Row: 4 Key Quantitative Stat Cards -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
            
            <div class="card card-blue" style="padding: 12px 14px; text-align: center;">
              <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue); letter-spacing: 0.5px;">Active Job Seekers</div>
              <div style="font-size: 34px; font-weight: 800; color: #1E3A8A; line-height: 1.1; margin: 4px 0;">90%</div>
              <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.35;">
                Applied in last 90 days<br>
                <span style="font-size: 10.5px; color: var(--slate-500);">(80% placements, 20% internships)</span>
              </div>
            </div>

            <div class="card card-indigo" style="padding: 12px 14px; text-align: center;">
              <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: #4F46E5; letter-spacing: 0.5px;">Multi-Role Volume</div>
              <div style="font-size: 34px; font-weight: 800; color: #3730A3; line-height: 1.1; margin: 4px 0;">80%</div>
              <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.35;">
                Applied across <strong>3+ role categories</strong><br>
                <span style="font-size: 10.5px; color: var(--slate-500);">(60% applied to 4+ roles)</span>
              </div>
            </div>

            <div class="card card-amber" style="padding: 12px 14px; text-align: center;">
              <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--amber-accent); letter-spacing: 0.5px;">Resume Variation</div>
              <div style="font-size: 34px; font-weight: 800; color: #92400E; line-height: 1.1; margin: 4px 0;">90%</div>
              <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.35;">
                Maintain multiple resume versions<br>
                <span style="font-size: 10.5px; color: var(--slate-500);">(Frequent alternate CV need)</span>
              </div>
            </div>

            <div class="card card-emerald" style="padding: 12px 14px; text-align: center;">
              <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--emerald-accent); letter-spacing: 0.5px;">Feature Intent</div>
              <div style="font-size: 34px; font-weight: 800; color: #065F46; line-height: 1.1; margin: 4px 0;">90%</div>
              <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.35;">
                Rated feature extremely useful<br>
                <span style="font-size: 10.5px; color: var(--slate-500);">(90% reported very likely to use)</span>
              </div>
            </div>

          </div>

          <!-- Middle Row: Role Distribution Chart + Motivations & Workarounds -->
          <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 16px; flex: 1;">
            
            <!-- Left: Visual Bar Chart of Role Categories -->
            <div class="card" style="padding: 14px 18px; display: flex; flex-direction: column; justify-content: space-between;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 12px; font-weight: 800; text-transform: uppercase; color: var(--navy-dark); letter-spacing: 0.5px;">
                  Role Categories Applied To (N=45)
                </span>
                <span class="badge badge-blue" style="font-size: 10px;">80% across 3+ roles</span>
              </div>
              
              <!-- Custom Visual CSS Horizontal Bar Chart -->
              <div style="display: flex; flex-direction: column; gap: 8px; flex: 1; justify-content: center;">
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 600; color: var(--slate-700); margin-bottom: 3px;">
                    <span>4 or more distinct role types</span>
                    <strong style="color: #1E3A8A;">60% (27 candidates)</strong>
                  </div>
                  <div style="width: 100%; height: 14px; background: #E2E8F0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 60%; height: 100%; background: linear-gradient(90deg, #1856EA, #3B82F6); border-radius: 4px;"></div>
                  </div>
                </div>

                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 600; color: var(--slate-700); margin-bottom: 3px;">
                    <span>3 distinct role types</span>
                    <strong style="color: #4F46E5;">20% (9 candidates)</strong>
                  </div>
                  <div style="width: 100%; height: 14px; background: #E2E8F0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 20%; height: 100%; background: linear-gradient(90deg, #6366F1, #818CF8); border-radius: 4px;"></div>
                  </div>
                </div>

                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 600; color: var(--slate-700); margin-bottom: 3px;">
                    <span>2 distinct role types</span>
                    <strong style="color: #0D9488;">15% (7 candidates)</strong>
                  </div>
                  <div style="width: 100%; height: 14px; background: #E2E8F0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 15%; height: 100%; background: linear-gradient(90deg, #0D9488, #14B8A6); border-radius: 4px;"></div>
                  </div>
                </div>

                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 600; color: var(--slate-700); margin-bottom: 3px;">
                    <span>1 role type only</span>
                    <strong style="color: var(--slate-600);">5% (2 candidates)</strong>
                  </div>
                  <div style="width: 100%; height: 14px; background: #E2E8F0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 5%; height: 100%; background: #94A3B8; border-radius: 4px;"></div>
                  </div>
                </div>
              </div>

              <div style="font-size: 11px; color: var(--slate-500); margin-top: 6px; padding-top: 6px; border-top: 1px solid var(--slate-100);">
                Key Insight: Only 5% of early-career applicants rely on a single narrow role profile.
              </div>
            </div>

            <!-- Right: Motivations & Workarounds Panels -->
            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div class="card card-teal" style="padding: 10px 14px; flex: 1;">
                <div style="font-size: 11.5px; font-weight: 700; color: #115E59; margin-bottom: 4px;">
                  💡 Reported Candidate Motivations
                </div>
                <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  Candidates tailor distinct CVs to align projects and skills with specific job descriptions, preventing mismatched keyword rejections.
                </div>
              </div>

              <div class="card card-amber" style="padding: 10px 14px; flex: 1;">
                <div style="font-size: 11.5px; font-weight: 700; color: #92400E; margin-bottom: 4px;">
                  📁 Current Workarounds & Friction
                </div>
                <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  Managing multiple files across Google Drive or desktop folders, manually verifying filenames before each apply, and dreading overwriting existing profile resumes.
                </div>
              </div>
            </div>

          </div>

          <!-- Bottom: Methodological Limitation Disclaimer -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 8px 16px; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 11.5px; color: var(--slate-600);">
              <strong style="color: var(--navy-dark);">Research Boundary:</strong> The survey was exploratory, based on personal outreach and predominantly student-focused. It does not establish market-wide demand or prove that the same problem affects all Naukri users.
            </div>
            <span style="font-size: 11px; color: var(--naukri-blue); font-weight: 700; white-space: nowrap; margin-left: 10px;">
              Full Q1–Q13 Data in Appendix A →
            </span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 05 — User Research & Findings (Suggested Duration: ~75 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To investigate the hypothesis, I conducted an exploratory survey with 45 college job seekers. Here are the core empirical findings:</p>
        <ul>
          <li><strong>90%</strong> were actively applying in the last 90 days—80% targeting campus placements and 20% seeking internships.</li>
          <li><strong>80%</strong> applied across three or more distinct role categories. Looking at the distribution chart, an overwhelming 60% applied to four or more roles. Only 5% applied to just one role.</li>
          <li><strong>90%</strong> maintain multiple resume versions, frequently needing an alternate version during active applications.</li>
          <li><strong>90%</strong> rated the proposed Resume Library extremely useful and expressed very high intent to use it.</li>
        </ul>
        <p>Candidates reported managing their CVs through clumsy external workarounds like Google Drive links and desktop folders, and constantly worry about overwriting files or attaching the wrong version.</p>
        <p>We explicitly note the boundary: this exploratory cohort is student-heavy; complete Q1 to Q13 responses are cataloged in Appendix A."</p>
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
                  Flow allows candidate to attach an alternate document directly within the application modal without leaving the page.
                </div>
              </div>
              <div style="background: #ECFDF5; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: #166534; margin-top: 8px;">
                ✓ Low friction; document submitted successfully.
              </div>
            </div>

            <!-- Path B: Profile-Attached Friction Path -->
            <div class="card card-rose" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-red">Path B</span>
                  <span style="font-size: 11px; color: #9F1239; font-weight: 700;">User-Reported Friction</span>
                </div>
                <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                  Profile-Attached Redirect
                </div>
                <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  Candidate encounters a workflow tied strictly to the profile resume. Must exit application, update profile CV, and search for the job again.
                </div>
              </div>
              <div style="background: #FFF1F2; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: #9F1239; margin-top: 8px;">
                ⚠️ High context-switching, overwrite risk & drop-off.
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
                  Application redirects out of Naukri to company career site (Workday, Greenhouse). Document handling is governed by external ATS.
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
              <strong style="color: var(--navy-dark);">Reported Friction Manifestation:</strong>
              Candidates report abandoning applications when switching documents requires profile navigation, or accidentally overwriting an executive CV with an analyst CV.
            </div>
            <div style="font-size: 11px; color: var(--slate-500); border-left: 2px solid var(--amber-accent); padding-left: 10px;">
              *Labelled as user-reported behavior. Platform-wide drop-off proportions require Naukri telemetry validation.
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 06 — Current Candidate Journey & Friction (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "When we map the candidate journey, friction surfaces right at step 4: deciding which resume to submit.</p>
        <p>Depending on the specific posting, candidates encounter three distinct paths:</p>
        <ul>
          <li><strong>Path A:</strong> In-flow upload allows attaching an alternate document. This works smoothly.</li>
          <li><strong>Path B (Friction Path):</strong> The candidate encounters a flow tied strictly to the profile resume. To submit a tailored version, they must navigate back to their profile, upload a new CV, return to the job search, and re-apply. This context-switching risks application drop-off and overwrites their master CV.</li>
          <li><strong>Path C:</strong> External ATS redirects to third-party portals, where document handling is outside Naukri's direct control.</li>
        </ul>
        <p>We specifically label Path B as user-reported friction that warrants telemetry validation inside Naukri."</p>
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
                    <span>✓ SUPPORTED BY CURRENT EVIDENCE (N=45)</span>
                  </div>
                  <ul style="font-size: 11.5px; color: #14532D; padding-left: 16px; line-height: 1.45; margin: 0;">
                    <li>Multi-role applications are standard practice (80% across 3+ roles).</li>
                    <li>Maintaining multiple resume versions is normal candidate behavior (90%).</li>
                    <li>Strong candidate intent and appetite for a dedicated library (90%).</li>
                    <li>Competitors have deployed multi-resume handling (LinkedIn, Indeed).</li>
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
                    <li>Database schema storage constraints for multiple resume files per candidate.</li>
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
                    <strong style="color: #4C1D95; font-size: 11.5px;">H1. Decoupled Selection Architecture:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Resume storage and application selection may be decoupled in certain legacy workflows.
                    </div>
                  </div>

                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H2. Lack of In-Flow Reusability:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Alternate uploads in Path A may not persist to the candidate's account for future re-use.
                    </div>
                  </div>

                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H3. Single-Slot Profile Data Model:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Profile schema historically accommodates a single primary resume file per user record.
                    </div>
                  </div>

                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H4. Absence of Transparent Traceability:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Candidates lack clear visibility into exactly which resume version was sent to past employers.
                    </div>
                  </div>

                  <div style="background: #FFFFFF; border: 1px solid #DDD6FE; border-radius: 5px; padding: 7px 10px;">
                    <strong style="color: #4C1D95; font-size: 11.5px;">H5. Recruiter Search Synchronization:</strong>
                    <div style="font-size: 11px; color: var(--slate-700); margin-top: 1px;">
                      Uncertainty regarding which resume should be indexed for recruiter queries (e.g. Resdex).
                    </div>
                  </div>
                </div>
              </div>

              <div style="font-size: 10.5px; color: #7C3AED; margin-top: 6px;">
                Diagnosing structural causes rather than just treating surface symptoms.
              </div>
            </div>

          </div>

          <!-- Bottom: Transition Banner -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 8px 16px; font-size: 11.5px; color: var(--slate-700);">
            <strong style="color: var(--navy-dark);">PM Assessment:</strong> Instead of assuming engineering defects, we treat these as structural design trade-offs that can be validated through internal telemetry and addressed via a non-destructive library architecture.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 07 — Problem Validation & Root Causes (Suggested Duration: ~75 seconds)</h4>
        <p><strong>Speaker Script:</strong> "A disciplined PM distinguishes firmly between verified sample data and unverified hypotheses.</p>
        <p>In <strong>Section A</strong>, our evidence confirms that multi-role applications are widespread (80%), multiple resumes are common (90%), and candidates express strong desire for a library. However, what <em>requires Naukri validation</em> is the internal telemetry: how many candidates abandon applications during resume edits, and what percentage of applications flow through Path A vs Path B vs Path C?</p>
        <p>In <strong>Section B</strong>, we examine five structural root causes behind the friction: decoupled selection in certain flows, lack of reusability, single-slot legacy profile schema, lack of version traceability in past applications, and recruiter indexing questions."</p>
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
                <div style="font-size: 16px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
                  1 Master Profile Resume
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  <div>
                    <strong>• Profile Attachment:</strong> Candidates attach a primary resume file to their main profile.
                  </div>
                  <div>
                    <strong>• FastForward Nuance:</strong> FastForward FAQ notes up to 5 profiles per username, with 1 resume per profile (specific to text/visual CV context).
                  </div>
                  <div>
                    <strong>• Builder Tools:</strong> Separate standalone resume builders exist with distinct capabilities.
                  </div>
                </div>
              </div>
              <div style="background: #EFF6FF; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: var(--naukri-blue); margin-top: 8px; font-weight: 600;">
                Opportunity: Add persistent in-profile resume library.
              </div>
            </div>

            <!-- LinkedIn Platform -->
            <div class="card card-indigo" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <span class="badge" style="background:#EDE9FE; color:#4F46E5;">LinkedIn</span>
                  <span style="font-size: 10.5px; color: var(--slate-500);">Documented</span>
                </div>
                <div style="font-size: 16px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
                  Up to 4 Reusable Resumes
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  <div>
                    <strong>• Reusable Storage:</strong> Stores up to 4 recently uploaded resumes in candidate settings.
                  </div>
                  <div>
                    <strong>• In-Flow Selection:</strong> Allows candidate to select from stored resumes during Easy Apply flows.
                  </div>
                  <div>
                    <strong>• Document History:</strong> Logs which specific resume was submitted to each job application.
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
                <div style="font-size: 16px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
                  1 Profile CV + In-Flow Upload
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                  <div>
                    <strong>• Single Stored File:</strong> 1 stored resume file on profile; uploading a new stored CV replaces previous.
                  </div>
                  <div>
                    <strong>• Apply-Time Upload:</strong> Candidates can upload a different document during specific application flows.
                  </div>
                  <div>
                    <strong>• Separation of State:</strong> Apply-time upload does not necessarily overwrite the master profile file.
                  </div>
                </div>
              </div>
              <div style="background: #F0FDFA; border-radius: 6px; padding: 6px 10px; font-size: 11px; color: var(--teal-accent); margin-top: 8px; font-weight: 600;">
                Validated model: Separation of apply file vs profile file.
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
            <span>*Sources: Public Help Centers & FAQs (Naukri FastForward, LinkedIn Help, Indeed India Support). Verified Nov 2026.</span>
            <span style="color: var(--naukri-blue); font-weight: 600;">Detailed documentation links in Appendix B →</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 08 — Competitor Benchmarking (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To understand market norms, we benchmarked official documentation across Naukri, LinkedIn, and Indeed India:</p>
        <ul>
          <li><strong>Naukri.com:</strong> Currently anchors the candidate to a single primary profile resume. While FastForward allows up to 5 profiles per username for specific paid/visual CV services, standard candidate job applications lack a persistent multi-document selector within one profile.</li>
          <li><strong>LinkedIn:</strong> Offers up to 4 reusable uploaded resumes directly accessible in Easy Apply, and logs submitted versions in application history.</li>
          <li><strong>Indeed India:</strong> Maintains 1 stored profile CV, but allows uploading alternate resumes during application without overwriting the master profile.</li>
        </ul>
        <p>The strategic takeaway: the opportunity is not just raw file uploading. It's giving candidates a <strong>persistent, candidate-controlled Resume Library inside their single profile</strong>, with application-time selection and non-destructive saving."</p>
        <div class='cue-box'><strong>Transition:</strong> Which product approach best solves this challenge? Let's evaluate five strategic alternatives.</div>
        """
    }
]
