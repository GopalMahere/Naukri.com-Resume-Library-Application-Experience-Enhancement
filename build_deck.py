# build_deck.py - Compiles styles, slides, and scripts into a single self-contained index.html

import os
import json
from styles import CSS_STYLES
from slides_part1 import SLIDES_PART1
from slides_part2 import SLIDES_PART2
from slides_part3 import SLIDES_PART3
from scripts_js import SCRIPTS_JS

def build_presentation():
    # 15 Core Slides starting directly with Title Cover!
    all_slides = SLIDES_PART1 + SLIDES_PART2 + SLIDES_PART3
    total_slides = len(all_slides)
    
    # Generate Slide Registry for JavaScript
    slide_registry = [
        {
            "id": slide["id"],
            "num": f"{idx + 1:02d}",
            "tag": slide["tag"],
            "title": slide["title"]
        }
        for idx, slide in enumerate(all_slides)
    ]
    slide_registry_json = json.dumps(slide_registry, indent=2)
    
    # Generate Slides HTML & Grid Cards HTML
    slides_html_list = []
    grid_cards_list = []
    
    for idx, slide in enumerate(all_slides):
        is_first = (idx == 0)
        active_class = "active" if is_first else ""
        slide_num = f"{idx + 1:02d}"
        
        # Grid Card HTML
        grid_cards_list.append(f"""
          <div class="grid-card {'active' if is_first else ''}" onclick="goToSlide({idx}); closeAllModals();">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="grid-card-num">SLIDE {slide_num}</span>
              <span class="grid-card-tag">{slide['tag']}</span>
            </div>
            <div class="grid-card-title">{slide['title']}</div>
          </div>
        """)
        
        # Slide HTML
        slide_html = f"""
        <section class="slide {active_class}" id="{slide['id']}">
          <div class="slide-top-meta">
            <div class="slide-breadcrumb">
              <span style="color: var(--naukri-blue); font-weight:800;">NAUKRI PRODUCT PROPOSAL</span>
              <span>›</span>
              <span>{slide['tag']}</span>
            </div>
            <div class="slide-number-pill">Slide {slide_num} / {total_slides:02d}</div>
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
  <title>One Profile, Multiple Resumes | Naukri.com Product Strategy Proposal</title>
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
        <span class="brand-badge">Product Strategy Case Study</span>
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
        <div class="grid-modal-title">Presentation Slide Index ({total_slides} Slides)</div>
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
      <div style="background: var(--navy-dark); border: 1px solid rgba(255,255,255,0.15); border-radius: var(--radius-md); padding: 24px; color: var(--slate-200); overflow-y: auto; max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px;">
        <div style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
          <span class="badge badge-blue" style="font-size: 11px; margin-bottom: 6px;">Independent Product Management Case Study</span>
          <h2 style="font-size: 20px; font-weight: 800; color: white;">One Profile, Multiple Resumes for Naukri.com</h2>
          <div style="font-size: 12.5px; color: var(--slate-300); margin-top: 4px;">
            <strong>Prepared by:</strong> Aditya Sharma &nbsp;•&nbsp; <strong>Scope:</strong> User Research, Product Discovery, UX Design, PRD, and Interactive Prototype
          </div>
        </div>
        
        <div>
          <h4 style="font-size: 13px; text-transform: uppercase; color: #60A5FA; letter-spacing: 0.5px; margin-bottom: 6px;">Core Hypothesis & Problem Statement</h4>
          <p style="font-size: 12.5px; line-height: 1.5; color: var(--slate-200);">
            Candidates who apply across multiple job categories often maintain different resume versions, but managing and switching between those documents during the application journey can create unnecessary friction. This deck proposes giving candidates a centralized, candidate-controlled resume library that allows them to select the right resume at the moment of application, without repeatedly replacing their primary resume or maintaining multiple profiles.
          </p>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 6px; border-left: 3px solid var(--naukri-blue);">
            <strong style="color: white; font-size: 12px;">Deck Structure (15 Slides):</strong>
            <ul style="font-size: 11.5px; margin-top: 6px; padding-left: 18px; line-height: 1.45; color: var(--slate-300);">
              <li>Slides 1–5: Problem Discovery & 45-Candidate Survey</li>
              <li>Slide 6: Competitor Benchmarking (Naukri, LinkedIn, Indeed)</li>
              <li>Slides 7–10: 3 Pillars, 8-Step Flow, Desktop Screens, PRD</li>
              <li>Slide 11: Live Interactive Candidate Simulator</li>
              <li>Slides 12–15: A/B Testing, Funnel Model, Roadmap & Appendix</li>
            </ul>
          </div>
          
          <div style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 6px; border-left: 3px solid var(--emerald-accent);">
            <strong style="color: white; font-size: 12px;">Navigation Quick Reference:</strong>
            <ul style="font-size: 11.5px; margin-top: 6px; padding-left: 18px; line-height: 1.45; color: var(--slate-300);">
              <li><kbd class="key-pill">←</kbd> / <kbd class="key-pill">→</kbd> or <kbd class="key-pill">Space</kbd>: Step through slides</li>
              <li><kbd class="key-pill">N</kbd>: Open Speaker Notes (detailed talking points)</li>
              <li><kbd class="key-pill">G</kbd>: Slide Overview Grid (jump to any slide)</li>
              <li><kbd class="key-pill">O</kbd>: Toggle this Evaluator Guide</li>
              <li><kbd class="key-pill">F</kbd>: Fullscreen Mode</li>
            </ul>
          </div>
        </div>
        
        <div style="text-align: right; margin-top: 6px;">
          <button class="nav-btn" style="background: var(--naukri-blue); padding: 8px 20px;" onclick="toggleEvaluatorGuide()">
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
        
    print(f"Successfully compiled presentation to: {output_path} ({len(full_html)} bytes)")

if __name__ == "__main__":
    build_presentation()
