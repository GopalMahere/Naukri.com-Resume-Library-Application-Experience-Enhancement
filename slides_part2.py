# slides_part2.py - Slides 6 to 10 (Benchmarking, Solution, Workflow, UI Mockups, PRD)

SLIDES_PART2 = [
    # SLIDE 6: COMPETITOR BENCHMARKING
    {
        "id": "slide-6",
        "number": "06",
        "tag": "Market Benchmarking",
        "title": "Competitor Benchmarking & Factual Market Evidence",
        "subtitle": "Analyzing documented product patterns across Naukri, LinkedIn, and Indeed based on official documentation",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 14px;">
          <!-- Comparison Table Card -->
          <div class="card" style="padding: 0; overflow: hidden; flex: 1;">
            <div class="table-scroll-wrap">
              <table class="deck-table">
                <thead>
                  <tr>
                    <th style="width: 25%;">Capability</th>
                    <th style="width: 28%; background: #EFF6FF; color: var(--navy-dark);">Naukri.com (Official Documented Info)</th>
                    <th style="width: 24%;">LinkedIn</th>
                    <th style="width: 23%;">Indeed India</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Multiple Profiles or Resumes</strong></td>
                    <td style="background: #F8FAFC;">
                      Up to <strong>5 profiles per username</strong> (1 resume per profile) in cited FastForward FAQ<a href="#ref-1" class="citation-mark">[1]</a>.<br>
                      <span style="font-size:10.5px; color:var(--slate-500);"><em>Note: FAQ specific to combining text/visual CVs; separate builder tools document varied limits (e.g. AI maker: 1 CV; online builder FAQ: up to 50)<a href="#ref-2" class="citation-mark">[2]</a>.</em></span>
                    </td>
                    <td>
                      Stores up to <strong>4 reusable</strong> recently uploaded resumes on account<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      Only <strong>1 resume file</strong> stored on account at a time; uploading a new file replaces existing<a href="#ref-5" class="citation-mark">[5]</a>.
                    </td>
                  </tr>
                  <tr>
                    <td><strong>Apply-Time Resume Selection</strong></td>
                    <td style="background: #F8FAFC;">
                      Needs validation across Naukri application types and mobile flows.
                    </td>
                    <td>
                      Supported in eligible LinkedIn applications (e.g. <em>Easy Apply</em> flows)<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      Existing profile resume can be used/selected during application<a href="#ref-4" class="citation-mark">[4]</a>.
                    </td>
                  </tr>
                  <tr>
                    <td><strong>Upload Another CV During Apply</strong></td>
                    <td style="background: #F8FAFC;">
                      Needs validation across direct and third-party application flows.
                    </td>
                    <td>
                      Supported natively within <em>Easy Apply</em>; not supported if redirected to employer site<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      Supported: candidate can upload a different resume file during application<a href="#ref-4" class="citation-mark">[4]</a>.
                    </td>
                  </tr>
                  <tr>
                    <td><strong>Persistent Reusable Named Library</strong></td>
                    <td style="background: #F8FAFC;">
                      Multiple profiles are documented; a unified named library within 1 profile needs validation.
                    </td>
                    <td>
                      Recent resume reuse is documented; custom naming capability not confirmed in referenced docs<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      One stored profile file at a time; new uploads replace old file<a href="#ref-5" class="citation-mark">[5]</a>.
                    </td>
                  </tr>
                  <tr>
                    <td><strong>Application-Specific Resume History</strong></td>
                    <td style="background: #F8FAFC;">
                      Verify current Naukri behaviour across application types.
                    </td>
                    <td>
                      LinkedIn documents viewing the resume submitted for Easy Apply jobs<a href="#ref-3" class="citation-mark">[3]</a>.
                    </td>
                    <td>
                      Verify exact application-history version tracking behaviour<a href="#ref-4" class="citation-mark">[4]</a>.
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          
          <!-- Recommended Defensible Competitor Conclusion -->
          <div class="card card-blue" style="padding: 12px 18px; display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 12px;">
              <div style="background: var(--naukri-blue); color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 15px; flex-shrink: 0;">
                💡
              </div>
              <div>
                <div style="font-weight: 800; font-size: 12.5px; color: var(--navy-dark);">Competitive Insight & Strategic Positioning</div>
                <div style="font-size: 11.5px; color: var(--slate-700); line-height: 1.45; margin-top: 2px;">
                  "Naukri already offers resume-related services and multiple-profile capabilities, while LinkedIn and Indeed demonstrate different forms of resume reuse and application-time uploading. The product opportunity is to explore a unified, independently managed resume library within one comprehensive candidate profile, with explicit application-time selection and non-destructive saving."
                </div>
              </div>
            </div>
            <div style="flex-shrink: 0; text-align: right; margin-left: 12px;">
              <span class="badge badge-gray" style="font-size: 10px;">Sources: Official Help Centers</span>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Defensible Competitor Positioning</h4>
        <p>A rigorous PM proposal must represent competitor capabilities accurately:</p>
        <ul>
          <li><strong>Naukri.com:</strong> Official FastForward FAQ documents that one username can have up to 5 profiles, with 1 resume per profile. However, this specifically relates to text and visual CVs, so we do not generalize it as a universal limitation. Additionally, Naukri's AI Resume Maker creates 1 resume, whereas an Online Builder FAQ mentions up to 50 resumes—these are separate tools, not one universal account rule.</li>
          <li><strong>LinkedIn:</strong> LinkedIn documents storing up to 4 recently uploaded reusable resumes for Easy Apply. Custom candidate naming is not confirmed in the cited documentation, and reuse does not apply to external employer redirects.</li>
          <li><strong>Indeed:</strong> In India, Indeed stores 1 resume on the profile (replacing previous uploads), but also allows uploading a different resume during an application.</li>
          <li><strong>The Takeaway:</strong> Our opportunity is not claiming an invented capability, but streamlining resume management into a single profile with transparent saving rules.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's examine the three architectural building blocks of our proposed solution.</div>
        """
    },

    # SLIDE 7: PROPOSED PRODUCT SOLUTION
    {
        "id": "slide-7",
        "number": "07",
        "tag": "Product Solution",
        "title": "Proposed Solution: The Three Core Building Blocks",
        "subtitle": "Architecting a unified, candidate-controlled ecosystem for multiple career opportunities",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 16px;">
          <!-- Three Pillars Grid -->
          <div class="grid-3" style="flex: 1;">
            <!-- Pillar 1 -->
            <div class="card" style="border-top: 4px solid var(--navy-dark); display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Component 01</span>
                <span class="badge badge-gray">Master Record</span>
              </div>
              <div class="card-title-lg">One Comprehensive Profile</div>
              <p class="card-text" style="margin-bottom: 10px;">
                The candidate maintains one central profile containing complete structured career information:
              </p>
              <ul style="font-size: 11.5px; color: var(--slate-700); padding-left: 16px; line-height: 1.45; margin-bottom: 10px;">
                <li>Personal and contact information</li>
                <li>Education and degrees</li>
                <li>Work experience & internships</li>
                <li>Projects, achievements, certifications & skills</li>
              </ul>
              <div style="margin-top: auto; background: var(--slate-50); padding: 7px 10px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600);">
                <strong>Value:</strong> Preserves single source of truth for recruiter search (Resdex).
              </div>
            </div>
            
            <!-- Pillar 2 -->
            <div class="card" style="border-top: 4px solid var(--naukri-blue); display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Component 02</span>
                <span class="badge badge-blue">Document Vault</span>
              </div>
              <div class="card-title-lg">Dedicated Resume Library</div>
              <p class="card-text" style="margin-bottom: 10px;">
                Candidates can upload and manage multiple independent resume files:
              </p>
              <div style="display: flex; flex-direction: column; gap: 5px; margin-bottom: 10px;">
                <div style="font-size: 11px; background: #F8FAFC; border: 1px solid var(--slate-200); padding: 4px 8px; border-radius: 4px; display: flex; justify-content: space-between;">
                  <span>💼 <strong>Product Management CV</strong></span>
                  <span style="color: var(--slate-400);">Product / APM</span>
                </div>
                <div style="font-size: 11px; background: #F8FAFC; border: 1px solid var(--slate-200); padding: 4px 8px; border-radius: 4px; display: flex; justify-content: space-between;">
                  <span>📊 <strong>Consulting CV</strong></span>
                  <span style="color: var(--slate-400);">Strategy Roles</span>
                </div>
                <div style="font-size: 11px; background: #F8FAFC; border: 1px solid var(--slate-200); padding: 4px 8px; border-radius: 4px; display: flex; justify-content: space-between;">
                  <span>⚙️ <strong>Operations CV</strong></span>
                  <span style="color: var(--slate-400);">Operations Roles</span>
                </div>
                <div style="font-size: 11px; background: #F8FAFC; border: 1px solid var(--slate-200); padding: 4px 8px; border-radius: 4px; display: flex; justify-content: space-between;">
                  <span>💻 <strong>Core Engineering CV</strong></span>
                  <span style="color: var(--slate-400);">Tech Roles</span>
                </div>
              </div>
              <div style="margin-top: auto; background: var(--slate-50); padding: 7px 10px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600);">
                <strong>Value:</strong> Custom names; changing or deleting one does not affect others.
              </div>
            </div>
            
            <!-- Pillar 3 -->
            <div class="card" style="border-top: 4px solid var(--emerald-accent); display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Component 03</span>
                <span class="badge badge-teal">Application Flow</span>
              </div>
              <div class="card-title-lg">Application-Time Selection</div>
              <p class="card-text" style="margin-bottom: 10px;">
                When applying, candidates choose which resume to submit:
              </p>
              <ul style="font-size: 11.5px; color: var(--slate-700); padding-left: 16px; line-height: 1.45; margin-bottom: 10px;">
                <li>Choose an existing saved document with 1 click</li>
                <li>Or upload a different document from device</li>
                <li><strong>Conditional save checkbox:</strong> Appears ONLY post-upload</li>
                <li>Review and verify before final submission</li>
              </ul>
              <div style="margin-top: auto; background: var(--slate-50); padding: 7px 10px; border-radius: 4px; font-size: 10.5px; color: var(--slate-600);">
                <strong>Value:</strong> Complete candidate control; zero forced context-switching.
              </div>
            </div>
          </div>
          
          <!-- System Guarantees Footer -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
            <div class="card card-tinted" style="padding: 10px 12px; display: flex; align-items: center; gap: 10px;">
              <span style="font-size: 16px;">🔒</span>
              <div style="font-size: 11px; color: var(--slate-700);">
                <strong>Candidate Privacy:</strong> Only the document selected for that application is submitted; other library resumes remain private.
              </div>
            </div>
            <div class="card card-tinted" style="padding: 10px 12px; display: flex; align-items: center; gap: 10px;">
              <span style="font-size: 16px;">🛡️</span>
              <div style="font-size: 11px; color: var(--slate-700);">
                <strong>Zero Auto-Overwrite:</strong> Uploading or updating one document never silently alters, replaces, or deletes another.
              </div>
            </div>
            <div class="card card-tinted" style="padding: 10px 12px; display: flex; align-items: center; gap: 10px;">
              <span style="font-size: 16px;">📜</span>
              <div style="font-size: 11px; color: var(--slate-700);">
                <strong>Application History:</strong> The submitted document version reference is recorded and preserved in application history.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>The Three Core Components</h4>
        <p>The solution architecture consists of three cohesive components:</p>
        <ul>
          <li><strong>Component 1: One Comprehensive Profile:</strong> We maintain a single structured master record for skills, education, and career experience. This protects Naukri's core search and matching infrastructure.</li>
          <li><strong>Component 2: Dedicated Resume Library:</strong> Rather than forcing multiple profile creations, we provide a clean, isolated document library where files have custom user-defined names.</li>
          <li><strong>Component 3: Application-Time Resume Selection:</strong> The candidate transparently picks which document to attach at the moment of apply.</li>
          <li><strong>Control Principle:</strong> The system preselects the candidate's designated default resume for convenience, while strictly requiring explicit review and confirmation before submission. If no default is designated, selection is required.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's follow the complete end-to-end workflow and its decision logic.</div>
        """
    },

    # SLIDE 8: END-TO-END WORKFLOW & DECISION ARCHITECTURE
    {
        "id": "slide-8",
        "number": "08",
        "tag": "System Architecture",
        "title": "End-to-End Product Workflow & Decision Logic",
        "subtitle": "Detailed 8-step sequence governing single-resume quick apply, selection, upload validation, and saving",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- 8-Step Sequential Pipeline Flow -->
          <div class="card" style="padding: 10px 14px;">
            <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 6px;">The 8-Step Product Workflow</div>
            <div style="display: flex; align-items: center; justify-content: space-between; position: relative;">
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 11%;">
                <div style="width: 22px; height: 22px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700;">1</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark); margin-top: 3px;">One Profile</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 11%;">
                <div style="width: 22px; height: 22px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700;">2</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark); margin-top: 3px;">Build Library</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 11%;">
                <div style="width: 22px; height: 22px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700;">3</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark); margin-top: 3px;">Click Apply</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 11%;">
                <div style="width: 22px; height: 22px; border-radius: 50%; background: var(--naukri-blue); color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700;">4</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--naukri-blue); margin-top: 3px;">Choose Resume</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 11%;">
                <div style="width: 22px; height: 22px; border-radius: 50%; background: var(--amber-accent); color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700;">5</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--amber-accent); margin-top: 3px;">Save Logic</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 11%;">
                <div style="width: 22px; height: 22px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700;">6</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark); margin-top: 3px;">Review & Submit</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 11%;">
                <div style="width: 22px; height: 22px; border-radius: 50%; background: var(--emerald-accent); color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700;">7</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--emerald-accent); margin-top: 3px;">History Snapshot</div>
              </div>
              <div style="color: var(--slate-300);">→</div>
              
              <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 11%;">
                <div style="width: 22px; height: 22px; border-radius: 50%; background: var(--navy-dark); color: white; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700;">8</div>
                <div style="font-size: 10.5px; font-weight: 700; color: var(--navy-dark); margin-top: 3px;">Manage Library</div>
              </div>
            </div>
          </div>
          
          <!-- Detailed Decision Branch Architecture -->
          <div style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 14px; flex: 1;">
            <!-- Left: Step 4 & Step 5 Logic -->
            <div class="card card-tinted" style="border-left: 4px solid var(--amber-accent); padding: 12px 16px;">
              <div class="card-header-sm">
                <span style="color: #B45309; font-weight: 800;">Step 4 & 5 Decision Logic: Crucial Product Rules</span>
                <span class="badge badge-amber">Decision Architecture</span>
              </div>
              
              <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 6px;">
                <!-- Scenario 1: One saved resume -->
                <div style="background: var(--pure-white); border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px 10px;">
                  <div style="font-size: 11.5px; font-weight: 700; color: var(--navy-dark);">Scenario 1: Candidate has 1 Saved Resume (Quick-Apply)</div>
                  <div style="font-size: 11px; color: var(--slate-600); margin-top: 2px;">
                    Preserve existing streamlined experience. Display current resume with a clear "Change Resume" link. No redundant selector required.
                  </div>
                </div>
                
                <!-- Gate: Pre-upload -->
                <div style="background: var(--pure-white); border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px 10px;">
                  <div style="font-size: 11.5px; font-weight: 700; color: var(--rose-accent);">Conditional Gate: Upload Success Required</div>
                  <div style="font-size: 11px; color: var(--slate-600); margin-top: 2px;">
                    The <code>Save to Resume Library</code> checkbox appears <strong>only after</strong> a new resume has uploaded successfully.
                  </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <div style="background: var(--pure-white); border: 1.5px solid var(--slate-300); border-radius: 6px; padding: 8px;">
                    <div style="font-size: 11px; font-weight: 700; color: var(--slate-700);">Case A: Checkbox Unchecked</div>
                    <div style="font-size: 10.5px; color: var(--slate-600); margin-top: 3px; line-height: 1.3;">
                      • Used for <em>current application only</em><br>
                      • Not added to library<br>
                      • Does not alter existing files
                    </div>
                  </div>
                  
                  <div style="background: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: 6px; padding: 8px;">
                    <div style="font-size: 11px; font-weight: 700; color: #166534;">Case B: Checkbox Checked</div>
                    <div style="font-size: 10.5px; color: #14532D; margin-top: 3px; line-height: 1.3;">
                      • Prompts for mandatory custom name<br>
                      • Added as new independent entry<br>
                      • <strong>Never overwrites</strong> older files
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Right: Edge Cases & Data Integrity -->
            <div class="card" style="padding: 12px 16px;">
              <div class="card-header-sm">Edge Cases & Data Integrity Rules</div>
              <div style="display: flex; flex-direction: column; gap: 7px; font-size: 11px; color: var(--slate-700);">
                <div style="padding-bottom: 5px; border-bottom: 1px solid var(--slate-100);">
                  <strong>Duplicate Filenames:</strong> Treat duplicate filenames as separate uploads. Never treat identical filenames as permission to overwrite.
                </div>
                <div style="padding-bottom: 5px; border-bottom: 1px solid var(--slate-100);">
                  <strong>Upload Failures:</strong> Show clear error message and retry option; withhold the save checkbox until successful upload.
                </div>
                <div style="padding-bottom: 5px; border-bottom: 1px solid var(--slate-100);">
                  <strong>Post-Apply Library Deletions:</strong> Deleting a library resume removes it from future apply flows, but <em>preserves</em> the previously submitted application record intact.
                </div>
                <div>
                  <strong>External Website Applications:</strong> For jobs redirecting to external company portals, clearly communicate that resume selection and storage behaviour depends on the third-party system.
                </div>
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Step-by-Step Workflow & Edge Cases</h4>
        <p>Notice the detailed handling of edge cases in this workflow:</p>
        <ul>
          <li><strong>Scenario 1 (One Saved Resume):</strong> If a candidate only maintains one resume, we preserve the existing quick-apply experience. We do not burden single-resume users with an unnecessary selector.</li>
          <li><strong>Scenario 2 (Multiple Resumes):</strong> If multiple resumes exist, the selector displays them clearly with their custom names and original filenames.</li>
          <li><strong>Upload & Save Gate:</strong> If the candidate uploads a new document, the save checkbox appears ONLY after the upload succeeds. If unchecked, it is application-only. If checked, they provide a custom name and it saves as an independent document.</li>
          <li><strong>Data Integrity:</strong> Deleting a resume from the library never erases that document from past submitted applications.</li>
        </ul>
        <div class='cue-box'><strong>Transition:</strong> Let's review the desktop screen mockups designed for this workflow.</div>
        """
    },

    # SLIDE 9: UX SCREEN DESIGNS
    {
        "id": "slide-9",
        "number": "09",
        "tag": "UX / UI Specification",
        "title": "Desktop Screen Designs: Six Core Product Interfaces",
        "subtitle": "Conceptual desktop web interfaces designed within modern job-portal design language",
        "content": """
        <div style="display: flex; flex-direction: column; height: 100%; gap: 12px;">
          <!-- 6 Screen Cards Gallery -->
          <div class="grid-3" style="flex: 1;">
            <!-- Screen 1 -->
            <div class="card card-tinted" style="display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Screen 01</span>
                <span class="badge badge-blue">Library UI</span>
              </div>
              <div style="font-weight: 700; font-size: 13px; color: var(--navy-dark); margin-bottom: 3px;">My Resume Library</div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px; margin: 4px 0; flex: 1; font-size: 10.5px;">
                <div style="font-weight: 700; color: var(--navy-dark); border-bottom: 1px solid var(--slate-100); padding-bottom: 3px; margin-bottom: 4px; display: flex; justify-content: space-between;">
                  <span>Resume Library (4)</span>
                  <span style="color: var(--naukri-blue); font-size: 9.5px;">+ Upload New</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 3px;">
                  <div style="background: #F8FAFC; padding: 3px 5px; border-radius: 4px; border: 1px solid #E2E8F0;">
                    <strong>Product Mgmt CV</strong> <span style="font-size:9px; color:var(--slate-500);">(PM_Resume.pdf)</span> • <span style="color: var(--emerald-accent); font-weight:700;">Default</span>
                  </div>
                  <div style="background: #F8FAFC; padding: 3px 5px; border-radius: 4px; border: 1px solid #E2E8F0;">
                    <strong>Consulting CV</strong> <span style="font-size:9px; color:var(--slate-500);">(Consulting_Resume.pdf)</span> • Sep 28
                  </div>
                  <div style="background: #F8FAFC; padding: 3px 5px; border-radius: 4px; border: 1px solid #E2E8F0;">
                    <strong>Operations CV</strong> <span style="font-size:9px; color:var(--slate-500);">(Operations_Resume.pdf)</span> • Aug 15
                  </div>
                  <div style="background: #F8FAFC; padding: 3px 5px; border-radius: 4px; border: 1px solid #E2E8F0;">
                    <strong>Core Engineering CV</strong> <span style="font-size:9px; color:var(--slate-500);">(Engineering_Resume.pdf)</span> • Jul 04
                  </div>
                </div>
              </div>
              <div style="font-size: 10px; color: var(--slate-500); line-height: 1.3;">
                Includes custom name, filename, preview. <em>Note: Rename, Delete, and Default preferences are phased capabilities (Phase 2/3) previewed in prototype.</em>
              </div>
            </div>
            
            <!-- Screen 2 -->
            <div class="card card-tinted" style="display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Screen 02</span>
                <span class="badge badge-blue">Selection UI</span>
              </div>
              <div style="font-weight: 700; font-size: 13px; color: var(--navy-dark); margin-bottom: 3px;">Apply & Select Resume</div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px; margin: 4px 0; flex: 1; font-size: 10.5px;">
                <div style="font-weight: 700; color: var(--navy-dark); margin-bottom: 4px;">Choose resume to submit:</div>
                <div style="display: flex; flex-direction: column; gap: 3px;">
                  <div style="background: var(--naukri-blue-light); border: 1px solid var(--naukri-blue); padding: 3px 5px; border-radius: 4px;">
                    🔘 <strong>Product Mgmt CV</strong> (PM_Resume.pdf)
                  </div>
                  <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 3px 5px; border-radius: 4px;">
                    ⚪ Consulting CV (Consulting_Resume.pdf)
                  </div>
                  <div style="background: #F8FAFC; border: 1px dashed #CBD5E1; padding: 3px 5px; border-radius: 4px;">
                    ⚪ <em>+ Upload a new resume</em>
                  </div>
                </div>
              </div>
              <div style="font-size: 10.5px; color: var(--slate-500); line-height: 1.3;">
                Single-choice radio options showing custom names and original filenames.
              </div>
            </div>
            
            <!-- Screen 3 -->
            <div class="card card-tinted" style="display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Screen 03</span>
                <span class="badge badge-teal">Conditional UI</span>
              </div>
              <div style="font-weight: 700; font-size: 13px; color: var(--navy-dark); margin-bottom: 3px;">Upload & Conditional Save</div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px; margin: 4px 0; flex: 1; font-size: 10.5px;">
                <div style="background: #ECFDF5; border: 1px solid #A7F3D0; padding: 3px 5px; border-radius: 4px; color: #065F46; font-weight: 600; margin-bottom: 4px;">
                  ✓ Upload complete: Product_Analyst.pdf
                </div>
                <div style="background: #F0FDF4; border: 1px dashed #86EFAC; padding: 5px; border-radius: 4px;">
                  <div style="font-weight: 700; color: #166534;">☑ Save this resume to Library</div>
                  <div style="margin-top: 3px; font-size: 9.5px; color: #15803D;">Name: [Product Analyst CV]</div>
                </div>
              </div>
              <div style="font-size: 10.5px; color: var(--slate-500); line-height: 1.3;">
                Save checkbox appears only post-upload. Checking reveals custom-name input.
              </div>
            </div>
            
            <!-- Screen 4 -->
            <div class="card card-tinted" style="display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Screen 04</span>
                <span class="badge badge-gray">Verification</span>
              </div>
              <div style="font-weight: 700; font-size: 13px; color: var(--navy-dark); margin-bottom: 3px;">Review Application</div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px; margin: 4px 0; flex: 1; font-size: 10.5px;">
                <div style="font-size: 10px; color: var(--slate-500);">Reviewing submission for:</div>
                <div style="font-weight: 700; color: var(--navy-dark);">Product Manager Intern</div>
                <div style="margin: 3px 0; padding: 3px 5px; background: #F8FAFC; border-radius: 4px; border: 1px solid var(--slate-200);">
                  📄 Attached: <strong>Product Management CV</strong>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 3px;">
                  <span style="color: var(--naukri-blue); font-size: 9.5px;">Change Resume</span>
                  <span style="background: var(--naukri-blue); color: white; padding: 2px 6px; border-radius: 4px; font-weight: 700; font-size: 9.5px;">Submit</span>
                </div>
              </div>
              <div style="font-size: 10.5px; color: var(--slate-500); line-height: 1.3;">
                Displays selected resume name, filename, preview card, and change resume link.
              </div>
            </div>
            
            <!-- Screen 5 -->
            <div class="card card-tinted" style="display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Screen 05</span>
                <span class="badge badge-teal">Confirmation</span>
              </div>
              <div style="font-weight: 700; font-size: 13px; color: var(--navy-dark); margin-bottom: 3px;">Application Submitted</div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px; margin: 4px 0; flex: 1; font-size: 10.5px; text-align: center;">
                <div style="font-size: 16px; margin-bottom: 2px;">🎉</div>
                <div style="font-weight: 700; color: var(--navy-dark);">Application Submitted!</div>
                <div style="font-size: 9.5px; color: var(--slate-500); margin: 3px 0;">Attached: Product Management CV</div>
                <div style="color: var(--naukri-blue); font-weight: 600; font-size: 10px; margin-top: 3px;">
                  View Application History →
                </div>
              </div>
              <div style="font-size: 10.5px; color: var(--slate-500); line-height: 1.3;">
                Confirmation screen showing company, role, date, and submitted resume.
              </div>
            </div>
            
            <!-- Screen 6 -->
            <div class="card card-tinted" style="display: flex; flex-direction: column;">
              <div class="card-header-sm">
                <span>Screen 06</span>
                <span class="badge badge-gray">History Log</span>
              </div>
              <div style="font-weight: 700; font-size: 13px; color: var(--navy-dark); margin-bottom: 3px;">Application History Log</div>
              <div style="background: white; border: 1px solid var(--slate-200); border-radius: 6px; padding: 8px; margin: 4px 0; flex: 1; font-size: 10.5px;">
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--slate-100); padding-bottom: 3px; margin-bottom: 3px;">
                  <strong>Example Tech</strong>
                  <span class="badge badge-blue" style="font-size: 8.5px;">PM CV (v1)</span>
                </div>
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--slate-100); padding-bottom: 3px; margin-bottom: 3px;">
                  <strong>McKinsey & Co</strong>
                  <span class="badge badge-gray" style="font-size: 8.5px;">Consulting CV</span>
                </div>
              </div>
              <div style="font-size: 10.5px; color: var(--slate-500); line-height: 1.3;">
                Records role, company, date, submitted resume, and immutable document reference.
              </div>
            </div>
          </div>
          
          <div style="background: var(--slate-100); padding: 7px 12px; border-radius: 4px; font-size: 11px; color: var(--slate-600); text-align: center;">
            <strong>Conceptual Mockup Notice:</strong> These interfaces are conceptual UI mockups illustrating the proposed Naukri feature enhancement.
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>Desktop UX/UI Screen Walkthrough</h4>
        <p>Here we see the six primary product touchpoints designed for desktop:</p>
        <ol>
          <li><strong>Screen 1 (Resume Library):</strong> Shows four resume cards with custom names, filenames, dates, preview, rename, and delete actions.</li>
          <li><strong>Screen 2 (Apply & Select):</strong> Single-choice radio options presenting saved CVs and an upload link.</li>
          <li><strong>Screen 3 (Upload & Conditional Save):</strong> Checkbox appears only post-upload. Checking it reveals the custom name input.</li>
          <li><strong>Screen 4 (Review):</strong> Allows the candidate to verify company, role, and the exact attached document before submission.</li>
          <li><strong>Screen 5 (Submitted):</strong> Confirmation indicating the specific document submitted.</li>
          <li><strong>Screen 6 (History):</strong> Audit record preserving the submitted document reference independently of future library changes.</li>
        </ol>
        <div class='cue-box'><strong>Transition:</strong> Let's formalize these specifications into a Product Requirements Document (PRD).</div>
        """
    },

    # SLIDE 10: PRD & MVP SCOPE
    {
        "id": "slide-10",
        "number": "10",
        "tag": "Product Requirements",
        "title": "Product Requirements Document (PRD) & MVP Scope",
        "subtitle": "Prioritized functional specifications and explicit scope boundaries for MVP release",
        "content": """
        <div style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 18px; height: 100%;">
          <!-- Left: Functional Requirements Matrix -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
            <div style="padding: 9px 14px; background: var(--slate-100); border-bottom: 1px solid var(--slate-200); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 11.5px; color: var(--navy-dark); text-transform: uppercase;">Functional Requirements Specification</span>
              <span class="badge badge-blue">MoSCoW Prioritized</span>
            </div>
            
            <div class="table-scroll-wrap" style="flex: 1;">
              <table class="deck-table" style="font-size: 11px;">
                <thead>
                  <tr>
                    <th style="width: 12%;">ID</th>
                    <th style="width: 60%;">Requirement</th>
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
                    <td>Allow custom names for saved resumes</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR03</strong></td>
                    <td>Allow selection of a saved resume during application</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR04</strong></td>
                    <td>Allow uploading a new resume during application</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR05</strong></td>
                    <td>Display the optional save checkbox only after a successful upload</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR06</strong></td>
                    <td>Save a newly uploaded resume as an additional independent entry</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR07</strong></td>
                    <td>Preserve unique document/version identifier in application history</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR08</strong></td>
                    <td>Support preview and confirmation before submission</td>
                    <td><span class="badge badge-must">Must</span></td>
                    <td>MVP</td>
                  </tr>
                  <tr>
                    <td><strong>FR09</strong></td>
                    <td>Support rename and delete management actions</td>
                    <td><span class="badge badge-should">Should</span></td>
                    <td>Phase 2</td>
                  </tr>
                  <tr>
                    <td><strong>FR10</strong></td>
                    <td>Support explicit replacement of an existing saved resume with confirmation</td>
                    <td><span class="badge badge-should">Should</span></td>
                    <td>Phase 2</td>
                  </tr>
                  <tr>
                    <td><strong>FR11</strong></td>
                    <td>Offer an optional default-resume preference for streamlined quick-apply</td>
                    <td><span class="badge badge-could">Could</span></td>
                    <td>Phase 3</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div style="padding: 6px 12px; background: var(--slate-50); border-top: 1px solid var(--slate-200); font-size: 10.5px; color: var(--slate-600);">
              <em>Note: FR09, FR10, and FR11 (Rename, Delete, and Default preference) are phased capabilities previewed in the interactive prototype as part of the full product vision.</em>
            </div>
          </div>
          
          <!-- Right: MVP Scope Boundaries (In-Scope vs Strictly Out-of-Scope) -->
          <div style="display: flex; flex-direction: column; gap: 12px;">
            <!-- In-Scope MVP Box -->
            <div class="card" style="border-left: 4px solid var(--emerald-accent); background: #F0FDF4; padding: 12px 14px;">
              <div class="card-header-sm">
                <span style="color: #065F46; font-weight: 800;">In-Scope for MVP</span>
                <span class="badge badge-teal">Core Delivery</span>
              </div>
              <ul style="font-size: 11px; color: #064E3B; padding-left: 16px; line-height: 1.4; margin-top: 4px;">
                <li>Multiple saved resumes with custom naming</li>
                <li>Resume selection during application</li>
                <li>Upload new resume during application</li>
                <li>Optional save checkbox after successful upload</li>
                <li>Non-destructive independent saving</li>
                <li>Review and confirmation screen</li>
                <li>Exact submitted resume recorded in application history</li>
              </ul>
            </div>
            
            <!-- Strictly Out-of-Scope Box -->
            <div class="card" style="border-left: 4px solid var(--rose-accent); background: #FFF5F5; padding: 12px 14px; flex: 1;">
              <div class="card-header-sm">
                <span style="color: #9F1239; font-weight: 800;">Explicitly Out of Scope for MVP</span>
                <span class="badge badge-red">Protected Scope</span>
              </div>
              <ul style="font-size: 11px; color: #4C0519; padding-left: 16px; line-height: 1.4; margin-top: 4px;">
                <li>❌ <strong>AI automatically choosing a resume:</strong> System does not pick for the candidate.</li>
                <li>❌ <strong>AI rewriting a resume:</strong> System does not generate or modify resume text.</li>
                <li>❌ <strong>Automatically merging resumes:</strong> Documents are never consolidated automatically.</li>
                <li>❌ <strong>Automatic profile modification:</strong> Uploads do not alter structured profile fields.</li>
                <li>❌ <strong>AI job-to-resume matching:</strong> Deferred to future exploration.</li>
                <li>❌ <strong>Automatic submission:</strong> Candidate confirmation is strictly required.</li>
              </ul>
              <div style="margin-top: 6px; font-size: 10.5px; color: #881337; font-weight: 600;">
                Core mandate: The feature remains entirely candidate-controlled.
              </div>
            </div>
          </div>
        </div>
        """,
        "speakerNotes": """
        <h4>PRD Prioritization & Scope Discipline</h4>
        <p>In this PRD, FR01 through FR08 are Must-Haves that establish the core loop of storing, selecting, uploading, non-destructive saving, and history retention.</p>
        <p>Notice the Out-of-Scope section on the right. We intentionally exclude AI auto-selection, AI rewriting, automatic document merging, and silent submissions.</p>
        <p>Keeping the feature candidate-controlled is essential for building user trust and ensuring that job seekers feel confident about exactly which document is delivered to recruiters.</p>
        <div class='cue-box'><strong>Transition:</strong> Let's see how this works in practice through our live interactive prototype.</div>
        """
    }
]
