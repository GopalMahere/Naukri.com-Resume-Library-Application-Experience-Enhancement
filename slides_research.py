# slides_research.py - Slides 07 to 12 (Research Methodology, Findings, Journey Map, Evidence Validation, Root Cause, Competitor Benchmarking)

SLIDES_RESEARCH = [
    # SLIDE 07: RESEARCH DESIGN AND METHODOLOGY
    {
        "id": "slide-7",
        "number": "07",
        "stage": "Research",
        "tag": "Research Methodology",
        "evidenceType": "Survey Finding",
        "title": "What We Wanted to Understand",
        "subtitle": "Research questions, exploratory survey design, and candidate sample profile",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 16px; flex: 1;">
            <!-- Left: 7 Key Research Questions -->
            <div class="card card-tinted" style="padding: 14px 18px; display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Core Inquiry Framework</span>
                <span class="badge badge-gray">7 Research Questions</span>
              </div>
              <div style="font-weight: 700; font-size: 13px; color: var(--navy-dark); margin-bottom: 6px;">
                Investigating Candidate Resume Management Practices
              </div>
              <div style="display: flex; flex-direction: column; gap: 5px; font-size: 11px; color: var(--slate-700); flex: 1;">
                <div><strong>Q1. Multiple Resumes:</strong> Do candidates maintain different resume versions?</div>
                <div><strong>Q2. Motivations:</strong> Why do they maintain tailored documents?</div>
                <div><strong>Q3. Category Breadth:</strong> How many role categories do they apply for?</div>
                <div><strong>Q4. Friction Frequency:</strong> How often is an alternate resume needed during apply?</div>
                <div><strong>Q5. Current Methods:</strong> How do they currently organize and store different versions?</div>
                <div><strong>Q6. Workarounds:</strong> What workarounds do they employ when friction occurs?</div>
                <div><strong>Q7. Perceived Value:</strong> Would a persistent in-portal Resume Library be useful?</div>
              </div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 4px; padding: 6px 10px; font-size: 10.5px; color: var(--slate-600); margin-top: 6px;">
                Designed to establish exploratory behavioural signals regarding multi-track job applications.
              </div>
            </div>
            
            <!-- Right: Methodology & Explicit Sample Profile -->
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div class="card" style="border-left: 4px solid var(--amber-accent); padding: 12px 16px;">
                <div class="card-header-sm">
                  <span>Methodology & Sample Profile</span>
                  <span class="evidence-tag evidence-tag-survey">N=45 Survey</span>
                </div>
                <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.45;">
                  <div>• <strong>Method:</strong> Structured survey via direct outreach.</div>
                  <div>• <strong>Sample Size:</strong> 45 respondents (student-focused cohort).</div>
                  <div>• <strong>Cohort Breakdown:</strong></div>
                  <div style="padding-left: 10px; font-size: 11px; color: var(--navy-dark); margin-top: 2px;">
                    - <strong>80%</strong> looking for placements or full-time roles.<br>
                    - <strong>20%</strong> looking for internships.
                  </div>
                  <div style="margin-top: 4px;">• <strong>Activity:</strong> 90% applied for jobs in the last 90 days.</div>
                </div>
              </div>
              
              <!-- Limitations Box -->
              <div class="card card-tinted" style="border-left: 4px solid var(--rose-accent); padding: 10px 14px; flex: 1;">
                <div class="card-header-sm">
                  <span>Methodological Limitations</span>
                  <span class="badge badge-red">Honest Disclosures</span>
                </div>
                <ul style="font-size: 10.5px; color: #4C0519; padding-left: 14px; line-height: 1.35;">
                  <li>Student-focused sample; does not represent all Naukri candidates or mid-career professionals.</li>
                  <li>Did not measure platform-specific market share or isolate portal-specific friction rates.</li>
                  <li>Exploratory sample (N=45) provides qualitative directional signal, not statistical proof of company-wide demand.</li>
                </ul>
              </div>
            </div>
          </div>
          
          <div style="background: var(--slate-100); padding: 7px 12px; border-radius: 4px; font-size: 11px; color: var(--slate-600); text-align: center;">
            <strong>Research Stance:</strong> These findings provide a directional foundation to explore candidate needs. We treat stated user interest as an exploratory indicator rather than guaranteed adoption.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 7 — Research Methodology & Transparency</h4>
        <p>A rigorous PM presentation must be completely candid about how research was conducted:</p>
        <ul>
          <li>We formulated seven specific questions to explore candidate behaviour: prevalence of multiple resumes, motivations, category breadth, friction frequency, current storage methods, workarounds, and stated usefulness.</li>
          <li>Our sample consisted of 45 college students contacted via personal outreach: 80% preparing for placements or full-time jobs, and 20% for internships. 90% had applied within the preceding 90 days.</li>
          <li>We clearly disclose our limitations: this is an exploratory student sample, not a representative demographic of all Naukri users or experienced professionals.</li>
          <li>Furthermore, the survey did not establish how many respondents experienced this specifically on Naukri.com, so we do not make that claim.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's review the exact reported findings from the survey.</div>
        """
    },

    # SLIDE 08: RESEARCH FINDINGS
    {
        "id": "slide-8",
        "number": "08",
        "stage": "Research",
        "tag": "Survey Evidence",
        "evidenceType": "Survey Finding",
        "title": "What We Learned from the Respondents",
        "subtitle": "Reported behaviours, role distribution, and stated candidate preferences (N=45)",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Top Row: Role Distribution Chart & Core KPIs -->
          <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 14px;">
            <!-- Role Distribution Breakdown -->
            <div class="card card-tinted" style="padding: 12px 16px;">
              <div class="card-header-sm">
                <span>Q3: Role Categories Applied For Concurrently</span>
                <span class="evidence-tag evidence-tag-survey">N=45 Cohort</span>
              </div>
              <div style="font-weight: 700; font-size: 12.5px; color: var(--navy-dark); margin-bottom: 6px;">
                80% Apply Across Three or More Role Categories
              </div>
              
              <!-- Visual Bar Breakdown -->
              <div style="display: flex; flex-direction: column; gap: 5px; margin-top: 4px;">
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 10.5px; margin-bottom: 1px;">
                    <span>4 or more role types</span>
                    <strong>60%</strong>
                  </div>
                  <div style="background: #E2E8F0; border-radius: 4px; height: 8px; overflow: hidden;">
                    <div style="width: 60%; background: var(--navy-dark); height: 100%;"></div>
                  </div>
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 10.5px; margin-bottom: 1px;">
                    <span>3 role types</span>
                    <strong>20%</strong>
                  </div>
                  <div style="background: #E2E8F0; border-radius: 4px; height: 8px; overflow: hidden;">
                    <div style="width: 20%; background: var(--naukri-blue); height: 100%;"></div>
                  </div>
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 10.5px; margin-bottom: 1px;">
                    <span>2 role types</span>
                    <strong>15%</strong>
                  </div>
                  <div style="background: #E2E8F0; border-radius: 4px; height: 8px; overflow: hidden;">
                    <div style="width: 15%; background: var(--slate-400); height: 100%;"></div>
                  </div>
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 10.5px; margin-bottom: 1px;">
                    <span>1 role type only</span>
                    <strong>5%</strong>
                  </div>
                  <div style="background: #E2E8F0; border-radius: 4px; height: 8px; overflow: hidden;">
                    <div style="width: 5%; background: var(--slate-300); height: 100%;"></div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- 4 Stat Callout Cards -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <div class="stat-box" style="padding: 10px;">
                <div class="stat-value" style="font-size: 26px;">90%</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark);">Maintain Multiple CVs</div>
                <div style="font-size: 9.5px; color: var(--slate-500); margin-top: 1px;">Keep tailored versions</div>
              </div>
              <div class="stat-box" style="padding: 10px;">
                <div class="stat-value" style="font-size: 26px; color: var(--amber-accent);">90%</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark);">Need Alternate CV</div>
                <div style="font-size: 9.5px; color: var(--slate-500); margin-top: 1px;">Frequently while applying</div>
              </div>
              <div class="stat-box" style="padding: 10px;">
                <div class="stat-value" style="font-size: 26px; color: var(--teal-accent);">90%</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark);">Extremely Useful</div>
                <div style="font-size: 9.5px; color: var(--slate-500); margin-top: 1px;">Feature valuation</div>
              </div>
              <div class="stat-box" style="padding: 10px;">
                <div class="stat-value" style="font-size: 26px; color: var(--emerald-accent);">90%</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark);">Very Likely to Use</div>
                <div style="font-size: 9.5px; color: var(--slate-500); margin-top: 1px;">Stated adoption intent</div>
              </div>
            </div>
          </div>
          
          <!-- Bottom: Qualitative Insights (Motivations & Workarounds) -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; flex: 1;">
            <div class="card" style="padding: 10px 14px;">
              <div class="card-header-sm">
                <span>Reported Motivations (Q5)</span>
                <span class="badge badge-gray">Qualitative</span>
              </div>
              <ul style="font-size: 10.5px; color: var(--slate-700); padding-left: 14px; line-height: 1.35;">
                <li>Highlighting distinct skill sets for different job functions.</li>
                <li>Applying to different industries (e.g. tech product vs. management consulting).</li>
                <li>Pursuing distinct career pathways simultaneously.</li>
                <li>Tailoring resume content to specific job descriptions.</li>
              </ul>
            </div>
            
            <div class="card" style="padding: 10px 14px;">
              <div class="card-header-sm">
                <span>Reported Workarounds (Q8)</span>
                <span class="badge badge-gray">Qualitative</span>
              </div>
              <ul style="font-size: 10.5px; color: var(--slate-700); padding-left: 14px; line-height: 1.35;">
                <li>Replacing the uploaded file on profile settings before applying.</li>
                <li>Uploading a different file directly during application when supported.</li>
                <li>Leaving the application flow and returning later.</li>
                <li>Sometimes postponing or skipping an application altogether.</li>
              </ul>
            </div>
          </div>
          
          <div style="background: var(--amber-light); border: 1px solid var(--amber-border); padding: 6px 12px; border-radius: 4px; font-size: 10.5px; color: #92400E; text-align: center;">
            <em>Honest Research Conclusion: Our exploratory survey suggests maintaining multiple role-specific resumes and needing alternate versions during applications are common behaviours within this student sample. These findings support further investigation of a more convenient resume-management and selection experience. Stated usefulness does not equal observed production adoption.</em>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 8 — Research Findings & Discipline</h4>
        <p>Let's review the survey data with exact mathematical fidelity:</p>
        <ul>
          <li><strong>Role Distribution:</strong> 60% applied to 4+ roles, 20% to 3 roles, 15% to 2 roles, and only 5% to 1 role. In total, 80% applied across three or more categories.</li>
          <li><strong>Multiple Resumes:</strong> 90% maintain different resume versions.</li>
          <li><strong>Friction Frequency:</strong> 90% report frequently needing an alternate resume while applying.</li>
          <li><strong>Stated Preference:</strong> 90% rated the proposed concept 'Extremely useful' and 90% said they were 'Very likely' to use it.</li>
          <li><strong>Critical PM Caveat:</strong> Stated preference in a survey is an exploratory signal, not observed behavioral adoption. We never claim that 90% of all Naukri users have this problem.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's map the current-state candidate journey and examine where friction occurs.</div>
        """
    },

    # SLIDE 09: CURRENT-STATE CANDIDATE JOURNEY
    {
        "id": "slide-9",
        "number": "09",
        "stage": "Validate",
        "tag": "Candidate Journey",
        "evidenceType": "Personal Observation",
        "title": "Where Resume Management Can Interrupt the Journey",
        "subtitle": "Mapping common application steps and branching paths across portal flows",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Top: Common Application Sequence -->
          <div class="card" style="padding: 10px 14px;">
            <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 6px;">Common Application Steps</div>
            <div style="display: flex; align-items: center; justify-content: space-between; text-align: center;">
              <div style="width: 22%;">
                <div style="background: var(--navy-dark); color: white; border-radius: 4px; padding: 4px; font-size: 11px; font-weight: 700;">1. Maintain Profile</div>
                <div style="font-size: 10px; color: var(--slate-500); margin-top: 2px;">Profile with 1 active CV</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              <div style="width: 22%;">
                <div style="background: var(--navy-dark); color: white; border-radius: 4px; padding: 4px; font-size: 11px; font-weight: 700;">2. Find Job</div>
                <div style="font-size: 10px; color: var(--slate-500); margin-top: 2px;">Target opening found</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              <div style="width: 22%;">
                <div style="background: var(--navy-dark); color: white; border-radius: 4px; padding: 4px; font-size: 11px; font-weight: 700;">3. Click Apply</div>
                <div style="font-size: 10px; color: var(--slate-500); margin-top: 2px;">Application begins</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              <div style="width: 26%;">
                <div style="background: var(--amber-accent); color: white; border-radius: 4px; padding: 4px; font-size: 11px; font-weight: 700;">4. Review Resume</div>
                <div style="font-size: 10px; color: var(--slate-500); margin-top: 2px;">Needs alternate CV version</div>
              </div>
            </div>
          </div>
          
          <!-- Middle: 3 Branching Flow Paths -->
          <div class="grid-3" style="flex: 1; gap: 12px;">
            <!-- Path A -->
            <div class="card card-tinted" style="border-top: 3px solid var(--emerald-accent);">
              <div class="card-header-sm">
                <span>Path A: In-Flow Upload</span>
                <span class="badge badge-teal">Supported Flow</span>
              </div>
              <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-bottom: 3px;">
                Direct Upload Option Available
              </div>
              <p style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                The application flow provides an upload button. Candidate chooses a file from local storage and submits directly.
              </p>
              <div style="margin-top: auto; background: white; border: 1px solid var(--slate-200); padding: 6px; border-radius: 4px; font-size: 10px; color: var(--slate-500);">
                <strong>Limitation:</strong> Document may not be saved into a reusable library for future roles.
              </div>
            </div>
            
            <!-- Path B -->
            <div class="card card-tinted" style="border-top: 3px solid var(--rose-accent);">
              <div class="card-header-sm">
                <span>Path B: Profile-Dependent</span>
                <span class="evidence-tag evidence-tag-obs">Reported Path</span>
              </div>
              <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-bottom: 3px;">
                Profile Attachment Required
              </div>
              <p style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                Flow submits the profile resume. To submit a different version, candidate leaves application, navigates to profile, replaces file, and returns.
              </p>
              <div style="margin-top: auto; background: #FFF1F2; border: 1px solid #FECDD3; padding: 6px; border-radius: 4px; font-size: 10px; color: #9F1239;">
                <strong>Risk:</strong> High drop-off friction, lost momentum, and potential overwriting of active profile CV.
              </div>
            </div>
            
            <!-- Path C -->
            <div class="card card-tinted" style="border-top: 3px solid var(--slate-400);">
              <div class="card-header-sm">
                <span>Path C: External Redirect</span>
                <span class="badge badge-gray">Third-Party ATS</span>
              </div>
              <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-bottom: 3px;">
                Company Portal Redirect
              </div>
              <p style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                Candidate is redirected to an external employer career site or ATS (e.g. Workday, Greenhouse).
              </p>
              <div style="margin-top: auto; background: white; border: 1px solid var(--slate-200); padding: 6px; border-radius: 4px; font-size: 10px; color: var(--slate-500);">
                <strong>Boundary:</strong> Resume handling and selection governed entirely by the external employer system.
              </div>
            </div>
          </div>
          
          <!-- Bottom: Reported Workarounds Summary -->
          <div class="card card-blue" style="padding: 8px 14px; font-size: 11px; color: var(--slate-700); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px;">
            <div>
              <strong>Reported Candidate Workarounds:</strong> Replacing uploaded profile CV • Uploading fresh file during apply • Leaving & returning • Postponing or skipping application.
            </div>
            <span class="badge badge-gray" style="font-size: 9.5px;">Pathways vary by job type</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 9 — Current-State Journey & Branching Paths</h4>
        <p>A major flaw in naive case studies is assuming that a platform has only one rigid workflow. In reality, Naukri supports different application types:</p>
        <ul>
          <li><strong>Path A:</strong> In application flows that offer an alternate file upload, the candidate can upload locally. However, this file is not necessarily saved into an organized, reusable library.</li>
          <li><strong>Path B:</strong> In flows that rely on the profile-attached resume, the candidate may feel compelled to leave the application flow, update their profile resume, and re-navigate back. This introduces drop-off friction.</li>
          <li><strong>Path C:</strong> External employer redirects send candidates to third-party ATS platforms where resume handling is outside Naukri's control.</li>
          <li>Recognizing these three paths makes our product proposal realistic and scoped specifically to supported on-platform journeys.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's conduct an honest audit of what our research establishes versus what remains unverified.</div>
        """
    },

    # SLIDE 10: PROBLEM VALIDATION
    {
        "id": "slide-10",
        "number": "10",
        "stage": "Validate",
        "tag": "Evidence Audit",
        "evidenceType": "Requires Naukri Validation",
        "title": "What the Evidence Supports — and What We Still Need to Verify",
        "subtitle": "Distinguishing established candidate signals from unanswered platform-side questions",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Two-Column Evidence Audit Table -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; flex: 1;">
            <!-- Column 1: Supported by Current Evidence -->
            <div class="card" style="border-top: 4px solid var(--emerald-accent); padding: 12px 16px; display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span style="color: #065F46; font-weight: 800;">Supported by Current Evidence</span>
                <span class="evidence-tag evidence-tag-survey">Survey & Public Data</span>
              </div>
              <ul style="font-size: 11px; color: var(--slate-700); padding-left: 16px; line-height: 1.45; display: flex; flex-direction: column; gap: 6px; flex: 1;">
                <li><strong>Multiple CVs are common:</strong> 90% of surveyed students maintain tailored resume versions.</li>
                <li><strong>Need for alternate CVs:</strong> 90% report frequently needing an alternate resume when applying.</li>
                <li><strong>Multi-category search breadth:</strong> 80% apply across 3 or more distinct role categories concurrently.</li>
                <li><strong>Competitor patterns exist:</strong> LinkedIn documents 4 reusable resumes; Indeed supports apply-time file uploads.</li>
                <li><strong>Firsthand user experience:</strong> Firsthand observation confirms that switching resumes in certain flows introduces extra steps.</li>
              </ul>
              <div style="background: #F0FDF4; border: 1px solid #A7F3D0; padding: 6px 10px; border-radius: 4px; font-size: 10.5px; color: #166534; margin-top: 6px;">
                ✓ Establishes a credible candidate-side need for better resume organization.
              </div>
            </div>
            
            <!-- Column 2: Not Yet Established / Requires Naukri Validation -->
            <div class="card" style="border-top: 4px solid var(--rose-accent); padding: 12px 16px; display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span style="color: #9F1239; font-weight: 800;">Requires Naukri Validation</span>
                <span class="evidence-tag evidence-tag-val">Requires Internal Data</span>
              </div>
              <ul style="font-size: 11px; color: var(--slate-700); padding-left: 16px; line-height: 1.45; display: flex; flex-direction: column; gap: 6px; flex: 1;">
                <li><strong>Platform-wide prevalence:</strong> Exactly what percentage of all Naukri job seekers experience this friction.</li>
                <li><strong>Flow breakdown:</strong> What proportion of applications on Naukri follow Path A vs. Path B vs. Path C.</li>
                <li><strong>Current flow capabilities:</strong> Which specific application types already allow alternate resume uploads.</li>
                <li><strong>True funnel abandonment:</strong> Whether candidates actually abandon applications due to resume switching.</li>
                <li><strong>Conversion lift:</strong> Whether a Resume Library genuinely improves application completion rates.</li>
                <li><strong>Recruiter matching impact:</strong> Whether role-tailored resumes improve recruiter shortlist rates.</li>
                <li><strong>Architecture constraints:</strong> Technical dependencies governing document versioning in Naukri's backend.</li>
              </ul>
              <div style="background: #FFF1F2; border: 1px solid #FECDD3; padding: 6px 10px; border-radius: 4px; font-size: 10.5px; color: #9F1239; margin-top: 6px;">
                ⚠️ Questions that only Naukri's internal product and analytics teams can definitively resolve.
              </div>
            </div>
          </div>
          
          <!-- Bottom Summary Anchor -->
          <div class="card card-blue" style="padding: 10px 14px; text-align: center;">
            <div style="font-weight: 700; font-size: 11.5px; color: var(--navy-dark);">
              "The current evidence establishes a credible candidate-side opportunity for further investigation, not proof of a platform-wide Naukri problem."
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 10 — Problem Validation: What We Know vs. What Requires Naukri</h4>
        <p>This is arguably the most important slide for demonstrating mature Product Management thinking:</p>
        <ul>
          <li>On the left, we summarize what our evidence actually supports: college candidates maintain multiple resumes, they apply across multiple roles, competitor platforms offer forms of reuse, and firsthand observation identified friction.</li>
          <li>On the right, we explicitly acknowledge what we CANNOT know from the outside: how many total Naukri candidates face this, which specific job postings follow Path A vs. Path B, what the actual abandonment rate is, and what backend constraints exist.</li>
          <li>By ending with the statement that this is a credible candidate-side opportunity for investigation rather than proof of a universal defect, we demonstrate professional humility and invite collaborative validation.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's conduct a root-cause diagnosis to explore why this friction may occur.</div>
        """
    },

    # SLIDE 11: ROOT-CAUSE ANALYSIS
    {
        "id": "slide-11",
        "number": "11",
        "stage": "Diagnose",
        "tag": "Diagnostic Analysis",
        "evidenceType": "Product Hypothesis",
        "title": "What May Be Causing the Friction?",
        "subtitle": "Diagnostic problem tree separating observed symptoms from root-cause hypotheses",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <div style="display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 16px; flex: 1;">
            <!-- Left: Observed Symptoms -->
            <div class="card card-tinted" style="padding: 14px 16px; display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Observed & Reported Symptoms</span>
                <span class="evidence-tag evidence-tag-obs">Symptoms</span>
              </div>
              <div style="font-weight: 700; font-size: 12.5px; color: var(--navy-dark); margin-bottom: 8px;">
                Surface Friction Experienced by Candidates
              </div>
              <div style="display: flex; flex-direction: column; gap: 6px; font-size: 11px; color: var(--slate-700); flex: 1;">
                <div style="background: white; border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  📁 <strong>Fragmented Storage:</strong> Candidates store files across laptops, Google Drive, and phones.
                </div>
                <div style="background: white; border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  🔄 <strong>Repeated Overwrites:</strong> Updating profile resume replaces the previous file.
                </div>
                <div style="background: white; border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  🚪 <strong>Flow Disruption:</strong> Navigating away from application to update profile file.
                </div>
                <div style="background: white; border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  ❓ <strong>Active CV Ambiguity:</strong> Uncertainty over which document recruiters currently see.
                </div>
                <div style="background: white; border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  ⏳ <strong>Postponed Applications:</strong> Candidates deferring applying when resume isn't ready.
                </div>
              </div>
            </div>
            
            <!-- Right: 5 Root-Cause Hypotheses -->
            <div class="card" style="border-left: 4px solid var(--naukri-blue); padding: 14px 16px; display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Diagnostic Hypotheses to Investigate</span>
                <span class="evidence-tag evidence-tag-hypo">5 Hypotheses</span>
              </div>
              <div style="font-weight: 700; font-size: 12.5px; color: var(--navy-dark); margin-bottom: 6px;">
                Underlying Structural Hypotheses
              </div>
              <div style="display: flex; flex-direction: column; gap: 6px; font-size: 10.5px; color: var(--slate-700); flex: 1;">
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  <strong>H1. Separation of Document vs. Application:</strong> Resume management is architecturally decoupled from the moment-of-apply decision point.
                </div>
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  <strong>H2. Absence of Persistent Role Library:</strong> In the flow studied, candidates lack a single home for named, reusable role-specific documents.
                </div>
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  <strong>H3. Journey Option Variance:</strong> Different application types expose varied upload capabilities, leading to inconsistent mental models.
                </div>
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  <strong>H4. Destructive Overwriting:</strong> Profile settings treat resume upload as file replacement rather than version addition.
                </div>
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px;">
                  <strong>H5. Traceability Gap:</strong> Application history may not visibly reflect which exact resume version was attached for past submissions.
                </div>
              </div>
            </div>
          </div>
          
          <div style="background: var(--slate-100); padding: 6px 12px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600); text-align: center;">
            <em>Rigor Note: These are hypotheses formulated to guide investigation. We do not claim insight into Naukri's proprietary internal codebase or service architecture.</em>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 11 — Root-Cause Analysis</h4>
        <p>In product design, treating surface symptoms without understanding root causes leads to ineffective features:</p>
        <ul>
          <li><strong>Symptoms:</strong> Candidates juggle files across devices, overwrite previously uploaded resumes, or navigate away during active applications.</li>
          <li><strong>Underlying Hypotheses:</strong>
            <ol>
              <li>Resume storage is decoupled from the application decision.</li>
              <li>There is no dedicated, persistent library of role-specific documents within the candidate profile.</li>
              <li>Different job types have different application flows, causing candidate confusion.</li>
              <li>Uploading a new document in profile settings often replaces the existing file destructively.</li>
              <li>Application history may not preserve an immutable reference to the submitted document.</li>
            </ol>
          </li>
          <li>By addressing these root causes, our proposal aims to resolve the underlying friction.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's see how competing platforms handle resume reuse and application-time uploading.</div>
        """
    },

    # SLIDE 12: COMPETITOR AND MARKET BENCHMARKING
    {
        "id": "slide-12",
        "number": "12",
        "stage": "Assess",
        "tag": "Market Benchmarking",
        "evidenceType": "Official Public Documentation",
        "title": "How Existing Platforms Handle Resume Selection",
        "subtitle": "Factual analysis of Naukri, LinkedIn, and Indeed India based on official help documentation",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Benchmark Comparison Table -->
          <div class="card" style="padding: 0; overflow: hidden; flex: 1;">
            <div class="table-scroll-wrap">
              <table class="deck-table" style="font-size: 11px;">
                <thead>
                  <tr>
                    <th style="width: 24%;">Capability</th>
                    <th style="width: 28%; background: #EFF6FF; color: var(--navy-dark);">Naukri.com (Official Documented Info)</th>
                    <th style="width: 24%;">LinkedIn</th>
                    <th style="width: 24%;">Indeed India</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Multiple Resumes on Account</strong></td>
                    <td style="background: #F8FAFC;">
                      Up to <strong>5 profiles per username</strong> (1 resume per profile) in FastForward FAQ<a href="#ref-1" class="citation-mark">[1]</a>.<br>
                      <span style="font-size:10px; color:var(--slate-500);"><em>FAQ relates specifically to text/visual CV packages. Separate builder tools have distinct limits (AI maker: 1 CV; online builder FAQ: up to 50)<a href="#ref-2" class="citation-mark">[2]</a>.</em></span>
                    </td>
                    <td>
                      Stores up to <strong>4 recently uploaded</strong> reusable resumes on account<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      Only <strong>1 resume file</strong> stored on account at a time; uploading a new file replaces existing<a href="#ref-5" class="citation-mark">[5]</a>.
                    </td>
                  </tr>
                  <tr>
                    <td><strong>Apply-Time Resume Selection</strong></td>
                    <td style="background: #F8FAFC;">
                      Requires hands-on validation across direct and third-party job flows.
                    </td>
                    <td>
                      Supported natively in eligible <em>Easy Apply</em> flows; not on external redirects<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      Candidate can select their uploaded resume during application<a href="#ref-4" class="citation-mark">[4]</a>.
                    </td>
                  </tr>
                  <tr>
                    <td><strong>Upload Another CV During Apply</strong></td>
                    <td style="background: #F8FAFC;">
                      Supported in certain direct flows; requires validation across all types.
                    </td>
                    <td>
                      Supported within <em>Easy Apply</em>; not on external employer redirects<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      Supported: candidate can upload a different resume file during application<a href="#ref-4" class="citation-mark">[4]</a>.
                    </td>
                  </tr>
                  <tr>
                    <td><strong>Persistent Reusable Named Library</strong></td>
                    <td style="background: #F8FAFC;">
                      Multiple profiles exist in specific services; a unified named library within 1 profile needs validation.
                    </td>
                    <td>
                      Recent resume reuse is documented; custom naming capability not confirmed in referenced docs<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      1 stored profile file at a time; new uploads replace previous file<a href="#ref-5" class="citation-mark">[5]</a>.
                    </td>
                  </tr>
                  <tr>
                    <td><strong>Submitted-Document Traceability</strong></td>
                    <td style="background: #F8FAFC;">
                      Requires verification of historical document reference behaviour.
                    </td>
                    <td>
                      LinkedIn documents viewing the resume submitted for Easy Apply jobs<a href="#ref-3b" class="citation-mark">[3b]</a>.
                    </td>
                    <td>
                      Requires verification of historical document reference tracking<a href="#ref-4" class="citation-mark">[4]</a>.
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          
          <!-- Defensible Competitor Takeaway -->
          <div class="card card-blue" style="padding: 10px 14px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
            <div style="font-size: 11px; color: var(--navy-dark); line-height: 1.45;">
              <strong>Competitive Insight:</strong> Competing platforms validate candidate demand for resume reuse and in-flow uploading. The opportunity for Naukri is to explore a unified, independently managed Resume Library within one candidate profile, with explicit application-time selection and non-destructive saving.
            </div>
            <span class="badge badge-gray" style="font-size: 9.5px;">Sources: Official Help Centers</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 12 — Competitor & Market Benchmarking</h4>
        <p>A rigorous PM benchmark must be factually precise and avoid overgeneralizing:</p>
        <ul>
          <li><strong>Naukri.com:</strong> Official FastForward FAQ documents up to 5 profiles per username with 1 resume each, but this specifically pertains to text and visual CV packages. Separate tools have specific limits (AI maker creates 1 CV; Online Builder FAQ notes up to 50). We do NOT generalize these as universal application profile rules.</li>
          <li><strong>LinkedIn:</strong> LinkedIn stores up to 4 recently uploaded reusable resumes for Easy Apply flows, and lets candidates view submitted resumes. However, custom naming is not confirmed in cited docs, and reuse does not apply to external employer redirects.</li>
          <li><strong>Indeed India:</strong> Indeed stores only 1 resume file on an account (replacing previous uploads), but allows uploading an alternate resume during an application.</li>
          <li><strong>Takeaway:</strong> These patterns demonstrate that candidate resume reuse and in-flow uploading are industry-tested concepts. The opportunity for Naukri is a persistent, candidate-controlled library within one master profile.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's compare five strategic product approaches to solve this problem.</div>
        """
    }
]
