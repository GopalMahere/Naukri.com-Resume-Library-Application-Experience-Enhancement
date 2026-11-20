# slides_discovery.py - Slides 01 to 04 (Cover, Executive Summary, Origin & Target Users, Problem Definition & JTBD)

SLIDES_DISCOVERY = [
    # SLIDE 01: INTRODUCTORY COVER
    {
        "id": "slide-1",
        "number": "01",
        "stage": "Discover",
        "tag": "Product Investigation",
        "evidenceType": "Project Introduction",
        "title": "Naukri.com – Apply with the Right Resume",
        "subtitle": "A candidate-controlled Resume Library for a simpler job application experience.",
        "content": """
        <div class="cover-layout">
          <!-- Left: Hero Header & Project Metadata -->
          <div class="cover-hero-box">
            <div>
              <span class="evidence-tag evidence-tag-intro" style="margin-bottom: 8px;">[PROJECT INTRODUCTION]</span>
              <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: var(--naukri-blue); margin-top: 4px;">
                NAUKRI.COM • CANDIDATE EXPERIENCE INVESTIGATION
              </div>
            </div>
            
            <h1 style="font-size: 34px; font-weight: 800; color: var(--navy-dark); line-height: 1.15; letter-spacing: -1px;">
              Apply with the<br><span style="color: var(--naukri-blue);">Right Resume</span>
            </h1>
            
            <p style="font-size: 15px; color: var(--slate-700); line-height: 1.5; font-weight: 500;">
              A candidate-controlled <strong>Resume Library</strong> that makes it easier to manage role-specific resumes and choose the appropriate document while applying for jobs on Naukri.com.
            </p>
            
            <div style="background: #EFF6FF; border-left: 4px solid var(--naukri-blue); padding: 12px 16px; border-radius: 0 8px 8px 0; font-size: 13px; color: #1E3A8A; line-height: 1.5;">
              <em>"Candidates frequently maintain different resumes for different opportunities. The challenge is having the right version ready when it is time to apply, without silently overwriting saved files."</em>
            </div>
            
            <!-- Metadata Grid -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 8px; padding-top: 14px; border-top: 1.5px solid var(--slate-200); font-size: 12px; color: var(--slate-600);">
              <div>
                <span style="color: var(--slate-400); display: block; font-size: 10.5px; text-transform: uppercase; font-weight: 700;">Prepared by</span>
                <strong style="color: var(--navy-dark); font-size: 13.5px;">Aditya Sharma</strong>
              </div>
              <div>
                <span style="color: var(--slate-400); display: block; font-size: 10.5px; text-transform: uppercase; font-weight: 700;">Project Type</span>
                <strong style="color: var(--navy-dark); font-size: 12.5px;">Independent PM Investigation</strong>
              </div>
              <div>
                <span style="color: var(--slate-400); display: block; font-size: 10.5px; text-transform: uppercase; font-weight: 700;">Platform Scope</span>
                <span style="font-weight: 600; color: var(--slate-700);">Naukri.com (Candidate Experience)</span>
              </div>
              <div>
                <span style="color: var(--slate-400); display: block; font-size: 10.5px; text-transform: uppercase; font-weight: 700;">Date & Status</span>
                <span style="font-weight: 600; color: var(--slate-700);">November 2026 • Proposal</span>
              </div>
            </div>
            
            <div style="font-size: 11px; color: var(--slate-500); margin-top: 4px;">
              *Independent proposal. Not affiliated with or endorsed by Info Edge / Naukri.com.
            </div>
          </div>
          
          <!-- Right: Visual Conceptual Product Diagram (Profile -> Resume Library -> Select Resume -> Apply) -->
          <div class="cover-illustration-wrap" style="background: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%); border: 1.5px solid var(--slate-200); border-radius: var(--radius-lg); padding: 20px;">
            <div style="font-size: 11.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; color: var(--naukri-blue); margin-bottom: 12px; text-align: center;">
              Core Product Flow Concept
            </div>
            
            <!-- Step 1: Candidate Profile -->
            <div style="background: var(--navy-dark); color: white; padding: 12px 16px; border-radius: 8px; text-align: center; box-shadow: 0 4px 12px rgba(11,27,61,0.15);">
              <div style="font-size: 10px; text-transform: uppercase; color: #93C5FD; font-weight: 700;">Single Master Record</div>
              <div style="font-size: 14px; font-weight: 800; margin-top: 2px;">Comprehensive Naukri Profile</div>
              <div style="font-size: 11px; color: #CBD5E1;">Master Education • Work Experience • Skills • Personal Details</div>
            </div>
            
            <!-- Connector Arrow -->
            <div style="text-align: center; color: var(--naukri-blue); font-size: 18px; font-weight: 800; margin: 4px 0;">↓</div>
            
            <!-- Step 2: Dedicated Resume Library -->
            <div style="background: white; border: 2px dashed #93C5FD; border-radius: 10px; padding: 12px 14px; box-shadow: 0 4px 14px rgba(24,86,234,0.06);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 12px; font-weight: 800; color: var(--navy-dark); display: flex; align-items: center; gap: 6px;">
                  📁 Dedicated Resume Library
                </span>
                <span class="badge badge-blue" style="font-size: 10px;">Proposed Capacity: Up to 5 Resumes*</span>
              </div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                <div style="background: #EFF6FF; border: 1.5px solid var(--naukri-blue); border-radius: 6px; padding: 8px 10px;">
                  <div style="font-size: 11.5px; font-weight: 700; color: #1E3A8A;">🔘 Product Mgmt CV</div>
                  <div style="font-size: 10px; color: var(--naukri-blue); font-weight: 600;">PM_Resume.pdf [Selected]</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px 10px;">
                  <div style="font-size: 11.5px; font-weight: 600; color: var(--slate-700);">⚪ Consulting CV</div>
                  <div style="font-size: 10px; color: var(--slate-500);">Consulting.pdf</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px 10px;">
                  <div style="font-size: 11.5px; font-weight: 600; color: var(--slate-700);">⚪ Operations CV</div>
                  <div style="font-size: 10px; color: var(--slate-500);">Ops_Resume.pdf</div>
                </div>
                <div style="background: #F8FAFC; border: 1.5px dashed #94A3B8; border-radius: 6px; padding: 8px 10px; text-align: center; display: flex; align-items: center; justify-content: center;">
                  <span style="font-size: 10.5px; color: var(--naukri-blue); font-weight: 700;">+ Upload New Resume</span>
                </div>
              </div>
            </div>
            
            <!-- Connector Arrow -->
            <div style="text-align: center; color: var(--emerald-accent); font-size: 18px; font-weight: 800; margin: 4px 0;">↓</div>
            
            <!-- Step 3: Moment of Apply -->
            <div style="background: #ECFDF5; border: 2px solid var(--emerald-accent); border-radius: 8px; padding: 12px 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                  <div style="font-size: 10.5px; text-transform: uppercase; color: #166534; font-weight: 700;">Job Application Target</div>
                  <div style="font-size: 13.5px; font-weight: 800; color: #14532D; margin-top: 2px;">Product Manager Intern</div>
                </div>
                <span class="badge badge-teal" style="font-size: 11px; padding: 4px 8px;">Attached: PM CV</span>
              </div>
              <div style="font-size: 11px; color: #15803D; margin-top: 6px; font-weight: 500;">
                ✓ Attached cleanly without altering other library resumes or overwriting the master profile
              </div>
            </div>
            
            <div style="text-align: center; font-size: 10.5px; color: var(--slate-500); margin-top: 8px;">
              *Proposed MVP capacity assumption: up to 5 resumes, subject to technical validation.
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 01 — Introductory Cover (Suggested Duration: ~45 seconds)</h4>
        <p><strong>Speaker Script:</strong> "Good morning. Today I'm presenting an independent Product Management case study on Naukri.com's candidate experience, titled: <em>Apply with the Right Resume</em>.</p>
        <p>The core concept is simple and candidate-first: job seekers maintain one comprehensive Naukri profile for their master records, but can upload, manage, and select from a dedicated <strong>Resume Library</strong> when applying for different role categories—such as Product Management, Consulting, Operations, or Engineering.</p>
        <p>Today's presentation takes you through the discovery process: the problem origin, candidate survey research, competitor benchmarks, strategic choices, product requirements, and an interactive prototype."</p>
        <div class='cue-box'><strong>Transition:</strong> Let's start with a high-level executive summary of what this investigation covers.</div>
        """
    },

    # SLIDE 02: EXECUTIVE SUMMARY
    {
        "id": "slide-2",
        "number": "02",
        "stage": "Discover",
        "tag": "Executive Summary",
        "evidenceType": "Proposed Solution",
        "title": "What This Investigation Is About",
        "subtitle": "A six-part executive overview: from candidate friction to a practical product improvement proposal",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 14px;">
          <!-- 6-Part Structured Visual Grid -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; flex: 1;">
            
            <!-- 1. Problem Origin -->
            <div class="card card-blue" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <span class="badge badge-blue">1. Origin</span>
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: #EFF6FF; color: var(--naukri-blue); display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">👤</div>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">Personal Experience</div>
                <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                  Began with personal firsthand observation: applying across multiple role categories required different resume versions, creating repetitive file management during applications.
                </div>
              </div>
              <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid #DBEAFE; font-size: 11px; font-weight: 700; color: var(--naukri-blue);">
                [Personal Observation Grounding]
              </div>
            </div>

            <!-- 2. Candidate Friction -->
            <div class="card card-rose" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <span class="badge badge-red">2. Candidate Problem</span>
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: #FFF1F2; color: var(--rose-accent); display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">⚠️</div>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">Application Friction</div>
                <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                  When a job requires a resume different from the profile-attached file, candidates may have to navigate away, update their profile resume, and re-enter the flow, risking drop-off.
                </div>
              </div>
              <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid #FECDD3; font-size: 11px; font-weight: 700; color: var(--rose-accent);">
                [Context-Switching & Overwriting Risk]
              </div>
            </div>

            <!-- 3. Research Evidence -->
            <div class="card card-teal" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <span class="badge badge-teal">3. Research</span>
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: #F0FDFA; color: var(--teal-accent); display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">📊</div>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">Exploratory Survey (N=100+)</div>
                <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                  Survey of 100+ college job seekers showed 80% applied across 3+ role types, 90% maintain multiple resumes, and 90% expressed high intent to use a resume library.
                </div>
              </div>
              <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid #99F6E4; font-size: 11px; font-weight: 700; color: var(--teal-accent);">
                [Early-Career & Placement Cohort]
              </div>
            </div>

            <!-- 4. Validation Boundaries -->
            <div class="card card-amber" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <span class="badge badge-amber">4. Boundaries</span>
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: #FFFBEB; color: var(--amber-accent); display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">🔍</div>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">Validation Limits</div>
                <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                  Evidence supports deeper investigation, but does not prove a platform-wide defect. Naukri's internal telemetry is required to verify actual drop-off rates and ATS splits.
                </div>
              </div>
              <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid #FDE68A; font-size: 11px; font-weight: 700; color: var(--amber-accent);">
                [Requires Naukri Internal Telemetry]
              </div>
            </div>

            <!-- 5. Product Opportunity -->
            <div class="card card-purple" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <span class="badge" style="background:#EDE9FE; color:#6D28D9;">5. Opportunity</span>
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: #F5F3FF; color: #7C3AED; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">💡</div>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">Resume Library</div>
                <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                  A persistent library of role-specific resumes (proposed MVP capacity assumption: up to 5) with application-time selection, conditional saving post-upload, and non-destructive storage.
                </div>
              </div>
              <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid #DDD6FE; font-size: 11px; font-weight: 700; color: #7C3AED;">
                [Simpler Job Application Experience]
              </div>
            </div>

            <!-- 6. Recommendation -->
            <div class="card card-emerald" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                  <span class="badge badge-teal">6. Next Steps</span>
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: #ECFDF5; color: var(--emerald-accent); display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;">🚀</div>
                </div>
                <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">Validate & Pilot</div>
                <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                  Collaborate with Naukri PMs to audit existing application journeys, test usability with multi-role job seekers, and evaluate via a controlled A/B experiment.
                </div>
              </div>
              <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid #A7F3D0; font-size: 11px; font-weight: 700; color: var(--emerald-accent);">
                [A/B Pilot on Direct Apply Flow]
              </div>
            </div>

          </div>
          
          <!-- Bottom Context Callout -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 10px 18px; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 12.5px; color: var(--slate-700);">
              <strong style="color: var(--navy-dark);">Core Product Philosophy:</strong> Give candidates complete agency over which document reaches the recruiter, without silent overwrites or profile disruption.
            </div>
            <span class="badge badge-blue" style="font-size: 11px;">10–12 Min Presentation Summary</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 02 — Executive Summary (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "Here is the entire investigation on a single page, structured across six logical dimensions:</p>
        <ul>
          <li><strong>1. Problem Origin:</strong> The idea originated from personal job-search experience applying across distinct functional roles.</li>
          <li><strong>2. Candidate Friction:</strong> Switching resume versions in certain application journeys requires manual profile updates or re-uploading, adding cognitive friction and drop-off risk.</li>
          <li><strong>3. Research:</strong> An exploratory survey with 100+ college students confirmed that 80% apply across 3 or more role types and 90% maintain multiple resumes.</li>
          <li><strong>4. Validation Boundaries:</strong> We acknowledge research boundaries upfront—this survey shows early-career candidate demand, but Naukri's internal telemetry is needed to quantify platform-wide impact.</li>
          <li><strong>5. Opportunity:</strong> A candidate-controlled Resume Library with conditional saving and application-time selection.</li>
          <li><strong>6. Recommendation:</strong> Conduct an internal telemetry audit followed by a controlled A/B experiment measuring application completion rates."</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's look closer at where this idea began and the specific candidates experiencing this friction.</div>
        """
    },

    # SLIDE 03: PROBLEM ORIGIN & TARGET CANDIDATES (Merges old Slides 4 & 5)
    {
        "id": "slide-3",
        "number": "03",
        "stage": "Discover",
        "tag": "Problem Origin & Target Users",
        "evidenceType": "Personal Observation",
        "title": "Where the Idea Started — Understanding the Candidate",
        "subtitle": "Firsthand job-seeker observation and the multi-role reality for early-career candidates",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 14px;">
          <!-- Top Row: Personal Experience & Multi-Role Reality -->
          <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 16px; flex: 1;">
            
            <!-- Left: Firsthand Personal Observation -->
            <div class="card card-blue" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <span class="evidence-tag evidence-tag-obs">[PERSONAL OBSERVATION]</span>
                  <span class="badge badge-blue">Origin Narrative</span>
                </div>
                <div style="font-size: 17px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
                  Personal Job-Seeker Experience
                </div>
                <div style="background: #FFFFFF; border-left: 3.5px solid var(--naukri-blue); padding: 12px 14px; border-radius: 4px; font-size: 13px; color: var(--slate-700); line-height: 1.55; margin-bottom: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                  <em>"This proposal began with my own experience of applying across different role categories. I maintained different resume versions for different opportunities. When the document I wanted to submit differed from the resume associated with my profile, managing the change could add steps to the application process in the flow I encountered."</em>
                </div>
                <div style="font-size: 12.5px; color: var(--slate-600); line-height: 1.5;">
                  Managing different documents manually across applications created cognitive friction and fear of accidentally submitting the wrong resume or overwriting a previously tailored CV.
                </div>
              </div>
              
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px 12px; font-size: 11.5px; color: var(--slate-600);">
                <strong>Methodological Note:</strong> Personal observation serves as the hypothesis generator. It is tested through candidate research and competitor benchmarking.
              </div>
            </div>

            <!-- Right: The Multi-Role Candidate Reality -->
            <div class="card card-indigo" style="display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <span class="badge" style="background:#EDE9FE; color:#4F46E5;">Candidate Reality</span>
                  <span style="font-size: 11px; color: var(--slate-400); font-weight: 600;">1 Candidate • Multiple Profiles</span>
                </div>
                <div style="font-size: 17px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">
                  One Candidate, Diverse Strengths
                </div>
                <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.45; margin-bottom: 10px;">
                  Modern early-career candidates rarely apply to a single narrow job title. They tailor distinct resumes highlighting relevant projects:
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <div style="background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 6px; padding: 8px 10px;">
                    <div style="font-size: 12px; font-weight: 700; color: #1E3A8A;">💼 Product Mgmt</div>
                    <div style="font-size: 10.5px; color: #2563EB;">Wireframing, PRDs, roadmaps</div>
                  </div>
                  <div style="background: #F5F3FF; border: 1px solid #DDD6FE; border-radius: 6px; padding: 8px 10px;">
                    <div style="font-size: 12px; font-weight: 700; color: #6D28D9;">📊 Consulting</div>
                    <div style="font-size: 10.5px; color: #7C3AED;">Case studies, business analysis</div>
                  </div>
                  <div style="background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 6px; padding: 8px 10px;">
                    <div style="font-size: 12px; font-weight: 700; color: #B45309;">⚙️ Business Ops</div>
                    <div style="font-size: 10.5px; color: #D97706;">Logistics, analytics, processes</div>
                  </div>
                  <div style="background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 6px; padding: 8px 10px;">
                    <div style="font-size: 12px; font-weight: 700; color: #166534;">💻 Tech / Eng</div>
                    <div style="font-size: 10.5px; color: #059669;">Codebases, APIs, SQL, models</div>
                  </div>
                </div>
              </div>
              
              <div style="font-size: 11px; color: #4338CA; margin-top: 6px;">
                Each role emphasizes different evidence from the same candidate's background.
              </div>
            </div>

          </div>

          <!-- Bottom: Target User Segmentation -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div style="background: #FFFFFF; border: 1.5px solid #86EFAC; border-left: 4px solid var(--emerald-accent); border-radius: 8px; padding: 10px 14px; box-shadow: 0 2px 6px rgba(5,150,105,0.04);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                <strong style="color: #14532D; font-size: 13.5px;">Primary Target Segment: College Students & Early-Career</strong>
                <span class="badge badge-teal" style="font-size: 10px;">High Frequency Multi-Role</span>
              </div>
              <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                Facing placement seasons, internship cycles, and off-campus drives where students must apply concurrently across analyst, product, software, and consulting roles with tailored resumes.
              </div>
            </div>

            <div style="background: #FFFFFF; border: 1.5px solid #FDE68A; border-left: 4px solid var(--amber-accent); border-radius: 8px; padding: 10px 14px; box-shadow: 0 2px 6px rgba(217,119,6,0.04);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                <strong style="color: #92400E; font-size: 13.5px;">Secondary Segment: Career Changers & Lateral Seekers</strong>
                <span class="badge badge-amber" style="font-size: 10px;">Requires Naukri Validation</span>
              </div>
              <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                Mid-career professionals exploring dual tracks (e.g. IC vs Engineering Manager, or Sales vs Account Management). Stated as a high-potential hypothesis requiring Naukri validation.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 03 — Problem Origin & Target Candidates (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "This proposal began with my personal experience. While applying for jobs across different domains, I maintained separate CVs tailored to Product Management, Consulting, Operations, and Software Engineering.</p>
        <p>When the resume I wanted to submit for a specific posting differed from the single resume tied to my Naukri profile, managing that swap added friction to the application flow. I'm deliberately labeling this as a <strong>[PERSONAL OBSERVATION]</strong>, not a proven platform-wide defect.</p>
        <p>This multi-role reality is especially acute for <strong>college students and early-career job seekers</strong> during placement seasons, where candidates apply across multiple tracks simultaneously. A secondary segment includes professionals exploring parallel career trajectories, which we flag for future validation with Naukri's user data."</p>
        <div class='cue-box'><strong>Transition:</strong> Let's define the precise candidate problem through a structured Job-to-be-Done framework.</div>
        """
    },

    # SLIDE 04: PROBLEM DEFINITION & JOB-TO-BE-DONE
    {
        "id": "slide-4",
        "number": "04",
        "stage": "Define",
        "tag": "Problem Definition & JTBD",
        "evidenceType": "Proposed Solution",
        "title": "Defining the Actual Candidate Problem",
        "subtitle": "Framing candidate friction through a structured Job-to-be-Done and formal problem boundary",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 12px;">
          <!-- Prominent JTBD Callout Banner -->
          <div style="background: linear-gradient(135deg, #1E3A8A 0%, #1856EA 100%); color: white; border-radius: 10px; padding: 14px 20px; box-shadow: 0 4px 14px rgba(24,86,234,0.2);">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; color: #93C5FD; margin-bottom: 4px;">
              Core Job-to-be-Done (JTBD)
            </div>
            <div style="font-size: 15.5px; font-weight: 600; line-height: 1.5; color: #FFFFFF;">
              <em>"When I apply to different types of roles, I want to choose the resume that best represents my relevant experience while keeping my other versions intact, so I can submit the document I intend without repeatedly managing profile files."</em>
            </div>
          </div>

          <!-- 4-Box Framing Matrix -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
            
            <div class="card card-blue" style="padding: 12px 14px;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 6px;">
                <span class="badge badge-blue">User</span>
              </div>
              <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 4px;">Who is struggling?</div>
              <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                Candidates who actively maintain multiple role-specific resumes (e.g. students, multi-track applicants).
              </div>
            </div>

            <div class="card card-indigo" style="padding: 12px 14px;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 6px;">
                <span class="badge" style="background:#EDE9FE; color:#4F46E5;">Situation</span>
              </div>
              <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 4px;">When does it happen?</div>
              <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                During job application flows where the intended submission file is not the current profile resume.
              </div>
            </div>

            <div class="card card-amber" style="padding: 12px 14px;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 6px;">
                <span class="badge badge-amber">Need</span>
              </div>
              <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 4px;">What do they need?</div>
              <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                To pick the right resume easily in-flow, without overwriting other saved files or leaving the application.
              </div>
            </div>

            <div class="card card-emerald" style="padding: 12px 14px;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 6px;">
                <span class="badge badge-teal">Outcome</span>
              </div>
              <div style="font-size: 14px; font-weight: 800; color: var(--navy-dark); margin-bottom: 4px;">Desired Result</div>
              <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                Faster application completion, higher submission accuracy, and peace of mind about historical records.
              </div>
            </div>

          </div>

          <!-- Bottom: Formal Problem Statement & Scope Distinction -->
          <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 14px;">
            <div style="background: #FFFFFF; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 12px 16px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue); letter-spacing: 0.6px; margin-bottom: 4px;">
                Formal Problem Statement
              </div>
              <div style="font-size: 13px; color: var(--navy-dark); font-weight: 600; line-height: 1.5;">
                "Candidates who maintain multiple role-specific resumes need a simple and reliable way to select the intended document during supported job application flows, without repeatedly replacing or losing access to other versions."
              </div>
            </div>

            <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 12px 14px;">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--slate-600); letter-spacing: 0.6px; margin-bottom: 4px;">
                Scope Boundary: Management vs Writing
              </div>
              <div style="font-size: 11.5px; color: var(--slate-600); line-height: 1.45;">
                <span style="color: var(--emerald-accent); font-weight: 700;">✓ IN SCOPE:</span> Document storage, in-flow selection, conditional saving, version naming.<br>
                <span style="color: var(--rose-accent); font-weight: 700;">✕ OUT OF SCOPE:</span> AI resume drafting, formatting templates, or keyword stuffing.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 04 — Problem Definition & JTBD (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To prevent solution bias, we formalize the candidate's actual need using the Job-to-be-Done framework:</p>
        <p><em>'When I apply to different types of roles, I want to choose the resume that best represents my relevant experience while keeping my other versions intact, so I can submit the document I intend without repeatedly managing profile files.'</em></p>
        <p>Notice the four-box breakdown: the user is a multi-role applicant; the situation is applying on Naukri; the need is choosing without overwriting; and the desired outcome is fast, confident submission.</p>
        <p>Crucially, we define a clear scope boundary: this proposal addresses <strong>resume management</strong>—storage, selection, and document retention. It is not a resume writing tool, AI template generator, or keyword builder."</p>
        <div class='cue-box'><strong>Transition:</strong> Now let's examine the empirical survey evidence collected from 100+ job seekers to test this problem definition.</div>
        """
    }
]
