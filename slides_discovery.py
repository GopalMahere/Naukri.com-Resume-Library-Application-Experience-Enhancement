# slides_discovery.py - Slides 01 to 06 (Discovery, Overview, PM Approach, Origin, Target Users, JTBD/Definition)

SLIDES_DISCOVERY = [
    # SLIDE 01: INTRODUCTORY COVER
    {
        "id": "slide-1",
        "number": "01",
        "stage": "Discover",
        "tag": "Product Investigation",
        "evidenceType": "Proposed Solution",
        "title": "Apply with the Right Resume",
        "subtitle": "A candidate-controlled Resume Library for a simpler job application experience on Naukri.com",
        "content": """
        <div class="cover-layout">
          <!-- Left: Hero Header & Project Metadata -->
          <div class="cover-hero-box">
            <div>
              <span class="evidence-tag evidence-tag-sol" style="margin-bottom: 8px;">Independent Product Improvement Proposal</span>
              <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: var(--naukri-blue); margin-top: 4px;">
                NAUKRI.COM • CANDIDATE EXPERIENCE INVESTIGATION
              </div>
            </div>
            
            <h1 style="font-size: 34px; font-weight: 800; color: var(--navy-dark); line-height: 1.15; letter-spacing: -1px;">
              Apply with the<br><span style="color: var(--naukri-blue);">Right Resume</span>
            </h1>
            
            <p style="font-size: 15px; color: var(--slate-700); line-height: 1.5; font-weight: 500;">
              A candidate-controlled <strong>Resume Library</strong> that makes it easier to manage role-specific resumes and choose the right document while applying for jobs.
            </p>
            
            <div style="background: var(--slate-50); border-left: 3px solid var(--naukri-blue); padding: 10px 14px; border-radius: 0 6px 6px 0; font-size: 12.5px; color: var(--slate-700); line-height: 1.45;">
              <em>"Candidates may maintain different resumes for different opportunities. The challenge is having the right version ready when it is time to apply."</em>
            </div>
            
            <!-- Metadata Grid -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 6px; padding-top: 12px; border-top: 1px solid var(--slate-200); font-size: 11.5px; color: var(--slate-600);">
              <div>
                <span style="color: var(--slate-400); display: block; font-size: 10px; text-transform: uppercase; font-weight: 700;">Prepared by</span>
                <strong style="color: var(--navy-dark); font-size: 12.5px;">Aditya Sharma</strong>
              </div>
              <div>
                <span style="color: var(--slate-400); display: block; font-size: 10px; text-transform: uppercase; font-weight: 700;">Project Type</span>
                <strong style="color: var(--navy-dark);">Independent PM Investigation</strong>
              </div>
              <div>
                <span style="color: var(--slate-400); display: block; font-size: 10px; text-transform: uppercase; font-weight: 700;">Platform Context</span>
                <span>Naukri.com (Candidate Journey)</span>
              </div>
              <div>
                <span style="color: var(--slate-400); display: block; font-size: 10px; text-transform: uppercase; font-weight: 700;">Date</span>
                <span>November 2026</span>
              </div>
            </div>
            
            <div style="font-size: 10px; color: var(--slate-500); margin-top: 2px;">
              *Independent proposal. Not affiliated with or endorsed by Info Edge / Naukri.com.
            </div>
          </div>
          
          <!-- Right: Visual Conceptual Product Diagram (Candidate -> Library -> Select -> Apply) -->
          <div class="cover-illustration-wrap">
            <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px; color: var(--naukri-blue); margin-bottom: 2px; text-align: center;">
              Conceptual User Flow
            </div>
            
            <!-- Node 1: Candidate Profile -->
            <div style="background: var(--navy-dark); color: white; padding: 10px 14px; border-radius: 8px; text-align: center; box-shadow: var(--shadow-sm);">
              <div style="font-size: 10px; text-transform: uppercase; color: #93C5FD; font-weight: 700;">Single Master Record</div>
              <div style="font-size: 13px; font-weight: 700; margin-top: 2px;">Comprehensive Naukri Profile</div>
              <div style="font-size: 10.5px; color: var(--slate-300);">Education • Experience • Skills • Personal Details</div>
            </div>
            
            <!-- Connector Arrow -->
            <div style="text-align: center; color: var(--naukri-blue); font-size: 14px; font-weight: 700; margin: -4px 0;">↓</div>
            
            <!-- Node 2: Dedicated Resume Library -->
            <div style="background: white; border: 1.5px dashed var(--naukri-blue); border-radius: 8px; padding: 10px 12px; box-shadow: var(--shadow-sm);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 11px; font-weight: 700; color: var(--navy-dark);">📁 Dedicated Resume Library</span>
                <span class="badge badge-blue" style="font-size: 9.5px;">Role-Specific Versions</span>
              </div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
                <div style="background: var(--naukri-blue-light); border: 1.5px solid var(--naukri-blue); border-radius: 6px; padding: 6px 8px;">
                  <div style="font-size: 11px; font-weight: 700; color: var(--navy-dark);">🔘 Product Mgmt CV</div>
                  <div style="font-size: 9.5px; color: var(--naukri-blue); font-weight: 600;">PM_Resume.pdf [Selected]</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 6px 8px; opacity: 0.85;">
                  <div style="font-size: 11px; font-weight: 600; color: var(--slate-700);">⚪ Consulting CV</div>
                  <div style="font-size: 9.5px; color: var(--slate-500);">Consulting.pdf</div>
                </div>
                <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 6px 8px; opacity: 0.85;">
                  <div style="font-size: 11px; font-weight: 600; color: var(--slate-700);">⚪ Operations CV</div>
                  <div style="font-size: 9.5px; color: var(--slate-500);">Ops_Resume.pdf</div>
                </div>
                <div style="background: #F8FAFC; border: 1px dashed var(--slate-300); border-radius: 6px; padding: 6px 8px; text-align: center; display: flex; align-items: center; justify-content: center;">
                  <span style="font-size: 10px; color: var(--naukri-blue); font-weight: 600;">+ Upload New CV</span>
                </div>
              </div>
            </div>
            
            <!-- Connector Arrow -->
            <div style="text-align: center; color: var(--emerald-accent); font-size: 14px; font-weight: 700; margin: -4px 0;">↓</div>
            
            <!-- Node 3: Moment of Apply -->
            <div style="background: #F0FDF4; border: 1.5px solid var(--emerald-accent); border-radius: 8px; padding: 10px 14px;">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                  <div style="font-size: 10px; text-transform: uppercase; color: #166534; font-weight: 700;">Job Application Target</div>
                  <div style="font-size: 12.5px; font-weight: 700; color: #14532D; margin-top: 2px;">Product Manager Intern</div>
                </div>
                <span class="badge badge-teal" style="font-size: 10px;">Attached: PM CV</span>
              </div>
              <div style="font-size: 10px; color: #15803D; margin-top: 4px;">
                ✓ Attached without altering other library versions or master profile
              </div>
            </div>
            
            <div style="text-align: center; font-size: 10.5px; color: var(--slate-500); margin-top: 4px;">
              Candidate Control • Transparent Selection • Non-Destructive Saving
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 1 — Welcome & Proposal Introduction</h4>
        <p>Good morning. My name is Aditya Sharma. Today I am sharing an independent Product Management investigation and proposal for Naukri.com titled <strong>'Apply with the Right Resume'</strong>.</p>
        <p>Job seekers frequently apply across varied roles—such as Product Management, Consulting, Analytics, or Engineering. Tailoring resumes to these distinct opportunities is common practice. However, when it comes to submitting the right document during the job application process, managing and switching between multiple resumes can introduce friction.</p>
        <p>This proposal explores a candidate-controlled <strong>Resume Library</strong> for Naukri.com, enabling candidates to maintain role-specific resumes in one place and choose the appropriate document when applying.</p>
        <div class='cue-box'><strong>Transition:</strong> Let's look at the proposal at a glance—its problem signals, research foundation, and proposed scope.</div>
        """
    },

    # SLIDE 02: THE PROPOSAL AT A GLANCE
    {
        "id": "slide-2",
        "number": "02",
        "stage": "Discover",
        "tag": "Executive Briefing",
        "evidenceType": "Proposed Solution",
        "title": "What This Investigation Is About",
        "subtitle": "Executive summary of problem signals, exploratory research, platform opportunity, and proposed validation",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- 6 Facet Grid -->
          <div class="grid-3" style="flex: 1; gap: 12px;">
            <!-- Facet 1: Problem Signal -->
            <div class="card card-tinted" style="border-top: 3px solid var(--slate-600);">
              <div class="card-header-sm">
                <span>01. Problem Signal</span>
                <span class="evidence-tag evidence-tag-obs">Personal Obs</span>
              </div>
              <div class="card-title-lg">Multi-Track Applications</div>
              <p class="card-text" style="font-size: 11.5px;">
                Candidates maintain multiple resume versions tailored to distinct roles. Tailoring documents is normal, but managing them across portal journeys requires effort.
              </p>
            </div>
            
            <!-- Facet 2: Candidate Difficulty -->
            <div class="card card-tinted" style="border-top: 3px solid var(--rose-accent);">
              <div class="card-header-sm">
                <span>02. Candidate Friction</span>
                <span class="evidence-tag evidence-tag-hypo">Hypothesis</span>
              </div>
              <div class="card-title-lg">Application Interruption</div>
              <p class="card-text" style="font-size: 11.5px;">
                When the resume to be submitted differs from the profile-attached file, candidates may need to leave the apply flow or repeatedly replace their active document.
              </p>
            </div>
            
            <!-- Facet 3: Research Signal -->
            <div class="card card-tinted" style="border-top: 3px solid var(--amber-accent);">
              <div class="card-header-sm">
                <span>03. User Evidence</span>
                <span class="evidence-tag evidence-tag-survey">N=45 Survey</span>
              </div>
              <div class="card-title-lg">Exploratory Signal</div>
              <p class="card-text" style="font-size: 11.5px;">
                In an exploratory survey of 45 college students, <strong>90%</strong> maintain multiple resumes, and <strong>90%</strong> frequently need an alternate CV during applications.
              </p>
            </div>
            
            <!-- Facet 4: Product Opportunity -->
            <div class="card card-tinted" style="border-top: 3px solid var(--naukri-blue);">
              <div class="card-header-sm">
                <span>04. Opportunity</span>
                <span class="evidence-tag evidence-tag-sol">Proposal</span>
              </div>
              <div class="card-title-lg">Persistent Resume Library</div>
              <p class="card-text" style="font-size: 11.5px;">
                A unified, candidate-controlled library within one Naukri profile, paired with application-time selection and optional non-destructive saving.
              </p>
            </div>
            
            <!-- Facet 5: Deliverables Built -->
            <div class="card card-tinted" style="border-top: 3px solid var(--teal-accent);">
              <div class="card-header-sm">
                <span>05. Concrete Output</span>
                <span class="evidence-tag evidence-tag-sol">Deliverable</span>
              </div>
              <div class="card-title-lg">PRD & Working Prototype</div>
              <p class="card-text" style="font-size: 11.5px;">
                Complete end-to-end decision logic, MoSCoW prioritized requirements, and a client-side simulated candidate journey prototype testing all scenarios.
              </p>
            </div>
            
            <!-- Facet 6: Validation Next Step -->
            <div class="card card-tinted" style="border-top: 3px solid var(--emerald-accent);">
              <div class="card-header-sm">
                <span>06. Proposed Next Step</span>
                <span class="evidence-tag evidence-tag-val">Naukri Input</span>
              </div>
              <div class="card-title-lg">Internal Flow Validation</div>
              <p class="card-text" style="font-size: 11.5px;">
                Invite Naukri Product Leadership to assess candidate drop-off patterns across application types and evaluate feasibility of an on-platform pilot.
              </p>
            </div>
          </div>
          
          <!-- Evidence Rigor Bar -->
          <div class="card card-blue" style="padding: 10px 14px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
            <div style="font-size: 11.5px; color: var(--navy-dark); line-height: 1.4;">
              <strong>Disciplined Product Stance:</strong> This proposal establishes a credible candidate-side opportunity. It does not claim to have proven platform-wide demand, nor does it assert universal technical limitations without access to internal Naukri product data.
            </div>
            <span class="badge badge-gray" style="font-size: 10px;">Independent Investigation</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 2 — Executive Briefing: The Proposal at a Glance</h4>
        <p>This slide provides a high-level summary across six key dimensions of the investigation:</p>
        <ul>
          <li><strong>Problem Signal:</strong> Job seekers pursuing varied roles routinely tailor resumes.</li>
          <li><strong>Candidate Friction:</strong> Switching documents during an active application flow can disrupt momentum.</li>
          <li><strong>Research Signal:</strong> Our exploratory survey of 45 college students showed that 90% maintain multiple resumes and 80% apply across 3 or more role categories.</li>
          <li><strong>The Opportunity:</strong> A persistent Resume Library with moment-of-apply selection and non-destructive saving.</li>
          <li><strong>The Proposed Deliverables:</strong> A prioritized PRD, edge-case decision trees, and a working client-side prototype.</li>
          <li><strong>Next Steps:</strong> We explicitly treat this as a proposal inviting collaboration and validation from Naukri's product team.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's examine the structured Product Management lifecycle that guided this work.</div>
        """
    },

    # SLIDE 03: PRODUCT MANAGEMENT APPROACH
    {
        "id": "slide-3",
        "number": "03",
        "stage": "Discover",
        "tag": "Product Process",
        "evidenceType": "Proposed Solution",
        "title": "From Problem Discovery to Product Recommendation",
        "subtitle": "A structured, iterative Product Management lifecycle guiding this independent investigation",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Lifecycle Linear Stage Diagram -->
          <div class="card" style="padding: 12px 14px;">
            <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 8px;">
              The 9-Stage Product Discovery & Delivery Lifecycle
            </div>
            
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 6px;">
              <div class="stage-step active" style="font-size: 10.5px; padding: 4px 8px;">1. Discover</div>
              <span class="stage-arrow">→</span>
              <div class="stage-step" style="font-size: 10.5px; padding: 4px 8px; background: #E2E8F0; color: #1E293B;">2. Define</div>
              <span class="stage-arrow">→</span>
              <div class="stage-step" style="font-size: 10.5px; padding: 4px 8px; background: #E2E8F0; color: #1E293B;">3. Research</div>
              <span class="stage-arrow">→</span>
              <div class="stage-step" style="font-size: 10.5px; padding: 4px 8px; background: #E2E8F0; color: #1E293B;">4. Validate</div>
              <span class="stage-arrow">→</span>
              <div class="stage-step" style="font-size: 10.5px; padding: 4px 8px; background: #E2E8F0; color: #1E293B;">5. Diagnose</div>
              <span class="stage-arrow">→</span>
              <div class="stage-step" style="font-size: 10.5px; padding: 4px 8px; background: #E2E8F0; color: #1E293B;">6. Assess</div>
              <span class="stage-arrow">→</span>
              <div class="stage-step" style="font-size: 10.5px; padding: 4px 8px; background: #E2E8F0; color: #1E293B;">7. Design</div>
              <span class="stage-arrow">→</span>
              <div class="stage-step" style="font-size: 10.5px; padding: 4px 8px; background: #E2E8F0; color: #1E293B;">8. Test</div>
              <span class="stage-arrow">→</span>
              <div class="stage-step" style="font-size: 10.5px; padding: 4px 8px; background: #E2E8F0; color: #1E293B;">9. Deliver</div>
            </div>
          </div>
          
          <!-- Lifecycle Stage Breakdown Grid -->
          <div class="grid-3" style="flex: 1; gap: 10px;">
            <div class="card card-tinted" style="padding: 10px 12px;">
              <div style="font-weight: 700; font-size: 11.5px; color: var(--navy-dark); margin-bottom: 2px;">Stage 1–3: Discovery & Research</div>
              <ul style="font-size: 10.5px; color: var(--slate-600); padding-left: 14px; line-height: 1.4;">
                <li><strong>Discover:</strong> Identify initial firsthand problem observation.</li>
                <li><strong>Define:</strong> Articulate user needs, Job-to-be-Done & scope boundaries.</li>
                <li><strong>Research:</strong> Design survey questions, respondent criteria & methodology.</li>
              </ul>
            </div>
            
            <div class="card card-tinted" style="padding: 10px 12px;">
              <div style="font-weight: 700; font-size: 11.5px; color: var(--navy-dark); margin-bottom: 2px;">Stage 4–6: Validation & Assessment</div>
              <ul style="font-size: 10.5px; color: var(--slate-600); padding-left: 14px; line-height: 1.4;">
                <li><strong>Validate:</strong> Separate established signals from unverified questions.</li>
                <li><strong>Diagnose:</strong> Analyze symptoms vs. 5 root-cause hypotheses.</li>
                <li><strong>Assess:</strong> Benchmark competitors & compare 5 strategic options.</li>
              </ul>
            </div>
            
            <div class="card card-tinted" style="padding: 10px 12px;">
              <div style="font-weight: 700; font-size: 11.5px; color: var(--navy-dark); margin-bottom: 2px;">Stage 7–9: Design, Test & Next Steps</div>
              <ul style="font-size: 10.5px; color: var(--slate-600); padding-left: 14px; line-height: 1.4;">
                <li><strong>Design:</strong> Formulate 3 pillars, UX flows, decision logic & PRD.</li>
                <li><strong>Test:</strong> Build client-side simulator & design controlled A/B experiment.</li>
                <li><strong>Deliver:</strong> Plan rollout, risk mitigations & invite Naukri PM feedback.</li>
              </ul>
            </div>
          </div>
          
          <div style="background: var(--slate-100); padding: 8px 12px; border-radius: 4px; font-size: 11px; color: var(--slate-600); text-align: center;">
            <em>Note: Product Discovery and Delivery are inherently iterative. Insights gained during competitor benchmarking and prototyping continuously refined our problem definition and PRD scope.</em>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 3 — The Product Management Lifecycle</h4>
        <p>Rather than jumping straight to a mockup or a feature pitch, this project adheres to a disciplined Product Management lifecycle:</p>
        <ul>
          <li>We start with the initial observation and define the Job-to-be-Done before running user research.</li>
          <li>Crucially, we include a dedicated validation step to separate what the survey actually establishes from what remains unverified without internal Naukri data.</li>
          <li>We conduct root-cause diagnosis and evaluate multiple product alternatives before detailing our recommended Resume Library concept.</li>
          <li>Finally, we define the PRD, testable acceptance criteria, controlled experiment metrics, and risk mitigations.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's examine how this project began with a personal application experience.</div>
        """
    },

    # SLIDE 04: PROBLEM IDENTIFICATION
    {
        "id": "slide-4",
        "number": "04",
        "stage": "Discover",
        "tag": "Problem Discovery",
        "evidenceType": "Personal Observation",
        "title": "Where the Idea Started",
        "subtitle": "Firsthand observation: applying across multiple role tracks within portal application journeys",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 14px;">
          <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 16px; flex: 1;">
            <!-- Left: First-Person Account & Context -->
            <div class="card card-tinted" style="padding: 16px 20px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div class="card-header-sm">
                  <span>Firsthand Problem Signal</span>
                  <span class="evidence-tag evidence-tag-obs">Personal Observation</span>
                </div>
                
                <div style="font-size: 14px; color: var(--navy-dark); font-weight: 600; line-height: 1.5; margin-bottom: 12px;">
                  "This proposal began with my own experience of applying across different role categories. I maintained different resume versions for different opportunities. When the document I wanted to submit differed from the resume associated with my profile, managing the change could add steps to the application process in the flow I encountered."
                </div>
                
                <p class="card-text" style="font-size: 12px; margin-bottom: 8px;">
                  Like many candidates exploring campus placements or diverse career tracks, I found myself preparing distinct presentations of my background:
                </p>
                <ul style="font-size: 11.5px; color: var(--slate-700); padding-left: 16px; line-height: 1.45;">
                  <li>A <strong>Product Management CV</strong> highlighting case competitions, wireframes, and metrics.</li>
                  <li>A <strong>Consulting CV</strong> highlighting market sizing, structured problem solving, and modeling.</li>
                  <li>An <strong>Operations CV</strong> emphasizing process workflows and logistics.</li>
                  <li>A <strong>Core Tech CV</strong> emphasizing software development and data structures.</li>
                </ul>
              </div>
              
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 10px 12px; font-size: 11px; color: var(--slate-600); margin-top: 10px;">
                <strong>Classification:</strong> This observation represents the initial spark of inquiry. It highlighted that document management at application time deserves systematic investigation.
              </div>
            </div>
            
            <!-- Right: The 3 Underlying Realities -->
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div class="card" style="padding: 12px 14px;">
                <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-bottom: 3px;">
                  1. Multiple Professional Stories
                </div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                  A single resume cannot optimally emphasize technical depth, analytical frameworks, and product leadership simultaneously.
                </div>
              </div>
              
              <div class="card" style="padding: 12px 14px;">
                <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-bottom: 3px;">
                  2. Role-Specific Job Matching
                </div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                  Recruiters look for specific keyword alignments and relevant project highlights tailored to their specific job description.
                </div>
              </div>
              
              <div class="card" style="padding: 12px 14px;">
                <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-bottom: 3px;">
                  3. Moment-of-Apply Friction
                </div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                  When an active job posting requires an alternate version, having to leave the flow or replace active profile documents risks abandonment or confusion.
                </div>
              </div>
            </div>
          </div>
          
          <div style="background: var(--amber-light); border: 1px solid var(--amber-border); padding: 8px 14px; border-radius: 4px; font-size: 11px; color: #92400E; display: flex; align-items: center; justify-content: space-between;">
            <span><strong>Research Boundary:</strong> A personal observation is a hypothesis, not proof of platform-wide defect. This prompted our exploratory user survey to see if other candidates experience similar needs.</span>
            <span class="evidence-tag evidence-tag-obs">Signal Origin</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 4 — Problem Identification & Personal Observation</h4>
        <p>Every genuine product investigation starts with an authentic observation. Here is how this project began:</p>
        <ul>
          <li>During my own job search across placement season, I prepared distinct resumes tailored to APM, Consulting, and Technical roles.</li>
          <li>When applying for a specific job that required an alternate resume, navigating away to update the profile-attached file felt like an unnecessary interruption.</li>
          <li>However, in professional Product Management, one person's experience is merely an anecdote. It cannot be presented as a universal defect or proof of widespread platform failure.</li>
          <li>Therefore, this firsthand experience served as the catalyst to design an exploratory survey and investigate competitor paradigms.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's define who experiences this problem and inspect a representative candidate scenario.</div>
        """
    },

    # SLIDE 05: WHO EXPERIENCES THE PROBLEM?
    {
        "id": "slide-5",
        "number": "05",
        "stage": "Define",
        "tag": "Target Cohort",
        "evidenceType": "Survey Finding",
        "title": "Understanding the Candidate Context",
        "subtitle": "Multi-track job seekers, early-career candidates, and cross-functional role seekers",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; flex: 1;">
            <!-- Left: Primary Target Segment -->
            <div class="card" style="border-left: 4px solid var(--naukri-blue); padding: 14px 18px; display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Primary Segment (Survey-Supported)</span>
                <span class="evidence-tag evidence-tag-survey">N=45 Cohort</span>
              </div>
              <div style="font-size: 14px; font-weight: 700; color: var(--navy-dark); margin-bottom: 6px;">
                College Students & Early-Career Multi-Track Seekers
              </div>
              <p class="card-text" style="font-size: 11.5px; margin-bottom: 10px;">
                Candidates entering placement seasons or early job searches who actively explore several functional career paths concurrently:
              </p>
              
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 10px;">
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px; font-size: 11px;">
                  💼 <strong>Product Management</strong>
                  <div style="font-size: 9.5px; color: var(--slate-500);">APM, Tech Analyst</div>
                </div>
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px; font-size: 11px;">
                  📊 <strong>Strategy & Consulting</strong>
                  <div style="font-size: 9.5px; color: var(--slate-500);">Analyst, Research</div>
                </div>
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px; font-size: 11px;">
                  ⚙️ <strong>Business Operations</strong>
                  <div style="font-size: 9.5px; color: var(--slate-500);">Supply Chain, Ops</div>
                </div>
                <div style="background: var(--slate-50); border: 1px solid var(--slate-200); padding: 6px 8px; border-radius: 4px; font-size: 11px;">
                  💻 <strong>Core Engineering</strong>
                  <div style="font-size: 9.5px; color: var(--slate-500);">Software, Data Eng</div>
                </div>
              </div>
              
              <div style="margin-top: auto; background: var(--naukri-blue-light); padding: 8px 10px; border-radius: 4px; font-size: 10.5px; color: var(--navy-dark);">
                <strong>Behavioral Reality:</strong> 80% of our surveyed student cohort reported applying across 3 or more distinct role types simultaneously.
              </div>
            </div>
            
            <!-- Right: Candidate Scenario & Secondary Segment Note -->
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <!-- Realistic Candidate Scenario -->
              <div class="card card-tinted" style="padding: 12px 14px; flex: 1;">
                <div class="card-header-sm">
                  <span>Illustrative Candidate Scenario</span>
                  <span class="badge badge-gray">Demo Persona</span>
                </div>
                <div style="font-size: 12.5px; font-weight: 700; color: var(--navy-dark); margin-bottom: 2px;">
                  Sample Candidate • Final-Year Engineering & Analytics Student
                </div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.45; margin-top: 4px;">
                  <em>"I am open to Associate Product Manager roles, Business Analyst roles at consulting firms, and Business Operations positions. I have 3 polished resumes tailored with specific keywords and projects. When I see a great APM job on Naukri, I want to submit my PM resume immediately without altering my profile's default document."</em>
                </div>
              </div>
              
              <!-- Secondary Segment (Hypothesis) -->
              <div class="card" style="border-left: 3px solid var(--slate-400); padding: 10px 14px;">
                <div class="card-header-sm">
                  <span>Secondary Segment (Potential)</span>
                  <span class="evidence-tag evidence-tag-hypo">Requires Validation</span>
                </div>
                <div style="font-weight: 700; font-size: 11.5px; color: var(--slate-700);">
                  Mid-Career Professionals Across Functions
                </div>
                <div style="font-size: 10.5px; color: var(--slate-500); line-height: 1.35; margin-top: 2px;">
                  Experienced candidates seeking cross-functional moves (e.g. Technical Program Manager vs. Strategy Director). <em>Note: Not represented in our 45-student survey; requires distinct professional cohort validation.</em>
                </div>
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 5 — Target Users & Candidate Context</h4>
        <p>Who experiences this problem?</p>
        <ul>
          <li>Our exploratory research directly captures college students and early-career seekers. 80% of respondents in our sample were looking for placement or full-time roles, and 20% for internships.</li>
          <li>Early-career job seekers often apply broadly across Product, Consulting, Operations, and Core Tech to maximize employment opportunities.</li>
          <li>We present a realistic candidate persona based on this scenario.</li>
          <li>Importantly, we note that mid-career working professionals may also experience this need, but we strictly classify that as a hypothesis requiring separate research.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's define the exact Job-to-be-Done and formal problem statement.</div>
        """
    },

    # SLIDE 06: PROBLEM DEFINITION
    {
        "id": "slide-6",
        "number": "06",
        "stage": "Define",
        "tag": "Problem Scoping",
        "evidenceType": "Proposed Solution",
        "title": "Defining the Actual Candidate Problem",
        "subtitle": "Establishing the Job-to-be-Done (JTBD), core problem statement, and scope boundaries",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 14px;">
          <!-- Top: Job-to-be-Done Anchor -->
          <div class="card card-blue" style="padding: 14px 18px; border-left: 4px solid var(--naukri-blue);">
            <div style="font-size: 10.5px; font-weight: 800; text-transform: uppercase; color: var(--naukri-blue); letter-spacing: 0.8px; margin-bottom: 4px;">
              The Job-to-be-Done (JTBD)
            </div>
            <div style="font-size: 15px; font-weight: 700; color: var(--navy-dark); line-height: 1.45;">
              "When I apply to different types of roles, I want to choose the resume that best represents my relevant experience while keeping my other versions intact, so I can submit the document I intend without repeatedly managing profile files."
            </div>
          </div>
          
          <!-- Middle: Formal Problem Statement & 4-Box Framing -->
          <div class="grid-4" style="flex: 1; gap: 10px;">
            <div class="card card-tinted" style="padding: 10px 12px;">
              <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500);">1. Target User</div>
              <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-top: 3px;">Multi-Track Applicant</div>
              <p style="font-size: 11px; color: var(--slate-600); margin-top: 4px; line-height: 1.35;">
                Candidates who maintain multiple role-specific resume documents.
              </p>
            </div>
            
            <div class="card card-tinted" style="padding: 10px 12px;">
              <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500);">2. Trigger Situation</div>
              <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-top: 3px;">Active Job Discovery</div>
              <p style="font-size: 11px; color: var(--slate-600); margin-top: 4px; line-height: 1.35;">
                Finding an attractive role on Naukri that requires an alternate resume version.
              </p>
            </div>
            
            <div class="card card-tinted" style="padding: 10px 12px;">
              <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500);">3. Core Need</div>
              <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-top: 3px;">In-Flow Selection</div>
              <p style="font-size: 11px; color: var(--slate-600); margin-top: 4px; line-height: 1.35;">
                Selecting or uploading the right document without leaving the application.
              </p>
            </div>
            
            <div class="card card-tinted" style="padding: 10px 12px;">
              <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500);">4. Desired Outcome</div>
              <div style="font-weight: 700; font-size: 12px; color: var(--navy-dark); margin-top: 3px;">Confident Submission</div>
              <p style="font-size: 11px; color: var(--slate-600); margin-top: 4px; line-height: 1.35;">
                Submitting the intended file with zero accidental overwriting and full traceability.
              </p>
            </div>
          </div>
          
          <!-- Bottom: Problem Statement & Explicit Boundary -->
          <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 12px;">
            <div class="card" style="padding: 10px 14px; border-left: 3px solid var(--emerald-accent);">
              <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: #166534; margin-bottom: 2px;">
                Formal Problem Statement
              </div>
              <div style="font-size: 11.5px; color: var(--slate-800); line-height: 1.4;">
                "Candidates who maintain multiple role-specific resumes need a simple and reliable way to select the intended document during supported job application flows, without repeatedly replacing or losing access to other versions."
              </div>
            </div>
            
            <div class="card card-tinted" style="padding: 10px 14px;">
              <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--rose-accent); margin-bottom: 2px;">
                Explicit Problem Scope Boundary
              </div>
              <div style="font-size: 10.5px; color: var(--slate-600); line-height: 1.35;">
                This investigation solves <strong>document storage, versioning, and selection</strong>. It explicitly excludes AI resume writing, automated bullet rewriting, and automated matching.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 6 — Problem Definition & Scoping</h4>
        <p>Clear problem definition is essential before designing any product solution:</p>
        <ul>
          <li><strong>Job-to-be-Done:</strong> The candidate wants to choose the resume that best represents their experience while keeping other versions intact.</li>
          <li><strong>The Problem Statement:</strong> Focuses specifically on having a reliable way to select the intended resume during supported application flows without repeatedly replacing profile documents.</li>
          <li><strong>Scope Discipline:</strong> We draw a sharp line here. This is NOT an AI resume writer or automated bullet generator. Confusing document management with content generation leads to bloated scope.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's look at how we designed our exploratory research to investigate this candidate need.</div>
        """
    }
]
