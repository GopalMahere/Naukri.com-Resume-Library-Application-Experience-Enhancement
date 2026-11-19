# styles.py - CSS styling for the Naukri.com "One Profile, Multiple Resumes" presentation

CSS_STYLES = """
:root {
  --navy-dark: #0B1B3D;
  --navy-mid: #13274F;
  --navy-light: #1E3A8A;
  --naukri-blue: #1856EA;
  --naukri-blue-hover: #1244C5;
  --naukri-blue-light: #EEF4FF;
  --naukri-blue-border: #C7DBFF;
  --teal-accent: #0D9488;
  --teal-light: #F0FDFA;
  --teal-border: #99F6E4;
  --emerald-accent: #059669;
  --emerald-light: #ECFDF5;
  --amber-accent: #D97706;
  --amber-light: #FFFBEB;
  --amber-border: #FDE68A;
  --rose-accent: #E11D48;
  --rose-light: #FFF1F2;
  --slate-900: #0F172A;
  --slate-800: #1E293B;
  --slate-700: #334155;
  --slate-600: #475569;
  --slate-500: #64748B;
  --slate-400: #94A3B8;
  --slate-300: #CBD5E1;
  --slate-200: #E2E8F0;
  --slate-100: #F1F5F9;
  --slate-50: #F8FAFC;
  --pure-white: #FFFFFF;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-xl: 18px;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  width: 100%;
  max-width: 100vw;
  overflow-x: hidden;
  font-family: var(--font-sans);
  background: #091224;
  color: var(--slate-800);
  line-height: 1.45;
  user-select: none;
}

body {
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

/* APP WRAPPER */
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
  max-width: 100vw;
  position: relative;
  background: #07101E;
  overflow-x: hidden;
}

/* TOP HEADER BAR */
header.deck-header {
  height: 52px;
  background: var(--navy-dark);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  color: var(--pure-white);
  z-index: 50;
  flex-shrink: 0;
  width: 100%;
  max-width: 100vw;
  overflow: hidden;
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  font-size: 15px;
  letter-spacing: -0.3px;
  color: var(--pure-white);
}

.brand-badge {
  background: rgba(24, 86, 234, 0.25);
  border: 1px solid rgba(24, 86, 234, 0.5);
  color: #93C5FD;
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 12px;
  font-weight: 600;
  letter-spacing: 0.2px;
}

.deck-title-center {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--slate-300);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.slide-tag {
  background: rgba(255, 255, 255, 0.1);
  padding: 3px 10px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  color: #60A5FA;
  flex-shrink: 0;
}

.slide-headline-indicator {
  font-weight: 600;
  color: var(--pure-white);
  white-space: nowrap;
  max-width: 400px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.header-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--slate-200);
  font-size: 12px;
  padding: 5px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-weight: 500;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.header-btn:hover {
  background: rgba(255, 255, 255, 0.18);
  color: var(--pure-white);
  border-color: rgba(255, 255, 255, 0.3);
}

.header-btn.active {
  background: var(--naukri-blue);
  color: var(--pure-white);
  border-color: var(--naukri-blue);
}

/* MAIN STAGE VIEWPORT (16:9 CONTAINER) */
main.deck-stage {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px 24px;
  position: relative;
  overflow: hidden;
  background: radial-gradient(circle at 50% 20%, #0F1E3D 0%, #060D1A 100%);
  width: 100%;
  max-width: 100vw;
}

#presentation-frame {
  width: 100%;
  max-width: 1400px;
  aspect-ratio: 16 / 9;
  max-height: calc(100vh - 120px);
  background: var(--pure-white);
  border-radius: var(--radius-lg);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

/* SLIDES WRAPPER */
.slides-wrapper {
  flex: 1;
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding: 34px 44px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateX(30px);
  transition: opacity 0.28s ease, transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.28s;
  display: flex;
  flex-direction: column;
  background: var(--pure-white);
  overflow-y: auto;
  user-select: text;
}

.slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateX(0);
  z-index: 10;
}

.slide.prev {
  transform: translateX(-30px);
}

/* SLIDE COMMON HEADER */
.slide-top-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
  flex-shrink: 0;
}

.slide-breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--naukri-blue);
}

.slide-number-pill {
  font-size: 12px;
  font-weight: 700;
  color: var(--slate-500);
  background: var(--slate-100);
  padding: 3px 10px;
  border-radius: 12px;
}

.slide-heading-row {
  margin-bottom: 16px;
  flex-shrink: 0;
}

.slide-title {
  font-size: 25px;
  font-weight: 800;
  color: var(--navy-dark);
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.slide-subtitle {
  font-size: 13.5px;
  color: var(--slate-600);
  margin-top: 4px;
  font-weight: 400;
}

.slide-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
  position: relative;
  width: 100%;
}

/* BOTTOM PRESENTATION CONTROLS */
footer.deck-footer {
  height: 52px;
  background: var(--navy-dark);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  color: var(--pure-white);
  z-index: 50;
  flex-shrink: 0;
  width: 100%;
  max-width: 100vw;
}

.footer-nav-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-btn {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--pure-white);
  font-size: 13px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.nav-btn:hover:not(:disabled) {
  background: var(--naukri-blue);
  border-color: var(--naukri-blue);
}

.nav-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.slide-indicator-text {
  font-size: 13px;
  font-weight: 600;
  color: var(--slate-300);
  min-width: 80px;
  text-align: center;
}

.footer-progress-container {
  flex: 1;
  max-width: 360px;
  height: 5px;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 3px;
  margin: 0 20px;
  overflow: hidden;
  position: relative;
}

.footer-progress-bar {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #3B82F6, #60A5FA);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.shortcut-pills {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  color: var(--slate-400);
}

.key-pill {
  background: rgba(255, 255, 255, 0.1);
  padding: 2px 6px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 10px;
  color: var(--slate-300);
  border: 1px solid rgba(255, 255, 255, 0.15);
}

/* SPEAKER NOTES DRAWER */
#speaker-notes-panel {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 230px;
  background: #0B162C;
  border-top: 2px solid var(--naukri-blue);
  box-shadow: 0 -10px 25px rgba(0, 0, 0, 0.4);
  color: var(--slate-100);
  z-index: 60;
  transform: translateY(100%);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}

#speaker-notes-panel.open {
  transform: translateY(0);
}

.notes-header {
  height: 38px;
  background: rgba(0, 0, 0, 0.25);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  font-size: 12px;
  font-weight: 700;
  color: #93C5FD;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.notes-body {
  flex: 1;
  padding: 16px 24px;
  overflow-y: auto;
  font-size: 13.5px;
  line-height: 1.6;
  color: #E2E8F0;
}

.notes-body h4 {
  font-size: 12px;
  color: #60A5FA;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}

.notes-body ul {
  padding-left: 20px;
  margin-bottom: 12px;
}

.notes-body li {
  margin-bottom: 4px;
}

.notes-body .cue-box {
  background: rgba(24, 86, 234, 0.15);
  border-left: 3px solid #3B82F6;
  padding: 8px 12px;
  border-radius: 4px;
  font-size: 12px;
  color: #BFDBFE;
  margin-top: 10px;
}

/* OVERVIEW & EVALUATOR MODALS */
#slide-grid-modal, #evaluator-guide-modal {
  position: fixed;
  inset: 0;
  background: rgba(7, 16, 30, 0.88);
  backdrop-filter: blur(8px);
  z-index: 100;
  display: none;
  flex-direction: column;
  padding: 24px 32px;
}

#slide-grid-modal.open, #evaluator-guide-modal.open {
  display: flex;
}

.grid-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  color: var(--pure-white);
}

.grid-modal-title {
  font-size: 19px;
  font-weight: 700;
}

.grid-cards-container {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 16px;
  overflow-y: auto;
  padding-right: 8px;
}

.grid-card {
  background: var(--navy-dark);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-md);
  padding: 14px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: all 0.15s ease;
  color: var(--slate-200);
}

.grid-card:hover {
  border-color: var(--naukri-blue);
  background: #152C5B;
  transform: translateY(-2px);
}

.grid-card.active {
  border-color: #60A5FA;
  box-shadow: 0 0 0 2px #60A5FA;
  background: #18336A;
}

.grid-card-num {
  font-size: 11px;
  font-weight: 700;
  color: #93C5FD;
}

.grid-card-tag {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--slate-400);
}

.grid-card-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--pure-white);
  line-height: 1.3;
}

/* REUSABLE CARD & GRID COMPONENTS */
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: 100%;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  width: 100%;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  width: 100%;
}

.card {
  background: var(--pure-white);
  border: 1px solid var(--slate-200);
  border-radius: var(--radius-md);
  padding: 18px;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  max-width: 100%;
}

.card-tinted {
  background: var(--slate-50);
  border: 1px solid var(--slate-200);
}

.card-blue {
  background: var(--naukri-blue-light);
  border: 1px solid var(--naukri-blue-border);
}

.card-amber {
  background: var(--amber-light);
  border: 1px solid var(--amber-border);
}

.card-teal {
  background: var(--teal-light);
  border: 1px solid var(--teal-border);
}

.card-header-sm {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  color: var(--slate-500);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-title-lg {
  font-size: 15.5px;
  font-weight: 700;
  color: var(--navy-dark);
  margin-bottom: 8px;
  line-height: 1.3;
}

.card-text {
  font-size: 13px;
  color: var(--slate-600);
  line-height: 1.5;
}

/* PILLS & BADGES */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  white-space: nowrap;
}

.badge-blue {
  background: #DBEAFE;
  color: #1E40AF;
}

.badge-teal {
  background: #CCFBF1;
  color: #115E59;
}

.badge-amber {
  background: #FEF3C7;
  color: #92400E;
}

.badge-red {
  background: #FFE4E6;
  color: #9F1239;
}

.badge-gray {
  background: #F1F5F9;
  color: #475569;
}

.badge-must {
  background: #FEE2E2;
  color: #991B1B;
  font-weight: 700;
}

.badge-should {
  background: #FEF3C7;
  color: #92400E;
  font-weight: 700;
}

.badge-could {
  background: #E0E7FF;
  color: #3730A3;
  font-weight: 700;
}

/* EVIDENCE TAG CLASSIFICATIONS */
.evidence-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 9.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 2px 7px;
  border-radius: 4px;
  border: 1px solid transparent;
  white-space: nowrap;
}

.evidence-tag-obs {
  background: #F1F5F9;
  color: #334155;
  border-color: #CBD5E1;
}

.evidence-tag-survey {
  background: #FEF3C7;
  color: #92400E;
  border-color: #FCD34D;
}

.evidence-tag-docs {
  background: #EFF6FF;
  color: #1E40AF;
  border-color: #BFDBFE;
}

.evidence-tag-hypo {
  background: #F3E8FF;
  color: #6B21A8;
  border-color: #D8B4FE;
}

.evidence-tag-sol {
  background: #ECFDF5;
  color: #065F46;
  border-color: #A7F3D0;
}

.evidence-tag-val {
  background: #FFF1F2;
  color: #9F1239;
  border-color: #FECDD3;
}

/* PM LIFECYCLE MINI TRACK IN SLIDE TOP META */
.stage-track {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 10px;
  color: var(--slate-400);
  font-weight: 600;
  background: var(--slate-50);
  border: 1px solid var(--slate-200);
  padding: 2px 8px;
  border-radius: 12px;
}

.stage-step {
  padding: 2px 6px;
  border-radius: 3px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.stage-step.active {
  background: var(--naukri-blue);
  color: white;
  font-weight: 700;
}

.stage-arrow {
  color: var(--slate-300);
  font-size: 9px;
}

/* COVER SLIDE COMPOSITION */
.cover-layout {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 28px;
  height: 100%;
  align-items: center;
}

.cover-hero-box {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cover-illustration-wrap {
  display: flex;
  flex-direction: column;
  gap: 10px;
  background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
  border: 1.5px solid var(--naukri-blue-border);
  border-radius: var(--radius-lg);
  padding: 18px;
  box-shadow: var(--shadow-md);
  position: relative;
}

/* STAT CALLOUT BOX */
.stat-box {
  background: var(--pure-white);
  border: 1px solid var(--slate-200);
  border-radius: var(--radius-md);
  padding: 16px;
  text-align: center;
  box-shadow: var(--shadow-sm);
  max-width: 100%;
}

.stat-value {
  font-size: 32px;
  font-weight: 800;
  color: var(--naukri-blue);
  line-height: 1;
  margin-bottom: 6px;
  letter-spacing: -1px;
}

.stat-label {
  font-size: 12px;
  font-weight: 600;
  color: var(--slate-700);
  margin-bottom: 4px;
}

.stat-sub {
  font-size: 11px;
  color: var(--slate-500);
  line-height: 1.3;
}

/* TABLES */
.table-scroll-wrap {
  width: 100%;
  max-width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.deck-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12.5px;
  text-align: left;
}

.deck-table th {
  background: var(--slate-100);
  color: var(--navy-dark);
  font-weight: 700;
  padding: 10px 14px;
  border-bottom: 2px solid var(--slate-300);
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  white-space: nowrap;
}

.deck-table td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--slate-200);
  color: var(--slate-700);
  line-height: 1.4;
  vertical-align: top;
}

.deck-table tr:hover td {
  background: var(--slate-50);
}

.citation-mark {
  font-size: 10px;
  color: var(--naukri-blue);
  font-weight: 700;
  cursor: help;
  vertical-align: super;
  text-decoration: none;
}

/* HORIZONTAL BAR CHART */
.bar-chart-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
}

.bar-row {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
}

.bar-label {
  width: 130px;
  font-size: 12px;
  font-weight: 600;
  color: var(--slate-700);
  text-align: right;
  flex-shrink: 0;
}

.bar-track {
  flex: 1;
  height: 24px;
  background: var(--slate-100);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
}

.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #2563EB, #3B82F6);
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 8px;
  color: var(--pure-white);
  font-size: 11px;
  font-weight: 700;
  transition: width 0.8s ease;
}

.bar-fill.bar-accent {
  background: linear-gradient(90deg, #1856EA, #1D4ED8);
}

/* FLOWCHART STEPS */
.flow-row {
  display: flex;
  align-items: stretch;
  gap: 10px;
  width: 100%;
  margin-top: 10px;
}

.flow-step {
  flex: 1;
  background: var(--pure-white);
  border: 1px solid var(--slate-200);
  border-radius: var(--radius-md);
  padding: 12px 14px;
  position: relative;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-sm);
}

.flow-step.active-step {
  border-color: var(--naukri-blue);
  box-shadow: 0 0 0 1px var(--naukri-blue);
  background: #F8FAFC;
}

.flow-step.warning-step {
  border-color: var(--amber-accent);
  background: #FFFDF5;
}

.flow-step-num {
  font-size: 10px;
  font-weight: 800;
  color: var(--naukri-blue);
  text-transform: uppercase;
  margin-bottom: 4px;
  letter-spacing: 0.5px;
}

.flow-step-title {
  font-size: 12.5px;
  font-weight: 700;
  color: var(--navy-dark);
  margin-bottom: 4px;
}

.flow-step-desc {
  font-size: 11px;
  color: var(--slate-500);
  line-height: 1.35;
}

.flow-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--slate-400);
  font-size: 18px;
  flex-shrink: 0;
}

/* INTERACTIVE PROTOTYPE STYLES (Slide 11) */
.prototype-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  background: #F1F5F9;
  border: 1px solid var(--slate-300);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.proto-top-nav {
  height: 44px;
  background: var(--navy-dark);
  color: var(--pure-white);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  font-size: 12px;
  flex-shrink: 0;
}

.proto-logo-badge {
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
}

.proto-user-tag {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--slate-300);
}

.proto-tab-bar {
  background: var(--pure-white);
  border-bottom: 1px solid var(--slate-200);
  display: flex;
  align-items: center;
  padding: 0 16px;
  gap: 20px;
  height: 38px;
  flex-shrink: 0;
  overflow-x: auto;
}

.proto-tab {
  font-size: 12px;
  font-weight: 600;
  color: var(--slate-600);
  padding: 8px 4px;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}

.proto-tab.active {
  color: var(--naukri-blue);
  border-bottom-color: var(--naukri-blue);
}

.proto-tab-count {
  background: var(--slate-100);
  padding: 1px 6px;
  border-radius: 10px;
  font-size: 10px;
}

.proto-body {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
  position: relative;
  background: #F8FAFC;
}

.proto-scenario-bar {
  background: #0F172A;
  color: var(--pure-white);
  padding: 8px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11.5px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  flex-wrap: wrap;
  gap: 8px;
}

.proto-scenario-buttons {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.scenario-btn {
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: var(--pure-white);
  font-size: 11px;
  padding: 4px 10px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.15s;
  white-space: nowrap;
}

.scenario-btn:hover {
  background: var(--naukri-blue);
  border-color: var(--naukri-blue);
}

.scenario-btn.active {
  background: var(--naukri-blue);
  font-weight: 700;
}

/* RESUME CARDS */
.resume-card-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  width: 100%;
}

.proto-resume-card {
  background: var(--pure-white);
  border: 1px solid var(--slate-200);
  border-radius: var(--radius-md);
  padding: 14px;
  display: flex;
  flex-direction: column;
  position: relative;
  box-shadow: var(--shadow-sm);
  transition: all 0.15s ease;
}

.proto-resume-card:hover {
  border-color: var(--naukri-blue-border);
  box-shadow: var(--shadow-md);
}

.card-top-line {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 6px;
  flex-wrap: wrap;
  gap: 4px;
}

.resume-name-title {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--navy-dark);
}

.file-meta-line {
  font-size: 11px;
  color: var(--slate-500);
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.card-actions-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: auto;
  padding-top: 10px;
  border-top: 1px solid var(--slate-100);
  flex-wrap: wrap;
}

.card-action-btn {
  font-size: 11px;
  color: var(--slate-600);
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 3px 6px;
  border-radius: 4px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.card-action-btn:hover {
  background: var(--slate-100);
  color: var(--naukri-blue);
}

.card-action-btn.btn-default-action {
  color: var(--teal-accent);
  font-weight: 600;
}

.card-action-btn.btn-default-action:hover {
  background: var(--teal-light);
}

/* RADIO SELECTION LIST */
.radio-select-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 14px 0;
  width: 100%;
}

.radio-select-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border: 1.5px solid var(--slate-200);
  border-radius: var(--radius-md);
  background: var(--pure-white);
  cursor: pointer;
  transition: all 0.15s ease;
  width: 100%;
}

.radio-select-item:hover {
  border-color: var(--naukri-blue-border);
  background: #FAF5FF;
}

.radio-select-item.selected {
  border-color: var(--naukri-blue);
  background: var(--naukri-blue-light);
}

.radio-custom-indicator {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 2px solid var(--slate-300);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.radio-select-item.selected .radio-custom-indicator {
  border-color: var(--naukri-blue);
}

.radio-select-item.selected .radio-custom-indicator::after {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--naukri-blue);
}

.radio-item-info {
  flex: 1;
}

.radio-item-title {
  font-size: 13px;
  font-weight: 700;
  color: var(--navy-dark);
}

.radio-item-sub {
  font-size: 11px;
  color: var(--slate-500);
}

/* UPLOAD SIMULATION BOX */
.upload-dropzone {
  border: 2px dashed var(--slate-300);
  border-radius: var(--radius-md);
  padding: 20px;
  text-align: center;
  background: var(--slate-50);
  cursor: pointer;
  transition: all 0.15s;
  width: 100%;
}

.upload-dropzone:hover {
  border-color: var(--naukri-blue);
  background: var(--naukri-blue-light);
}

.upload-progress-wrap {
  width: 100%;
  height: 8px;
  background: var(--slate-200);
  border-radius: 4px;
  margin: 12px 0 6px;
  overflow: hidden;
}

.upload-progress-fill {
  height: 100%;
  width: 0%;
  background: var(--naukri-blue);
  border-radius: 4px;
  transition: width 0.3s ease;
}

/* CONDITIONAL SAVE BOX & VALIDATION */
.conditional-save-box {
  background: #F0FDF4;
  border: 1.5px solid #86EFAC;
  border-radius: var(--radius-md);
  padding: 14px 16px;
  margin-top: 14px;
  display: none;
  animation: fadeIn 0.3s ease;
  width: 100%;
}

.conditional-save-box.visible {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}

.save-checkbox-label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  font-weight: 700;
  color: #166534;
  cursor: pointer;
}

.save-checkbox-label input[type="checkbox"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: var(--emerald-accent);
}

.custom-name-field-row {
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px dashed #86EFAC;
  display: none;
}

.custom-name-field-row.visible {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.custom-name-input {
  width: 100%;
  padding: 8px 12px;
  border: 1.5px solid #86EFAC;
  border-radius: 6px;
  font-size: 13px;
  color: var(--slate-800);
  outline: none;
  background: var(--pure-white);
  transition: border-color 0.15s;
}

.custom-name-input:focus {
  border-color: var(--emerald-accent);
  box-shadow: 0 0 0 2px rgba(5, 150, 105, 0.2);
}

.custom-name-input.input-error {
  border-color: var(--rose-accent) !important;
  background: #FFF5F5 !important;
}

.validation-error-msg {
  color: #9F1239;
  font-size: 11.5px;
  font-weight: 600;
  display: none;
  margin-top: 2px;
}

.validation-error-msg.visible {
  display: block;
}

/* REVIEW CARD */
.review-summary-card {
  background: var(--pure-white);
  border: 1px solid var(--slate-200);
  border-radius: var(--radius-md);
  padding: 16px;
  margin-bottom: 14px;
  width: 100%;
}

.review-detail-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  font-size: 12.5px;
  border-bottom: 1px solid var(--slate-100);
  gap: 8px;
}

.review-detail-row:last-child {
  border-bottom: none;
}

.review-detail-label {
  color: var(--slate-500);
}

.review-detail-val {
  font-weight: 600;
  color: var(--navy-dark);
  text-align: right;
}

/* ======================================================== */
/* STRICT RESPONSIVE DESIGN (320px, 375px, 390px, 768px, 1024px) */
/* ======================================================== */

@media (max-width: 1024px) {
  html, body {
    overflow-y: auto !important;
    overflow-x: hidden !important;
    height: auto !important;
    width: 100% !important;
    max-width: 100vw !important;
  }
  
  #app {
    height: auto !important;
    min-height: 100vh;
    width: 100% !important;
    max-width: 100vw !important;
    overflow-x: hidden !important;
  }
  
  main.deck-stage {
    padding: 10px !important;
    height: auto !important;
    overflow: visible !important;
    display: block !important;
    width: 100% !important;
    max-width: 100vw !important;
  }
  
  #presentation-frame {
    aspect-ratio: auto !important;
    max-height: none !important;
    height: auto !important;
    min-height: calc(100vh - 110px);
    width: 100% !important;
    max-width: 100% !important;
    border-radius: var(--radius-md);
    overflow: visible !important;
  }
  
  .slides-wrapper {
    height: auto !important;
    min-height: 560px;
    position: relative;
    overflow: visible !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  
  .slide {
    position: relative !important;
    top: auto !important;
    left: auto !important;
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    min-height: 560px;
    padding: 20px 16px !important;
    transform: none !important;
    display: none;
    overflow: visible !important;
  }
  
  .slide.active {
    display: flex !important;
  }
  
  .slide.prev {
    display: none !important;
  }
  
  .grid-2, .grid-3, .grid-4 {
    grid-template-columns: 1fr !important;
    gap: 12px !important;
    width: 100% !important;
  }
  
  .cover-layout {
    grid-template-columns: 1fr !important;
    gap: 16px !important;
    height: auto !important;
  }
  
  .flow-row {
    flex-direction: column !important;
    gap: 8px !important;
  }
  
  .flow-arrow {
    transform: rotate(90deg);
    padding: 2px 0;
  }
  
  .resume-card-grid {
    grid-template-columns: 1fr !important;
  }
  
  .deck-title-center {
    display: none !important;
  }
  
  .shortcut-pills {
    display: none !important;
  }
  
  .slide-title {
    font-size: 21px !important;
  }
  
  .slide-subtitle {
    font-size: 12.5px !important;
  }
}

@media (max-width: 640px) {
  header.deck-header {
    padding: 0 10px !important;
    height: 46px !important;
  }
  
  .brand-badge {
    display: none !important;
  }
  
  .header-btn {
    padding: 4px 7px !important;
    font-size: 11px !important;
  }
  
  .header-btn .key-pill {
    display: none !important;
  }
  
  footer.deck-footer {
    padding: 0 10px !important;
    height: 48px !important;
  }
  
  .footer-progress-container {
    max-width: 90px !important;
    margin: 0 6px !important;
  }
  
  .slide {
    padding: 16px 12px !important;
  }
  
  .slide-title {
    font-size: 18px !important;
  }
  
  .slide-subtitle {
    font-size: 11.5px !important;
  }
  
  .proto-scenario-bar {
    padding: 6px 8px !important;
  }
  
  .scenario-btn {
    font-size: 9.5px !important;
    padding: 3px 6px !important;
  }
  
  .proto-tab-bar {
    gap: 10px !important;
    padding: 0 8px !important;
  }

  .stat-value {
    font-size: 26px !important;
  }

  .bar-label {
    width: 95px !important;
    font-size: 10.5px !important;
  }
}

/* PRINT MEDIA QUERIES FOR PDF EXPORT */
@media print {
  body {
    background: white;
    color: black;
    overflow: visible !important;
    height: auto !important;
  }
  
  header.deck-header,
  footer.deck-footer,
  #speaker-notes-panel,
  #slide-grid-modal,
  #evaluator-guide-modal,
  .scenario-btn,
  .shortcut-pills {
    display: none !important;
  }
  
  main.deck-stage {
    padding: 0 !important;
    background: none !important;
    overflow: visible !important;
    display: block !important;
  }
  
  #presentation-frame {
    max-width: 100% !important;
    max-height: none !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    overflow: visible !important;
    aspect-ratio: auto !important;
  }
  
  .slides-wrapper {
    overflow: visible !important;
    position: static !important;
  }
  
  .slide {
    position: relative !important;
    top: auto !important;
    left: auto !important;
    width: 100% !important;
    height: 100vh !important;
    page-break-after: always !important;
    opacity: 1 !important;
    visibility: visible !important;
    transform: none !important;
    padding: 30px !important;
    box-sizing: border-box !important;
    display: flex !important;
  }
}
"""
