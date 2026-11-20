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
        "subtitle": "Qualitative product assessment of five strategic alternatives across candidate control, reusability, and feasibility",
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
                    <td style="color: #9F1239; font-weight: 600;">Variable by flow type</td>
                    <td style="color: var(--slate-600);">Low (1 active CV)</td>
                    <td style="color: #B45309; font-weight: 600;">Variable by application type</td>
                    <td style="color: #9F1239;">High overwrite risk</td>
                    <td style="color: #166534; font-weight: 600;">Immediate (no build)</td>
                  </tr>

                  <tr style="border-bottom: 1px solid var(--slate-100);">
                    <td style="padding: 10px 14px;">
                      <strong>Option B: Multiple Profiles</strong><br>
                      <span style="font-size: 10px; color: var(--slate-500);">Multiple profiles under 1 username</span>
                    </td>
                    <td style="color: #B45309;">Medium (profile switching)</td>
                    <td style="color: #B45309;">Medium (profile-bound)</td>
                    <td style="color: #9F1239;">Low (switch profile per role)</td>
                    <td style="color: var(--slate-700);">Separate profiles</td>
                    <td style="color: #9F1239;">Profile fragmentation overhead</td>
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
                Qualitative Product Assessment: Why Option D is the Optimal Choice
              </div>
              <div style="font-size: 12px; color: var(--slate-700); line-height: 1.45;">
                Option D provides a persistent home for role-specific documents within the candidate's existing single profile. It reduces repeated uploads by allowing candidates to reuse previously saved, role-specific documents (Option C), avoids the overhead of managing multiple profiles under one username (Option B), and avoids candidate mistrust of black-box AI algorithms (Option E). Candidate control and resume-selection flexibility vary by application type. Some flows may allow alternate uploads, while others may rely on the profile-associated document.
              </div>
            </div>

            <div class="card card-amber" style="padding: 12px 14px;">
              <div style="font-weight: 800; font-size: 12px; color: #92400E; margin-bottom: 2px;">
                Out of Scope: AI Auto-Matching
              </div>
              <div style="font-size: 11.5px; color: #78350F; line-height: 1.4;">
                AI-based document matching is not required to solve the immediate document management problem and introduces candidate agency concerns. Excluded from MVP scope.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 09 — Strategic Alternatives (Suggested Duration: ~60 seconds)</h4>
        <p><strong>Speaker Script:</strong> "To assess the opportunity objectively, we conducted a qualitative product evaluation of five distinct architectural approaches:</p>
        <ul>
          <li><strong>Option A (Status Quo):</strong> Candidate control and resume-selection flexibility vary by application type. Some flows may allow alternate uploads, while others may rely on the profile-associated document. No new engineering required.</li>
          <li><strong>Option B (Multiple Profiles under One Username):</strong> Naukri's FastForward FAQ documents creating up to 5 profiles under one username for CV services; however, managing multiple profiles fragments candidate history and adds context-switching overhead across applications.</li>
          <li><strong>Option C (Upload-Only):</strong> Easy to implement, but provides zero reusability, forcing candidates to repeatedly re-upload files across devices.</li>
          <li><strong>Option D (Resume Library - Proposed):</strong> Offers the best qualitative balance: candidate control, persistent organization, and non-destructive saving within a single unified profile.</li>
          <li><strong>Option E (AI Auto-Matching):</strong> Premature for MVP. Candidates insist on explicit agency over what recruiters receive, and automated selection introduces trust issues.</li>
        </ul>
        <p>This comparison represents a qualitative product assessment rather than empirical performance proof."</p>
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
                Dedicated candidate workspace storing role-specific resumes (proposed MVP capacity assumption: up to 5 resumes, subject to validation). Each document receives a custom label (e.g. <em>PM CV, Consulting CV</em>).
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
                  Application history preserves an exact document reference of what was submitted to each employer.
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
          <li><strong>2. Dedicated Resume Library:</strong> A clean management area with a proposed MVP capacity of up to 5 resumes (subject to technical and user testing validation), with custom names like 'Product Management CV' or 'Consulting CV'.</li>
          <li><strong>3. Application-Time Selection:</strong> An interactive selector inside the apply modal, allowing candidates to pick an existing resume or upload a new one.</li>
        </ul>
        <p>This is guided by five foundational principles: candidate control, privacy by default (unselected resumes are never exposed to recruiters), independent files, zero silent overwriting, and transparent application history tracking."</p>
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
        "subtitle": "Two distinct application paths: select a saved resume, or upload a new document",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; justify-content: space-between; gap: 10px;">
          <!-- Top: Two-Path Overview Header -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 10px 14px;">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--slate-500); letter-spacing: 0.6px; margin-bottom: 6px;">Two Distinct Application Paths — Candidate Always Decides</div>
            <div style="display: flex; align-items: center; gap: 8px; font-size: 11px; flex-wrap: wrap;">
              <span style="background: #DBEAFE; color: #1E3A8A; padding: 3px 10px; border-radius: 20px; font-weight: 700;">Path A: Select a Saved Resume</span>
              <span style="color: var(--slate-400);">Select → Review → Submit</span>
              <span style="margin: 0 8px; color: var(--slate-300);">|</span>
              <span style="background: #FEF3C7; color: #92400E; padding: 3px 10px; border-radius: 20px; font-weight: 700;">Path B: Upload a New Resume</span>
              <span style="color: var(--slate-400);">Upload → Success → Optional save gate → Review → Submit</span>
            </div>
          </div>

          <!-- Middle: Two-Path Side-by-Side Detail -->
          <div style="display: grid; grid-template-columns: 1fr 1.3fr; gap: 12px; flex: 1;">

            <!-- Path A: Select Existing Saved Resume -->
            <div class="card card-blue" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-blue">Path A: Select Saved Resume</span>
                  <span style="font-size: 10px; color: var(--naukri-blue); font-weight: 700;">Direct Apply</span>
                </div>
                <div style="font-size: 12px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">Choose an existing document from library</div>

                <div style="display: flex; flex-direction: column; gap: 5px;">
                  <div style="display: flex; align-items: center; gap: 8px; background: white; border: 1px solid #BFDBFE; border-radius: 5px; padding: 6px 10px;">
                    <span style="background: var(--naukri-blue); color: white; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; flex-shrink: 0;">1</span>
                    <span style="font-size: 11px; color: var(--slate-700);">Candidate opens application modal</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 8px; background: white; border: 1px solid #BFDBFE; border-radius: 5px; padding: 6px 10px;">
                    <span style="background: var(--naukri-blue); color: white; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; flex-shrink: 0;">2</span>
                    <span style="font-size: 11px; color: var(--slate-700);">Sees saved resumes with custom names; selects exactly one</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 8px; background: white; border: 1px solid #BFDBFE; border-radius: 5px; padding: 6px 10px;">
                    <span style="background: var(--naukri-blue); color: white; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; flex-shrink: 0;">3</span>
                    <span style="font-size: 11px; color: var(--slate-700);">Reviews: selected filename, role, company confirmed</span>
                  </div>
                  <div style="display: flex; align-items: center; gap: 8px; background: white; border: 1px solid #BFDBFE; border-radius: 5px; padding: 6px 10px;">
                    <span style="background: #059669; color: white; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; flex-shrink: 0;">&#10003;</span>
                    <span style="font-size: 11px; color: var(--slate-700);"><strong>Submits application</strong> — library unchanged</span>
                  </div>
                </div>

                <div style="background: #DBEAFE; border-radius: 5px; padding: 6px 10px; margin-top: 8px; font-size: 10.5px; color: #1E3A8A; font-weight: 600;">
                  &#10003; No upload flow. No save checkbox. Direct select &#8594; review &#8594; submit.
                </div>
              </div>
              <div style="font-size: 10px; color: var(--naukri-blue); margin-top: 6px;">
                *Default preference (future scope): a designated default may be pre-highlighted for convenience, with explicit review required before submission.
              </div>
            </div>

            <!-- Path B: Upload a New Resume + Conditional Save Gate -->
            <div class="card card-amber" style="padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                  <span class="badge badge-amber">Path B: Upload a New Resume</span>
                  <span style="font-size: 10px; color: #92400E; font-weight: 700; background: #FEF3C7; padding: 2px 7px; border-radius: 10px;">Includes Save Gate</span>
                </div>
                <div style="font-size: 12px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">Upload from device + optional save to library</div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <!-- Left: Upload Steps -->
                  <div style="display: flex; flex-direction: column; gap: 4px;">
                    <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 2px;">Upload Flow</div>
                    <div style="display: flex; align-items: center; gap: 6px; background: white; border: 1px solid #FDE68A; border-radius: 5px; padding: 5px 8px;">
                      <span style="background: var(--amber-accent); color: white; width: 18px; height: 18px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; font-weight: 700; flex-shrink: 0;">1</span>
                      <span style="font-size: 10.5px; color: var(--slate-700);">Click &#8220;Upload a new resume&#8221;</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 6px; background: white; border: 1px solid #FDE68A; border-radius: 5px; padding: 5px 8px;">
                      <span style="background: var(--amber-accent); color: white; width: 18px; height: 18px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; font-weight: 700; flex-shrink: 0;">2</span>
                      <span style="font-size: 10.5px; color: var(--slate-700);">Select file &#8594; upload in progress</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 6px; background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 5px; padding: 5px 8px;">
                      <span style="background: #059669; color: white; width: 18px; height: 18px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; font-weight: 700; flex-shrink: 0;">3</span>
                      <span style="font-size: 10.5px; color: #166534;"><strong>Upload 100% success</strong></span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 6px; background: #FFFBEB; border: 1.5px solid #FCD34D; border-radius: 5px; padding: 5px 8px;">
                      <span style="font-size: 11px; font-weight: 800; color: #B45309;">&#9733;</span>
                      <span style="font-size: 10.5px; color: #92400E; font-weight: 700;">Save checkbox NOW appears</span>
                    </div>
                  </div>

                  <!-- Right: Save Gate Decision -->
                  <div style="display: flex; flex-direction: column; gap: 4px;">
                    <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 2px;">Save Gate Decision</div>
                    <div style="background: white; border: 1.5px solid var(--slate-300); border-radius: 5px; padding: 6px 8px; flex: 1;">
                      <div style="font-size: 10px; font-weight: 700; color: var(--slate-600); margin-bottom: 3px;">[ ] Unchecked (default)</div>
                      <div style="font-size: 10px; color: var(--slate-500); line-height: 1.4;">
                        &#8594; This job only<br>
                        &#8594; Library unchanged<br>
                        &#8594; No overwrite
                      </div>
                    </div>
                    <div style="background: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: 5px; padding: 6px 8px; flex: 1;">
                      <div style="font-size: 10px; font-weight: 700; color: #166534; margin-bottom: 3px;">[&#10003;] Checked &#8594; name required</div>
                      <div style="font-size: 10px; color: #14532D; line-height: 1.4;">
                        &#8594; Mandatory custom label<br>
                        &#8594; Saved as new entry<br>
                        &#8594; Never overwrites existing
                      </div>
                    </div>
                  </div>
                </div>

                <div style="display: flex; align-items: center; gap: 6px; background: white; border: 1px solid #FDE68A; border-radius: 5px; padding: 5px 8px; margin-top: 6px;">
                  <span style="background: #059669; color: white; width: 18px; height: 18px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 9px; font-weight: 700; flex-shrink: 0;">&#10003;</span>
                  <span style="font-size: 10.5px; color: var(--slate-700);">Review selected document &#8594; Confirm &#8594; Submit &#8594; History logged</span>
                </div>
              </div>
              <div style="font-size: 10px; color: #92400E; margin-top: 6px; font-weight: 600;">
                Save checkbox strictly hidden during upload. Appears only after 100% upload success.
              </div>
            </div>

          </div>

          <!-- Bottom: Shared Safeguards Banner -->
          <div style="background: #F8FAFC; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 8px 16px; display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: var(--slate-700);">
            <span><strong style="color: var(--navy-dark);">Shared safeguards:</strong> Duplicate filenames &#8594; unique IDs (no overwrite) &#8226; History preserves submitted version &#8226; Single-resume: pre-attached with Change/Upload actions</span>
            <span style="font-size: 10px; color: var(--naukri-blue); font-weight: 600; white-space: nowrap; margin-left: 10px;">MVP capacity: up to 5 resumes (proposed assumption)</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 11 — Future Workflow & Logic (Suggested Duration: ~75 seconds)</h4>
        <p><strong>Speaker Script:</strong> "This slide clearly shows two distinct application paths the candidate can follow:</p>
        <ul>
          <li><strong>Path A — Select a saved resume:</strong> The candidate opens the apply modal, sees their library of custom-named resumes, selects one, reviews their selection (file name, company, role confirmed), and submits. No upload. No save checkbox. Direct and frictionless.</li>
          <li><strong>Path B — Upload a new resume:</strong> The candidate chooses to upload a fresh document. The save checkbox is strictly hidden while the upload is in progress. Only after the upload reaches 100% success does the conditional save gate appear. If unchecked (default), the file is used for this application only and the library is unchanged. If checked, the candidate must supply a mandatory custom name, and the file is saved as a new independent entry — no existing resumes are overwritten.</li>
        </ul>
        <p>Both paths end with an explicit review screen before submission. No silent auto-submission. Application history preserves a reference to the exact version submitted.</p>
        <p>Default-resume preference (pre-highlighting a designated default) is kept in future scope, not an MVP requirement.</p>
        <div class='cue-box'><strong>Transition:</strong> Now let's see what these interactions look like in the visual UI walkthrough and interactive prototype on the next slide.</div>
        """
    },

    # SLIDE 12: APPLICATION EXPERIENCE — UI/UX WALKTHROUGH & INTERACTIVE PROTOTYPE
    {
        "id": "slide-12",
        "number": "12",
        "stage": "Design",
        "tag": "UI/UX Walkthrough & Prototype",
        "evidenceType": "Proposed Solution",
        "title": "Application Experience: How Candidates Select and Save a Resume",
        "subtitle": "A visual walkthrough of the application-time resume selection journey",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 8px;">

          <!-- Toggle Buttons: Mockups vs Prototype -->
          <div style="display: flex; align-items: center; gap: 8px; justify-content: space-between;">
            <div style="display: flex; gap: 6px;">
              <button onclick="showUXView('mockups')" id="btn-mockups"
                style="background: #1856EA; color: white; border: none; padding: 5px 14px; border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer;">
                &#128444; UI Walkthrough (4 Screens)
              </button>
              <button onclick="showUXView('prototype')" id="btn-prototype"
                style="background: rgba(255,255,255,0.1); color: var(--navy-dark); border: 1.5px solid var(--slate-200); padding: 5px 14px; border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer;">
                &#9654; Try Interactive Prototype
              </button>
            </div>
            <span style="font-size: 10.5px; color: var(--slate-500);">Company: Example Technologies &nbsp;|&nbsp; Role: Product Manager Intern</span>
          </div>

          <!-- MOCKUPS VIEW -->
          <div id="ux-mockups-view" style="display: flex; flex-direction: column; flex: 1; gap: 0;">

            <!-- 4 UI Screens in 2x2 grid -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 8px; flex: 1;">

              <!-- SCREEN 01: Choose a Resume -->
              <div style="background: white; border: 1.5px solid #E2E8F0; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <!-- Screen Header Bar -->
                <div style="background: #1856EA; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center;">
                  <span style="color: white; font-size: 10px; font-weight: 700;">naukri &nbsp;|&nbsp; Apply to Product Manager Intern &mdash; Example Technologies</span>
                  <span style="background: rgba(255,255,255,0.15); color: white; font-size: 9px; padding: 1px 6px; border-radius: 10px;">Screen 1 of 4</span>
                </div>
                <!-- Modal Content -->
                <div style="padding: 8px 10px; flex: 1; display: flex; flex-direction: column; gap: 5px;">
                  <div style="font-size: 11px; font-weight: 800; color: #0B1B3D; margin-bottom: 2px;">Choose the resume you want to submit</div>
                  <!-- Resume cards -->
                  <div style="border: 2px solid #1856EA; border-radius: 6px; padding: 5px 8px; background: #EFF6FF; display: flex; align-items: center; gap: 7px;">
                    <div style="width: 13px; height: 13px; border-radius: 50%; border: 2px solid #1856EA; background: #1856EA; flex-shrink: 0; display: flex; align-items: center; justify-content: center;">
                      <div style="width: 5px; height: 5px; border-radius: 50%; background: white;"></div>
                    </div>
                    <div>
                      <div style="font-size: 10.5px; font-weight: 700; color: #1E3A8A;">Product Management CV</div>
                      <div style="font-size: 9.5px; color: #64748B;">PM_Resume.pdf &nbsp;&bull;&nbsp; Selected</div>
                    </div>
                  </div>
                  <div style="border: 1px solid #E2E8F0; border-radius: 6px; padding: 5px 8px; background: #F8FAFC; display: flex; align-items: center; gap: 7px;">
                    <div style="width: 13px; height: 13px; border-radius: 50%; border: 1.5px solid #CBD5E1; flex-shrink: 0;"></div>
                    <div>
                      <div style="font-size: 10.5px; font-weight: 600; color: #374151;">Consulting CV</div>
                      <div style="font-size: 9.5px; color: #94A3B8;">Consulting_Resume.pdf</div>
                    </div>
                  </div>
                  <div style="border: 1px solid #E2E8F0; border-radius: 6px; padding: 5px 8px; background: #F8FAFC; display: flex; align-items: center; gap: 7px;">
                    <div style="width: 13px; height: 13px; border-radius: 50%; border: 1.5px solid #CBD5E1; flex-shrink: 0;"></div>
                    <div>
                      <div style="font-size: 10.5px; font-weight: 600; color: #374151;">Operations CV</div>
                      <div style="font-size: 9.5px; color: #94A3B8;">Operations_Resume.pdf</div>
                    </div>
                  </div>
                  <div style="border: 1px dashed #93C5FD; border-radius: 6px; padding: 5px 8px; display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <span style="font-size: 13px; color: #1856EA; font-weight: 800;">+</span>
                    <span style="font-size: 10.5px; color: #1856EA; font-weight: 600;">Upload a new resume</span>
                  </div>
                  <div style="margin-top: auto; display: flex; gap: 6px; justify-content: flex-end;">
                    <button style="background: #E2E8F0; border: none; padding: 4px 10px; border-radius: 5px; font-size: 10px; font-weight: 600; cursor: pointer; color: #374151;">Cancel</button>
                    <button style="background: #1856EA; color: white; border: none; padding: 4px 12px; border-radius: 5px; font-size: 10px; font-weight: 700; cursor: pointer;">Continue &rarr;</button>
                  </div>
                </div>
                <div style="background: #F1F5F9; padding: 3px 10px; font-size: 9.5px; color: #64748B; font-weight: 600; border-top: 1px solid #E2E8F0;">
                  &#128274; Only the selected resume will be shared with the employer
                </div>
              </div>

              <!-- SCREEN 02: Upload a New Resume -->
              <div style="background: white; border: 1.5px solid #E2E8F0; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="background: #1856EA; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center;">
                  <span style="color: white; font-size: 10px; font-weight: 700;">naukri &nbsp;|&nbsp; Upload a resume for this application</span>
                  <span style="background: rgba(255,255,255,0.15); color: white; font-size: 9px; padding: 1px 6px; border-radius: 10px;">Screen 2 of 4</span>
                </div>
                <div style="padding: 8px 10px; flex: 1; display: flex; flex-direction: column; gap: 5px;">
                  <div style="font-size: 11px; font-weight: 800; color: #0B1B3D; margin-bottom: 2px;">Upload a resume for this application</div>
                  <!-- Upload area - success state -->
                  <div style="border: 2px solid #059669; border-radius: 7px; padding: 8px 10px; background: #ECFDF5; display: flex; flex-direction: column; align-items: center; gap: 3px;">
                    <div style="font-size: 20px;">&#128196;</div>
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">Product_Analyst.pdf</div>
                    <div style="font-size: 9.5px; color: #059669;">PDF &nbsp;&bull;&nbsp; 156 KB &nbsp;&bull;&nbsp; Upload complete</div>
                    <!-- Progress bar full -->
                    <div style="width: 100%; height: 5px; background: #A7F3D0; border-radius: 3px; overflow: hidden; margin-top: 2px;">
                      <div style="width: 100%; height: 100%; background: #059669; border-radius: 3px;"></div>
                    </div>
                    <div style="background: #059669; color: white; font-size: 9.5px; font-weight: 700; padding: 2px 10px; border-radius: 10px; margin-top: 2px;">&#10003; Upload Successful</div>
                  </div>
                  <!-- States legend -->
                  <div style="display: flex; gap: 6px; font-size: 9px; color: #64748B;">
                    <span style="background: #F1F5F9; border: 1px solid #E2E8F0; padding: 2px 7px; border-radius: 10px;">State 1: Select file</span>
                    <span style="background: #FEF3C7; border: 1px solid #FCD34D; padding: 2px 7px; border-radius: 10px;">State 2: Uploading&hellip;</span>
                    <span style="background: #ECFDF5; border: 1px solid #A7F3D0; padding: 2px 7px; border-radius: 10px; font-weight: 700; color: #059669;">&#10003; State 3: Success (shown)</span>
                  </div>
                  <div style="background: #FEF3C7; border: 1px solid #FCD34D; border-radius: 5px; padding: 5px 8px; font-size: 10px; color: #92400E; font-weight: 600;">
                    &#8505; Save checkbox does NOT appear during States 1 or 2. Only shown after upload success.
                  </div>
                </div>
                <div style="background: #F1F5F9; padding: 3px 10px; font-size: 9.5px; color: #64748B; font-weight: 600; border-top: 1px solid #E2E8F0;">
                  File validated &#10003; &nbsp; Proceeding to save decision &rarr;
                </div>
              </div>

              <!-- SCREEN 03: Conditional Save Option -->
              <div style="background: white; border: 2px solid #F59E0B; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 2px 10px rgba(245,158,11,0.15);">
                <div style="background: #92400E; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center;">
                  <span style="color: white; font-size: 10px; font-weight: 700;">naukri &nbsp;|&nbsp; &#9733; Key Decision: Save to Library?</span>
                  <span style="background: rgba(255,255,255,0.2); color: white; font-size: 9px; padding: 1px 6px; border-radius: 10px;">Screen 3 of 4 — Most Important</span>
                </div>
                <div style="padding: 8px 10px; flex: 1; display: flex; flex-direction: column; gap: 5px;">
                  <div style="font-size: 11px; font-weight: 800; color: #0B1B3D; margin-bottom: 1px;">Your resume has been uploaded successfully.</div>
                  <!-- File badge -->
                  <div style="display: flex; align-items: center; gap: 7px; background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 5px; padding: 4px 8px;">
                    <span style="font-size: 13px;">&#128196;</span>
                    <span style="font-size: 10.5px; font-weight: 700; color: #166534;">Product_Analyst.pdf</span>
                    <span style="background: #059669; color: white; font-size: 9px; padding: 1px 7px; border-radius: 10px; font-weight: 700; margin-left: auto;">&#10003; Upload successful</span>
                  </div>
                  <!-- Two states side by side -->
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; flex: 1;">
                    <!-- State A: Unchecked -->
                    <div style="border: 1.5px solid #CBD5E1; border-radius: 6px; padding: 7px 8px; background: #F8FAFC;">
                      <div style="display: flex; align-items: center; gap: 5px; margin-bottom: 5px;">
                        <div style="width: 12px; height: 12px; border: 1.5px solid #94A3B8; border-radius: 2px; flex-shrink: 0;"></div>
                        <span style="font-size: 9.5px; font-weight: 700; color: #374151;">Save to Resume Library</span>
                      </div>
                      <div style="font-size: 9px; color: #64748B; line-height: 1.4;">
                        This resume will be used for the current application only. It will not be added to your Resume Library.
                      </div>
                      <div style="font-size: 9px; color: #94A3B8; margin-top: 4px; font-style: italic;">No name field appears.</div>
                      <div style="margin-top: 5px; padding-top: 4px; border-top: 1px solid #E2E8F0; font-size: 8.5px; color: #64748B; font-weight: 600;">State A: Unchecked (default)</div>
                    </div>
                    <!-- State B: Checked -->
                    <div style="border: 1.5px solid #059669; border-radius: 6px; padding: 7px 8px; background: #F0FDF4;">
                      <div style="display: flex; align-items: center; gap: 5px; margin-bottom: 5px;">
                        <div style="width: 12px; height: 12px; border: 1.5px solid #059669; border-radius: 2px; flex-shrink: 0; background: #059669; display: flex; align-items: center; justify-content: center;">
                          <span style="color: white; font-size: 8px; font-weight: 900;">&#10003;</span>
                        </div>
                        <span style="font-size: 9.5px; font-weight: 700; color: #166534;">Save to Resume Library</span>
                      </div>
                      <div style="margin-bottom: 3px;">
                        <div style="font-size: 8.5px; font-weight: 700; color: #166534; margin-bottom: 2px;">Resume name *</div>
                        <div style="border: 1px solid #059669; border-radius: 4px; padding: 3px 7px; background: white; font-size: 9.5px; color: #374151;">Product Analyst CV</div>
                      </div>
                      <div style="font-size: 9px; color: #166534; line-height: 1.3;">This will be added as a new, independent resume. Your existing saved resumes will remain unchanged.</div>
                      <div style="margin-top: 3px; padding-top: 4px; border-top: 1px solid #A7F3D0; font-size: 8.5px; color: #059669; font-weight: 600;">State B: Checked &mdash; name required</div>
                    </div>
                  </div>
                </div>
                <div style="background: #FEF3C7; padding: 3px 10px; font-size: 9.5px; color: #92400E; font-weight: 600; border-top: 1px solid #FCD34D;">
                  &#9733; Checkbox appears ONLY after successful upload &nbsp;|&nbsp; Blank name blocks continuation
                </div>
              </div>

              <!-- SCREEN 04: Review Before Submission -->
              <div style="background: white; border: 1.5px solid #E2E8F0; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="background: #0B1B3D; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center;">
                  <span style="color: white; font-size: 10px; font-weight: 700;">naukri &nbsp;|&nbsp; Review your application</span>
                  <span style="background: rgba(255,255,255,0.15); color: white; font-size: 9px; padding: 1px 6px; border-radius: 10px;">Screen 4 of 4</span>
                </div>
                <div style="padding: 8px 10px; flex: 1; display: flex; flex-direction: column; gap: 5px;">
                  <div style="font-size: 11px; font-weight: 800; color: #0B1B3D; margin-bottom: 2px;">Review your application</div>
                  <!-- Application details -->
                  <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 6px 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 4px; font-size: 10px;">
                    <div><span style="color: #64748B; font-weight: 600;">Company:</span><br><strong style="color: #0B1B3D;">Example Technologies</strong></div>
                    <div><span style="color: #64748B; font-weight: 600;">Role:</span><br><strong style="color: #0B1B3D;">Product Manager Intern</strong></div>
                  </div>
                  <!-- Resume attachment box -->
                  <div style="border: 1.5px solid #1856EA; border-radius: 6px; padding: 7px 10px; background: #EFF6FF;">
                    <div style="font-size: 9.5px; font-weight: 700; text-transform: uppercase; color: #1856EA; margin-bottom: 4px;">&#128206; Resume Attached</div>
                    <div style="display: flex; align-items: center; gap: 7px;">
                      <span style="font-size: 18px;">&#128196;</span>
                      <div style="flex: 1;">
                        <div style="font-size: 10.5px; font-weight: 700; color: #1E3A8A;">Product_Analyst.pdf</div>
                        <div style="font-size: 9.5px; color: #64748B;">PDF &nbsp;&bull;&nbsp; 156 KB</div>
                      </div>
                      <div style="display: flex; flex-direction: column; gap: 2px; align-items: flex-end;">
                        <button style="background: none; border: 1px solid #93C5FD; color: #1856EA; padding: 2px 7px; border-radius: 4px; font-size: 9px; cursor: pointer; font-weight: 600;">Preview</button>
                        <button style="background: none; border: 1px solid #CBD5E1; color: #64748B; padding: 2px 7px; border-radius: 4px; font-size: 9px; cursor: pointer; font-weight: 600;">Change</button>
                      </div>
                    </div>
                    <div style="font-size: 9px; color: #3B82F6; margin-top: 5px; padding-top: 4px; border-top: 1px solid #BFDBFE;">
                      Only the resume selected here will be attached to this application. Your other saved resumes remain private.
                    </div>
                  </div>
                  <!-- Submit button -->
                  <div style="margin-top: auto;">
                    <button style="width: 100%; background: #1856EA; color: white; border: none; padding: 7px; border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; letter-spacing: 0.3px;">
                      &#10003; &nbsp;Submit Application
                    </button>
                  </div>
                </div>
                <div style="background: #F1F5F9; padding: 3px 10px; font-size: 9.5px; color: #64748B; font-weight: 600; border-top: 1px solid #E2E8F0;">
                  Explicit review required before submission &nbsp;|&nbsp; History logged on submit
                </div>
              </div>

            </div>

            <!-- Journey connector labels below grid -->
            <div style="display: flex; align-items: center; justify-content: space-around; padding: 4px 0; font-size: 9.5px; color: var(--slate-500); font-weight: 600;">
              <span>&#9312; Select Resume</span>
              <span style="color: var(--slate-300);">&rarr;</span>
              <span>&#9313; Upload (if needed)</span>
              <span style="color: var(--slate-300);">&rarr;</span>
              <span style="color: #92400E; font-weight: 700;">&#9314; &#9733; Save Decision</span>
              <span style="color: var(--slate-300);">&rarr;</span>
              <span>&#9315; Review &amp; Submit</span>
            </div>
          </div>

          <!-- PROTOTYPE VIEW (hidden by default) -->
          <div id="ux-prototype-view" style="display: none; flex-direction: column; flex: 1; gap: 6px;">
            <!-- Scenario buttons bar -->
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
                  3. Scenario A: Apply-Only Upload
                </button>
                <button class="scenario-btn" id="scenario-preset-b" onclick="runProtoPreset('B', event)" title="Upload a new resume and save to library">
                  4. Scenario B: Upload &amp; Save
                </button>
                <button class="scenario-btn" style="background: rgba(225,29,72,0.25); border-color: rgba(225,29,72,0.4);" onclick="resetProtoState(event)">
                  &#8635; Reset Prototype
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
                  &#128193; My Resume Library <span class="proto-tab-count" id="proto-library-count">4</span>
                </div>
                <div class="proto-tab" id="tab-job" onclick="switchProtoView('job', event)">
                  &#128188; Job Opening: PM Intern
                </div>
                <div class="proto-tab" id="tab-apply" onclick="switchProtoView('apply', event)">
                  &#9889; Apply Modal <span class="proto-tab-count" id="proto-apply-step-indicator">Step 1</span>
                </div>
                <div class="proto-tab" id="tab-history" onclick="switchProtoView('history', event)">
                  &#128220; Application History <span class="proto-tab-count" id="proto-history-count">1</span>
                </div>
              </div>

              <!-- Dynamic Prototype Viewport Body -->
              <div class="proto-body" id="proto-body-viewport">
                <!-- Dynamically populated by scripts_js.py -->
              </div>
            </div>

            <!-- Prototype Footer Note -->
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 10.5px; color: var(--slate-500);">
              <span>*Client-side simulated interactive prototype. Conditional save gate, mandatory naming, and history logging demonstrated.</span>
              <span style="color: var(--naukri-blue); font-weight: 600;">Full UX Specifications in Appendix C &rarr;</span>
            </div>
          </div>

        </div>

        <script>
          function showUXView(view) {
            var mockupsView = document.getElementById('ux-mockups-view');
            var protoView = document.getElementById('ux-prototype-view');
            var btnMockups = document.getElementById('btn-mockups');
            var btnProto = document.getElementById('btn-prototype');
            if (view === 'mockups') {
              mockupsView.style.display = 'flex';
              protoView.style.display = 'none';
              btnMockups.style.background = '#1856EA';
              btnMockups.style.color = 'white';
              btnMockups.style.border = 'none';
              btnProto.style.background = 'rgba(255,255,255,0.1)';
              btnProto.style.color = 'var(--navy-dark)';
              btnProto.style.border = '1.5px solid var(--slate-200)';
            } else {
              mockupsView.style.display = 'none';
              protoView.style.display = 'flex';
              btnProto.style.background = '#1856EA';
              btnProto.style.color = 'white';
              btnProto.style.border = 'none';
              btnMockups.style.background = 'rgba(255,255,255,0.1)';
              btnMockups.style.color = 'var(--navy-dark)';
              btnMockups.style.border = '1.5px solid var(--slate-200)';
              if (typeof renderProtoView === 'function') { renderProtoView(); }
            }
          }
        </script>
        """,
        "speakerNotes": """
        <h4>Slide 12 — UI/UX Walkthrough & Interactive Prototype (Suggested Duration: ~90 seconds)</h4>
        <p><strong>Speaker Script:</strong> "This slide shows what the proposed candidate experience actually looks like — from clicking Apply through to reviewing and submitting. There are four sequential screens:</p>
        <ul>
          <li><strong>Screen 1 — Choose a Resume:</strong> The candidate sees their saved resumes with custom names (Product Management CV, Consulting CV, Operations CV) in a single-select radio-button modal. They can also choose to upload a new document.</li>
          <li><strong>Screen 2 — Upload a New Resume:</strong> A clean file upload interface with three visual states: before selection, uploading in progress, and successful upload. The save checkbox does NOT appear during states 1 or 2.</li>
          <li><strong>Screen 3 — Conditional Save Option (the most important screen):</strong> After successful upload, the candidate sees the save checkbox. State A (unchecked, default): the resume is used for this application only, nothing saved, no name field shown. State B (checked): a mandatory custom name field appears; the file is saved as a new, independent entry and existing resumes are never touched.</li>
          <li><strong>Screen 4 — Review Before Submission:</strong> The candidate reviews exactly which resume is attached, with options to Preview or Change. Only then can they submit. Application history records this exact version."</li>
        </ul>
        <p>Click <strong>"Try Interactive Prototype"</strong> to explore all four scenarios live: single resume quick apply, multi-resume selector, apply-only upload, and upload-and-save.</p>
        <div class='cue-box'><strong>Transition:</strong> With the proposed UX illustrated and the interactive prototype demonstrated, let's move to MVP scope and product validation.</div>
        """
    }
]
