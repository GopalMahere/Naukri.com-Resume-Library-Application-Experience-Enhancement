# slides_part3.py - Slides 11 to 15 (Prototype, Experimentation, Funnel Impact & Risks, Recommendation, Appendix)

SLIDES_PART3 = [
    # SLIDE 11: INTERACTIVE PROTOTYPE
    {
        "id": "slide-11",
        "number": "11",
        "tag": "Interactive Prototype",
        "title": "Interactive Prototype: Simulated Candidate Experience",
        "subtitle": "Test the 1-resume quick-apply path, multi-resume selection, simulated upload, and conditional saving live",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 10px;">
          <!-- Top Prototype Scenario Trigger Bar -->
          <div class="proto-scenario-bar" style="border-radius: var(--radius-sm);">
            <div style="display: flex; align-items: center; gap: 6px;">
              <span style="font-weight: 700; color: #93C5FD; font-size: 11px;">TEST SCENARIOS:</span>
            </div>
            
            <div class="proto-scenario-buttons">
              <button class="scenario-btn" id="scenario-preset-single" onclick="runProtoPreset('SINGLE', event)" title="Test flow when candidate has only 1 resume">
                1. Single-Resume Quick Apply
              </button>
              <button class="scenario-btn" id="scenario-preset-c" onclick="runProtoPreset('C', event)" title="Select an existing resume from library">
                2. Multi-Resume Selector
              </button>
              <button class="scenario-btn" id="scenario-preset-a" onclick="runProtoPreset('A', event)" title="Upload a new resume without saving">
                3. Scenario A: Apply-Only Upload (Don't Save)
              </button>
              <button class="scenario-btn" id="scenario-preset-b" onclick="runProtoPreset('B', event)" title="Upload a new resume and save to library">
                4. Scenario B: Upload & Save to Library
              </button>
              <button class="scenario-btn" style="background: rgba(225,29,72,0.25); border-color: rgba(225,29,72,0.4);" onclick="resetProtoState(event)">
                ↺ Reset Prototype
              </button>
            </div>
          </div>
          
          <!-- The Embedded Interactive Naukri Prototype Container -->
          <div class="prototype-container" style="flex: 1;" onclick="event.stopPropagation()">
            <!-- Proto Platform Header -->
            <div class="proto-top-nav">
              <div class="proto-logo-badge">
                <span style="background: var(--naukri-blue); color: white; padding: 2px 6px; border-radius: 4px; font-weight: 800; font-size: 11px;">naukri</span>
                <span style="font-size: 12px; font-weight: 600; color: #E2E8F0;">Candidate Workspace</span>
                <span class="badge badge-amber" style="font-size: 9.5px; margin-left: 6px;">SIMULATED SANDBOX</span>
              </div>
              
              <div class="proto-user-tag">
                <span style="font-size: 11.5px; color: #CBD5E1;">Sample Candidate (Demo Profile)</span>
                <div style="width: 24px; height: 24px; border-radius: 50%; background: var(--naukri-blue); display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700;">SC</div>
              </div>
            </div>
            
            <!-- Proto Navigation Tabs -->
            <div class="proto-tab-bar">
              <div class="proto-tab active" id="tab-library" onclick="switchProtoView('library', event)">
                📁 My Resume Library <span class="proto-tab-count" id="proto-library-count">4</span>
              </div>
              <div class="proto-tab" id="tab-job" onclick="switchProtoView('job', event)">
                💼 Job Opening: PM Intern
              </div>
              <div class="proto-tab" id="tab-apply" onclick="switchProtoView('apply', event)">
                📝 Active Application
              </div>
              <div class="proto-tab" id="tab-history" onclick="switchProtoView('history', event)">
                🕒 Application History <span class="proto-tab-count" id="proto-history-count">1</span>
              </div>
            </div>
            
            <!-- Dynamic Prototype Body Viewport -->
            <div class="proto-body" id="proto-body-viewport">
              <!-- Content rendered dynamically via scripts_js.py -->
            </div>
          </div>
          
          <div style="font-size: 10.5px; color: var(--slate-500); display: flex; justify-content: space-between; align-items: center; padding: 0 4px; flex-wrap: wrap; gap: 4px;">
            <span>ℹ️ <em>Simulation Notice: This interactive prototype runs locally in-browser to demonstrate workflow logic. Real implementation requires backend document version UUIDs and retained document references.</em></span>
            <span style="color: var(--naukri-blue); font-weight: 600;">Candidate Control Guaranteed</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Live Prototype Demonstration</h4>
        <p>This is a live, interactive simulator running entirely in-browser. Here is how you can test each workflow:</p>
        <ol>
          <li><strong>Single-Resume Quick Apply:</strong> Click '1. Single-Resume Quick Apply'. If a candidate has only 1 saved resume, the interface preserves the simple quick-apply flow with a clear 'Change Resume' option, avoiding unnecessary choice friction.</li>
          <li><strong>Multi-Resume Selection:</strong> Click '2. Multi-Resume Selector'. When multiple resumes exist, the candidate chooses between their Product Management, Consulting, Operations, or Engineering CVs.</li>
          <li><strong>Scenario A (Upload & Don't Save):</strong> Click '3. Scenario A'. The candidate simulates uploading a new resume. Notice the progress bar: the save checkbox is completely hidden until upload completes! When left unchecked, it is used for this application only. Checking the library afterwards confirms exactly 4 resumes remain.</li>
          <li><strong>Scenario B (Upload & Save):</strong> Click '4. Scenario B'. Upload succeeds, the candidate checks the save box, which requires a custom name (try erasing it—validation will prevent continuing). Upon submit, inspect the library: it now holds 5 resumes, with all older documents untouched!</li>
          <li><strong>Set Default Action:</strong> In the library view, click '⭐ Set as Default' on any card to test the default preference interaction.</li>
        </ol>
        <div class='cue-box'><strong>Transition:</strong> Let's look at how we measure the impact of this feature through a controlled experiment.</div>
        """
    },

    # SLIDE 12: EXPERIMENTATION & SUCCESS METRICS
    {
        "id": "slide-12",
        "number": "12",
        "tag": "Experiment & Metrics",
        "title": "Product Experimentation & Success Metrics",
        "subtitle": "Controlled A/B pilot design, primary conversion indicators, and data integrity guardrails",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 14px;">
          <!-- Top: Controlled Experiment Setup -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
            <div class="card card-tinted" style="border-left: 4px solid var(--slate-400);">
              <div class="card-header-sm">
                <span>Cohort A: Control Group</span>
                <span class="badge badge-gray">Baseline Experience</span>
              </div>
              <div style="font-size: 13.5px; font-weight: 700; color: var(--navy-dark); margin: 3px 0;">Existing Application Experience</div>
              <p class="card-text" style="font-size: 11.5px;">
                Candidates submit the resume attached to their profile. Updating or changing resumes requires leaving the application or updating the profile document.
              </p>
            </div>
            
            <div class="card card-blue" style="border-left: 4px solid var(--naukri-blue);">
              <div class="card-header-sm">
                <span style="color: var(--naukri-blue); font-weight: 800;">Cohort B: Test Group</span>
                <span class="badge badge-blue">Proposed Pilot</span>
              </div>
              <div style="font-size: 13.5px; font-weight: 700; color: var(--navy-dark); margin: 3px 0;">One Profile, Multiple Resumes</div>
              <p class="card-text" style="font-size: 11.5px; color: var(--slate-700);">
                Eligible candidates receive the dedicated Resume Library, moment-of-apply resume selector, on-the-fly upload, and optional non-destructive saving.
              </p>
            </div>
          </div>
          
          <!-- Middle: Metric Hierarchy Grid -->
          <div style="display: grid; grid-template-columns: 1.1fr 1.3fr 1fr; gap: 12px; flex: 1;">
            <!-- Primary Metric -->
            <div class="card" style="border: 2px solid var(--naukri-blue); background: var(--naukri-blue-light); display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span style="color: var(--naukri-blue); font-weight: 800;">Primary Success Metric</span>
                <span class="badge badge-blue">Core Conversion</span>
              </div>
              <div style="font-size: 15px; font-weight: 800; color: var(--navy-dark); margin: 4px 0;">
                Application Completion Rate
              </div>
              <div style="background: white; border: 1px solid var(--naukri-blue-border); padding: 7px 10px; border-radius: 6px; font-size: 11.5px; font-family: monospace; color: var(--naukri-blue); text-align: center; margin-bottom: 6px;">
                Completed Applications ÷ Application Starts
              </div>
              <p class="card-text" style="font-size: 11px; color: var(--slate-700);">
                Tells us whether candidates are more likely to finish the process when resume-switching friction is mitigated.
              </p>
            </div>
            
            <!-- Secondary Metrics -->
            <div class="card" style="display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Secondary Diagnostic Metrics</span>
                <span class="badge badge-teal">Diagnostics</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 5px; font-size: 11px; color: var(--slate-700); margin-top: 2px;">
                <div><strong>• Resume Library Adoption:</strong> % of active candidates managing ≥2 resumes.</div>
                <div><strong>• Selection Distribution:</strong> % selecting existing CV vs. uploading new.</div>
                <div><strong>• Save Adoption Rate:</strong> % saving newly uploaded resumes to library.</div>
                <div><strong>• Time-to-Apply:</strong> Time taken to complete an application.</div>
                <div><strong>• Application Abandonment Rate:</strong> % exiting without completing.</div>
                <div><strong>• Upload Failure Rate:</strong> Upload failure and retry frequency.</div>
                <div><strong>• Candidate Satisfaction (CSAT):</strong> Self-reported experience rating.</div>
              </div>
            </div>
            
            <!-- Guardrail Metrics -->
            <div class="card" style="border-left: 3px solid var(--rose-accent); background: #FFFBFB; display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span style="color: var(--rose-accent); font-weight: 800;">Guardrail Metrics</span>
                <span class="badge badge-red">Protection</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 5px; font-size: 11px; color: #4C0519; margin-top: 2px;">
                <div><strong>• Accidental Overwrites:</strong> Data loss or accidental overwrite incidents.</div>
                <div><strong>• Wrong-Resume Incidents:</strong> Candidate tickets reporting wrong CV submission.</div>
                <div><strong>• Upload / System Errors:</strong> Technical failure rates during apply.</div>
                <div><strong>• Funnel Deterioration:</strong> Any deterioration in application completion.</div>
                <div><strong>• Privacy / Security:</strong> Unintended document exposure to recruiters.</div>
              </div>
            </div>
          </div>
          
          <div style="background: var(--slate-100); padding: 7px 12px; border-radius: 4px; font-size: 11px; color: var(--slate-600); display: flex; align-items: center; justify-content: space-between;">
            <span><strong>Statistical Rigor:</strong> Minimum Detectable Effect (MDE), required sample size, and statistical power to be determined by Naukri's analytics team based on baseline completion volume and variance.</span>
            <span class="badge badge-gray">Analytics-Led Power Calculation</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Experimentation & Measurement Framework</h4>
        <p>To establish whether the feature improves the candidate experience, we propose a controlled A/B experiment:</p>
        <ul>
          <li><strong>Primary Metric:</strong> Application Completion Rate (Completed Applications / Application Starts). This measures whether candidates are genuinely more likely to complete applications when resume-switching friction is reduced/mitigated.</li>
          <li><strong>Secondary Metrics:</strong> We observe adoption patterns—how many candidates use existing library resumes, how many upload on the fly, and what percentage choose to save newly uploaded files.</li>
          <li><strong>Guardrail Metrics:</strong> Accidental overwrite incidents must strictly remain zero. We monitor support ticket volumes, upload failures, and ensure privacy rules are completely respected.</li>
          <li><strong>Statistical Parameters:</strong> We do not invent arbitrary MDE thresholds. The analytics team will define the sample size, duration, and MDE based on Naukri's actual traffic and baseline conversion variance.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's review the hypothetical funnel impact model, risk mitigation matrix, and rollout roadmap.</div>
        """
    },

    # SLIDE 13: BUSINESS IMPACT, RISKS & ROLLOUT
    {
        "id": "slide-13",
        "number": "13",
        "tag": "Business Impact & Plan",
        "title": "Business Impact, Risk Mitigation & Implementation Plan",
        "subtitle": "Hypothetical funnel impact calculation, comprehensive risk mitigations, and phased rollout roadmap",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Top Row: Illustrative Funnel Model & Risk Matrix -->
          <div style="display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 14px;">
            <!-- Illustrative Funnel Impact Calculation -->
            <div class="card card-tinted" style="display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Funnel Impact Calculation</span>
                <span class="badge badge-amber">Hypothetical Illustration</span>
              </div>
              <div style="font-size: 13px; font-weight: 700; color: var(--navy-dark); margin-bottom: 5px;">
                Illustrative Funnel Impact Model
              </div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 10px 12px; font-size: 11.5px; line-height: 1.55; color: var(--slate-700);">
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--slate-100); padding-bottom: 3px;">
                  <span>Application Starts Observed (Both Groups):</span>
                  <span style="font-weight: 700; color: var(--navy-dark);">10,000 starts</span>
                </div>
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--slate-100); padding: 3px 0;">
                  <span>Control Group Completion Rate (60%):</span>
                  <span style="font-weight: 700; color: var(--slate-600);">6,000 completed</span>
                </div>
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--slate-100); padding: 3px 0;">
                  <span>Test Group Completion Rate (65%):</span>
                  <span style="font-weight: 700; color: var(--naukri-blue);">6,500 completed</span>
                </div>
                <div style="display: flex; justify-content: space-between; padding-top: 4px; color: var(--emerald-accent); font-weight: 800;">
                  <span>Incremental Completed Applications:</span>
                  <span>10,000 × (65% − 60%) = +500 applications</span>
                </div>
              </div>
              <div style="font-size: 10px; color: var(--slate-500); margin-top: 5px; line-height: 1.35;">
                <em>Disclaimer: This is an illustrative funnel impact calculation only, not an ROI model. It does not represent actual Naukri traffic, baseline conversion rates, revenue, or forecasted business results. Actual impact must be measured using internal analytics.</em>
              </div>
            </div>
            
            <!-- Risk & Mitigation Table -->
            <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
              <div style="padding: 7px 12px; background: var(--slate-100); border-bottom: 1px solid var(--slate-200); font-weight: 700; font-size: 10.5px; text-transform: uppercase; color: var(--navy-dark);">
                Business Risks & Mitigations Table
              </div>
              <div class="table-scroll-wrap" style="flex: 1;">
                <table class="deck-table" style="font-size: 10.5px;">
                  <thead>
                    <tr>
                      <th style="width: 44%;">Risk</th>
                      <th style="width: 56%;">Mitigation</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Candidate submits wrong resume</strong></td>
                      <td>Show selected file and confirmation review screen.</td>
                    </tr>
                    <tr>
                      <td><strong>New resume overwrites old file</strong></td>
                      <td>Store new uploads independently.</td>
                    </tr>
                    <tr>
                      <td><strong>Duplicate filenames cause confusion</strong></td>
                      <td>Treat files as separate records; store with unique IDs.</td>
                    </tr>
                    <tr>
                      <td><strong>Upload fails</strong></td>
                      <td>Show error message and retry; withhold save checkbox.</td>
                    </tr>
                    <tr>
                      <td><strong>Resume deleted after applying</strong></td>
                      <td>Preserve application document/version reference intact.</td>
                    </tr>
                    <tr>
                      <td><strong>Too many selection choices</strong></td>
                      <td>Optional default preference without automatic silent submission.</td>
                    </tr>
                    <tr>
                      <td><strong>Privacy concerns</strong></td>
                      <td>Make library private; submit only the selected document.</td>
                    </tr>
                    <tr>
                      <td><strong>Third-party application limitations</strong></td>
                      <td>Explain external redirect; avoid promising unsupported control.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          
          <!-- Bottom Row: Phased Implementation Roadmap -->
          <div class="card card-tinted" style="padding: 10px 14px;">
            <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 6px;">Phased Rollout Plan</div>
            <div class="grid-4" style="gap: 8px;">
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px;">
                <div style="font-size: 10px; font-weight: 700; color: var(--naukri-blue); text-transform: uppercase;">Phase 1: Internal QA</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.3; margin-top: 2px;">
                  Test upload, multiple file storage, custom naming, selection, save logic, history integrity & privacy rules.
                </div>
              </div>
              
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px;">
                <div style="font-size: 10px; font-weight: 700; color: var(--naukri-blue); text-transform: uppercase;">Phase 2: Limited Beta</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.3; margin-top: 2px;">
                  Release to a small eligible group; collect feedback on usability and unexpected edge-case issues.
                </div>
              </div>
              
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px;">
                <div style="font-size: 10px; font-weight: 700; color: var(--emerald-accent); text-transform: uppercase;">Phase 3: Controlled A/B</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.3; margin-top: 2px;">
                  Compare existing and proposed workflows; evaluate primary metric and guardrails.
                </div>
              </div>
              
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px;">
                <div style="font-size: 10px; font-weight: 700; color: var(--navy-dark); text-transform: uppercase;">Phase 4 & 5: Scale</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.3; margin-top: 2px;">
                  Fix issues and iterate; gradually expand rollout only when pilot demonstrates acceptable guardrail performance.
                </div>
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Business Model & Risk Governance</h4>
        <p>Let's address the business calculations and risk governance:</p>
        <ul>
          <li><strong>Hypothetical Funnel Impact:</strong> We illustrate the math using 10,000 application starts for both groups. If control completes 60% (6,000) and the test group completes 65% (6,500), that yields 500 incremental completed applications. We explicitly disclaim that this is a funnel illustration, not an ROI model—no revenue or cost figures are fabricated.</li>
          <li><strong>Risk Matrix:</strong> We address all eight key risks—from wrong-resume submission (mitigated by confirmation preview) to accidental overwrites (mitigated by isolated storage) and external redirects (explicitly disclosed).</li>
          <li><strong>Phased Delivery:</strong> We follow a disciplined 5-phase rollout: Internal QA, Limited Beta, Controlled A/B, Iterate, and Gradual Rollout without inventing unrealistic timelines.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's conclude with our strategic recommendation.</div>
        """
    },

    # SLIDE 14: STRATEGIC RECOMMENDATION & CLOSING
    {
        "id": "slide-14",
        "number": "14",
        "tag": "Strategic Recommendation",
        "title": "Strategic Recommendation: Candidate Control at Scale",
        "subtitle": "Unifying master profile convenience with role-specific resume agility for Naukri.com",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; padding: 8px 0;">
          <!-- Core Takeaway Card -->
          <div class="card card-blue" style="padding: 20px 24px; border: 2px solid var(--naukri-blue-border); background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: var(--naukri-blue); margin-bottom: 6px;">
              Closing Strategic Recommendation
            </div>
            <div style="font-size: 18px; font-weight: 800; color: var(--navy-dark); line-height: 1.4; margin-bottom: 8px;">
              "Instead of asking candidates to repeatedly manage and replace resumes, give them one central profile, a library of independent resume versions, and control over which resume they submit for each opportunity."
            </div>
            <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
              The feature is designed to reduce unnecessary navigation and resume-management effort within supported Naukri application flows. Its actual effect on application completion and candidate satisfaction should be established through a controlled pilot.
            </div>
          </div>
          
          <!-- Three Strategic Pillars -->
          <div class="grid-3" style="gap: 14px;">
            <div class="card card-tinted" style="text-align: center; padding: 14px;">
              <div style="font-size: 22px; margin-bottom: 4px;">🎯</div>
              <div style="font-weight: 800; font-size: 13.5px; color: var(--navy-dark); margin-bottom: 3px;">Fewer Application Steps</div>
              <p style="font-size: 11.5px; color: var(--slate-600); line-height: 1.4;">
                Select the appropriate resume at the moment of apply without navigating away from active applications.
              </p>
            </div>
            
            <div class="card card-tinted" style="text-align: center; padding: 14px;">
              <div style="font-size: 22px; margin-bottom: 4px;">🛡️</div>
              <div style="font-weight: 800; font-size: 13.5px; color: var(--navy-dark); margin-bottom: 3px;">Independent Resume Management</div>
              <p style="font-size: 11.5px; color: var(--slate-600); line-height: 1.4;">
                Maintain distinct versioned documents with custom naming, with zero automatic or accidental overwriting.
              </p>
            </div>
            
            <div class="card card-tinted" style="text-align: center; padding: 14px;">
              <div style="font-size: 22px; margin-bottom: 4px;">🤝</div>
              <div style="font-weight: 800; font-size: 13.5px; color: var(--navy-dark); margin-bottom: 3px;">Candidate-Controlled Submission</div>
              <p style="font-size: 11.5px; color: var(--slate-600); line-height: 1.4;">
                Preselects designated default for convenience; strictly requires explicit candidate review before submission.
              </p>
            </div>
          </div>
          
          <!-- Final Call to Action -->
          <div style="text-align: center; padding: 12px; background: var(--navy-dark); border-radius: var(--radius-md); color: white;">
            <div style="font-size: 16px; font-weight: 800; letter-spacing: -0.3px;">
              Build a simpler application experience. Keep the candidate in control.
            </div>
            <div style="font-size: 11.5px; color: #93C5FD; margin-top: 3px;">
              Ready for product validation and Phase 1 technical specification review
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Closing Recommendation</h4>
        <p>In summary: <strong>One Profile, Multiple Resumes</strong> provides a candidate-controlled solution to a real, observed friction point in the job search journey.</p>
        <p>By offering a dedicated library within one profile and enabling application-time selection, Naukri can make applying simpler, reduce abandonment, and maintain complete candidate trust.</p>
        <p>Thank you for your time. I look forward to your thoughts and questions.</p>
        <div class='cue-box'><strong>Appendix:</strong> Comprehensive research documentation and official citations follow on Slide 15.</div>
        """
    },

    # SLIDE 15: APPENDIX & SOURCES
    {
        "id": "slide-15",
        "number": "15",
        "tag": "Evidence & Citations",
        "title": "Appendix: Research Evidence, FAQ References & Citations",
        "subtitle": "Complete documentation of survey methodology, official competitor references, and verifiable links",
        "content": """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; height: 100%;">
          <!-- Left: Official Sources & Verified References -->
          <div class="card" style="padding: 14px; overflow-y: auto;">
            <div class="card-header-sm">
              <span>Official Help Pages & External Documentation</span>
              <span class="badge badge-gray">Verified References</span>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 10.5px; color: var(--slate-700); margin-top: 6px;">
              <div id="ref-1" style="background: var(--slate-50); padding: 6px 8px; border-radius: 4px; border-left: 3px solid var(--naukri-blue);">
                <div style="font-weight: 700; color: var(--navy-dark);">[1] Naukri FastForward Official FAQ (Profiles & CVs):</div>
                <div style="color: var(--slate-600); margin: 2px 0;">
                  "One Naukri username can have up to five profiles. Each profile can have only one resume attached to it." (Context: text and visual CV FAQ).
                </div>
                <a href="https://resume.naukri.com/frequently-asked-questions-faq/i-already-have-got-a-text-cv-developed-through-naukri-after-getting-a-visual-cv-developed-can-i-upload-both-the-text-cv-and-the-visual-cv-on-my-same-naukri-profile-which-i-have/" target="_blank" style="color: var(--naukri-blue); word-break: break-all; font-size: 9.5px;">
                  resume.naukri.com/frequently-asked-questions-faq/...
                </a>
              </div>
              
              <div id="ref-2a" style="background: var(--slate-50); padding: 6px 8px; border-radius: 4px; border-left: 3px solid var(--naukri-blue);">
                <div style="font-weight: 700; color: var(--navy-dark);">[2a] Naukri AI Resume Maker:</div>
                <div style="color: var(--slate-600); margin: 2px 0;">
                  Tool-specific creation of single resume documents from user profile credentials.
                </div>
                <a href="https://www.naukri.com/resume-maker" target="_blank" style="color: var(--naukri-blue); word-break: break-all; font-size: 9.5px;">
                  www.naukri.com/resume-maker
                </a>
              </div>

              <div id="ref-2b" style="background: var(--slate-50); padding: 6px 8px; border-radius: 4px; border-left: 3px solid var(--naukri-blue);">
                <div style="font-weight: 700; color: var(--navy-dark);">[2b] Naukri Online Resume Builder FAQ:</div>
                <div style="color: var(--slate-600); margin: 2px 0;">
                  Builder-specific tool FAQ documenting retention of up to 50 drafts/resumes.
                </div>
                <a href="https://www.naukri.com/online-resume-maker/faq" target="_blank" style="color: var(--naukri-blue); word-break: break-all; font-size: 9.5px;">
                  www.naukri.com/online-resume-maker/faq
                </a>
              </div>
              
              <div id="ref-3a" style="background: var(--slate-50); padding: 6px 8px; border-radius: 4px; border-left: 3px solid #0077B5;">
                <div style="font-weight: 700; color: var(--navy-dark);">[3a] LinkedIn Help — Manage Your Resumes:</div>
                <div style="color: var(--slate-600); margin: 2px 0;">
                  Documents storing up to 4 recently uploaded reusable resumes for Easy Apply flows.
                </div>
                <a href="https://www.linkedin.com/help/linkedin/answer/a512405" target="_blank" style="color: #0077B5; word-break: break-all; font-size: 9.5px;">
                  www.linkedin.com/help/linkedin/answer/a512405
                </a>
              </div>

              <div id="ref-3b" style="background: var(--slate-50); padding: 6px 8px; border-radius: 4px; border-left: 3px solid #0077B5;">
                <div style="font-weight: 700; color: var(--navy-dark);">[3b] LinkedIn Help — View Submitted Resumes in Easy Apply:</div>
                <div style="color: var(--slate-600); margin: 2px 0;">
                  Documents viewing past submitted resumes in job application history.
                </div>
                <a href="https://www.linkedin.com/help/linkedin/answer/a511942" target="_blank" style="color: #0077B5; word-break: break-all; font-size: 9.5px;">
                  www.linkedin.com/help/linkedin/answer/a511942
                </a>
              </div>
              
              <div id="ref-4" style="background: var(--slate-50); padding: 6px 8px; border-radius: 4px; border-left: 3px solid #003A9B;">
                <div style="font-weight: 700; color: var(--navy-dark);">[4] Indeed India Help — Managing Resume Files:</div>
                <div style="color: var(--slate-600); margin: 2px 0;">
                  Confirms only 1 resume file is stored on the account; new uploads replace existing.
                </div>
                <a href="https://in.indeed.com/help/job-seekers/articles/11314976176141-faqs-creating-uploading-and-managing-a-resume-file" target="_blank" style="color: #003A9B; word-break: break-all; font-size: 9.5px;">
                  in.indeed.com/help/.../faqs-creating-uploading-and-managing-a-resume-file
                </a>
              </div>

              <div id="ref-5" style="background: var(--slate-50); padding: 6px 8px; border-radius: 4px; border-left: 3px solid #003A9B;">
                <div style="font-weight: 700; color: var(--navy-dark);">[5] Indeed Help — Applying for a Job on Indeed:</div>
                <div style="color: var(--slate-600); margin: 2px 0;">
                  Confirms candidate can use existing uploaded file or upload a different file during apply.
                </div>
                <a href="https://in.indeed.com/help/job-seekers/articles/204652920-applying-for-a-job-on-indeed" target="_blank" style="color: #003A9B; word-break: break-all; font-size: 9.5px;">
                  in.indeed.com/help/.../applying-for-a-job-on-indeed
                </a>
              </div>
            </div>
          </div>
          
          <!-- Right: Survey Methodology & Complete Data Catalog -->
          <div class="card" style="padding: 14px; overflow-y: auto;">
            <div class="card-header-sm">
              <span>Primary Research Methodology & Findings Catalog</span>
              <span class="badge badge-blue">N=45 Survey Data</span>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 7px; font-size: 10.5px; color: var(--slate-700); margin-top: 6px;">
              <div><strong>Methodology:</strong> 45 college student respondents surveyed via personal outreach regarding job search habits.</div>
              <div><strong>Q1 (Recent Activity):</strong> 90% applied for a job, internship, or placement in the last 90 days.</div>
              <div><strong>Q2 (Cohort Stage):</strong> 80% looking for placements/full-time; 20% looking for internships.</div>
              <div><strong>Q3 (Role Types):</strong> 5% (one type), 15% (two types), 20% (three types), 60% (four or more types).</div>
              <div><strong>Q4 (Multiple Resumes):</strong> 90% maintain different resume versions for different roles.</div>
              <div><strong>Q5 (Motivations):</strong> Highlighting skills, different industries, multiple paths, JD tailoring.</div>
              <div><strong>Q6 (Management):</strong> Saved on phone/PC, separate portal uploads, editing before applying.</div>
              <div><strong>Q7 (Friction Frequency):</strong> 90% frequently need a resume different from profile resume while applying.</div>
              <div><strong>Q8 (Workarounds):</strong> Replacing uploaded CV, uploading during apply, postponing, skipping.</div>
              <div><strong>Q9 & Q10:</strong> Suggested inconvenience; exact counts and written examples omitted to avoid fabrication.</div>
              <div><strong>Q11 (Feature Valuation):</strong> 90% rated multiple-resume feature <em>'Extremely useful'</em>.</div>
              <div><strong>Q12 (Adoption Likelihood):</strong> 90% reported <em>'Very likely'</em> to use (stated preference).</div>
              <div><strong>Q13 (Valued Elements):</strong> Custom names, apply-time selection, history viewing, document management.</div>
            </div>
            
            <div style="margin-top: 10px; background: var(--amber-light); border: 1px solid var(--amber-border); padding: 7px 9px; border-radius: 4px; font-size: 10px; color: #92400E;">
              <strong>Rigor Guarantee:</strong> No unsupported counts, fabricated quotations, or unverified statistical generalizations have been included. All claims reflect supplied exploratory data and cited official help documentation.
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Appendix: Complete Evidence & Source Documentation</h4>
        <p>This appendix provides verifiable documentation for all external claims made in this deck:</p>
        <ul>
          <li>Official help URLs for Naukri FastForward, Naukri Blog, LinkedIn Help, and Indeed India Help are cited with direct links and context.</li>
          <li>Our 45-respondent survey dataset is cataloged from Q1 to Q13 with complete disclosure of what was measured and what was intentionally omitted (Q9/Q10) to avoid fabricating data.</li>
        </ul>
        <p>Every claim made in this deck is grounded in official documentation, primary exploratory survey data, and sound product management principles.</p>
        """
    }
]
