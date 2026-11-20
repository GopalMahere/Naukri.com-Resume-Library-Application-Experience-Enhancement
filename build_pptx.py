"""
Naukri.com – One Profile, Multiple Resumes
Full 20-slide PowerPoint generator using python-pptx
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
import copy
from lxml import etree

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY    = RGBColor(0x0D, 0x2B, 0x5A)   # dark navy
BLUE    = RGBColor(0x18, 0x56, 0xEA)   # Naukri-ish blue
LBLUE   = RGBColor(0xDB, 0xEA, 0xFE)   # light-blue fill
AMBER   = RGBColor(0xD9, 0x77, 0x06)   # amber accent
LAMBER  = RGBColor(0xFE, 0xF3, 0xC7)   # light amber fill
TEAL    = RGBColor(0x0D, 0x94, 0x88)   # teal accent
LTEAL   = RGBColor(0xCC, 0xFB, 0xF1)   # light teal fill
GREEN   = RGBColor(0x05, 0x96, 0x69)   # green
LGREEN  = RGBColor(0xD1, 0xFA, 0xE5)   # light green
ROSE    = RGBColor(0xE1, 0x1D, 0x48)   # rose/red
LROSE   = RGBColor(0xFF, 0xE4, 0xE6)   # light rose
SLATE   = RGBColor(0x64, 0x74, 0x8B)   # slate grey text
LIGHT   = RGBColor(0xF1, 0xF5, 0xF9)   # very light bg
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
BLACK   = RGBColor(0x0F, 0x17, 0x2A)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

# ── Helper functions ─────────────────────────────────────────────────────────

def blank_slide():
    layout = prs.slide_layouts[6]   # completely blank
    return prs.slides.add_slide(layout)

def rect(slide, x, y, w, h, fill_rgb=None, line_rgb=None, line_width=Pt(0)):
    shape = slide.shapes.add_shape(1, x, y, w, h)   # MSO_SHAPE_TYPE.RECTANGLE = 1
    shape.line.width = line_width
    if fill_rgb:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_rgb
    else:
        shape.fill.background()
    if line_rgb:
        shape.line.color.rgb = line_rgb
    else:
        shape.line.fill.background()
    return shape

def txt(slide, text, x, y, w, h,
        size=Pt(12), bold=False, italic=False, color=BLACK,
        align=PP_ALIGN.LEFT, wrap=True, font_name="Calibri"):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tb.word_wrap = wrap
    p  = tb.text_frame.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size  = size
    run.font.bold  = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name  = font_name
    return tb

def header_band(slide, title, subtitle=None,
                band_color=NAVY, title_color=WHITE, sub_color=LBLUE):
    """Dark top band common to all content slides."""
    rect(slide, 0, 0, SLIDE_W, Inches(1.15), fill_rgb=band_color)
    txt(slide, title,
        Inches(0.4), Inches(0.12), Inches(12.5), Inches(0.6),
        size=Pt(26), bold=True, color=title_color, align=PP_ALIGN.LEFT)
    if subtitle:
        txt(slide, subtitle,
            Inches(0.4), Inches(0.72), Inches(12.5), Inches(0.35),
            size=Pt(13), color=sub_color, align=PP_ALIGN.LEFT)

def slide_number(slide, n):
    txt(slide, str(n),
        Inches(12.9), Inches(7.15), Inches(0.4), Inches(0.3),
        size=Pt(9), color=SLATE, align=PP_ALIGN.RIGHT)

def bullet_box(slide, items, x, y, w, h,
               bg=LIGHT, border=None, title=None, title_color=NAVY,
               item_size=Pt(11.5), item_color=BLACK, bullet="▪"):
    rect(slide, x, y, w, h, fill_rgb=bg,
         line_rgb=border if border else RGBColor(0xE2,0xE8,0xF0),
         line_width=Pt(1))
    ty = y + Inches(0.1)
    if title:
        txt(slide, title, x+Inches(0.15), ty, w-Inches(0.3), Inches(0.3),
            size=Pt(11), bold=True, color=title_color)
        ty += Inches(0.3)
    for item in items:
        txt(slide, f"{bullet}  {item}",
            x+Inches(0.15), ty, w-Inches(0.3), Inches(0.28),
            size=item_size, color=item_color)
        ty += Inches(0.3)

def card(slide, x, y, w, h, bg, label=None, label_bg=None,
         label_color=WHITE, body=None, body_size=Pt(11), body_color=BLACK,
         border=None, big_text=None, big_color=NAVY, big_size=Pt(28)):
    rect(slide, x, y, w, h, fill_rgb=bg,
         line_rgb=border if border else RGBColor(0xE2,0xE8,0xF0),
         line_width=Pt(1))
    cy = y + Inches(0.12)
    if label:
        lbg = label_bg or bg
        rect(slide, x+Inches(0.12), cy, Inches(len(label)*0.11+0.2), Inches(0.22),
             fill_rgb=lbg)
        txt(slide, label, x+Inches(0.15), cy, w, Inches(0.22),
            size=Pt(8.5), bold=True, color=label_color)
        cy += Inches(0.26)
    if big_text:
        txt(slide, big_text, x+Inches(0.12), cy, w-Inches(0.25), Inches(0.5),
            size=big_size, bold=True, color=big_color)
        cy += Inches(0.5)
    if body:
        txt(slide, body, x+Inches(0.12), cy, w-Inches(0.25), h-(cy-y)-Inches(0.1),
            size=body_size, color=body_color, wrap=True)

def add_chart(slide, categories, values, x, y, w, h,
              chart_type=XL_CHART_TYPE.COLUMN_CLUSTERED,
              series_name="", bar_color=BLUE):
    chart_data = ChartData()
    chart_data.categories = categories
    chart_data.add_series(series_name, values)
    ch = slide.shapes.add_chart(chart_type, x, y, w, h, chart_data).chart
    ch.has_legend = False
    ch.has_title  = False
    # colour series
    try:
        pt = ch.series[0].format.fill
        pt.solid()
        pt.fore_color.rgb = bar_color
    except Exception:
        pass
    return ch

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — Title Slide
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()

# Full dark background
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=NAVY)

# Decorative accent bar
rect(sl, 0, Inches(5.6), SLIDE_W, Inches(0.06), fill_rgb=BLUE)

# Project badge
rect(sl, Inches(0.4), Inches(0.4), Inches(2.8), Inches(0.3), fill_rgb=BLUE)
txt(sl, "INDEPENDENT PM CASE STUDY  |  NAUKRI.COM",
    Inches(0.44), Inches(0.4), Inches(2.8), Inches(0.3),
    size=Pt(8), bold=True, color=WHITE)

txt(sl, "One Profile,\nMultiple Resumes",
    Inches(0.6), Inches(1.1), Inches(9), Inches(2.0),
    size=Pt(44), bold=True, color=WHITE, font_name="Calibri Light")

txt(sl, "Improving the Naukri.com Application Experience",
    Inches(0.6), Inches(3.1), Inches(9), Inches(0.5),
    size=Pt(19), color=LBLUE)

txt(sl, "Aditya Sharma  ·  Product Management  ·  November 2026",
    Inches(0.6), Inches(5.75), Inches(10), Inches(0.3),
    size=Pt(11), color=SLATE)

# Right-side visual suggestion strip
rect(sl, Inches(10.4), Inches(1.2), Inches(2.6), Inches(4.1), fill_rgb=RGBColor(0x1A,0x38,0x6E))
for i, (lbl, clr) in enumerate([
        ("Product Mgmt CV", BLUE),
        ("Consulting CV",   TEAL),
        ("Operations CV",   AMBER),
        ("+ Upload New",    SLATE),]):
    rect(sl, Inches(10.6), Inches(1.4)+Inches(i)*Inches(0.9),
         Inches(2.1), Inches(0.7),
         fill_rgb=RGBColor(0x0D,0x2B,0x5A),
         line_rgb=clr, line_width=Pt(1.5))
    txt(sl, lbl, Inches(10.75), Inches(1.5)+Inches(i)*Inches(0.9),
        Inches(1.9), Inches(0.4), size=Pt(10), color=WHITE)

slide_number(sl, 1)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — Executive Summary
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Executive Summary",
            "The problem, the investigation, the proposed solution — on one page")
slide_number(sl, 2)

cols = [
    (LROSE,  ROSE,  "The Problem",
     "Candidates who maintain role-specific resumes may need to leave an in-progress "
     "application, change their profile resume and re-find the job before applying. "
     "This adds friction and risks drop-off."),
    (LTEAL,  TEAL,  "The Investigation",
     "Survey of 100+ college students. 80% applied across 3+ role types. "
     "90% maintained multiple resumes. Competitor benchmarking of LinkedIn, "
     "Indeed India and Naukri.com FastForward."),
    (LBLUE,  BLUE,  "The Proposed Solution",
     "A Resume Library: store up to 5 role-specific resumes, choose the right one "
     "at application time, optionally save new uploads — without overwriting existing files."),
    (LGREEN, GREEN, "The Expected Benefit",
     "Smoother application experience, fewer repeated steps, better candidate "
     "control. Actual impact on completion rates to be validated through A/B testing."),
]
for i, (bg, accent, title, body) in enumerate(cols):
    cx = Inches(0.3) + i * Inches(3.25)
    card(sl, cx, Inches(1.3), Inches(3.1), Inches(5.7),
         bg=bg, label=title, label_bg=accent,
         body=body, body_size=Pt(12), body_color=BLACK, border=accent)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — My Observation
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "My Observation",
            "Where this idea started — a firsthand job-search experience")
slide_number(sl, 3)

rect(sl, Inches(0.4), Inches(1.3), Inches(7.5), Inches(5.6), fill_rgb=LIGHT,
     line_rgb=RGBColor(0xE2,0xE8,0xF0), line_width=Pt(1))

txt(sl, "[PERSONAL OBSERVATION]",
    Inches(0.55), Inches(1.45), Inches(3), Inches(0.25),
    size=Pt(8.5), bold=True, color=BLUE)

txt(sl, "Applying to Different Roles — a Real Friction Point",
    Inches(0.55), Inches(1.75), Inches(7.1), Inches(0.4),
    size=Pt(17), bold=True, color=NAVY)

quote = (
    '"While applying for jobs across different types of roles — Product Management, '
    'Consulting, Operations — I maintained separate tailored resumes for each. When the '
    'resume I wanted to submit differed from the one attached to my Naukri profile, '
    'managing that swap added steps to my application process. '
    'I worried about accidentally submitting the wrong version."'
)
txt(sl, quote,
    Inches(0.55), Inches(2.25), Inches(7.1), Inches(1.9),
    size=Pt(13.5), italic=True, color=SLATE)

txt(sl, "Methodological Note:",
    Inches(0.55), Inches(4.2), Inches(7.1), Inches(0.25),
    size=Pt(11), bold=True, color=NAVY)
txt(sl, "This personal experience is the hypothesis generator, not proof of a platform-wide defect. "
        "It was tested through candidate research and competitor benchmarking.",
    Inches(0.55), Inches(4.5), Inches(7.1), Inches(0.6),
    size=Pt(11), color=SLATE)

# Right: who faces this problem
rect(sl, Inches(8.2), Inches(1.3), Inches(4.7), Inches(5.6), fill_rgb=LBLUE,
     line_rgb=BLUE, line_width=Pt(1.5))
txt(sl, "Who faces this friction?",
    Inches(8.4), Inches(1.45), Inches(4.3), Inches(0.3),
    size=Pt(13), bold=True, color=NAVY)

segments = [
    ("🎓 College Students",  "Applying concurrently to PM, Consulting, Ops and Tech roles during placement season."),
    ("🔄 Career Changers",   "Exploring different tracks simultaneously (e.g. IC roles vs management roles)."),
    ("💼 Multi-Track Seekers","Applying across industries or functions at the same time."),
]
for i, (seg, desc) in enumerate(segments):
    ty = Inches(1.85) + i * Inches(1.5)
    rect(sl, Inches(8.4), ty, Inches(4.3), Inches(1.25),
         fill_rgb=WHITE, line_rgb=BLUE, line_width=Pt(0.75))
    txt(sl, seg,  Inches(8.55), ty+Inches(0.1),  Inches(4.0), Inches(0.3),
        size=Pt(12), bold=True, color=NAVY)
    txt(sl, desc, Inches(8.55), ty+Inches(0.4),  Inches(4.0), Inches(0.75),
        size=Pt(10.5), color=SLATE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — The Actual Problem
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "The Actual Problem",
            "What happens when the required resume differs from the profile-attached resume")
slide_number(sl, 4)

# Problem statement box
rect(sl, Inches(0.4), Inches(1.3), Inches(12.5), Inches(1.1),
     fill_rgb=LROSE, line_rgb=ROSE, line_width=Pt(2))
txt(sl, "Core Problem Statement",
    Inches(0.6), Inches(1.35), Inches(5), Inches(0.25),
    size=Pt(10), bold=True, color=ROSE)
txt(sl, 'Candidates who maintain multiple role-specific resumes need a simple way to select '
        'the intended document during job applications — without repeatedly replacing or losing '
        'access to other saved versions.',
    Inches(0.6), Inches(1.62), Inches(12.1), Inches(0.7),
    size=Pt(13), bold=True, color=NAVY)

# Two-column explanation
left_items = [
    "On Naukri, candidates maintain one profile with one resume attached.",
    "In some application flows the author encountered, the profile-attached resume is used by default.",
    "If a different resume is needed, the candidate may need to leave the in-progress application.",
    "They navigate to their profile, replace the resume, return and find the same job again.",
    "This creates context-switching, friction and risk of accidental overwriting.",
]
right_items = [
    "No overwrite protection — replacing the profile resume removes the previous version.",
    "No in-flow resume selector in the flows the author encountered.",
    "No ability to save multiple named resumes independently.",
    "No record of which resume was submitted for which application.",
    "No way to resume an interrupted application easily.",
]

rect(sl, Inches(0.4), Inches(2.55), Inches(6.1), Inches(4.3), fill_rgb=LIGHT,
     line_rgb=RGBColor(0xE2,0xE8,0xF0), line_width=Pt(1))
txt(sl, "What the current experience involves",
    Inches(0.55), Inches(2.65), Inches(5.8), Inches(0.3),
    size=Pt(11), bold=True, color=NAVY)
for i, item in enumerate(left_items):
    txt(sl, f"▪  {item}",
        Inches(0.6), Inches(3.0)+i*Inches(0.7), Inches(5.7), Inches(0.6),
        size=Pt(11), color=BLACK)

rect(sl, Inches(6.75), Inches(2.55), Inches(6.1), Inches(4.3), fill_rgb=LROSE,
     line_rgb=ROSE, line_width=Pt(1))
txt(sl, "What is currently missing",
    Inches(6.9), Inches(2.65), Inches(5.8), Inches(0.3),
    size=Pt(11), bold=True, color=ROSE)
for i, item in enumerate(right_items):
    txt(sl, f"▪  {item}",
        Inches(6.9), Inches(3.0)+i*Inches(0.7), Inches(5.7), Inches(0.6),
        size=Pt(11), color=BLACK)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — Problem Journey (the painful loop)
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "The Problem Journey",
            "The repeated cycle a candidate may face when the wrong resume is attached")
slide_number(sl, 5)

steps = [
    (LBLUE, BLUE,  "1. Find a Job", "Candidate searches Naukri and finds a suitable role requiring a specific resume type."),
    (LROSE, ROSE,  "2. Click Apply", "Candidate starts the application — but the resume attached to their profile may not be the right one for this role."),
    (LAMBER, AMBER,"3. Leave the Application", "Candidate exits the application to change their profile resume — losing their progress."),
    (LTEAL, TEAL,  "4. Update Profile Resume", "Candidate navigates to profile, uploads the correct resume — overwriting the previous one."),
    (LROSE, ROSE,  "5. Find the Job Again", "Candidate returns to the job listing and applies. Meanwhile the job may have closed, the link may be lost, or another role now requires a different resume."),
    (LGREEN, GREEN,"6. Risk and Repetition", "Each role type may trigger this loop again. Candidates managing 3–4 resume types repeat this cycle frequently."),
]

cols = 3
for i, (bg, accent, title, body) in enumerate(steps):
    row, col = divmod(i, cols)
    cx = Inches(0.3) + col * Inches(4.3)
    cy = Inches(1.3) + row * Inches(2.9)
    card(sl, cx, cy, Inches(4.1), Inches(2.65), bg=bg,
         label=title, label_bg=accent,
         body=body, body_size=Pt(11.5), body_color=BLACK, border=accent)
    # arrow right
    if col < cols - 1:
        txt(sl, "→", cx+Inches(4.15), cy+Inches(1.1), Inches(0.4), Inches(0.4),
            size=Pt(20), bold=True, color=SLATE, align=PP_ALIGN.CENTER)
    # arrow down between rows
    if i == 2:
        txt(sl, "↓", Inches(0.3)+2*Inches(4.3)+Inches(2.0), cy+Inches(2.68),
            Inches(0.4), Inches(0.35), size=Pt(20), bold=True, color=SLATE,
            align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 6 — Why This Problem Matters
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Why This Problem Matters",
            "Impact on candidates and potential business implications — requiring validation")
slide_number(sl, 6)

impacts = [
    (LROSE,  ROSE,  "Candidate Experience",
     ["Repeated manual steps add friction to what should be a simple action.",
      "Risk of submitting the wrong resume increases stress and reduces confidence.",
      "Some candidates may postpone or skip applications altogether."]),
    (LAMBER, AMBER, "Application Completion",
     ["Interrupting an in-progress application to fix a resume creates drop-off risk.",
      "Returning to find the same job requires extra effort and is not always possible.",
      "Whether this materially impacts completion rates requires Naukri telemetry validation."]),
    (LTEAL,  TEAL,  "Candidate Control",
     ["No way to maintain independent named resume versions safely.",
      "No overwrite protection — a replaced resume cannot be recovered.",
      "No visibility into which resume was submitted for each past application."]),
    (LBLUE,  BLUE,  "Business Consideration (Hypothesis)",
     ["Higher friction at application time could affect satisfaction and return usage.",
      "This is a testable hypothesis — not a proven business impact.",
      "A controlled A/B experiment would be needed to verify any effect on metrics."]),
]

for i, (bg, accent, title, bullets) in enumerate(impacts):
    cx = Inches(0.3) + (i % 2) * Inches(6.5)
    cy = Inches(1.3) + (i // 2) * Inches(2.9)
    rect(sl, cx, cy, Inches(6.2), Inches(2.65), fill_rgb=bg,
         line_rgb=accent, line_width=Pt(1.5))
    txt(sl, title, cx+Inches(0.15), cy+Inches(0.1), Inches(5.9), Inches(0.3),
        size=Pt(13), bold=True, color=accent)
    for j, b in enumerate(bullets):
        txt(sl, f"▪  {b}",
            cx+Inches(0.15), cy+Inches(0.5)+j*Inches(0.65), Inches(5.9), Inches(0.6),
            size=Pt(11), color=BLACK)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 7 — Target Users
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Target Users",
            "Which candidates are most likely to experience this friction")
slide_number(sl, 7)

segments_detail = [
    (LBLUE, BLUE, "🎓 College Students (Primary)",
     ["Applying during placement seasons to PM, Consulting, Tech and Ops roles simultaneously.",
      "Maintaining 3–4 tailored resumes is common practice.",
      "Surveyed cohort: 100+ college students across India.",
      "Highest frequency of multi-role applications in a short time window."]),
    (LTEAL, TEAL, "🔄 Career Changers",
     ["Mid-career professionals exploring a different function or domain.",
      "May maintain a current-role resume and a target-role resume simultaneously.",
      "High motivation to avoid submitting the wrong version.",
      "Secondary segment — requires Naukri user-data validation."]),
    (LGREEN, GREEN, "💼 Multi-Track Active Seekers",
     ["Applying across industries (e.g. finance + product + strategy) at the same time.",
      "Every role type may require a different resume emphasis.",
      "Workaround today: manual file management across drives and portals.",
      "Volume of applications amplifies the friction of the current process."]),
    (LAMBER, AMBER, "Out of Scope (for MVP)",
     ["Passive candidates not actively applying to multiple role types.",
      "Candidates maintaining a single generalised resume.",
      "Executive-level roles with dedicated headhunter processes.",
      "Naukri's internal user distribution across these segments is unknown to us."]),
]

for i, (bg, accent, title, bullets) in enumerate(segments_detail):
    cx = Inches(0.3) + (i % 2) * Inches(6.5)
    cy = Inches(1.3) + (i // 2) * Inches(2.9)
    rect(sl, cx, cy, Inches(6.2), Inches(2.65), fill_rgb=bg,
         line_rgb=accent, line_width=Pt(1.5))
    txt(sl, title, cx+Inches(0.15), cy+Inches(0.1), Inches(5.9), Inches(0.3),
        size=Pt(12.5), bold=True, color=accent)
    for j, b in enumerate(bullets):
        txt(sl, f"▪  {b}",
            cx+Inches(0.15), cy+Inches(0.5)+j*Inches(0.52), Inches(5.9), Inches(0.5),
            size=Pt(10.5), color=BLACK)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 8 — Survey Findings
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Survey Findings — N=100+ College Students",
            "Exploratory survey via personal outreach. Results scoped to this student cohort only.")
slide_number(sl, 8)

# 4 big stat cards
stats = [
    (LBLUE, BLUE,   "90%", "Q1: Active job applicants\n(applied within last 90 days)"),
    (LTEAL, TEAL,   "80%", "Q3: Applied across 3 or\nmore role categories"),
    (LGREEN, GREEN, "90%", "Q4: Maintain multiple\nrole-specific resumes"),
    (LAMBER, AMBER, "90%", "Q7: Frequently needed a\ndifferent resume while applying"),
]
for i, (bg, accent, pct, label) in enumerate(stats):
    cx = Inches(0.3) + i * Inches(3.25)
    card(sl, cx, Inches(1.3), Inches(3.1), Inches(1.75),
         bg=bg, border=accent, big_text=pct, big_color=accent, big_size=Pt(32),
         body=label, body_size=Pt(10.5), body_color=NAVY)

# bar chart data for role distribution
chart_data = ChartData()
chart_data.categories = ["4+ role types (60%)", "3 role types (20%)", "2 role types (15%)", "1 role type (5%)"]
chart_data.add_series("Respondents", (60, 20, 15, 5))
ch_shape = sl.shapes.add_chart(
    XL_CHART_TYPE.BAR_CLUSTERED,
    Inches(0.3), Inches(3.2), Inches(5.5), Inches(3.8),
    chart_data)
ch = ch_shape.chart
ch.has_legend = False
ch.has_title = True
ch.chart_title.text_frame.text = "Role Categories Applied To (N=100+)"
ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(11)
ch.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True

# Right: qualitative + limitation
rect(sl, Inches(6.1), Inches(3.2), Inches(6.8), Inches(1.75),
     fill_rgb=LTEAL, line_rgb=TEAL, line_width=Pt(1))
txt(sl, "Q11 & Q12: Feature Interest",
    Inches(6.25), Inches(3.3), Inches(6.4), Inches(0.28),
    size=Pt(11), bold=True, color=TEAL)
txt(sl, "90% rated the proposed Resume Library 4 or 5 out of 5 for usefulness.\n"
        "90% said they were very likely to use it if available.",
    Inches(6.25), Inches(3.62), Inches(6.4), Inches(1.1),
    size=Pt(11), color=BLACK)

rect(sl, Inches(6.1), Inches(5.1), Inches(6.8), Inches(1.9),
     fill_rgb=LAMBER, line_rgb=AMBER, line_width=Pt(1))
txt(sl, "⚠  Survey Limitations — Important",
    Inches(6.25), Inches(5.2), Inches(6.4), Inches(0.28),
    size=Pt(11), bold=True, color=AMBER)
limitations = [
    "Sample: 100+ college students. Does not represent all Naukri users.",
    "Personal outreach, not randomised platform-wide sampling.",
    "Stated intent (90%) must be tested against actual behaviour in A/B testing.",
    "Open-ended Q5, Q6, Q8, Q9, Q13: qualitative only — no fabricated exact counts.",
]
for j, lim in enumerate(limitations):
    txt(sl, f"▪  {lim}",
        Inches(6.25), Inches(5.52)+j*Inches(0.35), Inches(6.4), Inches(0.33),
        size=Pt(10), color=BLACK)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 9 — Competitor Benchmarking
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Competitor Benchmarking",
            "How LinkedIn, Indeed India and Naukri.com handle resume management — from official documentation")
slide_number(sl, 9)

platforms = [
    (LBLUE, BLUE, "Naukri.com",
     [("FastForward FAQs", "Documents up to 5 profiles per username, 1 resume per profile, within text/visual CV packages."),
      ("Author's Observation", "Profile-associated resume was used in the application flow the author encountered."),
      ("Requires Validation", "Whether alternate resume selection is available across all Naukri application types is not established."),
      ("Source", "resume.naukri.com/faqs — Verified Nov 2026")],
     "Opportunity: a persistent candidate-controlled Resume Library"),
    (RGBColor(0xEE,0xF2,0xFF), RGBColor(0x4F,0x46,0xE5), "LinkedIn",
     [("4 Reusable Resumes", "Candidates can store up to 4 recently uploaded resumes in Easy Apply settings."),
      ("In-Flow Selection", "Resume is selected inside the application modal — no profile editing required."),
      ("Application History", "LinkedIn allows candidates to view the resume submitted for an Easy Apply application through Job Tracker."),
      ("Source", "linkedin.com/help — Articles a512405 and a506680 — Verified Nov 2026")],
     "Documented model: in-flow selection from a stored resume set"),
    (LTEAL, TEAL, "Indeed India",
     [("1 Stored Resume", "Candidates can store 1 resume file on their Indeed profile."),
      ("Apply-Time Upload", "Candidates can upload a different resume file when applying for a specific position."),
      ("Documentation Boundary", "Public documentation does not establish whether an apply-time upload changes the stored profile resume."),
      ("Source", "in.indeed.com/help — Articles 11314976176141 and 204652920 — Verified Nov 2026")],
     "Documented capability: apply-time upload option exists"),
]

for i, (bg, accent, platform, points, takeaway) in enumerate(platforms):
    cx = Inches(0.3) + i * Inches(4.3)
    rect(sl, cx, Inches(1.3), Inches(4.1), Inches(5.5), fill_rgb=bg,
         line_rgb=accent, line_width=Pt(1.5))
    txt(sl, platform, cx+Inches(0.15), Inches(1.4), Inches(3.9), Inches(0.3),
        size=Pt(14), bold=True, color=accent)
    for j, (label, detail) in enumerate(points):
        ty = Inches(1.8) + j * Inches(0.9)
        txt(sl, label+":",
            cx+Inches(0.15), ty, Inches(3.9), Inches(0.22),
            size=Pt(10), bold=True, color=NAVY)
        txt(sl, detail,
            cx+Inches(0.15), ty+Inches(0.22), Inches(3.9), Inches(0.6),
            size=Pt(9.5), color=SLATE, wrap=True)
    rect(sl, cx+Inches(0.1), Inches(5.95), Inches(3.9), Inches(0.6),
         fill_rgb=accent)
    txt(sl, takeaway,
        cx+Inches(0.15), Inches(5.98), Inches(3.85), Inches(0.55),
        size=Pt(9.5), bold=True, color=WHITE, wrap=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 10 — Root Cause Analysis
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Root Cause Analysis",
            "Why the current application experience creates friction — framed as hypotheses for validation")
slide_number(sl, 10)

hypotheses = [
    ("H1", BLUE,   "Single-Resume Profile Model",
     "The candidate data model appears to associate one primary resume with the profile. "
     "An independent multi-document library may not be part of the core architecture. "
     "Hypothesis — requires engineering confirmation."),
    ("H2", TEAL,   "No In-Flow Resume Selector",
     "In the flows the author encountered, there was no modal to select an alternate resume "
     "at the moment of clicking Apply. A selector would need to be introduced into the flow."),
    ("H3", AMBER,  "No Overwrite Protection",
     "Uploading a new resume to the profile replaces the existing one with no easy recovery path. "
     "Candidates risk losing a carefully prepared document permanently."),
    ("H4", RGBColor(0x7C,0x3A,0xED), "No Version Traceability",
     "No visible record of which document was submitted for each past application. "
     "Candidates cannot confirm what a recruiter received without external note-taking."),
    ("H5", GREEN,  "Reusability Gap",
     "Documents uploaded during some application flows may not be automatically saved to the "
     "candidate's account for reuse in future applications."),
]

for i, (code, accent, title, body) in enumerate(hypotheses):
    cy = Inches(1.3) + i * Inches(1.14)
    rect(sl, Inches(0.3), cy, Inches(0.65), Inches(1.0),
         fill_rgb=accent)
    txt(sl, code, Inches(0.3), cy+Inches(0.3), Inches(0.65), Inches(0.4),
        size=Pt(13), bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    rect(sl, Inches(0.98), cy, Inches(11.65), Inches(1.0),
         fill_rgb=LIGHT, line_rgb=RGBColor(0xE2,0xE8,0xF0), line_width=Pt(1))
    txt(sl, title, Inches(1.1), cy+Inches(0.08), Inches(11.4), Inches(0.3),
        size=Pt(12.5), bold=True, color=NAVY)
    txt(sl, body, Inches(1.1), cy+Inches(0.42), Inches(11.4), Inches(0.5),
        size=Pt(11), color=SLATE)

rect(sl, Inches(0.3), Inches(7.0), Inches(12.6), Inches(0.3),
     fill_rgb=LAMBER, line_rgb=AMBER, line_width=Pt(1))
txt(sl, "⚠  These are analytical hypotheses for investigation — not confirmed internal Naukri architecture facts.",
    Inches(0.4), Inches(7.02), Inches(12.4), Inches(0.26),
    size=Pt(10), bold=True, color=AMBER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 11 — Proposed Solution
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Proposed Solution: One Profile, Multiple Resumes",
            "A candidate-controlled Resume Library built into the existing Naukri profile")
slide_number(sl, 11)

rect(sl, Inches(0.4), Inches(1.3), Inches(12.5), Inches(0.95),
     fill_rgb=RGBColor(0x0D,0x2B,0x5A))
txt(sl, "Core Idea:",
    Inches(0.6), Inches(1.35), Inches(2), Inches(0.25),
    size=Pt(10), bold=True, color=LBLUE)
txt(sl, "Candidates maintain one comprehensive Naukri profile AND an independent Resume Library "
        "of up to 5 named, role-specific documents. At application time, they choose which resume to submit.",
    Inches(0.6), Inches(1.6), Inches(12.1), Inches(0.55),
    size=Pt(13), color=WHITE)

pillars = [
    (LBLUE, BLUE, "Pillar 1\nComprehensive Profile",
     ["One profile with education,\nexperience and skills.",
      "Profile remains unchanged by\nresume library actions.",
      "Current profile resume is fully\npreserved as-is."]),
    (LTEAL, TEAL, "Pillar 2\nDedicated Resume Library",
     ["Store up to 5 resumes\n(proposed MVP capacity).",
      "Each resume has a custom name\n(e.g. 'Product Management CV').",
      "Adding a new resume never\ndeletes an existing one."]),
    (LGREEN, GREEN, "Pillar 3\nApply-Time Selector",
     ["On clicking Apply, a small\nwindow shows the resume library.",
      "Candidate selects existing resume\nor uploads a new one.",
      "Post-upload save is optional and\nexplicit — not automatic."]),
    (LAMBER, AMBER, "Pillar 4\nApplication History",
     ["Each submitted application records\nwhich resume was used.",
      "Candidates can review past\napplications and document versions.",
      "No silent overwrites.\nFull candidate control."]),
]

for i, (bg, accent, title, bullets) in enumerate(pillars):
    cx = Inches(0.3) + i * Inches(3.25)
    rect(sl, cx, Inches(2.45), Inches(3.1), Inches(4.7), fill_rgb=bg,
         line_rgb=accent, line_width=Pt(1.5))
    txt(sl, title, cx+Inches(0.15), Inches(2.55), Inches(2.9), Inches(0.6),
        size=Pt(12), bold=True, color=accent)
    for j, b in enumerate(bullets):
        txt(sl, f"▪  {b}", cx+Inches(0.15), Inches(3.25)+j*Inches(1.15), Inches(2.9), Inches(1.0),
            size=Pt(11), color=BLACK)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 12 — How It Works (Application Flow)
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "How It Works — The Application Flow",
            "Step-by-step: what a candidate sees and does when applying with the Resume Library")
slide_number(sl, 12)

flow_steps = [
    (BLUE,  "1", "Click Apply",          "Candidate finds a suitable role and clicks Apply."),
    (TEAL,  "2", "Resume Selector Opens","A modal shows the Resume Library with named options."),
    (NAVY,  "3", "Choose or Upload",     "Select an existing resume OR upload a new file from device."),
    (AMBER, "4", "Save Gate (upload only)","After successful upload, a checkbox asks: 'Save to library?' Unchecked = this application only. Checked = saved as new named entry."),
    (GREEN, "5", "Review",               "Candidate sees the selected resume name before submitting."),
    (ROSE,  "6", "Submit",               "Application submitted. History records the exact document used."),
]

for i, (accent, num, title, body) in enumerate(flow_steps):
    cx = Inches(0.3) + (i % 3) * Inches(4.3)
    cy = Inches(1.3) + (i // 3) * Inches(2.8)
    rect(sl, cx, cy, Inches(4.1), Inches(2.6), fill_rgb=LIGHT,
         line_rgb=accent, line_width=Pt(2))
    rect(sl, cx, cy, Inches(0.45), Inches(0.45), fill_rgb=accent)
    txt(sl, num, cx, cy+Inches(0.05), Inches(0.45), Inches(0.35),
        size=Pt(14), bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txt(sl, title, cx+Inches(0.55), cy+Inches(0.08), Inches(3.4), Inches(0.3),
        size=Pt(13), bold=True, color=accent)
    txt(sl, body,  cx+Inches(0.15), cy+Inches(0.5),  Inches(3.8), Inches(1.9),
        size=Pt(11.5), color=BLACK)
    # horizontal arrow
    if i % 3 < 2:
        txt(sl, "→", cx+Inches(4.15), cy+Inches(1.1), Inches(0.3), Inches(0.4),
            size=Pt(20), bold=True, color=SLATE, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 13 — Application-wise Resume Tracking
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Application-wise Resume Tracking",
            "Candidates can see exactly which resume was submitted for each job")
slide_number(sl, 13)

# Left explanation
rect(sl, Inches(0.3), Inches(1.3), Inches(5.0), Inches(5.6), fill_rgb=LIGHT,
     line_rgb=RGBColor(0xE2,0xE8,0xF0), line_width=Pt(1))
txt(sl, "What is tracked?", Inches(0.45), Inches(1.4), Inches(4.7), Inches(0.3),
    size=Pt(13), bold=True, color=NAVY)
items = [
    "Company name and role title.",
    "Date of application.",
    "Name of the resume submitted.",
    "Resume version at the time of submission — independent of future edits.",
    "Option to preview the submitted document.",
]
for i, item in enumerate(items):
    txt(sl, f"▪  {item}",
        Inches(0.45), Inches(1.85)+i*Inches(0.65), Inches(4.7), Inches(0.6),
        size=Pt(12), color=BLACK)

txt(sl, "Why it matters?", Inches(0.45), Inches(4.65), Inches(4.7), Inches(0.3),
    size=Pt(13), bold=True, color=NAVY)
txt(sl, "If a recruiter calls, the candidate can immediately identify which resume was sent "
        "and what it contained — without searching through files or emails.",
    Inches(0.45), Inches(5.0), Inches(4.7), Inches(1.0),
    size=Pt(11.5), color=SLATE)

# Right: mock history table
rect(sl, Inches(5.6), Inches(1.3), Inches(7.3), Inches(5.6), fill_rgb=WHITE,
     line_rgb=BLUE, line_width=Pt(1.5))
txt(sl, "Application History Log (Mockup)",
    Inches(5.75), Inches(1.38), Inches(7.0), Inches(0.3),
    size=Pt(11.5), bold=True, color=NAVY)

headers = ["Company & Role", "Date", "Resume Used"]
header_widths = [Inches(3.0), Inches(1.3), Inches(2.7)]
for j, (hdr, hw) in enumerate(zip(headers, header_widths)):
    hx = Inches(5.6) + sum(header_widths[:j])
    rect(sl, hx, Inches(1.75), hw, Inches(0.35), fill_rgb=NAVY)
    txt(sl, hdr, hx+Inches(0.05), Inches(1.78), hw-Inches(0.1), Inches(0.3),
        size=Pt(10), bold=True, color=WHITE)

rows = [
    ("Myntra — Product Manager Intern",  "14 Nov 2026", "Product Management CV"),
    ("Deloitte — Business Analyst",      "12 Nov 2026", "Consulting CV"),
    ("Amazon — Operations Manager",      "10 Nov 2026", "Operations CV"),
    ("Flipkart — Associate PM",          "07 Nov 2026", "Product Management CV"),
    ("McKinsey — Business Analyst",      "03 Nov 2026", "Consulting CV"),
]
row_bgs = [LIGHT, WHITE, LIGHT, WHITE, LIGHT]
for r, (company, date, resume) in enumerate(rows):
    ry = Inches(2.1) + r * Inches(0.72)
    row_data = [company, date, resume]
    row_colors = [LGREEN, LTEAL, LBLUE]
    for j, (cell, hw) in enumerate(zip(row_data, header_widths)):
        hx = Inches(5.6) + sum(header_widths[:j])
        rect(sl, hx, ry, hw, Inches(0.68), fill_rgb=row_bgs[r],
             line_rgb=RGBColor(0xE2,0xE8,0xF0), line_width=Pt(0.75))
        clr = GREEN if j == 2 else BLACK
        txt(sl, cell, hx+Inches(0.07), ry+Inches(0.17), hw-Inches(0.1), Inches(0.4),
            size=Pt(10), color=clr, bold=(j==2))

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 14 — Screen Designs / UI Mockups
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Screen Designs — Key Moments in the Candidate Experience",
            "Illustrative UI concepts for the Resume Library and application flow")
slide_number(sl, 14)

screens = [
    (LBLUE, BLUE, "Screen A: Resume Library",
     ["My Resume Library", "○  Product Management CV   |  Uploaded 10 Nov",
      "○  Consulting CV   |  Uploaded 05 Nov", "○  Operations CV   |  Uploaded 01 Nov",
      "[ + Upload a new resume ]"]),
    (LTEAL, TEAL, "Screen B: Choose at Apply",
     ["Applying for: PM Intern @ Myntra", "Select resume:",
      "●  Product Management CV  ← Selected", "○  Consulting CV",
      "[ Continue ] [ Cancel ]"]),
    (LAMBER, AMBER, "Screen C: Save Gate",
     ["Upload successful ✓", "[ ] Save this resume to my library?",
      "(unchecked = use for this application only)",
      "If checked: enter a name for this resume →",
      "e.g. 'Ops – Supply Chain Focus'"]),
    (LGREEN, GREEN, "Screen D: Review Before Submit",
     ["Confirm Your Application", "Role: Operations Manager @ Amazon",
      "Resume: Operations CV  [Preview] [Change]",
      "By submitting, this resume version is recorded.",
      "[ Submit Application ]"]),
]

for i, (bg, accent, title, lines) in enumerate(screens):
    cx = Inches(0.3) + (i % 2) * Inches(6.5)
    cy = Inches(1.3) + (i // 2) * Inches(2.9)
    rect(sl, cx, cy, Inches(6.2), Inches(2.65), fill_rgb=bg,
         line_rgb=accent, line_width=Pt(1.5))
    txt(sl, title, cx+Inches(0.15), cy+Inches(0.08), Inches(5.9), Inches(0.3),
        size=Pt(12), bold=True, color=accent)
    for j, line in enumerate(lines):
        txt(sl, line, cx+Inches(0.15), cy+Inches(0.47)+j*Inches(0.42),
            Inches(5.9), Inches(0.4), size=Pt(10.5), color=BLACK)

rect(sl, Inches(0.3), Inches(7.1), Inches(12.6), Inches(0.25),
     fill_rgb=LIGHT, line_rgb=RGBColor(0xE2,0xE8,0xF0), line_width=Pt(1))
txt(sl, "These are illustrative concept screens, not final design specifications. Actual UI requires Naukri design system and engineering review.",
    Inches(0.4), Inches(7.12), Inches(12.4), Inches(0.22),
    size=Pt(9), color=SLATE, italic=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 15 — MVP Scope
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "MVP Scope — What to Build First",
            "Focused first release: the minimum to validate the core candidate benefit")
slide_number(sl, 15)

must = [
    "Resume Library with up to 5 stored resumes (proposed capacity — requires validation).",
    "Custom naming for each stored resume.",
    "Apply-time resume selector modal.",
    "In-flow upload of a new resume during application.",
    "Conditional save checkbox (appears only after successful upload).",
    "Mandatory custom name when saving a new resume to library.",
    "Application history recording which resume was submitted.",
    "No silent overwrite of existing library resumes.",
]
future = [
    "Renaming and deleting saved resumes from library settings.",
    "Candidate-designated default resume (pre-highlighted for convenience).",
    "Resume version comparison view.",
    "AI-assisted resume suggestions (explicitly out of MVP scope).",
    "Recruiter-facing resume version visibility.",
]

rect(sl, Inches(0.3), Inches(1.3), Inches(7.5), Inches(5.5), fill_rgb=LGREEN,
     line_rgb=GREEN, line_width=Pt(1.5))
txt(sl, "✓  MVP: Must Have — First Release",
    Inches(0.45), Inches(1.4), Inches(7.2), Inches(0.3),
    size=Pt(13), bold=True, color=GREEN)
for i, item in enumerate(must):
    txt(sl, f"▪  {item}",
        Inches(0.45), Inches(1.8)+i*Inches(0.56), Inches(7.2), Inches(0.52),
        size=Pt(11.5), color=BLACK)

rect(sl, Inches(8.05), Inches(1.3), Inches(4.9), Inches(5.5), fill_rgb=LAMBER,
     line_rgb=AMBER, line_width=Pt(1.5))
txt(sl, "⏳  Future Scope — Post-MVP",
    Inches(8.2), Inches(1.4), Inches(4.6), Inches(0.3),
    size=Pt(13), bold=True, color=AMBER)
for i, item in enumerate(future):
    txt(sl, f"▪  {item}",
        Inches(8.2), Inches(1.8)+i*Inches(0.86), Inches(4.6), Inches(0.78),
        size=Pt(11.5), color=BLACK)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 16 — Implementation Plan
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Implementation Plan",
            "Phased delivery from internal audit to full rollout — illustrative proposal")
slide_number(sl, 16)

phases = [
    (BLUE,  "Phase 1\n(Weeks 1–3)",  "Internal Audit & Discovery",
     ["Naukri engineering audit of current resume data model.",
      "Telemetry review: how many candidates edit profile resume between job search and apply.",
      "Define technical approach for multi-document storage.",
      "Confirm scope feasibility with product and engineering."]),
    (TEAL,  "Phase 2\n(Weeks 4–8)",  "Build & Integration",
     ["Develop Resume Library backend: multi-document storage, metadata, naming.",
      "Build apply-time selector modal integrated into supported application flows.",
      "Implement conditional save gate: upload → success → checkbox → name → save.",
      "Build application history resume tracking."]),
    (AMBER, "Phase 3\n(Weeks 9–10)", "Internal Testing",
     ["End-to-end QA across supported application types.",
      "Security and privacy review of candidate document storage.",
      "Verify no overwrite scenarios — zero-tolerance guardrail.",
      "Fix any accessibility or upload-failure edge cases."]),
    (GREEN, "Phase 4\n(Weeks 11–13)","Usability Testing & Pilot",
     ["Usability sessions with 10–15 target candidates (illustrative sample size).",
      "Gather qualitative feedback on selector flow, naming, save gate.",
      "5% controlled pilot on native direct-apply flows (illustrative percentage).",
      "Monitor completion rates, adoption and error signals."]),
    (ROSE,  "Phase 5\n(Weeks 14+)", "Evaluate & Iterate",
     ["Full A/B results analysis — statistical significance required before scaling.",
      "Address issues found in pilot.",
      "Decide: scale to full rollout, iterate, or scope further.",
      "Document learnings for future resume-management features."]),
]

for i, (accent, phase_title, stage, bullets) in enumerate(phases):
    cy = Inches(1.3) + i * Inches(1.14)
    rect(sl, Inches(0.3), cy, Inches(1.6), Inches(1.0), fill_rgb=accent)
    txt(sl, phase_title, Inches(0.3), cy+Inches(0.15), Inches(1.6), Inches(0.7),
        size=Pt(9.5), bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    rect(sl, Inches(1.95), cy, Inches(2.0), Inches(1.0),
         fill_rgb=LIGHT, line_rgb=accent, line_width=Pt(1))
    txt(sl, stage, Inches(2.05), cy+Inches(0.3), Inches(1.9), Inches(0.4),
        size=Pt(11), bold=True, color=accent)
    rect(sl, Inches(3.98), cy, Inches(8.95), Inches(1.0),
         fill_rgb=LIGHT, line_rgb=RGBColor(0xE2,0xE8,0xF0), line_width=Pt(0.75))
    for j, b in enumerate(bullets):
        txt(sl, f"▪  {b}",
            Inches(4.08), cy+Inches(0.05)+j*Inches(0.23), Inches(8.75), Inches(0.22),
            size=Pt(10), color=BLACK)

rect(sl, Inches(0.3), Inches(7.0), Inches(12.6), Inches(0.3),
     fill_rgb=LAMBER, line_rgb=AMBER, line_width=Pt(1))
txt(sl, "⚠  Timeline is illustrative. Actual schedule depends on Naukri engineering capacity and architecture review findings.",
    Inches(0.4), Inches(7.02), Inches(12.4), Inches(0.26),
    size=Pt(10), bold=True, color=AMBER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 17 — Success Metrics
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Success Metrics",
            "How to measure whether the Resume Library genuinely improves the candidate experience")
slide_number(sl, 17)

metric_groups = [
    (LGREEN, GREEN, "Primary Metric",
     [("Application Completion Rate",
       "Completed Applications ÷ Application Starts",
       "Target group (Resume Library users) vs control. Needs statistical significance before scaling.")]),
    (LBLUE, BLUE, "Secondary — Adoption & Behaviour",
     [("Library Adoption",          "% of active applicants who upload ≥2 resumes to library", ""),
      ("Selection Distribution",    "% selecting existing vs uploading new at apply time",         ""),
      ("Save-to-Library Rate",      "% of uploads saved vs used for one application only",         ""),
      ("Time to Apply",             "Average time from Apply click to Submit",                     ""),]),
    (LAMBER, AMBER, "Quality & Guardrails",
     [("Accidental Overwrite",      "Must remain at zero — zero-tolerance guardrail.",              ""),
      ("Wrong-Resume Reports",      "Support tickets citing incorrect resume submitted",            ""),
      ("Upload Success Rate",       "% of file uploads completing without error",                   ""),
      ("Application Abandonment",   "Drop-off during resume selection step",                       ""),]),
    (LROSE, ROSE, "Post-Pilot — Business Signal",
     [("Feature Satisfaction Score", "Survey of Resume Library users (CSAT or similar)",          ""),
      ("Return-to-Apply Rate",       "Do candidates using the library return to apply more often?", ""),
      ("Recruiter Quality Signal",   "If recruiter data available: relevance of submitted resumes", ""),]),
]

for i, (bg, accent, group_title, metrics) in enumerate(metric_groups):
    cx = Inches(0.3) + (i % 2) * Inches(6.5)
    cy = Inches(1.3) + (i // 2) * Inches(2.9)
    rect(sl, cx, cy, Inches(6.2), Inches(2.65), fill_rgb=bg,
         line_rgb=accent, line_width=Pt(1.5))
    txt(sl, group_title, cx+Inches(0.15), cy+Inches(0.1), Inches(5.9), Inches(0.28),
        size=Pt(12), bold=True, color=accent)
    for j, (name, formula, note) in enumerate(metrics):
        ty = cy + Inches(0.48) + j * Inches(0.5)
        txt(sl, f"▪  {name}:", cx+Inches(0.15), ty, Inches(5.9), Inches(0.22),
            size=Pt(11), bold=True, color=NAVY)
        if formula:
            txt(sl, formula, cx+Inches(0.4), ty+Inches(0.22), Inches(5.6), Inches(0.22),
                size=Pt(10), color=SLATE, italic=bool(note))
        if note:
            txt(sl, note, cx+Inches(0.4), ty+Inches(0.42), Inches(5.6), Inches(0.22),
                size=Pt(9.5), color=SLATE)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 18 — Risks and Considerations
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Risks and Considerations",
            "Known risks and how the design addresses each one")
slide_number(sl, 18)

risks = [
    (LROSE, ROSE, "Technical Feasibility",
     "Risk: The current candidate data model may not support multi-document libraries natively.",
     "Mitigation: Engineering audit in Phase 1 before committing to build. Scope may be revised based on findings."),
    (LAMBER, AMBER, "Data Privacy",
     "Risk: Storing multiple documents per candidate increases data-volume and compliance scope.",
     "Mitigation: Dedicated data-retention review. Candidates control their own documents. Clear deletion options in future scope."),
    (LROSE, ROSE, "Accidental Wrong Resume",
     "Risk: Candidate selects the wrong resume from the selector modal.",
     "Mitigation: Explicit review screen before final submission. Resume name and preview option shown. No silent auto-select."),
    (LTEAL, TEAL, "Overwrite Protection",
     "Risk: A new upload could overwrite a previously saved resume.",
     "Mitigation: New uploads are always saved as new, independent entries. Existing resumes are never modified or deleted by an upload."),
    (LBLUE, BLUE, "Application History Integrity",
     "Risk: If the submitted version is not stored separately, future edits could alter the historical record.",
     "Mitigation: History stores a reference to the document version at submission time, independent of later library edits."),
    (LAMBER, AMBER, "Scope Creep",
     "Risk: Requests to add AI rewriting, automatic matching or other features during build.",
     "Mitigation: MVP scope is defined and locked. AI features, default-preference logic and renaming are explicitly deferred."),
]

for i, (bg, accent, title, risk_text, mitigation) in enumerate(risks):
    cx = Inches(0.3) + (i % 2) * Inches(6.5)
    cy = Inches(1.3) + (i // 3) * Inches(2.0) + (i // 2 % 2 - i // 3) * Inches(0)
    # Recompute layout: 2 cols x 3 rows
    row = i // 2
    col = i % 2
    cx = Inches(0.3) + col * Inches(6.5)
    cy = Inches(1.3) + row * Inches(2.0)
    rect(sl, cx, cy, Inches(6.2), Inches(1.85), fill_rgb=bg,
         line_rgb=accent, line_width=Pt(1.5))
    txt(sl, title, cx+Inches(0.15), cy+Inches(0.08), Inches(5.9), Inches(0.28),
        size=Pt(12), bold=True, color=accent)
    txt(sl, f"Risk: {risk_text}",
        cx+Inches(0.15), cy+Inches(0.42), Inches(5.9), Inches(0.42),
        size=Pt(10.5), color=BLACK, italic=True)
    txt(sl, f"Mitigation: {mitigation}",
        cx+Inches(0.15), cy+Inches(0.9), Inches(5.9), Inches(0.75),
        size=Pt(10.5), color=NAVY)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 19 — Expected Impact
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=WHITE)
header_band(sl, "Expected Impact",
            "What this proposal aims to achieve — and what must be validated through testing")
slide_number(sl, 19)

impacts_left = [
    (GREEN, "🟢 Validated through A/B experiment",
     ["Application completion rate difference between Resume Library users and control group.",
      "Resume Library adoption rate among active multi-role applicants.",
      "Time-to-apply before and after the library feature is introduced.",
      "Drop-off rate at the resume selection step vs existing flow."]),
    (AMBER, "🟡 Hypothesised — requires pilot data",
     ["Reduction in support requests related to wrong-resume submissions.",
      "Increase in returning candidates completing multiple applications.",
      "Improvement in candidate satisfaction scores related to application experience."]),
]
for i, (accent, label, items) in enumerate(impacts_left):
    cy = Inches(1.3) + i * Inches(2.9)
    rect(sl, Inches(0.3), cy, Inches(6.5), Inches(2.65), fill_rgb=LIGHT,
         line_rgb=accent, line_width=Pt(2))
    txt(sl, label, Inches(0.45), cy+Inches(0.1), Inches(6.2), Inches(0.3),
        size=Pt(12), bold=True, color=accent)
    for j, item in enumerate(items):
        txt(sl, f"▪  {item}",
            Inches(0.45), cy+Inches(0.5)+j*Inches(0.52), Inches(6.2), Inches(0.5),
            size=Pt(11), color=BLACK)

# Right: candidate value narrative
rect(sl, Inches(7.0), Inches(1.3), Inches(5.9), Inches(5.5), fill_rgb=LBLUE,
     line_rgb=BLUE, line_width=Pt(1.5))
txt(sl, "What changes for the candidate",
    Inches(7.15), Inches(1.42), Inches(5.6), Inches(0.3),
    size=Pt(13), bold=True, color=NAVY)

befores = [
    "Leave application mid-way to fix resume.",
    "Overwrite a saved resume to submit the right one.",
    "Re-search for the same job after a profile edit.",
    "No record of which resume was submitted where.",
    "Fear of submitting the wrong version.",
]
afters = [
    "Select the right resume without leaving the application.",
    "New uploads never overwrite existing saved resumes.",
    "Resume selection is part of the application flow.",
    "Every application records the exact resume submitted.",
    "Explicit review step before submission.",
]
for j, (before, after) in enumerate(zip(befores, afters)):
    cy = Inches(1.85) + j * Inches(0.86)
    rect(sl, Inches(7.1), cy, Inches(2.75), Inches(0.75), fill_rgb=LROSE,
         line_rgb=ROSE, line_width=Pt(0.5))
    txt(sl, before, Inches(7.18), cy+Inches(0.14), Inches(2.6), Inches(0.5),
        size=Pt(9.5), color=BLACK)
    txt(sl, "→", Inches(9.9), cy+Inches(0.2), Inches(0.3), Inches(0.4),
        size=Pt(14), bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    rect(sl, Inches(10.2), cy, Inches(2.55), Inches(0.75), fill_rgb=LGREEN,
         line_rgb=GREEN, line_width=Pt(0.5))
    txt(sl, after, Inches(10.28), cy+Inches(0.14), Inches(2.4), Inches(0.5),
        size=Pt(9.5), color=BLACK)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 20 — Closing Slide
# ══════════════════════════════════════════════════════════════════════════════
sl = blank_slide()
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_rgb=NAVY)
rect(sl, 0, Inches(5.6), SLIDE_W, Inches(0.06), fill_rgb=BLUE)

txt(sl, "One Profile, Multiple Resumes",
    Inches(0.6), Inches(0.9), Inches(11), Inches(0.8),
    size=Pt(36), bold=True, color=WHITE, font_name="Calibri Light")

txt(sl, "A simple, candidate-first improvement to the Naukri.com application experience.",
    Inches(0.6), Inches(1.75), Inches(10.5), Inches(0.4),
    size=Pt(16), color=LBLUE)

closing_points = [
    ("The Problem is Real",        "Candidates managing multiple resume versions face repeated friction in the current flow."),
    ("The Evidence Supports Exploration", "100+ students surveyed. 90% maintain multiple resumes. 90% frequently need an alternate at apply time."),
    ("The Solution is Targeted",   "No AI, no complexity. Just: store named resumes, choose the right one, and always know what was submitted."),
    ("The Validation Path is Clear","A/B experiment measuring completion rate, adoption and guardrails — before any broad rollout."),
    ("The Ask",                    "Internal telemetry review and an engineering feasibility conversation to determine if and how to proceed."),
]

for i, (title, body) in enumerate(closing_points):
    cy = Inches(2.4) + i * Inches(0.95)
    rect(sl, Inches(0.6), cy, Inches(0.06), Inches(0.65), fill_rgb=BLUE)
    txt(sl, title, Inches(0.8), cy+Inches(0.02), Inches(3.5), Inches(0.3),
        size=Pt(13), bold=True, color=WHITE)
    txt(sl, body,  Inches(0.8), cy+Inches(0.32), Inches(11.5), Inches(0.4),
        size=Pt(12), color=LBLUE)

txt(sl, "Aditya Sharma  ·  Independent PM Case Study  ·  Naukri.com  ·  November 2026",
    Inches(0.6), Inches(5.75), Inches(12), Inches(0.3),
    size=Pt(10), color=SLATE)

slide_number(sl, 20)

# ── Save ─────────────────────────────────────────────────────────────────────
OUT = r"C:\Users\adity\.gemini\antigravity\scratch\naukri-resume-library-presentation\Naukri_One_Profile_Multiple_Resumes.pptx"
prs.save(OUT)
print(f"Saved: {OUT}")
print(f"Slides: {len(prs.slides)}")
