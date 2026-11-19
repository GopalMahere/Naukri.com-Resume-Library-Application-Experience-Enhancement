# scripts_js.py - Presentation controls and Interactive Prototype JavaScript

SCRIPTS_JS = """
// PRESENTATION STATE
let currentSlideIndex = 0;
let isNotesOpen = false;
let isGridOpen = false;
let isGuideOpen = false;

// PROTOTYPE STATE
const initialResumes = [
  { id: 'res-1', name: 'Product Management CV', filename: 'PM_Resume.pdf', size: '142 KB', date: 'Oct 12, 2024', isDefault: true, summary: 'APM & Tech Lead experience, product teardowns, metrics & agile delivery.' },
  { id: 'res-2', name: 'Consulting CV', filename: 'Consulting_Resume.pdf', size: '128 KB', date: 'Sep 28, 2024', isDefault: false, summary: 'Strategy consulting case study finalist, financial modeling, market entry analysis.' },
  { id: 'res-3', name: 'Operations CV', filename: 'Operations_Resume.pdf', size: '115 KB', date: 'Aug 15, 2024', isDefault: false, summary: 'Supply chain optimization, logistics process re-engineering, inventory analytics.' },
  { id: 'res-4', name: 'Core Engineering CV', filename: 'Engineering_Resume.pdf', size: '156 KB', date: 'Jul 04, 2024', isDefault: false, summary: 'Distributed systems, microservices architecture, Python, algorithms & database tuning.' }
];

const initialApplications = [
  { id: 'app-1', company: 'Sample Consulting Firm (Demo)', role: 'Business Analyst', date: 'Sep 30, 2024', resumeName: 'Consulting CV', filename: 'Consulting_Resume.pdf', version: 'v1.0 (Immutable Reference)', status: 'Under Review' }
];

let protoResumes = JSON.parse(JSON.stringify(initialResumes));
let protoApplications = JSON.parse(JSON.stringify(initialApplications));
let protoActiveTab = 'library'; // 'library' | 'job' | 'apply' | 'history'
let protoApplySubStep = 'select'; // 'select' | 'upload' | 'review' | 'submitted'
let protoSelectedResumeId = 'res-1'; // 'res-1'..'res-4' or 'upload-new'
let protoUploadState = {
  filename: 'Product_Analyst_v2.pdf',
  isUploading: false,
  isUploaded: false,
  progress: 0,
  willSave: false,
  customName: 'Product Analyst CV'
};

// SLIDE DATA REGISTRY (Dynamically provided by build template)
if (typeof slideRegistry === 'undefined') {
  window.slideRegistry = [];
  window.totalSlides = document.querySelectorAll('.slide').length || 23;
}

// INITIALIZATION
document.addEventListener('DOMContentLoaded', () => {
  initPresentation();
  initPrototype();
});

function initPresentation() {
  goToSlide(0);
  
  // Keyboard Navigation
  window.addEventListener('keydown', (e) => {
    // Avoid interfering with form inputs in prototype
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
      return;
    }
    
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      e.preventDefault();
      nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      e.preventDefault();
      prevSlide();
    } else if (e.key === 'n' || e.key === 'N') {
      e.preventDefault();
      toggleSpeakerNotes();
    } else if (e.key === 'g' || e.key === 'G') {
      e.preventDefault();
      toggleSlideGrid();
    } else if (e.key === 'o' || e.key === 'O' || e.key === 'e' || e.key === 'E') {
      e.preventDefault();
      toggleEvaluatorGuide();
    } else if (e.key === 'f' || e.key === 'F') {
      e.preventDefault();
      toggleFullscreen();
    } else if (e.key === 'Escape') {
      closeAllModals();
    }
  });
}

function goToSlide(index) {
  if (index < 0 || index >= totalSlides) return;
  
  const slides = document.querySelectorAll('.slide');
  slides.forEach((s, idx) => {
    s.classList.remove('active', 'prev');
    if (idx === index) {
      s.classList.add('active');
    } else if (idx < index) {
      s.classList.add('prev');
    }
  });
  
  currentSlideIndex = index;
  updateControls();
  updateNotesContent();
  updateGridSelection();
  
  // If active slide contains the interactive prototype, ensure it is fresh & rendered
  const activeSlide = document.querySelector('.slide.active');
  if (activeSlide && activeSlide.querySelector('#proto-body-viewport')) {
    renderProtoView();
  }
}

function nextSlide() {
  if (currentSlideIndex < totalSlides - 1) {
    goToSlide(currentSlideIndex + 1);
  }
}

function prevSlide() {
  if (currentSlideIndex > 0) {
    goToSlide(currentSlideIndex - 1);
  }
}

function updateControls() {
  const current = slideRegistry[currentSlideIndex];
  if (!current) return;
  
  // Header updates
  const headerTag = document.getElementById('header-slide-tag');
  const headerTitle = document.getElementById('header-slide-title');
  if (headerTag) headerTag.textContent = current.tag;
  if (headerTitle) headerTitle.textContent = current.title;
  
  // Footer updates
  const footerIndicator = document.getElementById('footer-indicator');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  
  if (footerIndicator) footerIndicator.textContent = `${current.num} / ${totalSlides < 10 ? '0' + totalSlides : totalSlides}`;
  if (prevBtn) prevBtn.disabled = (currentSlideIndex === 0);
  if (nextBtn) nextBtn.disabled = (currentSlideIndex === totalSlides - 1);
  
  // Progress bar
  const progressBar = document.getElementById('footer-progress-bar');
  if (progressBar) {
    const progressPercent = ((currentSlideIndex + 1) / totalSlides) * 100;
    progressBar.style.width = `${progressPercent}%`;
  }
}

function updateNotesContent() {
  const activeSlide = document.querySelector('.slide.active');
  const notesPanel = document.getElementById('notes-content-body');
  if (activeSlide && notesPanel) {
    const hiddenNotes = activeSlide.querySelector('.speaker-notes-data');
    if (hiddenNotes) {
      notesPanel.innerHTML = hiddenNotes.innerHTML;
    } else {
      notesPanel.innerHTML = "<p>No speaker notes provided for this slide.</p>";
    }
  }
}

function toggleSpeakerNotes() {
  const panel = document.getElementById('speaker-notes-panel');
  const btn = document.getElementById('btn-toggle-notes');
  isNotesOpen = !isNotesOpen;
  if (isNotesOpen) {
    panel.classList.add('open');
    if (btn) btn.classList.add('active');
  } else {
    panel.classList.remove('open');
    if (btn) btn.classList.remove('active');
  }
}

function toggleSlideGrid() {
  const modal = document.getElementById('slide-grid-modal');
  isGridOpen = !isGridOpen;
  if (isGridOpen) {
    modal.classList.add('open');
    updateGridSelection();
  } else {
    modal.classList.remove('open');
  }
}

function toggleEvaluatorGuide() {
  const modal = document.getElementById('evaluator-guide-modal');
  if (!modal) return;
  isGuideOpen = !isGuideOpen;
  if (isGuideOpen) {
    modal.classList.add('open');
  } else {
    modal.classList.remove('open');
  }
}

function updateGridSelection() {
  const cards = document.querySelectorAll('.grid-card');
  cards.forEach((card, idx) => {
    if (idx === currentSlideIndex) {
      card.classList.add('active');
    } else {
      card.classList.remove('active');
    }
  });
}

function closeAllModals() {
  const gridModal = document.getElementById('slide-grid-modal');
  if (gridModal && isGridOpen) {
    gridModal.classList.remove('open');
    isGridOpen = false;
  }
  const guideModal = document.getElementById('evaluator-guide-modal');
  if (guideModal && isGuideOpen) {
    guideModal.classList.remove('open');
    isGuideOpen = false;
  }
  const notesPanel = document.getElementById('speaker-notes-panel');
  if (notesPanel && isNotesOpen) {
    notesPanel.classList.remove('open');
    const btn = document.getElementById('btn-toggle-notes');
    if (btn) btn.classList.remove('active');
    isNotesOpen = false;
  }
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(() => {});
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}

function triggerPrint() {
  window.print();
}

// -------------------------------------------------------------
// INTERACTIVE PROTOTYPE ENGINE (SLIDE 11 & EMBEDDED MODALS)
// -------------------------------------------------------------

function initPrototype() {
  renderProtoView();
}

function switchProtoView(tab, e) {
  if (e) e.stopPropagation();
  protoActiveTab = tab;
  
  document.querySelectorAll('.proto-tab').forEach(t => t.classList.remove('active'));
  const activeTabEl = document.getElementById(`tab-${tab}`);
  if (activeTabEl) activeTabEl.classList.add('active');
  
  renderProtoView();
}

function renderProtoView() {
  const viewport = document.getElementById('proto-body-viewport');
  if (!viewport) return;
  
  // Update counts
  const libCountEl = document.getElementById('proto-library-count');
  if (libCountEl) libCountEl.textContent = protoResumes.length;
  const histCountEl = document.getElementById('proto-history-count');
  if (histCountEl) histCountEl.textContent = protoApplications.length;
  
  if (protoActiveTab === 'library') {
    viewport.innerHTML = getProtoLibraryHTML();
  } else if (protoActiveTab === 'job') {
    viewport.innerHTML = getProtoJobHTML();
  } else if (protoActiveTab === 'apply') {
    viewport.innerHTML = getProtoApplyHTML();
  } else if (protoActiveTab === 'history') {
    viewport.innerHTML = getProtoHistoryHTML();
  }
}

function getProtoLibraryHTML() {
  let cardsHtml = protoResumes.map((res, i) => `
    <div class="proto-resume-card">
      <div class="card-top-line">
        <div class="resume-name-title">${res.name}</div>
        ${res.isDefault ? '<span class="badge badge-teal" style="font-size:10px;">Primary Default</span>' : ''}
      </div>
      <div class="file-meta-line">
        <span>📄 ${res.filename}</span>
        <span>•</span>
        <span>${res.size}</span>
        <span>•</span>
        <span>Updated ${res.date}</span>
      </div>
      <div style="font-size: 11px; color: var(--slate-600); line-height: 1.4; margin-bottom: 8px;">
        ${res.summary}
      </div>
      <div class="card-actions-row">
        <button class="card-action-btn" onclick="alertSim('Previewing ${res.filename}'); event.stopPropagation();">👁️ Preview</button>
        <button class="card-action-btn" onclick="renameSim('${res.id}'); event.stopPropagation();">✏️ Rename</button>
        ${!res.isDefault ? `<button class="card-action-btn btn-default-action" onclick="setDefaultSim('${res.id}', event);">⭐ Set as Default</button>` : ''}
        <button class="card-action-btn" onclick="alertSim('Downloaded ${res.filename}'); event.stopPropagation();">⬇️ Download</button>
        ${!res.isDefault ? `<button class="card-action-btn" style="color:var(--rose-accent);" onclick="deleteSim('${res.id}', event);">🗑️ Delete</button>` : ''}
      </div>
    </div>
  `).join('');

  return `
    <div style="display: flex; flex-direction: column; gap: 12px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
        <div>
          <h3 style="font-size: 15px; font-weight: 800; color: var(--navy-dark);">My Resume Library (${protoResumes.length})</h3>
          <p style="font-size: 11.5px; color: var(--slate-600);">Manage independent resumes for varied role opportunities.</p>
        </div>
        <div style="display:flex; gap: 8px;">
          <button class="nav-btn" style="background: var(--naukri-blue); font-size: 11.5px; padding: 5px 12px;" onclick="switchProtoView('job', event)">
            💼 View Jobs & Apply →
          </button>
        </div>
      </div>
      
      <div class="resume-card-grid">
        ${cardsHtml}
      </div>
      
      <div class="card card-blue" style="padding: 9px 12px; display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 15px;">💡</span>
        <div style="font-size: 11px; color: var(--slate-700);">
          <strong>Independent Storage:</strong> Resumes are stored as separate entries. Renaming, updating, or deleting one entry never modifies any other resume in your library.
        </div>
      </div>
    </div>
  `;
}

function setDefaultSim(id, e) {
  if (e) e.stopPropagation();
  protoResumes.forEach(r => {
    r.isDefault = (r.id === id);
  });
  protoSelectedResumeId = id; // Update preselection so entering apply preselects the newly set default
  renderProtoView();
}

function getProtoJobHTML() {
  return `
    <div style="display: flex; flex-direction: column; gap: 12px; max-width: 760px; margin: 0 auto;">
      <div class="card" style="padding: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">
          <div>
            <span class="badge badge-blue" style="margin-bottom: 4px;">Verified Opening</span>
            <h2 style="font-size: 17px; font-weight: 800; color: var(--navy-dark);">Product Manager Intern [Demo Job]</h2>
            <div style="font-size: 12.5px; font-weight: 600; color: var(--slate-700); margin-top: 2px;">
              Example Technologies (Sample Employer) • Bengaluru, India (Hybrid)
            </div>
          </div>
          <div style="text-align: right;">
            <div style="font-size: 13.5px; font-weight: 700; color: var(--emerald-accent);">₹60,000 - ₹80,000 / month</div>
            <div style="font-size: 10.5px; color: var(--slate-500);">Posted 2 days ago • 142 applicants</div>
          </div>
        </div>
        
        <div style="border-top: 1px solid var(--slate-100); padding-top: 8px; margin-top: 4px; font-size: 11.5px; color: var(--slate-600); line-height: 1.45;">
          <strong>About the Role:</strong> Example Technologies is looking for a proactive Product Management Intern to lead product discovery, drive user analytics, formulate PRDs, and coordinate with engineering sprints for our high-scale consumer platform.
        </div>
        
        <div style="margin-top: 8px; display: flex; gap: 6px; flex-wrap: wrap;">
          <span class="badge badge-gray">Product Strategy</span>
          <span class="badge badge-gray">SQL & Analytics</span>
          <span class="badge badge-gray">Agile PRD</span>
          <span class="badge badge-gray">Wireframing</span>
        </div>
        
        <div style="margin-top: 14px; display: flex; align-items: center; justify-content: space-between; padding-top: 10px; border-top: 1px solid var(--slate-200); flex-wrap: wrap; gap: 8px;">
          <div style="font-size: 11px; color: var(--slate-500);">
            ✓ Matches your profile credentials (Demo Profile: B.Tech Candidate)
          </div>
          <button class="nav-btn" style="background: var(--naukri-blue); padding: 7px 18px; font-size: 12.5px;" onclick="startProtoApply(event)">
            Apply with Naukri Profile →
          </button>
        </div>
      </div>
    </div>
  `;
}

function startProtoApply(e) {
  if (e) e.stopPropagation();
  protoActiveTab = 'apply';
  protoApplySubStep = 'select';
  
  // Dynamically select designated default resume; fallback to first resume if any
  const defaultResume = protoResumes.find(r => r.isDefault);
  protoSelectedResumeId = defaultResume ? defaultResume.id : (protoResumes.length > 0 ? protoResumes[0].id : 'upload-new');
  
  document.querySelectorAll('.proto-tab').forEach(t => t.classList.remove('active'));
  const applyTab = document.getElementById('tab-apply');
  if (applyTab) applyTab.classList.add('active');
  
  renderProtoView();
}

function getProtoApplyHTML() {
  if (protoApplySubStep === 'select') {
    return getApplySelectSubStepHTML();
  } else if (protoApplySubStep === 'upload') {
    return getApplyUploadSubStepHTML();
  } else if (protoApplySubStep === 'review') {
    return getApplyReviewSubStepHTML();
  } else if (protoApplySubStep === 'submitted') {
    return getApplySubmittedSubStepHTML();
  }
}

function getApplySelectSubStepHTML() {
  // Scenario 1: Exactly 1 saved resume -> Streamlined Quick-Apply pathway
  if (protoResumes.length === 1) {
    const onlyRes = protoResumes[0];
    return `
      <div style="max-width: 660px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px;">
        <div style="border-bottom: 1px solid var(--slate-200); padding-bottom: 8px;">
          <span class="badge badge-teal" style="font-size: 10px; margin-bottom: 4px;">Quick-Apply Mode (1 Saved Resume)</span>
          <h3 style="font-size: 16px; font-weight: 800; color: var(--navy-dark);">Review & Submit Application</h3>
          <p style="font-size: 12px; color: var(--slate-600); margin-top: 2px;">
            You have one resume in your library. It is pre-attached for a fast, streamlined application.
          </p>
        </div>
        
        <div class="card card-tinted" style="padding: 14px; border: 1.5px solid var(--naukri-blue); background: var(--naukri-blue-light);">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
              <div style="font-size: 13.5px; font-weight: 700; color: var(--navy-dark);">📄 ${onlyRes.name}</div>
              <div style="font-size: 11px; color: var(--slate-600); margin-top: 2px;">${onlyRes.filename} • ${onlyRes.size} • Updated ${onlyRes.date}</div>
            </div>
            <span class="badge badge-blue">Primary Profile Resume</span>
          </div>
        </div>
        
        <div style="background: var(--slate-50); border: 1px dashed var(--slate-300); padding: 10px 14px; border-radius: 6px; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 11.5px; color: var(--slate-600);">Need a different resume for this opportunity?</span>
          <button class="card-action-btn" style="color: var(--naukri-blue); font-weight: 700;" onclick="selectResumeOption('upload-new', event); continueFromSelection(event);">
            + Upload New Resume
          </button>
        </div>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px; padding-top: 10px; border-top: 1px solid var(--slate-200);">
          <button class="nav-btn" style="background: var(--slate-200); color: var(--slate-700);" onclick="switchProtoView('job', event)">
            Cancel
          </button>
          <button class="nav-btn" style="background: var(--naukri-blue); padding: 8px 24px;" onclick="selectResumeOption('${onlyRes.id}', event); continueFromSelection(event);">
            Continue to Review →
          </button>
        </div>
      </div>
    `;
  }

  // Scenario 2: Multiple saved resumes -> Multi-Resume Selector pathway
  let resumeOptions = protoResumes.map(r => `
    <div class="radio-select-item ${protoSelectedResumeId === r.id ? 'selected' : ''}" onclick="selectResumeOption('${r.id}', event)">
      <div class="radio-custom-indicator"></div>
      <div class="radio-item-info">
        <div class="radio-item-title">${r.name}</div>
        <div class="radio-item-sub">📄 ${r.filename} • ${r.size} • Updated ${r.date}</div>
      </div>
      ${r.isDefault ? '<span class="badge badge-gray" style="font-size:10px;">Default</span>' : ''}
    </div>
  `).join('');

  return `
    <div style="max-width: 660px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px;">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--slate-200); padding-bottom: 8px; flex-wrap: wrap; gap: 6px;">
        <div>
          <span style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue);">Step 1: Document Selection</span>
          <h3 style="font-size: 15.5px; font-weight: 800; color: var(--navy-dark);">Choose the Resume to Submit</h3>
        </div>
        <div style="font-size: 11px; color: var(--slate-500);">Applying for: <strong>Product Manager Intern</strong></div>
      </div>
      
      <p style="font-size: 11.5px; color: var(--slate-600);">
        Select the resume most appropriate for this opportunity, or upload an alternate version:
      </p>
      
      <div class="radio-select-group">
        ${resumeOptions}
        
        <!-- Upload New Radio Item -->
        <div class="radio-select-item ${protoSelectedResumeId === 'upload-new' ? 'selected' : ''}" onclick="selectResumeOption('upload-new', event)" style="border-style: dashed;">
          <div class="radio-custom-indicator"></div>
          <div class="radio-item-info">
            <div class="radio-item-title" style="color: var(--naukri-blue);">+ Upload a new resume for this application</div>
            <div class="radio-item-sub">Upload an alternate PDF or Word document from your device</div>
          </div>
        </div>
      </div>
      
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px; padding-top: 10px; border-top: 1px solid var(--slate-200);">
        <button class="nav-btn" style="background: var(--slate-200); color: var(--slate-700);" onclick="switchProtoView('job', event)">
          Cancel
        </button>
        <button class="nav-btn" style="background: var(--naukri-blue); padding: 7px 22px;" onclick="continueFromSelection(event)">
          Continue →
        </button>
      </div>
    </div>
  `;
}

function selectResumeOption(id, e) {
  if (e) e.stopPropagation();
  protoSelectedResumeId = id;
  renderProtoView();
}

function continueFromSelection(e) {
  if (e) e.stopPropagation();
  if (protoSelectedResumeId === 'upload-new') {
    protoApplySubStep = 'upload';
    protoUploadState.isUploaded = false;
    protoUploadState.isUploading = false;
    protoUploadState.progress = 0;
    protoUploadState.willSave = false;
    protoUploadState.customName = 'Product Analyst CV';
  } else {
    protoApplySubStep = 'review';
  }
  renderProtoView();
}

function getApplyUploadSubStepHTML() {
  const { isUploading, isUploaded, progress, willSave, customName } = protoUploadState;

  return `
    <div style="max-width: 660px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px;">
      <div style="border-bottom: 1px solid var(--slate-200); padding-bottom: 8px;">
        <span style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue);">Step 1b: Upload New Document</span>
        <h3 style="font-size: 15.5px; font-weight: 800; color: var(--navy-dark);">Upload a Resume for this Application</h3>
        <p style="font-size: 11.5px; color: var(--slate-600); margin-top: 2px;">
          Attach an alternate document specifically for <strong>Example Technologies</strong>.
        </p>
      </div>
      
      ${!isUploaded ? `
        <div class="upload-dropzone" onclick="triggerSimulatedUpload(event)">
          <div style="font-size: 26px; margin-bottom: 4px;">📄</div>
          <div style="font-weight: 700; font-size: 13px; color: var(--navy-dark);">
            ${isUploading ? 'Uploading & Validating Document...' : 'Simulate Selecting a Resume File'}
          </div>
          <div style="font-size: 11px; color: var(--slate-500); margin-top: 2px;">
            ${isUploading ? 'Simulating validation & file hash verification' : 'Preselected sample: Product_Analyst_v2.pdf (PDF up to 2MB)'}
          </div>
          
          ${isUploading ? `
            <div class="upload-progress-wrap">
              <div class="upload-progress-fill" style="width: ${progress}%;"></div>
            </div>
            <div style="font-size: 10.5px; font-weight: 700; color: var(--naukri-blue);">${progress}%</div>
          ` : `
            <button class="nav-btn" style="background: var(--naukri-blue); margin-top: 10px; font-size: 11.5px;" onclick="triggerSimulatedUpload(event)">
              Simulate File Upload (PDF)
            </button>
          `}
        </div>
      ` : `
        <div style="background: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: var(--radius-md); padding: 12px 14px; display: flex; align-items: center; justify-content: space-between;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="background: #22C55E; color: white; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px;">
              ✓
            </div>
            <div>
              <div style="font-weight: 700; font-size: 13px; color: #14532D;">Upload Successful: ${protoUploadState.filename}</div>
              <div style="font-size: 10.5px; color: #166534;">148 KB • PDF • Validated</div>
            </div>
          </div>
          <button class="card-action-btn" style="color: var(--slate-600);" onclick="reuploadSim(event)">
            Replace
          </button>
        </div>
      `}
      
      <!-- CONDITIONAL SAVE BOX (CRITICAL REQUIREMENT: APPEARS ONLY POST-UPLOAD) -->
      <div class="conditional-save-box ${isUploaded ? 'visible' : ''}">
        <label class="save-checkbox-label">
          <input type="checkbox" id="proto-save-checkbox" ${willSave ? 'checked' : ''} onchange="toggleSaveCheckbox(event)">
          <span>Save this resume to my Resume Library</span>
        </label>
        
        <div style="font-size: 11px; color: #166534; margin: 4px 0 0 28px;">
          ${willSave ? 
            '💾 Will be saved as a new independent library entry. It will NEVER overwrite any existing resume.' : 
            '📄 This resume will be used for the current application only. It will NOT be added to your library.'}
        </div>
        
        <!-- Custom Name Input Field (Revealed when checked, with MANDATORY validation) -->
        <div class="custom-name-field-row ${willSave ? 'visible' : ''}" style="margin-left: 28px;">
          <label style="font-size: 11px; font-weight: 700; color: #14532D;">
            Resume Name: <span style="color:#9F1239;">*</span>
          </label>
          <input type="text" class="custom-name-input ${willSave && !customName.trim() ? 'input-error' : ''}" id="proto-custom-name-input" value="${customName}" oninput="updateCustomName(event)" placeholder="e.g. Product Analyst CV">
          <div class="validation-error-msg ${willSave && !customName.trim() ? 'visible' : ''}" id="proto-name-error-msg">
            ⚠️ Custom resume name is required when saving to your library.
          </div>
          <span style="font-size: 10px; color: #15803D;">Name your document so you can identify and reuse it for future roles.</span>
        </div>
      </div>
      
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px; padding-top: 10px; border-top: 1px solid var(--slate-200);">
        <button class="nav-btn" style="background: var(--slate-200); color: var(--slate-700);" onclick="backToSelect(event)">
          ← Back to Selection
        </button>
        <button class="nav-btn" id="proto-continue-review-btn" style="background: var(--naukri-blue); padding: 7px 22px;" ${(!isUploaded || (willSave && !customName.trim())) ? 'disabled' : ''} onclick="continueToReview(event)">
          Continue to Review →
        </button>
      </div>
    </div>
  `;
}

function triggerSimulatedUpload(e) {
  if (e) e.stopPropagation();
  if (protoUploadState.isUploading) return;
  
  protoUploadState.isUploading = true;
  protoUploadState.progress = 0;
  renderProtoView();
  
  const interval = setInterval(() => {
    protoUploadState.progress += 25;
    if (protoUploadState.progress >= 100) {
      clearInterval(interval);
      protoUploadState.isUploading = false;
      protoUploadState.isUploaded = true;
      protoUploadState.progress = 100;
      renderProtoView();
    } else {
      renderProtoView();
    }
  }, 180);
}

function reuploadSim(e) {
  if (e) e.stopPropagation();
  protoUploadState.isUploaded = false;
  protoUploadState.isUploading = false;
  protoUploadState.progress = 0;
  protoUploadState.willSave = false;
  renderProtoView();
}

function toggleSaveCheckbox(e) {
  if (e) e.stopPropagation();
  const checkbox = document.getElementById('proto-save-checkbox');
  protoUploadState.willSave = checkbox ? checkbox.checked : false;
  if (!protoUploadState.willSave) {
    protoUploadState.customName = 'Product Analyst CV';
  }
  renderProtoView();
}

function updateCustomName(e) {
  if (e) e.stopPropagation();
  protoUploadState.customName = e.target.value;
  validateCustomNameInput();
}

function validateCustomNameInput() {
  const input = document.getElementById('proto-custom-name-input');
  const errorMsg = document.getElementById('proto-name-error-msg');
  const reviewBtn = document.getElementById('proto-continue-review-btn');
  if (!input) return true;
  
  const isValid = (!protoUploadState.willSave) || (protoUploadState.customName.trim().length > 0);
  
  if (!isValid) {
    input.classList.add('input-error');
    if (errorMsg) errorMsg.classList.add('visible');
    if (reviewBtn) reviewBtn.disabled = true;
    return false;
  } else {
    input.classList.remove('input-error');
    if (errorMsg) errorMsg.classList.remove('visible');
    if (reviewBtn && protoUploadState.isUploaded) reviewBtn.disabled = false;
    return true;
  }
}

function backToSelect(e) {
  if (e) e.stopPropagation();
  protoApplySubStep = 'select';
  renderProtoView();
}

function continueToReview(e) {
  if (e) e.stopPropagation();
  if (protoUploadState.willSave && !protoUploadState.customName.trim()) {
    validateCustomNameInput();
    return;
  }
  protoApplySubStep = 'review';
  renderProtoView();
}

function getApplyReviewSubStepHTML() {
  let resumeName = '';
  let filename = '';
  let size = '';
  let willSaveBadge = '';

  if (protoSelectedResumeId === 'upload-new') {
    resumeName = protoUploadState.willSave ? protoUploadState.customName.trim() : 'Newly Uploaded Resume (Application-Only)';
    filename = protoUploadState.filename;
    size = '148 KB';
    willSaveBadge = protoUploadState.willSave ? 
      '<span class="badge badge-teal">Will Save to Library as Independent Entry</span>' : 
      '<span class="badge badge-amber">Application Only (Not Added to Library)</span>';
  } else {
    const res = protoResumes.find(r => r.id === protoSelectedResumeId);
    resumeName = res ? res.name : 'Product Management CV';
    filename = res ? res.filename : 'PM_Resume.pdf';
    size = res ? res.size : '142 KB';
    willSaveBadge = '<span class="badge badge-blue">Saved Library Document</span>';
  }

  return `
    <div style="max-width: 660px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px;">
      <div style="border-bottom: 1px solid var(--slate-200); padding-bottom: 8px;">
        <span style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--naukri-blue);">Step 2: Review Before Submission</span>
        <h3 style="font-size: 15.5px; font-weight: 800; color: var(--navy-dark);">Review Your Application</h3>
        <p style="font-size: 11.5px; color: var(--slate-600); margin-top: 2px;">
          Confirm document details before submitting to <strong>Example Technologies</strong>.
        </p>
      </div>
      
      <div class="review-summary-card">
        <div class="review-detail-row">
          <span class="review-detail-label">Job Title:</span>
          <span class="review-detail-val">Product Manager Intern [Demo Job]</span>
        </div>
        <div class="review-detail-row">
          <span class="review-detail-label">Company:</span>
          <span class="review-detail-val">Example Technologies (Sample Employer)</span>
        </div>
        <div class="review-detail-row">
          <span class="review-detail-label">Selected Resume:</span>
          <span class="review-detail-val" style="color: var(--naukri-blue); font-weight:700;">${resumeName}</span>
        </div>
        <div class="review-detail-row">
          <span class="review-detail-label">Original Filename:</span>
          <span class="review-detail-val">📄 ${filename} (${size})</span>
        </div>
        <div class="review-detail-row">
          <span class="review-detail-label">Library Storage Policy:</span>
          <div>${willSaveBadge}</div>
        </div>
      </div>
      
      <!-- Visual Resume Preview Card -->
      <div class="card card-tinted" style="padding: 12px 14px; border: 1.5px solid var(--slate-200);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
          <span style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--slate-500);">Document Preview</span>
          <button class="card-action-btn" onclick="startProtoApply(event)">Change Resume ↺</button>
        </div>
        <div style="background: white; border: 1px solid var(--slate-200); border-radius: 4px; padding: 8px 10px; font-size: 11px; color: var(--slate-600); line-height: 1.4;">
          <div style="font-weight: 700; color: var(--navy-dark);">Sample Candidate — Demo Profile</div>
          <div>B.Tech in Computer Science, Example University • Minor in Economics</div>
          <div style="margin-top: 2px; color: var(--slate-500);">
            Highlights: Product teardown competition winner, user interview synthesis, SQL dashboards, agile sprint delivery.
          </div>
        </div>
      </div>
      
      <div class="card card-blue" style="padding: 9px 12px; display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 15px;">🔒</span>
        <div style="font-size: 11px; color: var(--slate-700);">
          <strong>Submission Privacy:</strong> Example Technologies recruiters receive only this selected resume. Your other saved resumes remain private.
        </div>
      </div>
      
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 4px; padding-top: 10px; border-top: 1px solid var(--slate-200);">
        <button class="nav-btn" style="background: var(--slate-200); color: var(--slate-700);" onclick="backFromReview(event)">
          ← Back
        </button>
        <button class="nav-btn" style="background: var(--emerald-accent); font-size: 13px; padding: 7px 22px;" onclick="submitProtoApplication(event)">
          Submit Application ✓
        </button>
      </div>
    </div>
  `;
}

function backFromReview(e) {
  if (e) e.stopPropagation();
  if (protoSelectedResumeId === 'upload-new') {
    protoApplySubStep = 'upload';
  } else {
    protoApplySubStep = 'select';
  }
  renderProtoView();
}

function submitProtoApplication(e) {
  if (e) e.stopPropagation();
  
  let finalResumeName = '';
  let finalFilename = '';

  if (protoSelectedResumeId === 'upload-new') {
    finalFilename = protoUploadState.filename;
    if (protoUploadState.willSave) {
      finalResumeName = protoUploadState.customName.trim() || 'Product Analyst CV';
      // Add to Library as a brand new independent entry!
      protoResumes.unshift({
        id: `res-${Date.now()}`,
        name: finalResumeName,
        filename: finalFilename,
        size: '148 KB',
        date: 'Just Now',
        isDefault: false,
        summary: 'Targeted custom upload for analytical & APM opportunities.'
      });
    } else {
      finalResumeName = 'Uploaded Resume (Application-Only)';
      // Case A: DO NOT SAVE TO LIBRARY. Library remains unchanged!
    }
  } else {
    const res = protoResumes.find(r => r.id === protoSelectedResumeId);
    finalResumeName = res ? res.name : 'Product Management CV';
    finalFilename = res ? res.filename : 'PM_Resume.pdf';
  }

  // Record into simulated immutable application history
  protoApplications.unshift({
    id: `app-${Date.now()}`,
    company: 'Example Technologies (Sample Employer)',
    role: 'Product Manager Intern [Demo Job]',
    date: 'Just Now',
    resumeName: finalResumeName,
    filename: finalFilename,
    version: 'v1.0 (Immutable Reference)',
    status: 'Application Submitted'
  });

  protoApplySubStep = 'submitted';
  renderProtoView();
}

function getApplySubmittedSubStepHTML() {
  const latestApp = protoApplications[0];

  return `
    <div style="max-width: 580px; margin: 16px auto; text-align: center; display: flex; flex-direction: column; gap: 12px;">
      <div style="background: #ECFDF5; border: 2px solid #6EE7B7; width: 56px; height: 56px; border-radius: 50%; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 28px; color: #059669;">
        ✓
      </div>
      
      <h2 style="font-size: 20px; font-weight: 800; color: var(--navy-dark);">Application Submitted Successfully!</h2>
      <p style="font-size: 12px; color: var(--slate-600);">
        Your application for <strong>Product Manager Intern [Demo Job]</strong> at <strong>Example Technologies (Sample Employer)</strong> has been received.
      </p>
      
      <div class="card card-tinted" style="padding: 14px; text-align: left; margin: 6px 0;">
        <div style="font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--slate-500); margin-bottom: 4px;">Confirmation Details</div>
        <div style="display: flex; justify-content: space-between; font-size: 12px; padding: 3px 0;">
          <span style="color: var(--slate-500);">Company:</span>
          <strong>Example Technologies (Sample Employer)</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 12px; padding: 3px 0;">
          <span style="color: var(--slate-500);">Role:</span>
          <span>Product Manager Intern [Demo Job]</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 12px; padding: 3px 0;">
          <span style="color: var(--slate-500);">Submitted Resume:</span>
          <strong style="color: var(--naukri-blue);">${latestApp.resumeName}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 12px; padding: 3px 0;">
          <span style="color: var(--slate-500);">Document Attached:</span>
          <span>📄 ${latestApp.filename}</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 12px; padding: 3px 0;">
          <span style="color: var(--slate-500);">Document Reference:</span>
          <span class="badge badge-teal">${latestApp.version}</span>
        </div>
      </div>
      
      <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
        <button class="nav-btn" style="background: var(--naukri-blue); padding: 7px 16px; font-size: 12px;" onclick="switchProtoView('history', event)">
          View in Application History 🕒
        </button>
        <button class="nav-btn" style="background: var(--slate-200); color: var(--slate-700); padding: 7px 16px; font-size: 12px;" onclick="switchProtoView('library', event)">
          Return to Resume Library 📁
        </button>
      </div>
    </div>
  `;
}

function getProtoHistoryHTML() {
  let rows = protoApplications.map(app => `
    <tr>
      <td><strong>${app.company}</strong></td>
      <td>${app.role}</td>
      <td><span class="badge badge-blue">${app.resumeName}</span></td>
      <td>📄 ${app.filename}</td>
      <td><span class="badge badge-teal" style="font-size:9.5px;">${app.version}</span></td>
      <td><span class="badge badge-gray">${app.status}</span></td>
    </tr>
  `).join('');

  return `
    <div style="display: flex; flex-direction: column; gap: 12px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px;">
        <div>
          <h3 style="font-size: 15px; font-weight: 800; color: var(--navy-dark);">Application History Log</h3>
          <p style="font-size: 11.5px; color: var(--slate-600);">
            Records role, company, date, submitted resume name, and retained document version reference.
          </p>
        </div>
        <button class="nav-btn" style="background: var(--naukri-blue); font-size: 11px; padding: 5px 12px;" onclick="switchProtoView('library', event)">
          Check Resume Library (${protoResumes.length}) →
        </button>
      </div>
      
      <div class="card" style="padding: 0; overflow: hidden;">
        <div class="table-scroll-wrap">
          <table class="deck-table" style="font-size: 11.5px;">
            <thead>
              <tr>
                <th>Company</th>
                <th>Role</th>
                <th>Submitted Resume Name</th>
                <th>Original File</th>
                <th>Document Reference</th>
                <th>Application Status</th>
              </tr>
            </thead>
            <tbody>
              ${rows}
            </tbody>
          </table>
        </div>
      </div>
      
      <div class="card card-tinted" style="padding: 9px 12px; font-size: 11px; color: var(--slate-600);">
        <strong>Data Integrity Requirement:</strong> Deleting or renaming items in the Resume Library does not alter previously submitted application records.
      </div>
    </div>
  `;
}

// SIMULATOR PRESET HELPERS
function runProtoPreset(scenario, e) {
  if (e) e.stopPropagation();
  
  document.querySelectorAll('.scenario-btn').forEach(b => b.classList.remove('active'));
  
  if (scenario === 'SINGLE') {
    const btn = document.getElementById('scenario-preset-single');
    if (btn) btn.classList.add('active');
    // Set 1 resume in library
    protoResumes = [
      { id: 'res-1', name: 'Product Management CV', filename: 'PM_Resume.pdf', size: '142 KB', date: 'Oct 12, 2024', isDefault: true, summary: 'APM & Tech Lead experience, product teardowns, metrics & agile delivery.' }
    ];
    protoActiveTab = 'apply';
    protoApplySubStep = 'select';
    protoSelectedResumeId = 'res-1';
    switchProtoView('apply');
  } else if (scenario === 'C') {
    const btn = document.getElementById('scenario-preset-c');
    if (btn) btn.classList.add('active');
    protoResumes = JSON.parse(JSON.stringify(initialResumes));
    protoActiveTab = 'apply';
    protoApplySubStep = 'select';
    const defRes = protoResumes.find(r => r.isDefault);
    protoSelectedResumeId = defRes ? defRes.id : (protoResumes.length > 0 ? protoResumes[0].id : 'upload-new');
    switchProtoView('apply');
  } else if (scenario === 'A') {
    const btn = document.getElementById('scenario-preset-a');
    if (btn) btn.classList.add('active');
    protoResumes = JSON.parse(JSON.stringify(initialResumes));
    protoActiveTab = 'apply';
    protoApplySubStep = 'upload';
    protoSelectedResumeId = 'upload-new';
    protoUploadState = {
      filename: 'Product_Analyst_v2.pdf',
      isUploading: false,
      isUploaded: true,
      progress: 100,
      willSave: false, // UNCHECKED!
      customName: 'Product Analyst CV'
    };
    switchProtoView('apply');
  } else if (scenario === 'B') {
    const btn = document.getElementById('scenario-preset-b');
    if (btn) btn.classList.add('active');
    protoResumes = JSON.parse(JSON.stringify(initialResumes));
    protoActiveTab = 'apply';
    protoApplySubStep = 'upload';
    protoSelectedResumeId = 'upload-new';
    protoUploadState = {
      filename: 'Product_Analyst_v2.pdf',
      isUploading: false,
      isUploaded: true,
      progress: 100,
      willSave: true, // CHECKED!
      customName: 'Product Analyst CV'
    };
    switchProtoView('apply');
  }
}

function resetProtoState(e) {
  if (e) e.stopPropagation();
  protoResumes = JSON.parse(JSON.stringify(initialResumes));
  protoApplications = JSON.parse(JSON.stringify(initialApplications));
  protoActiveTab = 'library';
  protoApplySubStep = 'select';
  const defRes = protoResumes.find(r => r.isDefault);
  protoSelectedResumeId = defRes ? defRes.id : (protoResumes.length > 0 ? protoResumes[0].id : 'upload-new');
  protoUploadState = {
    filename: 'Product_Analyst_v2.pdf',
    isUploading: false,
    isUploaded: false,
    progress: 0,
    willSave: false,
    customName: 'Product Analyst CV'
  };
  document.querySelectorAll('.scenario-btn').forEach(b => b.classList.remove('active'));
  switchProtoView('library');
}

function alertSim(msg) {
  alert(`[Prototype Simulation] ${msg}`);
}

function renameSim(id) {
  const res = protoResumes.find(r => r.id === id);
  if (!res) return;
  const newName = prompt(`Enter new custom name for ${res.name}:`, res.name);
  if (newName && newName.trim()) {
    res.name = newName.trim();
    renderProtoView();
  }
}

function deleteSim(id, e) {
  if (e) e.stopPropagation();
  if (confirm('Are you sure you want to delete this resume from your library? Past applications referencing this document will remain intact.')) {
    protoResumes = protoResumes.filter(r => r.id !== id);
    renderProtoView();
  }
}
"""
