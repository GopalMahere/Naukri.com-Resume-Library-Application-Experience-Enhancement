# slides_solution.py - Slides 13 to 17 (Alternatives, Solution Pillars, Workflow/Logic, UX & Prototype, PRD & MVP)

SLIDES_SOLUTION = [
    # SLIDE 13: OPPORTUNITY ASSESSMENT AND ALTERNATIVES
    {
        "id": "slide-13",
        "number": "13",
        "stage": "Assess",
        "tag": "Strategic Alternatives",
        "evidenceType": "Proposed Solution",
        "title": "Which Product Approach Best Addresses the Problem?",
        "subtitle": "Qualitative evaluation of five product options across candidate control, reusability, and feasibility",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- 5 Options Comparison Table -->
          <div class="card" style="padding: 0; overflow: hidden; flex: 1;">
            <div class="table-scroll-wrap">
              <table class="deck-table" style="font-size: 10.5px;">
                <thead>
                  <tr>
                    <th style="width: 18%;">Strategic Option</th>
                    <th style="width: 16%;">Candidate Control</th>
                    <th style="width: 16%;">Reusability</th>
                    <th style="width: 18%;">Application Convenience</th>
                    <th style="width: 16%;">Data Protection</th>
                    <th style="width: 16%;">Feasibility / Risk</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Option A: Status Quo</strong><br><span style="font-size:9.5px; color:var(--slate-500);">Rely on profile CV</span></td>
                    <td>Low (profile replacement needed)</td>
                    <td>Low (1 active CV)</td>
                    <td>Low (requires leaving active flow)</td>
                    <td>High risk of overwriting active CV</td>
                    <td>High feasibility (no development)</td>
                  </tr>
                  <tr>
                    <td><strong>Option B: Separate Profiles</strong><br><span style="font-size:9.5px; color:var(--slate-500);">Multiple accounts/profiles</span></td>
                    <td>Medium (must switch profiles)</td>
                    <td>Medium (profile-bound)</td>
                    <td>Low (high context-switching overhead)</td>
                    <td>Isolated documents</td>
                    <td>Complex profile synchronization</td>
                  </tr>
                  <tr>
                    <td><strong>Option C: In-Flow Upload Only</strong><br><span style="font-size:9.5px; color:var(--slate-500);">Upload fresh file every time</span></td>
                    <td>High (upload any file)</td>
                    <td>Zero (not saved to account)</td>
                    <td>Medium (must re-upload file repeatedly)</td>
                    <td>No profile overwriting</td>
                    <td>Moderate development effort</td>
                  </tr>
                  <tr style="background: #EFF6FF; border: 1.5px solid var(--naukri-blue);">
                    <td><strong>Option D: Resume Library</strong><br><span style="font-size:9.5px; color:var(--naukri-blue); font-weight:700;">★ RECOMMENDED</span></td>
                    <td><strong>Highest</strong> (candidate chooses)</td>
                    <td><strong>Highest</strong> (persistent named CVs)</td>
                    <td><strong>Highest</strong> (1-click select in flow)</td>
                    <td><strong>Non-destructive</strong> independent entries</td>
                    <td>Balanced (manageable MVP scope)</td>
                  </tr>
                  <tr>
                    <td><strong>Option E: AI Auto-Matching</strong><br><span style="font-size:9.5px; color:var(--slate-500);">AI auto-picks/rewrites CV</span></td>
                    <td>Low (algorithmic decision)</td>
                    <td>Variable (auto-generated)</td>
                    <td>Variable (opaque candidate review)</td>
                    <td>Unintended modification risk</td>
                    <td>High technical & privacy risk</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          
          <!-- Justification Box for Option D -->
          <div class="card card-blue" style="padding: 10px 14px;">
            <div style="font-weight: 700; font-size: 11.5px; color: var(--navy-dark); margin-bottom: 2px;">
              Why Option D (Persistent Resume Library) is the Optimal Choice
            </div>
            <div style="font-size: 11px; color: var(--slate-700); line-height: 1.45;">
              Option D solves the root cause by providing a dedicated, persistent home for role-specific documents within the candidate's master profile. It eliminates repeated file uploading (Option C), avoids the fragmentation of multiple profiles (Option B), and avoids the opacity and candidate mistrust associated with algorithmic AI selection (Option E).
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 13 — Strategic Alternatives Evaluation</h4>
        <p>Before committing to a product design, a strong PM examines multiple alternatives:</p>
        <ul>
          <li><strong>Option A (Status Quo):</strong> Low engineering cost, but leaves candidate friction unresolved.</li>
          <li><strong>Option B (Multiple Profiles):</strong> Maintaining separate profiles fragments search history, causes duplicate candidate records, and creates high maintenance overhead.</li>
          <li><strong>Option C (One-Off Uploads):</strong> Uploading every time offers flexibility, but provides zero reusability, forcing candidates to repeatedly re-upload files on their phones or laptops.</li>
          <li><strong>Option D (Resume Library - Recommended):</strong> Offers the best combination of candidate control, persistent organization, and non-destructive saving within a single profile.</li>
          <li><strong>Option E (AI Auto-Matching):</strong> Premature for MVP. Candidates want full agency over what recruiters receive; automated selection introduces mistrust and error risk.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's look at the three building blocks of our recommended Resume Library solution.</div>
        """
    },

    # SLIDE 14: THE RECOMMENDED SOLUTION
    {
        "id": "slide-14",
        "number": "14",
        "stage": "Design",
        "tag": "Product Solution",
        "evidenceType": "Proposed Solution",
        "title": "A Resume Library Built Around Candidate Choice",
        "subtitle": "Architecting a candidate-controlled ecosystem for multiple role opportunities",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- Three Pillars Grid -->
          <div class="grid-3" style="flex: 1; gap: 14px;">
            <!-- Pillar 1 -->
            <div class="card" style="border-top: 4px solid var(--navy-dark); display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Pillar 01</span>
                <span class="badge badge-gray">Master Record</span>
              </div>
              <div class="card-title-lg">One Comprehensive Profile</div>
              <p class="card-text" style="font-size: 11.5px; margin-bottom: 8px;">
                The candidate maintains a single structured profile containing complete career details:
              </p>
              <ul style="font-size: 11px; color: var(--slate-700); padding-left: 14px; line-height: 1.4; margin-bottom: 10px;">
                <li>Personal & contact information</li>
                <li>Education, degrees & certifications</li>
                <li>Work experience & internships</li>
                <li>Comprehensive skill inventory</li>
              </ul>
              <div style="margin-top: auto; background: var(--slate-50); padding: 6px 10px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600);">
                <strong>Role:</strong> Keeps structured candidate credentials intact and separate from specific resume documents.
              </div>
            </div>
            
            <!-- Pillar 2 -->
            <div class="card" style="border-top: 4px solid var(--naukri-blue); display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Pillar 02</span>
                <span class="badge badge-blue">Document Vault</span>
              </div>
              <div class="card-title-lg">Dedicated Resume Library</div>
              <p class="card-text" style="font-size: 11.5px; margin-bottom: 8px;">
                Candidates upload and independently organize multiple versioned resume documents:
              </p>
              <div style="display: flex; flex-direction: column; gap: 4px; margin-bottom: 8px;">
                <div style="font-size: 10.5px; background: #F8FAFC; border: 1px solid var(--slate-200); padding: 4px 8px; border-radius: 4px; display: flex; justify-content: space-between;">
                  <span>💼 <strong>Product Management CV</strong></span>
                  <span style="color: var(--naukri-blue); font-size: 9.5px;">Default</span>
                </div>
                <div style="font-size: 10.5px; background: #F8FAFC; border: 1px solid var(--slate-200); padding: 4px 8px; border-radius: 4px; display: flex; justify-content: space-between;">
                  <span>📊 <strong>Consulting CV</strong></span>
                  <span style="color: var(--slate-400); font-size: 9.5px;">Sep 28</span>
                </div>
                <div style="font-size: 10.5px; background: #F8FAFC; border: 1px solid var(--slate-200); padding: 4px 8px; border-radius: 4px; display: flex; justify-content: space-between;">
                  <span>⚙️ <strong>Operations CV</strong></span>
                  <span style="color: var(--slate-400); font-size: 9.5px;">Aug 15</span>
                </div>
                <div style="font-size: 10.5px; background: #F8FAFC; border: 1px solid var(--slate-200); padding: 4px 8px; border-radius: 4px; display: flex; justify-content: space-between;">
                  <span>💻 <strong>Core Engineering CV</strong></span>
                  <span style="color: var(--slate-400); font-size: 9.5px;">Jul 04</span>
                </div>
              </div>
              <div style="margin-top: auto; background: var(--slate-50); padding: 6px 10px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600);">
                <strong>Role:</strong> Custom names; independent entries with zero accidental overwriting.
              </div>
            </div>
            
            <!-- Pillar 3 -->
            <div class="card" style="border-top: 4px solid var(--emerald-accent); display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Pillar 03</span>
                <span class="badge badge-teal">Application Flow</span>
              </div>
              <div class="card-title-lg">Application-Time Selection</div>
              <p class="card-text" style="font-size: 11.5px; margin-bottom: 8px;">
                At the moment of applying, candidates choose the exact resume to attach:
              </p>
              <ul style="font-size: 11px; color: var(--slate-700); padding-left: 14px; line-height: 1.4; margin-bottom: 10px;">
                <li>Preselects designated default for convenience</li>
                <li>Or select an alternate saved resume with 1 click</li>
                <li>Or upload a fresh document directly from device</li>
                <li><strong>Conditional Save Gate:</strong> Checkbox appears only post-upload</li>
                <li>Explicit review screen before final submission</li>
              </ul>
              <div style="margin-top: auto; background: var(--slate-50); padding: 6px 10px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600);">
                <strong>Role:</strong> Complete candidate agency; zero forced context-switching.
              </div>
            </div>
          </div>
          
          <!-- 5 Design Principles Footer -->
          <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px;">
            <div class="card card-tinted" style="padding: 7px 10px; text-align: center;">
              <div style="font-weight: 700; font-size: 10.5px; color: var(--navy-dark);">Candidate Control</div>
              <div style="font-size: 9.5px; color: var(--slate-600); margin-top: 2px;">User makes final choice</div>
            </div>
            <div class="card card-tinted" style="padding: 7px 10px; text-align: center;">
              <div style="font-weight: 700; font-size: 10.5px; color: var(--navy-dark);">Privacy by Default</div>
              <div style="font-size: 9.5px; color: var(--slate-600); margin-top: 2px;">Other CVs remain hidden</div>
            </div>
            <div class="card card-tinted" style="padding: 7px 10px; text-align: center;">
              <div style="font-weight: 700; font-size: 10.5px; color: var(--navy-dark);">Independent Files</div>
              <div style="font-size: 9.5px; color: var(--slate-600); margin-top: 2px;">No coupled records</div>
            </div>
            <div class="card card-tinted" style="padding: 7px 10px; text-align: center;">
              <div style="font-weight: 700; font-size: 10.5px; color: var(--navy-dark);">No Overwriting</div>
              <div style="font-size: 9.5px; color: var(--slate-600); margin-top: 2px;">New files save separately</div>
            </div>
            <div class="card card-tinted" style="padding: 7px 10px; text-align: center;">
              <div style="font-weight: 700; font-size: 10.5px; color: var(--navy-dark);">Document History</div>
              <div style="font-size: 9.5px; color: var(--slate-600); margin-top: 2px;">Snapshot retained in log</div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 14 — The Three Core Solution Pillars</h4>
        <p>The proposed Resume Library consists of three complementary pillars:</p>
        <ul>
          <li><strong>Pillar 1: One Comprehensive Profile:</strong> We maintain a single structured master record for candidate credentials. We do not make premature claims about internal recruiter search algorithms, but keep structured profile data conceptually separate from resume files.</li>
          <li><strong>Pillar 2: Dedicated Resume Library:</strong> A persistent document vault where resumes are stored as independent entries with custom names. Editing or deleting one file never affects others.</li>
          <li><strong>Pillar 3: Application-Time Selection:</strong> Job seekers can preselect a default resume for convenience, choose an alternate saved document, or upload a fresh file.</li>
          <li><strong>Core Principles:</strong> Privacy by default (recruiters see only the attached document), zero silent overwriting, and immutable application history tracking.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's examine the detailed 11-step end-to-end workflow and its decision logic.</div>
        """
    },

    # SLIDE 15: FUTURE-STATE WORKFLOW AND DECISION LOGIC
    {
        "id": "slide-15",
        "number": "15",
        "stage": "Design",
        "tag": "System Logic",
        "evidenceType": "Proposed Solution",
        "title": "How the Proposed Experience Would Work",
        "subtitle": "11-step end-to-end sequence governing selection, conditional save logic, and history tracking",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- 11-Step Sequential Pipeline Flow -->
          <div class="card" style="padding: 10px 12px;">
            <div style="font-size: 10px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 5px;">The 11-Step Product Pipeline</div>
            <div style="display: flex; align-items: center; justify-content: space-between; position: relative;">
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">1</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--navy-dark); margin-top: 2px;">Profile</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">2</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--navy-dark); margin-top: 2px;">Library</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">3</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--navy-dark); margin-top: 2px;">Find Job</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">4</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--navy-dark); margin-top: 2px;">Apply</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--naukri-blue); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">5</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--naukri-blue); margin-top: 2px;">Choose CV</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--naukri-blue); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">6</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--naukri-blue); margin-top: 2px;">Upload</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--amber-accent); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">7</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--amber-accent); margin-top: 2px;">Save Gate</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">8</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--navy-dark); margin-top: 2px;">Review</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--emerald-accent); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">9</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--emerald-accent); margin-top: 2px;">Submit</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">10</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--navy-dark); margin-top: 2px;">History</div>
              </div>
              <span class="stage-arrow">→</span>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 8%;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 9.5px; font-weight: 700;">11</div>
                <div style="font-size: 9.5px; font-weight: 700; color: var(--navy-dark); margin-top: 2px;">Manage</div>
              </div>
            </div>
          </div>
          
          <!-- Detailed Decision Architecture -->
          <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 14px; flex: 1;">
            <!-- Left: Step 5 & 7 Decision Logic -->
            <div class="card card-tinted" style="border-left: 4px solid var(--amber-accent); padding: 12px 14px;">
              <div class="card-header-sm">
                <span style="color: #B45309; font-weight: 800;">Step 5 & 7: Conditional Save Gate & Selection Rules</span>
                <span class="badge badge-amber">Core Logic</span>
              </div>
              
              <div style="display: flex; flex-direction: column; gap: 6px; margin-top: 4px;">
                <div style="background: white; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 10px;">
                  <div style="font-size: 11px; font-weight: 700; color: var(--navy-dark);">Scenario 1: Candidate has 1 Saved Resume (Quick-Apply)</div>
                  <div style="font-size: 10.5px; color: var(--slate-600); margin-top: 2px;">
                    Pre-attach the single resume to preserve quick-apply speed. Provide inline "Change Resume" and "+ Upload New Resume" options.
                  </div>
                </div>
                
                <div style="background: white; border: 1px solid var(--slate-200); border-radius: 5px; padding: 6px 10px;">
                  <div style="font-size: 11px; font-weight: 700; color: var(--rose-accent);">Conditional Gate: Upload Success Required</div>
                  <div style="font-size: 10.5px; color: var(--slate-600); margin-top: 2px;">
                    The <code>Save to Resume Library</code> checkbox is <strong>strictly hidden</strong> until the document finishes uploading successfully.
                  </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
                  <div style="background: white; border: 1.5px solid var(--slate-300); border-radius: 5px; padding: 6px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: var(--slate-700);">Case A: Unchecked</div>
                    <div style="font-size: 10px; color: var(--slate-600); margin-top: 2px;">
                      • Used for <em>this job only</em><br>
                      • Not added to library<br>
                      • Zero impact on saved files
                    </div>
                  </div>
                  
                  <div style="background: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: 5px; padding: 6px 8px;">
                    <div style="font-size: 10.5px; font-weight: 700; color: #166534;">Case B: Checked</div>
                    <div style="font-size: 10px; color: #14532D; margin-top: 2px;">
                      • Enforce custom name<br>
                      • Saved as new independent CV<br>
                      • <strong>Never overwrites</strong> older files
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Right: Edge Cases & Data Integrity Rules -->
            <div class="card" style="padding: 12px 14px;">
              <div class="card-header-sm">Edge Cases & Data Integrity Rules</div>
              <div style="display: flex; flex-direction: column; gap: 6px; font-size: 10.5px; color: var(--slate-700);">
                <div style="padding-bottom: 4px; border-bottom: 1px solid var(--slate-100);">
                  <strong>Default-Resume Behaviour:</strong> Designated default is preselected for convenience, but <em>never silently submitted</em>. If no default is designated, selection is required.
                </div>
                <div style="padding-bottom: 4px; border-bottom: 1px solid var(--slate-100);">
                  <strong>Duplicate Filenames:</strong> Two files named <code>Resume.pdf</code> receive distinct internal UUIDs. Duplicate names never trigger silent overwrites.
                </div>
                <div style="padding-bottom: 4px; border-bottom: 1px solid var(--slate-100);">
                  <strong>Library Deletions Post-Apply:</strong> Deleting a resume from the library removes it from future apply flows, but <em>preserves historical application references intact</em>.
                </div>
                <div>
                  <strong>Third-Party Applications:</strong> For jobs redirecting to external ATS platforms, transparently inform candidates that document handling depends on the employer site.
                </div>
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 15 — End-to-End Workflow & Edge Cases</h4>
        <p>This 11-step sequence governs the complete candidate journey:</p>
        <ul>
          <li><strong>Quick-Apply:</strong> If a candidate has only 1 resume, we preserve existing speed by pre-attaching it with clear Change and Upload links.</li>
          <li><strong>Default Preselection:</strong> If a candidate sets a default resume, it is preselected for convenience, but never silently submitted—explicit candidate confirmation is strictly required.</li>
          <li><strong>The Conditional Save Gate:</strong> Notice step 7: the save checkbox is completely hidden until upload succeeds. If left unchecked, it is application-only. If checked, a custom name is mandatory and it saves as a new independent file.</li>
          <li><strong>Data Integrity:</strong> Identical filenames receive distinct internal UUIDs and never overwrite each other. Deleting a resume later from the library does not alter past application audit records.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's test these interactions live in our interactive candidate simulator.</div>
        """
    },

    # SLIDE 16: UX DESIGN AND INTERACTIVE PROTOTYPE
    {
        "id": "slide-16",
        "number": "16",
        "stage": "Design",
        "tag": "Interactive Prototype",
        "evidenceType": "Proposed Solution",
        "title": "Turning the Product Concept into a Candidate Experience",
        "subtitle": "Interactive candidate simulator: test single-resume quick-apply, selector, upload, and conditional save",
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
          
          <div style="font-size: 10px; color: var(--slate-500); display: flex; justify-content: space-between; align-items: center; padding: 0 4px; flex-wrap: wrap; gap: 4px;">
            <span>ℹ️ <em>Simulation Notice: Client-side simulated prototype running locally. No real Naukri backend, recruiter account or application submission is connected. Document history is simulated metadata.</em></span>
            <span style="color: var(--naukri-blue); font-weight: 600;">Candidate Agency Preserved</span>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 16 — Live Interactive Prototype Demonstration</h4>
        <p>This is a live, interactive simulator running entirely in-browser. Here is how you can test each workflow:</p>
        <ol>
          <li><strong>Single-Resume Quick Apply:</strong> Click '1. Single-Resume Quick Apply'. If a candidate has only 1 saved resume, the interface preserves the simple quick-apply flow with a clear 'Change Resume' option, avoiding unnecessary choice friction.</li>
          <li><strong>Multi-Resume Selection:</strong> Click '2. Multi-Resume Selector'. When multiple resumes exist, the candidate chooses between their Product Management, Consulting, Operations, or Engineering CVs. The designated default is preselected for convenience.</li>
          <li><strong>Scenario A (Upload & Don't Save):</strong> Click '3. Scenario A'. The candidate simulates uploading a new resume. Notice the progress bar: the save checkbox is completely hidden until upload completes! When left unchecked, it is used for this application only. Checking the library afterwards confirms exactly 4 resumes remain.</li>
          <li><strong>Scenario B (Upload & Save):</strong> Click '4. Scenario B'. Upload succeeds, the candidate checks the save box, which requires a custom name (try erasing it—validation will prevent continuing). Upon submit, inspect the library: it now holds 5 resumes, with all older documents untouched!</li>
          <li><strong>Set Default Action:</strong> In the library view, click '⭐ Set as Default' on any card to test the default preference interaction.</li>
        </ol>
        <div class='cue-box'><strong>Transition:</strong> Let's formalize these specifications into a prioritized PRD and MVP scope.</div>
        """
    },

    # SLIDE 17: PRD AND MVP DEFINITION
    {
        "id": "slide-17",
        "number": "17",
        "stage": "Specify",
        "tag": "Product Requirements",
        "evidenceType": "Proposed Solution",
        "title": "Defining What Should Be Built First",
        "subtitle": "MoSCoW prioritized specifications, testable acceptance criteria, and technical scope",
        "content": """
        <div style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 16px; height: 100%;">
          <!-- Left: MoSCoW Requirements Matrix -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
            <div style="padding: 8px 12px; background: var(--slate-100); border-bottom: 1px solid var(--slate-200); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 11px; color: var(--navy-dark); text-transform: uppercase;">Functional Requirements Specification</span>
              <span class="badge badge-blue">MoSCoW Prioritized</span>
            </div>
            
            <div class="table-scroll-wrap" style="flex: 1;">
              <table class="deck-table" style="font-size: 10.5px;">
                <thead>
                  <tr>
                    <th style="width: 12%;">ID</th>
                    <th style="width: 60%;">Requirement Description</th>
                    <th style="width: 14%;">Priority</th>
                    <th style="width: 14%;">Scope</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>FR01</strong></td>
                    <td>Support multiple independently stored resume files within one account</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR02</strong></td>
                    <td>Allow custom user-defined names for saved resumes</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR03</strong></td>
                    <td>Allow selection of an existing saved resume during supported applications</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR04</strong></td>
                    <td>Allow uploading a new resume during the application flow</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR05</strong></td>
                    <td>Display optional save checkbox only after successful upload</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR06</strong></td>
                    <td>Save checked upload as an independent library entry (no overwriting)</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR07</strong></td>
                    <td>Preserve unique submitted document reference in application history</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR08</strong></td>
                    <td>Provide document preview & confirmation before final submission</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR09</strong></td>
                    <td>Support rename and delete management actions in library</td>
                    <td><span class="badge badge-should">Should</span></td>
                    <td>Phase 2</td>
                  </tr>
                  <tr>
                    <td><strong>FR10</strong></td>
                    <td>Support explicit replacement of existing saved resume with confirmation</td>
                    <td><span class="badge badge-should">Should</span></td>
                    <td>Phase 2</td>
                  </tr>
                  <tr>
                    <td><strong>FR11</strong></td>
                    <td>Offer an optional default-resume preference for quick-apply</td>
                    <td><span class="badge badge-could">Could</span></td>
                    <td>Phase 3</td>
                  </tr>
                </tbody>
              </table>
            </div>
            
            <div style="padding: 6px 12px; background: var(--slate-50); border-top: 1px solid var(--slate-200); font-size: 10px; color: var(--slate-600);">
              <em>Note: FR09, FR10, and FR11 are phased enhancements shown in the prototype demo as a full-vision preview.</em>
            </div>
          </div>
          
          <!-- Right: Testable Acceptance Criteria & Boundaries -->
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <!-- Testable Acceptance Criteria Box -->
            <div class="card" style="border-left: 4px solid var(--emerald-accent); background: #F0FDF4; padding: 10px 12px;">
              <div class="card-header-sm">
                <span style="color: #065F46; font-weight: 800;">Sample Acceptance Criteria (Given/When/Then)</span>
                <span class="badge badge-teal">Testable Rules</span>
              </div>
              <div style="font-size: 10.5px; color: #064E3B; line-height: 1.4; display: flex; flex-direction: column; gap: 4px; margin-top: 2px;">
                <div>• <strong>Pre-upload:</strong> Given a file upload has not succeeded, the save checkbox is hidden.</div>
                <div>• <strong>Post-upload:</strong> Given upload succeeds, the save checkbox becomes visible.</div>
                <div>• <strong>Unchecked:</strong> Given checkbox is unchecked, no new library record is created.</div>
                <div>• <strong>Checked:</strong> Given checkbox is checked, mandatory custom name validation is enforced.</div>
                <div>• <strong>Duplicate Name:</strong> Given identical filenames, store with unique internal UUIDs without overwriting.</div>
              </div>
            </div>
            
            <!-- Protected Out-of-Scope Box -->
            <div class="card" style="border-left: 4px solid var(--rose-accent); background: #FFF5F5; padding: 10px 12px; flex: 1;">
              <div class="card-header-sm">
                <span style="color: #9F1239; font-weight: 800;">Explicitly Out of Scope for MVP</span>
                <span class="badge badge-red">Protected Scope</span>
              </div>
              <ul style="font-size: 10.5px; color: #4C0519; padding-left: 14px; line-height: 1.35; margin-top: 2px;">
                <li>❌ <strong>AI automatically choosing a resume:</strong> System does not pick for the candidate.</li>
                <li>❌ <strong>AI rewriting a resume:</strong> System does not generate or modify resume text.</li>
                <li>❌ <strong>Automatically merging resumes:</strong> Documents are never consolidated automatically.</li>
                <li>❌ <strong>Automatic profile modification:</strong> Uploads do not alter structured profile fields.</li>
                <li>❌ <strong>Silent submission:</strong> Candidate confirmation is strictly required.</li>
              </ul>
              <div style="margin-top: 4px; font-size: 10px; color: #881337; font-weight: 600;">
                Core mandate: The feature remains entirely candidate-controlled.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Slide 17 — PRD, Acceptance Criteria & Scope Discipline</h4>
        <p>In this PRD, we establish clear prioritization and testable acceptance criteria:</p>
        <ul>
          <li><strong>Must-Haves (FR01–FR08):</strong> Establishing the core loop of storing multiple files, custom naming, apply-time selection, conditional save checkbox post-upload, non-destructive saving, preview review, and history tracking.</li>
          <li><strong>Phased Enhancements:</strong> FR09 (rename/delete), FR10 (explicit replace), and FR11 (default preference) are scheduled for Phase 2/3 and previewed in our prototype.</li>
          <li><strong>Acceptance Criteria:</strong> Structured as testable Given/When/Then statements. For example, the save checkbox MUST NOT appear until upload succeeds.</li>
          <li><strong>Out of Scope:</strong> We strictly protect scope against AI auto-selection, AI rewriting, automatic merging, and silent submissions.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's see how Naukri could measure the impact of this feature through a controlled experiment.</div>
        """
    }
]
