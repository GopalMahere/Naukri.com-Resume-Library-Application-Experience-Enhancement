# slides_solution.py - Slides 09 to 12 (Alternatives, Solution Pillars, Workflow/Logic, UX & Interactive Prototype)

SLIDES_SOLUTION = [
    # SLIDE 09: STRATEGIC ALTERNATIVES & OPPORTUNITY ASSESSMENT
    {
        "id": "slide-9",
        "number": "09",
        "stage": "Assess",
        "tag": "Strategic Alternatives",
        "evidenceType": "Proposed Solution",
        "title": "Which Product Approach Best Addresses the Problem?",
        "subtitle": "Qualitative evaluation of five product options across candidate control, reusability, and feasibility",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 12px;">
          <!-- 5 Options Qualitative Comparison Table -->
          <div class="card" style="padding: 0; overflow: hidden; flex: 1; border: 1.5px solid var(--slate-200);">
            <div class="table-scroll-wrap">
              <table class="deck-table" style="font-size: 11.5px; width: 100%;">
                <thead>
                  <tr style="background: var(--navy-dark); color: white;">
                    <th style="width: 20%; padding: 10px 14px;">Strategic Option</th>
                    <th style="width: 16%; padding: 10px 12px;">Candidate Control</th>
                    <th style="width: 16%; padding: 10px 12px;">Reusability</th>
                    <th style="width: 16%; padding: 10px 12px;">Application Speed</th>
                    <th style="width: 16%; padding: 10px 12px;">Data Safety</th>
                    <th style="width: 16%; padding: 10px 12px;">Feasibility / Risk</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid var(--slate-100);">
                    <td style="padding: 10px 14px;">
                      <strong>Option A: Status Quo</strong><br>
                      <span style="font-size: 10px; color: var(--slate-500);">Single profile-attached CV</span>
                    </td>
                    <td style="color: #9F1239; font-weight: 600;">Low (profile swap needed)</td>
                    <td style="color: var(--slate-600);">Low (1 active CV)</td>
                    <td style="color: #9F1239; font-weight: 600;">Low (must leave flow)</td>
                    <td style="color: #9F1239;">High overwrite risk</td>
                    <td style="color: #166534; font-weight: 600;">Immediate (no build)</td>
                  </tr>

                  <tr style="border-bottom: 1px solid var(--slate-100);">
                    <td style="padding: 10px 14px;">
                      <strong>Option B: Multiple Profiles</strong><br>
                      <span style="font-size: 10px; color: var(--slate-500);">Separate logins/profiles</span>
                    </td>
                    <td style="color: #B45309;">Medium (account hopping)</td>
                    <td style="color: #B45309;">Medium (profile-bound)</td>
                    <td style="color: #9F1239;">Low (high login friction)</td>
                    <td style="color: var(--slate-700);">Separate records</td>
                    <td style="color: #9F1239;">High complexity & fragmentation</td>
                  </tr>

                  <tr style="border-bottom: 1px solid var(--slate-100);">
                    <td style="padding: 10px 14px;">
                      <strong>Option C: In-Flow Upload Only</strong><br>
                      <span style="font-size: 10px; color: var(--slate-500);">Upload fresh file every time</span>
                    </td>
                    <td style="color: #166534; font-weight: 600;">High (upload any file)</td>
                    <td style="color: #9F1239; font-weight: 600;">Zero (not saved to account)</td>
                    <td style="color: #B45309;">Medium (repetitive uploads)</td>
                    <td style="color: #166534;">Safe (no overwrite)</td>
                    <td style="color: #166534; font-weight: 600;">Moderate engineering</td>
                  </tr>

                  <tr style="background: #EFF6FF; border: 2px solid var(--naukri-blue);">
                    <td style="padding: 10px 14px;">
                      <strong style="color: #1E3A8A; font-size: 12.5px;">Option D: Resume Library</strong><br>
                      <span class="badge badge-blue" style="font-size: 9.5px; margin-top: 2px;">★ PROPOSED CONCEPT</span>
                    </td>
                    <td style="color: #166534; font-weight: 800;">Highest (candidate choice)</td>
                    <td style="color: #166534; font-weight: 800;">Highest (persistent CVs)</td>
                    <td style="color: #166534; font-weight: 800;">Highest (1-click selector)</td>
                    <td style="color: #166534; font-weight: 800;">Non-destructive storage</td>
                    <td style="color: #1E3A8A; font-weight: 700;">Balanced MVP scope</td>
                  </tr>

                  <tr>
                    <td style="padding: 10px 14px;">
                      <strong>Option E: AI Auto-Matching</strong><br>
                      <span style="font-size: 10px; color: var(--slate-500);">AI auto-selects or rewrites</span>
                    </td>
                    <td style="color: #9F1239; font-weight: 600;">Low (black-box algorithmic)</td>
                    <td style="color: var(--slate-600);">Variable (synthetic output)</td>
                    <td style="color: #166534; font-weight: 600;">High (fully automated)</td>
                    <td style="color: #9F1239;">Risk of hallucinations</td>
                    <td style="color: #9F1239; font-weight: 600;">High technical & legal risk</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          
          <!-- Bottom Decision Justification Banner -->
          <div style="display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 14px;">
            <div class="card card-blue" style="padding: 12px 16px;">
              <div style="font-weight: 800; font-size: 13px; color: var(--navy-dark); margin-bottom: 3px;">
                Why Option D (Resume Library) is the Optimal Product Solution
              </div>
              <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                Option D provides a persistent home for role-specific documents within the candidate's existing single profile. It eliminates repeated uploading (Option C), avoids account fragmentation (Option B), and avoids candidate distrust of black-box AI algorithms (Option E).
              </div>
            </div>

            <div class="card card-amber" style="padding: 12px 14px;">
              <div style="font-weight: 800; font-size: 12px; color: #92400E; margin-bottom: 2px;">
                Out of Scope: AI Auto-Matching
              </div>
              <div style="font-size: 11.5px; color: #78350F; line-height: 1.4;">
                AI-based document matching is not required to solve the immediate file management problem and introduces candidate agency concerns. Excluded from MVP.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 09 — Strategic Alternatives (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To assess the opportunity objectively, we evaluated five distinct architectural approaches:</p>
        <ul>
          <li><strong>Option A (Status Quo):</strong> Retains friction and forces candidates to navigate away to change CVs.</li>
          <li><strong>Option B (Multiple Profiles):</strong> Fragments candidate identities, creates duplicate records, and introduces heavy context-switching.</li>
          <li><strong>Option C (Upload-Only):</strong> Easy to implement, but provides zero reusability, forcing candidates to repeatedly re-upload files on their phones or laptops.</li>
          <li><strong>Option D (Resume Library - Proposed):</strong> The sweet spot. Delivers persistent candidate control, 1-click apply-time selection, and non-destructive storage within one unified master profile.</li>
          <li><strong>Option E (AI Auto-Matching):</strong> Premature for MVP. Candidates insist on explicit agency over what recruiters see, and automated selection introduces hallucination and trust issues.</li>
        </ul>
        <p>We deliberately choose Option D for our product proposal."</p>
        <div class='cue-box'><strong>Transition:</strong> Let's look at the three architectural pillars and design principles of the Resume Library.</div>
        """
    },

    # SLIDE 10: PROPOSED SOLUTION
    {
        "id": "slide-10",
        "number": "10",
        "stage": "Design",
        "tag": "Proposed Solution",
        "evidenceType": "Proposed Solution",
        "title": "A Resume Library Built Around Candidate Choice",
        "subtitle": "Three core pillars and five foundational design principles for candidate control",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 12px;">
          <!-- Top: The Three Core Architectural Pillars -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
            
            <!-- Pillar 1: Single Profile -->
            <div class="card card-blue" style="padding: 16px 18px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span class="badge badge-blue">Pillar 1</span>
                <span style="font-size: 20px;">👤</span>
              </div>
              <div style="font-size: 16px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                One Comprehensive Profile
              </div>
              <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                Single source of truth. Master education, verified skills, employment history, and contact details remain unified. No duplicate accounts or fragmented job histories.
              </div>
            </div>

            <!-- Pillar 2: Dedicated Library -->
            <div class="card card-indigo" style="padding: 16px 18px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span class="badge" style="background:#EDE9FE; color:#4F46E5;">Pillar 2</span>
                <span style="font-size: 20px;">📁</span>
              </div>
              <div style="font-size: 16px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                Dedicated Resume Library
              </div>
              <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                Dedicated workspace storing up to 5 role-specific resumes. Each document receives a custom label (e.g. <em>PM CV, Consulting CV, Ops CV</em>) and independent version management.
              </div>
            </div>

            <!-- Pillar 3: Apply-Time Selection -->
            <div class="card card-emerald" style="padding: 16px 18px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span class="badge badge-teal">Pillar 3</span>
                <span style="font-size: 20px;">⚡</span>
              </div>
              <div style="font-size: 16px; font-weight: 800; color: var(--navy-dark); margin-bottom: 6px;">
                Application-Time Selection
              </div>
              <div style="font-size: 12.5px; color: var(--slate-700); line-height: 1.5;">
                Select from stored resumes directly inside the job application modal. Candidates can also upload a fresh resume with optional conditional saving to the library.
              </div>
            </div>

          </div>

          <!-- Bottom: 5 Foundational Product Principles -->
          <div class="card" style="padding: 14px 18px; border: 1.5px solid var(--slate-200);">
            <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; color: var(--navy-dark); letter-spacing: 0.6px; margin-bottom: 10px;">
              Five Foundational Design Principles
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px;">
              
              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 10px 12px;">
                <div style="font-size: 12px; font-weight: 700; color: var(--naukri-blue); margin-bottom: 3px;">1. Candidate Control</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                  The system never silently auto-submits a document without explicit candidate confirmation.
                </div>
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 10px 12px;">
                <div style="font-size: 12px; font-weight: 700; color: #4F46E5; margin-bottom: 3px;">2. Privacy by Default</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                  Library resumes remain private. Only the specific resume attached to an application is shared.
                </div>
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 10px 12px;">
                <div style="font-size: 12px; font-weight: 700; color: #0D9488; margin-bottom: 3px;">3. Independent Files</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                  Uploading, editing, or deleting one resume has zero destructive impact on any other stored resume.
                </div>
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 10px 12px;">
                <div style="font-size: 12px; font-weight: 700; color: #D97706; margin-bottom: 3px;">4. No Silent Overwrite</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                  Uploads default to application-only unless the candidate explicitly checks to save as a new file.
                </div>
              </div>

              <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 6px; padding: 10px 12px;">
                <div style="font-size: 12px; font-weight: 700; color: #059669; margin-bottom: 3px;">5. Transparent History</div>
                <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4;">
                  Application history preserves an exact immutable snapshot of the document submitted to each employer.
                </div>
              </div>

            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 10 — Proposed Solution Pillars (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "Our proposed feature, <strong>Resume Library</strong>, rests on three clear product pillars:</p>
        <ul>
          <li><strong>1. One Comprehensive Profile:</strong> A single source of truth for the candidate's career data—education, skills, work history. No secondary accounts.</li>
          <li><strong>2. Dedicated Resume Library:</strong> A clean management area for up to 5 role-specific resumes, with custom names like 'Product Management CV' or 'Consulting CV'.</li>
          <li><strong>3. Application-Time Selection:</strong> An interactive selector inside the apply modal, allowing candidates to pick an existing resume or upload a new one.</li>
        </ul>
        <p>This is guided by five foundational principles: candidate control, privacy by default (unselected resumes are never exposed to recruiters), independent files, zero silent overwriting, and immutable application history logs."</p>
        <div class='cue-box'><strong>Transition:</strong> How does this workflow function step-by-step, especially when uploading a new document? Let's trace the decision logic.</div>
        """
    },

    # SLIDE 11: FUTURE WORKFLOW & DECISION LOGIC
    {
        "id": "slide-11",
        "number": "11",
        "stage": "Design",
        "tag": "Future Workflow & Logic",
        "evidenceType": "Proposed Solution",
        "title": "How the Proposed Experience Would Work",
        "subtitle": "End-to-end candidate journey with prominent conditional save logic",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 10px;">
          <!-- Top: 11-Step Linear Workflow Pipeline -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 10px 14px;">
            <div style="font-size: 10.5px; font-weight: 800; text-transform: uppercase; color: var(--slate-500); letter-spacing: 0.6px; margin-bottom: 8px;">
              End-to-End Application Pipeline (11 Steps)
            </div>
            
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: nowrap; overflow-x: auto; gap: 4px;">
              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--navy-dark); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--navy-dark); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">1</div>
                <div>Profile</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--navy-dark); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--navy-dark); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">2</div>
                <div>Library</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--navy-dark); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--navy-dark); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">3</div>
                <div>Find Job</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--naukri-blue); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--naukri-blue); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">4</div>
                <div>Apply</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--naukri-blue); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--naukri-blue); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">5</div>
                <div>Select CV</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--naukri-blue); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--naukri-blue); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">6</div>
                <div>Upload</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 800; color: var(--amber-accent); min-width: 75px; background: #FFFBEB; border: 1.5px solid #FCD34D; border-radius: 5px; padding: 2px 4px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--amber-accent); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">7</div>
                <div>Save Gate</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--navy-dark); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--navy-dark); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">8</div>
                <div>Decision</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--navy-dark); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--navy-dark); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">9</div>
                <div>Review</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--emerald-accent); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--emerald-accent); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">10</div>
                <div>Confirm</div>
              </div>
              <span style="color: var(--slate-400); font-size: 10px;">→</span>

              <div style="text-align: center; font-size: 10px; font-weight: 700; color: var(--emerald-accent); min-width: 65px;">
                <div style="width: 18px; height: 18px; border-radius: 50%; background: var(--emerald-accent); color: white; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; margin-bottom: 2px;">11</div>
                <div>History</div>
              </div>
            </div>
          </div>

          <!-- Middle: Prominent Conditional Save Logic Gate -->
          <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 14px; flex: 1;">
            
            <!-- Left: Conditional Save Logic Diagram -->
            <div class="card card-amber" style="padding: 12px 16px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span style="font-size: 12px; font-weight: 800; text-transform: uppercase; color: #92400E; letter-spacing: 0.5px;">
                    Step 7: The Conditional Save Gate
                  </span>
                  <span class="badge badge-amber">Core Safety Rule</span>
                </div>
                
                <div style="background: white; border: 1.5px solid #FDE68A; border-radius: 6px; padding: 10px 14px; margin-bottom: 8px;">
                  <div style="font-size: 11px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 2px;">
                    Condition: Appears ONLY After Upload Success
                  </div>
                  <div style="font-size: 13px; font-weight: 700; color: var(--navy-dark);">
                    [ &nbsp; ] Save this resume to my Resume Library
                  </div>
                  <div style="font-size: 11px; color: var(--slate-500); margin-top: 2px;">
                    Checkbox is hidden while uploading. Appears exclusively when file upload reaches 100%.
                  </div>
                </div>

                <!-- Two Branch Outcomes -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                  <div style="background: white; border: 1.5px solid var(--slate-300); border-radius: 6px; padding: 8px 10px;">
                    <div style="font-size: 11.5px; font-weight: 700; color: var(--slate-700);">Case A: Unchecked (Default)</div>
                    <div style="font-size: 11px; color: var(--slate-600); margin-top: 3px; line-height: 1.4;">
                      • Submitted to <strong>this job only</strong><br>
                      • Not added to library<br>
                      • Existing 4 resumes untouched
                    </div>
                  </div>

                  <div style="background: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: 6px; padding: 8px 10px;">
                    <div style="font-size: 11.5px; font-weight: 700; color: #166534;">Case B: Checked by User</div>
                    <div style="font-size: 11px; color: #14532D; margin-top: 3px; line-height: 1.4;">
                      • Mandatory custom label required<br>
                      • Saved as <strong>5th independent file</strong><br>
                      • Never overwrites older files
                    </div>
                  </div>
                </div>
              </div>

              <div style="font-size: 10.5px; color: #92400E; margin-top: 6px; font-weight: 600;">
                Protects candidates against accidental profile loss while supporting one-off tailored CVs.
              </div>
            </div>

            <!-- Right: Flow Safeguards & Fast Paths -->
            <div class="card" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between; border: 1.5px solid var(--slate-200);">
              <div>
                <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; color: var(--navy-dark); letter-spacing: 0.5px; margin-bottom: 6px;">
                  Flow Safeguards & Quick Paths
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 11.5px; color: var(--slate-700);">
                  <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 10px;">
                    <strong>Single-Resume Quick Apply:</strong> If candidate has only 1 resume, it is pre-attached to preserve 1-click speed, with clear "Change" and "Upload" links.
                  </div>

                  <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 10px;">
                    <strong>Default Preselection:</strong> User-designated default is preselected, but <em>never auto-submitted</em> without candidate clicking submit.
                  </div>

                  <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 10px;">
                    <strong>Duplicate Filenames:</strong> Two files named <code>Resume.pdf</code> receive separate UUIDs; identical filenames never overwrite each other.
                  </div>

                  <div style="background: #F8FAFC; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 10px;">
                    <strong>External ATS Boundary:</strong> External redirect listings display an informative note explaining that document handling is on the external portal.
                  </div>
                </div>
              </div>

              <div style="font-size: 10.5px; color: var(--slate-500); margin-top: 6px;">
                Detailed edge cases and acceptance criteria documented in Appendix C.
              </div>
            </div>

          </div>

          <!-- Bottom: Status Banner -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 8px 16px; font-size: 11.5px; color: var(--slate-700);">
            <strong style="color: var(--navy-dark);">Data Integrity Guarantee:</strong> Historical application records store an immutable snapshot ID of the exact document version submitted, ensuring complete legal and audit transparency.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 11 — Future Workflow & Logic (Suggested Duration: ~75 seconds)</h4>
        <p><strong>Speaker Script:</strong> "Here is how the proposed experience works end-to-end across an 11-step pipeline.</p>
        <p>The linchpin is <strong>Step 7: The Conditional Save Gate</strong>:</p>
        <ul>
          <li>When a candidate uploads a new document, the 'Save to Resume Library' checkbox is strictly hidden until the file upload reaches 100% success.</li>
          <li><strong>If left unchecked (Case A):</strong> The resume is used for this specific job application only. It is not saved to the library, and existing files remain untouched.</li>
          <li><strong>If checked (Case B):</strong> The system mandates a custom name, and saves it as a new independent resume entry. It never overwrites previous files.</li>
        </ul>
        <p>We also preserve single-resume quick apply speed, honor default preselection with explicit confirmation, isolate duplicate filenames via UUIDs, and preserve immutable application history."</p>
        <div class='cue-box'><strong>Transition:</strong> Now let's see how these interactions look and feel in our interactive candidate prototype.</div>
        """
    },

    # SLIDE 12: UX DESIGN & INTERACTIVE PROTOTYPE
    {
        "id": "slide-12",
        "number": "12",
        "stage": "Design",
        "tag": "Interactive Prototype",
        "evidenceType": "Proposed Solution",
        "title": "From Product Concept to Candidate Experience",
        "subtitle": "Six conceptual desktop UI screens and a fully interactive candidate simulator",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 10px;">
          <!-- Top Prototype Scenario Trigger Bar -->
          <div class="proto-scenario-bar" style="border-radius: var(--radius-sm);">
            <div style="display: flex; align-items: center; gap: 6px;">
              <span style="font-weight: 800; color: #93C5FD; font-size: 11px;">TEST SCENARIOS:</span>
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
          
          <!-- Embedded Interactive Prototype Container -->
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
                ⚡ Apply Modal <span class="proto-tab-count" id="proto-apply-step-indicator">Step 1</span>
              </div>
              <div class="proto-tab" id="tab-history" onclick="switchProtoView('history', event)">
                📜 Application History <span class="proto-tab-count" id="proto-history-count">1</span>
              </div>
            </div>
            
            <!-- Dynamic Prototype Viewport Body -->
            <div class="proto-body" id="proto-body-viewport">
              <!-- Dynamically populated by scripts_js.py -->
            </div>
          </div>
          
          <!-- Prototype Footer Clarification Note -->
          <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: var(--slate-500); padding: 0 4px;">
            <span>*Client-side simulated interactive prototype. Implements dynamic default preselection, conditional save gates, mandatory custom naming, and immutable audit logs.</span>
            <span style="color: var(--naukri-blue); font-weight: 600;">Full UX Specifications in Appendix C →</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 12 — UX Design & Interactive Prototype (Suggested Duration: ~90 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To make this proposal concrete, I built an interactive prototype simulating the candidate experience across desktop viewports.</p>
        <p>You can test four primary scenarios using the top preset buttons:</p>
        <ul>
          <li><strong>Preset 1 (Single-Resume Quick Apply):</strong> Demonstrates how a candidate with only one resume retains the fast, frictionless experience with pre-attached CV.</li>
          <li><strong>Preset 2 (Multi-Resume Selector):</strong> Lets a candidate easily choose between their Product Management CV, Consulting CV, or Operations CV. Notice how setting a default updates preselection dynamically.</li>
          <li><strong>Preset 3 (Scenario A - Apply-Only Upload):</strong> The candidate uploads a fresh file, leaves the save checkbox unchecked, and applies. The existing library remains exactly at 4 resumes.</li>
          <li><strong>Preset 4 (Scenario B - Upload & Save):</strong> The candidate checks 'Save to Resume Library'. Notice that a custom name becomes mandatory, and upon submission, the library expands to 5 independent files without overwriting any existing resumes.</li>
        </ul>
        <p>Finally, the 'Application History' tab shows how every submission permanently logs the exact document version submitted."</p>
        <div class='cue-box'><strong>Transition:</strong> With the solution validated in prototype, how should Naukri prioritize MVP delivery and measure business success? Let's look at Slide 13.</div>
        """
    }
]
