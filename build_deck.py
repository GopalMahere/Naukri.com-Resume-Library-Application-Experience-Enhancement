# build_deck.py - Compiles styles, slides, and scripts into a single self-contained index.html

import os
import json
from styles import CSS_STYLES
from slides_discovery import SLIDES_DISCOVERY
from slides_research import SLIDES_RESEARCH
from slides_solution import SLIDES_SOLUTION
from slides_strategy import SLIDES_STRATEGY
from scripts_js import SCRIPTS_JS

STAGES_ORDER = [
    "Discover",
    "Define",
    "Research",
    "Validate",
    "Diagnose",
    "Assess",
    "Design",
    "Test",
    "Deliver"
]

def get_evidence_badge(evidence_type):
    if not evidence_type:
        return ""
    t = evidence_type.lower()
    if "personal" in t or "observation" in t:
        cls = "evidence-tag-obs"
    elif "survey" in t:
        cls = "evidence-tag-survey"
    elif "official" in t or "public" in t or "documentation" in t:
        cls = "evidence-tag-docs"
    elif "hypothesis" in t:
        cls = "evidence-tag-hypo"
    elif "validation" in t or "requires" in t:
        cls = "evidence-tag-val"
    elif "intro" in t:
        cls = "evidence-tag-intro"
    else:
        cls = "evidence-tag-sol"
    return f'<span class="evidence-tag {cls}">[{evidence_type.upper()}]</span>'

def render_stage_track(current_stage):
    if current_stage == "Appendix":
        return '<div class="stage-track"><span class="stage-step active" style="background:#4F46E5; color:white; border-color:#6366F1;">📚 Supporting Appendix</span></div>'
    if current_stage not in STAGES_ORDER:
        return f'<div class="stage-track"><span class="stage-step active">{current_stage}</span></div>'
    
    steps_html = []
    for idx, stg in enumerate(STAGES_ORDER):
        is_active = (stg == current_stage)
        active_class = "active" if is_active else ""
        steps_html.append(f'<span class="stage-step {active_class}">{stg}</span>')
        if idx < len(STAGES_ORDER) - 1:
            steps_html.append('<span class="stage-arrow">›</span>')
            
    return f'<div class="stage-track">{" ".join(steps_html)}</div>'

def build_presentation():
    # 16 Slides: 13 Core Presentation Slides + 3 Detailed Appendices
    all_slides = SLIDES_DISCOVERY + SLIDES_RESEARCH + SLIDES_SOLUTION + SLIDES_STRATEGY
    total_slides = len(all_slides)
    
    # Generate Slide Registry for JavaScript
    slide_registry = []
    for idx, slide in enumerate(all_slides):
        if idx < 13:
            slide_num_str = f"{idx + 1:02d}"
        else:
            appx_letter = chr(65 + idx - 13)
            slide_num_str = f"{idx + 1:02d} (Appx {appx_letter})"
            
        slide_registry.append({
            "id": slide["id"],
            "num": slide_num_str,
            "stage": slide.get("stage", "Discover"),
            "tag": slide["tag"],
            "title": slide["title"]
        })
    slide_registry_json = json.dumps(slide_registry, indent=2)
    
    # Generate Slides HTML & Grid Cards HTML
    slides_html_list = []
    grid_cards_list = []
    
    for idx, slide in enumerate(all_slides):
        is_first = (idx == 0)
        active_class = "active" if is_first else ""
        slide_stage = slide.get("stage", "Discover")
        evidence_badge_html = get_evidence_badge(slide.get("evidenceType", ""))
        stage_track_html = render_stage_track(slide_stage)
        
        if idx < 13:
            card_num_display = f"SLIDE {idx + 1:02d}"
            slide_pill_display = f"Slide {idx + 1:02d} / {total_slides:02d}"
        else:
            appx_letter = chr(65 + idx - 13)
            card_num_display = f"APPENDIX {appx_letter} (SLIDE {idx + 1:02d})"
            slide_pill_display = f"Slide {idx + 1:02d} / {total_slides:02d} • Appx {appx_letter}"
        
        # Grid Card HTML
        grid_cards_list.append(f"""
          <div class="grid-card {'active' if is_first else ''}" onclick="goToSlide({idx}); closeAllModals();">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="grid-card-num" style="{'color:#A78BFA;' if idx >= 13 else ''}">{card_num_display}</span>
              <span class="grid-card-tag">{slide_stage} • {slide['tag']}</span>
            </div>
            <div class="grid-card-title">{slide['title']}</div>
          </div>
        """)
        
        # Slide HTML
        slide_html = f"""
        <section class="slide {active_class}" id="{slide['id']}">
          <div class="slide-top-meta">
            <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
              <div class="slide-breadcrumb">
                <span style="color: var(--naukri-blue); font-weight:800;">NAUKRI INVESTIGATION</span>
                <span>›</span>
                <span>{slide['tag']}</span>
              </div>
              {stage_track_html}
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
              {evidence_badge_html}
              <div class="slide-number-pill">{slide_pill_display}</div>
            </div>
          </div>
          
          <div class="slide-heading-row">
            <h2 class="slide-title">{slide['title']}</h2>
            <p class="slide-subtitle">{slide['subtitle']}</p>
          </div>
          
          <div class="slide-body">
            {slide['content']}
          </div>
          
          <!-- Hidden Speaker Notes Data Container -->
          <div class="speaker-notes-data" style="display: none;">
            {slide['speakerNotes']}
          </div>
        </section>
        """
        slides_html_list.append(slide_html)
        
    slides_markup = "\n".join(slides_html_list)
    grid_markup = "\n".join(grid_cards_list)
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Naukri.com – Apply with the Right Resume | Candidate Experience Investigation & Product Improvement Proposal</title>
  <style>
{CSS_STYLES}
  </style>
</head>
<body>
  <div id="app">
    <!-- TOP HEADER BAR -->
    <header class="deck-header">
      <div class="brand-section">
        <div class="brand-logo">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <rect width="24" height="24" rx="5" fill="#1856EA"/>
            <path d="M6 17V7L11 13V7H13V17L8 11V17H6Z" fill="white"/>
            <circle cx="17.5" cy="7.5" r="1.5" fill="#38BDF8"/>
          </svg>
          <span>naukri<span style="color:#60A5FA;">.com</span></span>
        </div>
        <span class="brand-badge">Candidate Experience Investigation</span>
      </div>
      
      <div class="deck-title-center">
        <span class="slide-tag" id="header-slide-tag">{all_slides[0]['tag']}</span>
        <span class="slide-headline-indicator" id="header-slide-title">{all_slides[0]['title']}</span>
      </div>
      
      <div class="header-controls">
        <button class="header-btn" onclick="toggleEvaluatorGuide()" title="Proposal Context & Evaluator Brief">
          <span>ℹ️ Evaluator Guide</span> <span class="key-pill">O</span>
        </button>
        <button class="header-btn" id="btn-toggle-notes" onclick="toggleSpeakerNotes()" title="Toggle Speaker Notes">
          <span>💬 Speaker Notes</span> <span class="key-pill">N</span>
        </button>
        <button class="header-btn" onclick="toggleSlideGrid()" title="Overview of all slides">
          <span>🗂️ Overview</span> <span class="key-pill">G</span>
        </button>
        <button class="header-btn" onclick="toggleFullscreen()" title="Fullscreen presentation mode">
          <span>⛶ Fullscreen</span> <span class="key-pill">F</span>
        </button>
        <button class="header-btn" onclick="triggerPrint()" title="Print or save as PDF">
          <span>🖨️ Export</span>
        </button>
      </div>
    </header>
    
    <!-- MAIN 16:9 VIEWPORT STAGE -->
    <main class="deck-stage">
      <div id="presentation-frame">
        <div class="slides-wrapper">
{slides_markup}
        </div>
      </div>
    </main>
    
    <!-- BOTTOM FOOTER CONTROLS -->
    <footer class="deck-footer">
      <div class="footer-nav-group">
        <button class="nav-btn" id="prev-btn" onclick="prevSlide()" title="Previous Slide (Left Arrow)">
          ← Previous
        </button>
        <button class="nav-btn" id="next-btn" onclick="nextSlide()" title="Next Slide (Right Arrow or Space)">
          Next →
        </button>
        <div class="slide-indicator-text" id="footer-indicator">01 / {total_slides:02d}</div>
      </div>
      
      <div class="footer-progress-container">
        <div class="footer-progress-bar" id="footer-progress-bar"></div>
      </div>
      
      <div class="shortcut-pills">
        <span>Navigate:</span>
        <span class="key-pill">←</span>
        <span class="key-pill">→</span>
        <span class="key-pill">Space</span>
        <span>|</span>
        <span>Notes:</span>
        <span class="key-pill">N</span>
        <span>|</span>
        <span>Guide:</span>
        <span class="key-pill">O</span>
        <span>|</span>
        <span>Grid:</span>
        <span class="key-pill">G</span>
        <span>|</span>
        <span>Fullscreen:</span>
        <span class="key-pill">F</span>
      </div>
    </footer>
    
    <!-- SPEAKER NOTES DRAWER -->
    <div id="speaker-notes-panel">
      <div class="notes-header">
        <span>🎙️ Presenter Notes & Speaking Guidance</span>
        <button style="background:none; border:none; color:#93C5FD; font-size:16px; cursor:pointer;" onclick="toggleSpeakerNotes()">✕</button>
      </div>
      <div class="notes-body" id="notes-content-body">
        <!-- Injected dynamically via scripts_js.py -->
      </div>
    </div>
    
    <!-- SLIDE OVERVIEW GRID MODAL -->
    <div id="slide-grid-modal">
      <div class="grid-modal-header">
        <div class="grid-modal-title">Presentation Slide Index ({total_slides} Slides: 13 Core + 3 Appendices)</div>
        <button class="header-btn" onclick="toggleSlideGrid()">Close ✕</button>
      </div>
      <div class="grid-cards-container">
{grid_markup}
      </div>
    </div>

    <!-- EVALUATOR GUIDE MODAL (Accessible on demand via top header) -->
    <div id="evaluator-guide-modal">
      <div class="grid-modal-header">
        <div class="grid-modal-title">Proposal Overview & Evaluator Guide</div>
        <button class="header-btn" onclick="toggleEvaluatorGuide()">Close ✕</button>
      </div>
      <div style="background: var(--navy-dark); border: 1px solid rgba(255,255,255,0.15); border-radius: var(--radius-md); padding: 22px; color: var(--slate-200); overflow-y: auto; max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 14px;">
        <div style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">
          <span class="badge badge-blue" style="font-size: 11px; margin-bottom: 4px;">Independent Product Management Investigation</span>
          <h2 style="font-size: 20px; font-weight: 800; color: white;">Naukri.com – Apply with the Right Resume</h2>
          <div style="font-size: 12px; color: var(--slate-300); margin-top: 2px;">
            <strong>Prepared by:</strong> Aditya Sharma &nbsp;•&nbsp; <strong>Scope:</strong> Problem Discovery, Survey (N=100+), Journey Mapping, Root-Cause Diagnosis, PRD & Prototype
          </div>
        </div>
        
        <div>
          <h4 style="font-size: 12px; text-transform: uppercase; color: #60A5FA; letter-spacing: 0.5px; margin-bottom: 4px;">Investigation Context & Intent</h4>
          <p style="font-size: 12px; line-height: 1.5; color: var(--slate-200);">
            This project began with a candidate-side problem encountered during job applications across multiple role tracks. We investigated how candidates manage multiple resume versions, collected exploratory user research (N=100+), examined competitor platform capabilities (Naukri, LinkedIn, Indeed), assessed strategic alternatives, and developed a practical improvement proposal for Naukri.com featuring a candidate-controlled Resume Library.
          </p>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
          <div style="background: rgba(255,255,255,0.05); padding: 10px 12px; border-radius: 6px; border-left: 3px solid var(--naukri-blue);">
            <strong style="color: white; font-size: 11.5px;">Deck Structure (16 Slides):</strong>
            <ul style="font-size: 11px; margin-top: 4px; padding-left: 16px; line-height: 1.4; color: var(--slate-300);">
              <li>Slides 01–04: Discovery, Origin & Problem Definition (JTBD & Scope)</li>
              <li>Slides 05–08: Research Findings (N=100+), Journey Map, Validation & Benchmarks</li>
              <li>Slides 09–12: Alternatives, 3 Pillars, 11-Step Logic & Interactive Prototype</li>
              <li>Slide 13: MVP Prioritization, Experimentation & Final Recommendation</li>
              <li>Slides 14–16: Appendices A, B & C (Full survey data, citations, PRD glossary)</li>
            </ul>
          </div>
          
          <div style="background: rgba(255,255,255,0.05); padding: 10px 12px; border-radius: 6px; border-left: 3px solid var(--emerald-accent);">
            <strong style="color: white; font-size: 11.5px;">Navigation Keyboard Shortcuts:</strong>
            <ul style="font-size: 11px; margin-top: 4px; padding-left: 16px; line-height: 1.4; color: var(--slate-300);">
              <li><kbd class="key-pill">←</kbd> / <kbd class="key-pill">→</kbd> or <kbd class="key-pill">Space</kbd>: Step through slides</li>
              <li><kbd class="key-pill">N</kbd>: Open Speaker Notes (detailed talking points & timing)</li>
              <li><kbd class="key-pill">G</kbd>: Slide Overview Grid (jump to any slide)</li>
              <li><kbd class="key-pill">O</kbd> / <kbd class="key-pill">E</kbd>: Toggle this Evaluator Guide</li>
              <li><kbd class="key-pill">F</kbd>: Fullscreen Mode</li>
            </ul>
          </div>
        </div>
        
        <div style="text-align: right; margin-top: 4px;">
          <button class="nav-btn" style="background: var(--naukri-blue); padding: 6px 16px;" onclick="toggleEvaluatorGuide()">
            Resume Presentation →
          </button>
        </div>
      </div>
    </div>
  </div>
  
  <script>
const slideRegistry = {slide_registry_json};
const totalSlides = slideRegistry.length;

{SCRIPTS_JS}
  </script>
</body>
</html>
"""
    
    output_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Successfully compiled presentation to: {output_path} ({len(full_html)} bytes, {total_slides} slides)")

if __name__ == "__main__":
    build_presentation()
