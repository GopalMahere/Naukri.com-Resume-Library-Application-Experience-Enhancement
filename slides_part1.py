# slides_part1.py - Slides 1 to 5 (Cover, Executive Summary, Problem Discovery, Journey, User Research)

SLIDES_PART1 = [
    # SLIDE 1: COVER
    {
        "id": "slide-1",
        "number": "01",
        "tag": "Product Improvement Proposal",
        "title": "One Profile, Multiple Resumes",
        "subtitle": "A candidate-controlled resume library that makes job applications simpler on Naukri.com",
        "content": """
        <div style="flex: 1; display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 24px; align-items: center; width: 100%;">
          <div style="display: flex; flex-direction: column; gap: 14px; width: 100%;">
            <div style="display: inline-flex; align-items: center; gap: 8px; flex-wrap: wrap;">
              <span class="badge badge-blue" style="font-size: 11px; padding: 4px 10px;">Product Strategy Proposal</span>
              <span class="badge badge-teal" style="font-size: 11px; padding: 4px 10px;">Interactive Prototype Included</span>
            </div>
            
            <h1 style="font-size: 34px; font-weight: 800; color: var(--navy-dark); line-height: 1.15; letter-spacing: -1px;">
              One Profile,<br><span style="color: var(--naukri-blue);">Multiple Resumes</span>
            </h1>
            
            <p style="font-size: 14px; color: var(--slate-600); line-height: 1.5; max-width: 520px;">
              A candidate-controlled resume library that enables job seekers to maintain one unified Naukri master profile while selecting role-specific resumes at the moment of application—reducing application friction without silent overwrites or multiple profiles.
            </p>
            
            <!-- Rigorous Presenter Identity & Scope Card -->
            <div class="card card-tinted" style="padding: 12px 14px; border-left: 3px solid var(--naukri-blue); width: 100%; max-width: 500px;">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 11.5px; color: var(--slate-700);">
                <div>
                  <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500);">Prepared By</div>
                  <strong style="color: var(--navy-dark); font-size: 12.5px;">Aditya Sharma</strong>
                </div>
                <div>
                  <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500);">Document Format</div>
                  <strong style="color: var(--navy-dark); font-size: 12.5px;">Independent PM Case Study</strong>
                </div>
                <div style="grid-column: span 2; margin-top: 2px;">
                  <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500);">Professional Scope</div>
                  <span style="color: var(--slate-600);">User Research, Product Discovery, UX Design, PRD, and Interactive Prototype</span>
                </div>
              </div>
            </div>
            
            <div style="font-size: 11px; color: var(--slate-500); display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
              <span><strong>Target Platform:</strong> Naukri.com Candidate Experience</span>
              <span>•</span>
              <span><strong>Date:</strong> November 2026</span>
            </div>
          </div>
          
          <!-- Visual Architectural Schematic -->
          <div class="card card-tinted" style="padding: 18px; border: 1.5px solid var(--naukri-blue-border); background: linear-gradient(145deg, #F8FAFC 0%, #EFF6FF 100%); width: 100%;">
            <div style="text-align: center; margin-bottom: 12px;">
              <span style="font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: var(--naukri-blue);">Proposed Architectural Model</span>
              <h3 style="font-size: 14px; font-weight: 700; color: var(--navy-dark); margin-top: 2px;">Single Master Profile, Dedicated Library</h3>
            </div>
            
            <div style="display: flex; flex-direction: column; align-items: center; gap: 8px; width: 100%;">
              <!-- Master Node -->
              <div style="background: var(--navy-dark); color: white; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 11.5px; box-shadow: var(--shadow-md); width: 100%; max-width: 320px; text-align: center; display: flex; align-items: center; justify-content: center; gap: 6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                Single Comprehensive Profile (Master Career Records)
              </div>
              
              <!-- Connector -->
              <div style="height: 12px; width: 2px; background: var(--naukri-blue);"></div>
              
              <!-- Dedicated Library Box -->
              <div style="background: var(--pure-white); border: 1.5px dashed var(--naukri-blue); border-radius: 6px; padding: 8px 12px; width: 100%; max-width: 340px; box-shadow: var(--shadow-sm);">
                <div style="font-size: 10px; font-weight: 700; color: var(--naukri-blue); text-transform: uppercase; margin-bottom: 4px; text-align: center;">Candidate Resume Library (Isolated Documents)</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px;">
                  <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 4px 6px; border-radius: 4px; font-size: 10.5px; font-weight: 600;">
                    📄 Product Mgmt CV
                  </div>
                  <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 4px 6px; border-radius: 4px; font-size: 10.5px; font-weight: 600;">
                    📄 Consulting CV
                  </div>
                  <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 4px 6px; border-radius: 4px; font-size: 10.5px; font-weight: 600;">
                    📄 Operations CV
                  </div>
                  <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 4px 6px; border-radius: 4px; font-size: 10.5px; font-weight: 600;">
                    📄 Core Tech CV
                  </div>
                </div>
              </div>
              
              <!-- Connector -->
              <div style="height: 12px; width: 2px; background: var(--emerald-accent);"></div>
              
              <!-- Apply Moment Selection -->
              <div style="background: var(--emerald-light); border: 1.5px solid var(--emerald-accent); color: #065F46; padding: 7px 12px; border-radius: 6px; font-weight: 700; font-size: 11.5px; text-align: center; width: 100%; max-width: 340px;">
                🎯 Moment-of-Application: Transparent Resume Selection
              </div>
            </div>
            
            <div style="margin-top: 10px; text-align: center; font-size: 10.5px; color: var(--slate-500);">
              Preserves candidate control • Non-destructive saving • Reliable history
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Executive Context & Proposal Introduction</h4>
        <p>Good morning. My name is Aditya Sharma, and this is an independent Product Management case study proposing an enhancement for Naukri.com titled <strong>'One Profile, Multiple Resumes'</strong>.</p>
        <p>Job seekers frequently apply across varied role categories (such as Product Management, Consulting, Operations, and Core Tech). Today, candidates often maintain different resume versions tailored to these roles, but switching or managing them during portal applications can introduce unnecessary friction.</p>
        <p>This proposal explores giving candidates a dedicated Resume Library within their single profile, allowing them to choose or upload the appropriate resume at the moment of applying without overwriting existing files.</p>
        <div class='cue-box'><strong>Transition:</strong> Let's examine the executive summary of the opportunity, research signals, and proposed product value.</div>
        """
    },

    # SLIDE 2: EXECUTIVE SUMMARY
    {
        "id": "slide-2",
        "number": "02",
        "tag": "Executive Briefing",
        "title": "Executive Summary: The Strategic Opportunity",
        "subtitle": "Bridging multi-role candidate reality with streamlined, candidate-controlled application UX",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 14px;">
          <div class="grid-4" style="flex: 1;">
            <!-- Pillar 1 -->
            <div class="card card-tinted" style="border-top: 3px solid var(--rose-accent);">
              <div class="card-header-sm">
                <span>01. The Problem</span>
                <span class="badge badge-red">Observed Friction</span>
              </div>
              <div class="card-title-lg">Resume-Switching Friction</div>
              <p class="card-text">
                Candidates who apply across diverse role tracks often maintain different resume versions. When applying, switching or updating resumes can require navigating away from active applications.
              </p>
              <div style="margin-top: auto; padding-top: 8px; font-size: 11px; color: var(--rose-accent); font-weight: 600;">
                Observed workaround: Leaving apply flow to update profile CV or juggling profiles.
              </div>
            </div>
            
            <!-- Pillar 2 -->
            <div class="card card-tinted" style="border-top: 3px solid var(--amber-accent);">
              <div class="card-header-sm">
                <span>02. Research Signal</span>
                <span class="badge badge-amber">N=45 Survey</span>
              </div>
              <div class="card-title-lg">Exploratory Signal</div>
              <p class="card-text">
                In an exploratory survey of 45 college students, <strong>90%</strong> reported maintaining multiple resumes, and <strong>90%</strong> frequently needed an alternate resume during applications.
              </p>
              <div style="margin-top: auto; padding-top: 8px; font-size: 11px; color: var(--amber-accent); font-weight: 600;">
                80% apply across 3 or more role types simultaneously within this sample.
              </div>
            </div>
            
            <!-- Pillar 3 -->
            <div class="card card-tinted" style="border-top: 3px solid var(--naukri-blue);">
              <div class="card-header-sm">
                <span>03. Proposed Solution</span>
                <span class="badge badge-blue">Product Concept</span>
              </div>
              <div class="card-title-lg">One Profile, Multiple Resumes</div>
              <p class="card-text">
                Maintain one comprehensive profile with a dedicated Resume Library. Select a saved resume or upload a new one at apply time, with optional non-destructive saving.
              </p>
              <div style="margin-top: auto; padding-top: 8px; font-size: 11px; color: var(--naukri-blue); font-weight: 600;">
                Preselects default CV for convenience; never submits without explicit review.
              </div>
            </div>
            
            <!-- Pillar 4 -->
            <div class="card card-tinted" style="border-top: 3px solid var(--emerald-accent);">
              <div class="card-header-sm">
                <span>04. Expected Value</span>
                <span class="badge badge-teal">Value Hypothesis</span>
              </div>
              <div class="card-title-lg">Streamlined Completion</div>
              <p class="card-text">
                Designed to reduce navigation steps, mitigate abandonment risks, and preserve document history integrity for both candidate and recruiter.
              </p>
              <div style="margin-top: auto; padding-top: 8px; font-size: 11px; color: var(--emerald-accent); font-weight: 600;">
                Hypothetical funnel model: +500 completed applications per 10,000 starts.
              </div>
            </div>
          </div>
          
          <!-- Core Philosophical Anchor -->
          <div class="card card-blue" style="padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
            <div style="display: flex; align-items: center; gap: 12px;">
              <div style="background: var(--naukri-blue); color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; flex-shrink: 0;">
                🛡️
              </div>
              <div>
                <div style="font-weight: 800; font-size: 13px; color: var(--navy-dark);">Core Product Mandate: Candidate Control & Transparency</div>
                <div style="font-size: 11.5px; color: var(--slate-600); margin-top: 2px;">
                  The system preselects the candidate's designated default resume for convenience, but never submits without explicit review and confirmation. If no default is designated, resume selection is required.
                </div>
              </div>
            </div>
            <div style="text-align: right; flex-shrink: 0;">
              <span class="badge badge-gray" style="font-size: 10px;">Non-Destructive Saving Architecture</span>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Executive Briefing Talking Points</h4>
        <ul>
          <li><strong>The Core Premise:</strong> Candidates often apply across different role categories requiring tailored resumes. When applying, switching resumes can create unnecessary friction.</li>
          <li><strong>The Exploratory Signal:</strong> Our survey of 45 college students suggests that multi-role job exploration is common (80% apply across 3+ role types), and 90% reported frequently needing an alternate resume while applying.</li>
          <li><strong>The Solution:</strong> One comprehensive profile, coupled with a dedicated Resume Library where files are independently stored and selectable at the moment of applying.</li>
          <li><strong>Candidate Control:</strong> The system preselects the candidate-designated default resume for convenience, but never submits without explicit candidate review and confirmation. If no default is set, selection is required.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's examine the candidate problem and user context that motivated this proposal.</div>
        """
    },

    # SLIDE 3: THE PROBLEM DISCOVERY
    {
        "id": "slide-3",
        "number": "03",
        "tag": "Problem Discovery",
        "title": "The Multi-Category Candidate Dilemma",
        "subtitle": "Why modern candidates maintain distinct resume versions and where portal friction occurs",
        "content": """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; height: 100%;">
          <!-- Left Column: The User Reality -->
          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div class="card" style="flex: 1;">
              <div class="card-header-sm">User Context & Multi-Track Reality</div>
              <div class="card-title-lg">One Candidate, Multiple Career Directions</div>
              <p class="card-text" style="margin-bottom: 10px;">
                Candidates often apply across different roles, departments, and industries simultaneously. For example, a candidate might be applying for:
              </p>
              
              <div style="display: flex; flex-direction: column; gap: 6px;">
                <div style="background: var(--slate-50); border-left: 3px solid #3B82F6; padding: 6px 10px; border-radius: 0 4px 4px 0;">
                  <strong style="font-size: 11.5px; color: var(--navy-dark);">Product Management (APM):</strong>
                  <span style="font-size: 11px; color: var(--slate-600);"> Emphasizing user empathy, product teardowns, metrics, and agile delivery.</span>
                </div>
                <div style="background: var(--slate-50); border-left: 3px solid #10B981; padding: 6px 10px; border-radius: 0 4px 4px 0;">
                  <strong style="font-size: 11.5px; color: var(--navy-dark);">Management Consulting:</strong>
                  <span style="font-size: 11px; color: var(--slate-600);"> Emphasizing structured problem-solving, case competitions, and strategy frameworks.</span>
                </div>
                <div style="background: var(--slate-50); border-left: 3px solid #F59E0B; padding: 6px 10px; border-radius: 0 4px 4px 0;">
                  <strong style="font-size: 11.5px; color: var(--navy-dark);">Business Operations / Analytics:</strong>
                  <span style="font-size: 11px; color: var(--slate-600);"> Emphasizing SQL dashboards, financial modeling, and process optimization.</span>
                </div>
                <div style="background: var(--slate-50); border-left: 3px solid #8B5CF6; padding: 6px 10px; border-radius: 0 4px 4px 0;">
                  <strong style="font-size: 11.5px; color: var(--navy-dark);">Core Engineering:</strong>
                  <span style="font-size: 11px; color: var(--slate-600);"> Emphasizing technical stack, architecture, algorithms, and code repositories.</span>
                </div>
              </div>
            </div>
            
            <div class="card card-tinted" style="padding: 10px 12px;">
              <div style="font-size: 11px; font-weight: 700; color: var(--navy-dark);">The Observed Difficulty:</div>
              <div style="font-size: 11px; color: var(--slate-600); margin-top: 2px;">
                The difficulty is not necessarily creating these resumes. The difficulty is <strong>managing and switching between them when applying for jobs</strong>.
              </div>
            </div>
          </div>
          
          <!-- Right Column: Formal Problem & Opportunity Statements -->
          <div style="display: flex; flex-direction: column; gap: 12px;">
            <!-- Formal Problem Statement Card -->
            <div class="card" style="border-left: 4px solid var(--rose-accent); background: #FFFBFB;">
              <div class="card-header-sm">
                <span style="color: var(--rose-accent); font-weight: 800;">Problem Statement</span>
                <span class="badge badge-red">Observed Experience</span>
              </div>
              <div style="font-size: 14px; font-weight: 700; color: #881337; line-height: 1.45; margin: 5px 0;">
                "Candidates who apply across multiple job categories often maintain different resume versions, but managing and switching between those documents during the application journey can create unnecessary friction."
              </div>
              <ul style="font-size: 11px; color: #4C0519; padding-left: 18px; margin-top: 4px; line-height: 1.45;">
                <li>Repeated profile/resume updates.</li>
                <li>Time spent navigating between application pages and settings.</li>
                <li>Confusion about which resume is currently uploaded.</li>
                <li>Risk of submitting a less relevant resume, or postponing an application.</li>
              </ul>
            </div>
            
            <!-- Formal Product Opportunity Statement Card -->
            <div class="card" style="border-left: 4px solid var(--emerald-accent); background: #F0FDF4; flex: 1;">
              <div class="card-header-sm">
                <span style="color: var(--emerald-accent); font-weight: 800;">Product Opportunity</span>
                <span class="badge badge-teal">Proposed Opportunity</span>
              </div>
              <div style="font-size: 14px; font-weight: 700; color: #064E3B; line-height: 1.45; margin: 5px 0;">
                "Give candidates a centralised, candidate-controlled resume library that allows them to select the right resume at the moment of application, without repeatedly replacing their primary resume or maintaining multiple profiles."
              </div>
              <div style="font-size: 11px; color: #047857; line-height: 1.45; margin-top: 5px;">
                The objective is to reduce unnecessary steps in the application journey and make resume management more convenient while keeping the candidate in full control.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Problem Statement & Candidate Context</h4>
        <p>In our discovery discussions, we observed that candidates naturally tailor their resumes depending on the role. An applicant targeting both Product Management and Management Consulting cannot highlight the exact same project narrative for both.</p>
        <p>Consequently, candidates maintain multiple resume files. Creating them on a laptop is straightforward—the friction arises when applying across job portals.</p>
        <p>Important distinction: we present this as an observed candidate experience that warrants structured validation across Naukri's application types.</p>
        <div class='cue-box'><strong>Transition:</strong> Let's trace the user-reported journey where this friction occurs.</div>
        """
    },

    # SLIDE 4: CURRENT CANDIDATE JOURNEY
    {
        "id": "slide-4",
        "number": "04",
        "tag": "Journey Mapping",
        "title": "The Current Candidate Journey: Observed Friction",
        "subtitle": "Mapping the user-reported application journey when an alternate resume is needed",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 14px;">
          <!-- Journey Steps Flowchart -->
          <div class="flow-row">
            <div class="flow-step">
              <div class="flow-step-num">Step 1</div>
              <div class="flow-step-title">Maintain Profile</div>
              <div class="flow-step-desc">Candidate maintains a Naukri profile with an attached resume.</div>
              <div style="margin-top: auto; padding-top: 4px;"><span class="badge badge-gray">Baseline</span></div>
            </div>
            
            <div class="flow-arrow">→</div>
            
            <div class="flow-step">
              <div class="flow-step-num">Step 2</div>
              <div class="flow-step-title">Find Job</div>
              <div class="flow-step-desc">Candidate finds a relevant job opening.</div>
              <div style="margin-top: auto; padding-top: 4px;"><span class="badge badge-blue">Discovery</span></div>
            </div>
            
            <div class="flow-arrow">→</div>
            
            <div class="flow-step">
              <div class="flow-step-num">Step 3</div>
              <div class="flow-step-title">Click Apply</div>
              <div class="flow-step-desc">Candidate clicks Apply to start the application process.</div>
              <div style="margin-top: auto; padding-top: 4px;"><span class="badge badge-blue">Apply Start</span></div>
            </div>
            
            <div class="flow-arrow">→</div>
            
            <div class="flow-step warning-step">
              <div class="flow-step-num" style="color: var(--amber-accent);">Step 4</div>
              <div class="flow-step-title">Realizes Mismatch</div>
              <div class="flow-step-desc">Candidate realizes a different resume would be more appropriate.</div>
              <div style="margin-top: auto; padding-top: 4px;"><span class="badge badge-amber">Hesitation</span></div>
            </div>
            
            <div class="flow-arrow">→</div>
            
            <!-- Friction Hotspot -->
            <div class="flow-step" style="border: 2px solid var(--rose-accent); background: #FFF5F5;">
              <div class="flow-step-num" style="color: var(--rose-accent);">Step 5: Friction Point</div>
              <div class="flow-step-title" style="color: #9F1239;">Leaves Application Flow</div>
              <div class="flow-step-desc" style="color: #4C0519;">May need to leave application journey to update or replace resume on profile.</div>
              <div style="margin-top: auto; padding-top: 4px;"><span class="badge badge-red">Observed Break</span></div>
            </div>
            
            <div class="flow-arrow">→</div>
            
            <div class="flow-step">
              <div class="flow-step-num">Step 6</div>
              <div class="flow-step-title">Return & Finish</div>
              <div class="flow-step-desc">Returns to job application and completes process.</div>
              <div style="margin-top: auto; padding-top: 4px;"><span class="badge badge-gray">Completion</span></div>
            </div>
          </div>
          
          <!-- Downstream Consequences Grid -->
          <div class="grid-3" style="flex: 1;">
            <div class="card card-tinted">
              <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                <span style="color: var(--rose-accent); font-size: 15px;">⏱️</span>
                <strong style="font-size: 12px; color: var(--navy-dark);">Time & Navigation Overhead</strong>
              </div>
              <p class="card-text" style="font-size: 11.5px;">
                Repeated profile updates and navigating between pages introduces friction and slows down the candidate's application momentum.
              </p>
            </div>
            
            <div class="card card-tinted">
              <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                <span style="color: var(--amber-accent); font-size: 15px;">⚠️</span>
                <strong style="font-size: 12px; color: var(--navy-dark);">Version Confusion & Relevance Risk</strong>
              </div>
              <p class="card-text" style="font-size: 11.5px;">
                Uncertainty about which resume is currently active on the profile creates anxiety and risks submitting a less relevant document.
              </p>
            </div>
            
            <div class="card card-tinted">
              <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                <span style="color: var(--rose-accent); font-size: 15px;">📉</span>
                <strong style="font-size: 12px; color: var(--navy-dark);">Application Postponement / Drop-off</strong>
              </div>
              <p class="card-text" style="font-size: 11.5px;">
                Breaking out of the linear application journey increases the possibility of abandoning or postponing an otherwise relevant application.
              </p>
            </div>
          </div>
          
          <!-- Explicit Validation Disclaimer -->
          <div style="background: var(--slate-100); border-left: 3px solid var(--slate-400); padding: 7px 12px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 6px;">
            <div>
              <strong>Important Scope Note:</strong> This reflects user-reported application friction from our exploratory research. Different job listings, external application links, and desktop vs. mobile experiences may behave differently. This represents an explicit validation item for the Naukri product team.
            </div>
            <span class="badge badge-gray" style="flex-shrink: 0;">Validation Item</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Walking Through the User-Reported Journey</h4>
        <p>This journey map represents the sequence reported by candidates during discovery.</p>
        <p>Notice Step 5: when a candidate realizes that their attached profile resume is tailored for a different role, they may exit the application flow to replace or re-upload a document on their profile before returning.</p>
        <p>As PMs, we know that any journey break in a high-intent conversion funnel can lead to postponement or drop-off.</p>
        <p>However, we present this transparently as an observed experience that warrants comprehensive validation across Naukri's application types and device platforms.</p>
        <div class='cue-box'><strong>Transition:</strong> Let's examine our exploratory survey of 45 college students to see how common this behavior is.</div>
        """
    },

    # SLIDE 5: USER RESEARCH (SURVEY OF 45 RESPONDENTS)
    {
        "id": "slide-5",
        "number": "05",
        "tag": "User Research",
        "title": "Exploratory User Research: Survey of 45 Respondents",
        "subtitle": "Exploratory candidate signals regarding multi-category applications and resume management practices",
        "content": """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; height: 100%;">
          <!-- Left Column: Key Survey Metrics & Horizontal Bar Chart -->
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <!-- Top Metric Stat Boxes -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;">
              <div class="stat-box" style="padding: 12px 8px;">
                <div class="stat-value" style="font-size: 28px;">90%</div>
                <div class="stat-label" style="font-size: 11px;">Recent Applicants</div>
                <div class="stat-sub" style="font-size: 10px;">Applied in last 90 days (Q1)</div>
              </div>
              <div class="stat-box" style="padding: 12px 8px;">
                <div class="stat-value" style="font-size: 28px;">90%</div>
                <div class="stat-label" style="font-size: 11px;">Multiple CVs</div>
                <div class="stat-sub" style="font-size: 10px;">Different versions (Q4)</div>
              </div>
              <div class="stat-box" style="padding: 12px 8px; border-color: var(--naukri-blue-border); background: var(--naukri-blue-light);">
                <div class="stat-value" style="font-size: 28px; color: var(--naukri-blue);">90%</div>
                <div class="stat-label" style="font-size: 11px;">Need Alternate CV</div>
                <div class="stat-sub" style="font-size: 10px;">Frequently while applying (Q7)</div>
              </div>
            </div>
            
            <!-- Horizontal Bar Chart: Q3 Number of role types applied for -->
            <div class="card" style="flex: 1; padding: 14px;">
              <div class="card-header-sm">
                <span>Q3: How many types of roles are you applying for?</span>
                <span class="badge badge-blue">N=45 Distribution</span>
              </div>
              
              <div class="bar-chart-container" style="margin-top: 6px;">
                <div class="bar-row">
                  <div class="bar-label">One Type</div>
                  <div class="bar-track">
                    <div class="bar-fill" style="width: 5%;">5%</div>
                  </div>
                </div>
                <div class="bar-row">
                  <div class="bar-label">Two Types</div>
                  <div class="bar-track">
                    <div class="bar-fill" style="width: 15%;">15%</div>
                  </div>
                </div>
                <div class="bar-row">
                  <div class="bar-label">Three Types</div>
                  <div class="bar-track">
                    <div class="bar-fill" style="width: 20%;">20%</div>
                  </div>
                </div>
                <div class="bar-row">
                  <div class="bar-label" style="font-weight: 700; color: var(--navy-dark);">Four or More Types</div>
                  <div class="bar-track">
                    <div class="bar-fill bar-accent" style="width: 60%; font-weight: 800;">60%</div>
                  </div>
                </div>
              </div>
              
              <div style="font-size: 11px; color: var(--slate-700); margin-top: 8px; line-height: 1.4; background: var(--slate-50); padding: 7px 9px; border-radius: 4px;">
                <strong>Key Interpretation:</strong> In our exploratory sample, <strong>80% of respondents reported applying across three or more role categories</strong> (20% three types + 60% four or more), suggesting that multi-role job searching is common within this group.
              </div>
            </div>
            
            <!-- Cohort Stage Breakdown (Q2) -->
            <div class="card card-tinted" style="padding: 8px 12px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 6px;">
              <div style="font-size: 10.5px; color: var(--slate-600);">
                <strong>Q2 Sample Breakdown:</strong> 80% college students seeking placements/full-time • 20% seeking internships
              </div>
              <span class="badge badge-amber" style="font-size: 9.5px;">Student-Focused Sample</span>
            </div>
          </div>
          
          <!-- Right Column: Qualitative Drivers, Feature Valuation & Limitations -->
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <!-- Reported Motivations & Workarounds -->
            <div class="card" style="padding: 10px 12px;">
              <div class="card-header-sm">Reported Motivations & Workarounds</div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                <div>
                  <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 2px;">Why Multiple Resumes? (Q5)</div>
                  <ul style="font-size: 10.5px; color: var(--slate-700); padding-left: 14px; line-height: 1.35;">
                    <li>Highlighting different skills</li>
                    <li>Applying to different industries</li>
                    <li>Pursuing different career paths</li>
                    <li>Tailoring to specific JDs</li>
                  </ul>
                </div>
                <div>
                  <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 2px;">Reported Workarounds (Q8)</div>
                  <ul style="font-size: 10.5px; color: var(--slate-700); padding-left: 14px; line-height: 1.35;">
                    <li>Replacing an existing resume</li>
                    <li>Uploading different resume in apply</li>
                    <li>Leaving apply and returning later</li>
                    <li>Sometimes skipping application</li>
                  </ul>
                </div>
              </div>
            </div>
            
            <!-- Stated Preferences (Q11, Q12, Q13) -->
            <div class="card card-blue" style="padding: 10px 12px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
                <span style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue);">Stated Preferences (Q11, Q12)</span>
                <span class="badge badge-blue" style="font-size: 9.5px;">Stated Intent</span>
              </div>
              <div style="display: flex; gap: 14px; margin-bottom: 3px;">
                <div style="font-size: 11px; color: var(--navy-dark);">
                  <strong>90%</strong> rated proposed feature <em>'Extremely useful'</em>
                </div>
                <div style="font-size: 11px; color: var(--navy-dark);">
                  <strong>90%</strong> reported <em>'Very likely'</em> to use
                </div>
              </div>
              <div style="font-size: 10px; color: var(--slate-600); line-height: 1.3;">
                <strong>Valued Features (Q13):</strong> Custom naming, apply-time selection, viewing submitted resume in history, and managing documents (edit/replace/delete).
              </div>
            </div>
            
            <!-- Research Limitations (Transparent Disclosure) -->
            <div class="card" style="border: 1px solid var(--amber-border); background: var(--amber-light); padding: 10px 12px; flex: 1;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 3px;">
                <span style="color: var(--amber-accent); font-size: 13px;">⚖️</span>
                <strong style="font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.5px; color: #92400E;">Research Limitations — Transparent Disclosure</strong>
              </div>
              <ul style="font-size: 10px; color: #78350F; padding-left: 14px; line-height: 1.35;">
                <li><strong>Sample size:</strong> 45 respondents via personal outreach; not statistically representative of all Naukri users.</li>
                <li><strong>Demographics:</strong> Predominantly college students in placement/internship search mode; do not generalise to all working professionals.</li>
                <li><strong>Exploratory scope:</strong> Establishes exploratory candidate behaviour; does not prove market-wide Naukri-specific demand.</li>
                <li><strong>Data fidelity:</strong> Multi-select questions (Q5, Q6, Q8, Q13) record qualitative motivations without exact counts. Q9/Q10 excluded to prevent data fabrication.</li>
                <li><strong>Stated vs. Observed:</strong> Usefulness and likelihood are self-reported stated preferences, not observed adoption.</li>
              </ul>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Navigating the Survey Data with Factual Precision</h4>
        <p>I want to highlight the rigor with which we present our survey findings:</p>
        <ul>
          <li>We surveyed 45 active job seekers, heavily concentrated in college placements (80%) and internships (20%). We do not generalize these findings to all working professionals or all Naukri users.</li>
          <li>Look at Q3: <strong>80% of respondents target three or more distinct role categories</strong> (20% for 3 roles, 60% for 4+ roles). This suggests that multi-role job exploration is common within this student cohort.</li>
          <li>90% stated that they frequently need a resume different from their profile CV at the moment of applying.</li>
          <li>Notice our transparent limitations box at the bottom right: usefulness and adoption likelihood are self-reported sentiments. This research establishes an exploratory problem signal justifying further product validation.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> How do existing job portals handle resume management? Let's examine official documentation across Naukri, LinkedIn, and Indeed India.</div>
        """
    }
]
