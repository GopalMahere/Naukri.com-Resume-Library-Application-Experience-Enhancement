import re
import os

html_path = r"C:\Users\adity\.gemini\antigravity\scratch\naukri-resume-library-presentation\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

print(f"Index.html size: {len(html)} bytes")

# 1. Slide count
slides = re.findall(r'<section class="slide[^"]*" id="([^"]+)">', html)
print(f"Total <section class='slide'> tags: {len(slides)}")
assert len(slides) == 16, f"Expected 16 slides, got {len(slides)}"

# 2. Speaker notes count
notes = re.findall(r'<div class="speaker-notes-data"', html)
print(f"Total speaker notes containers: {len(notes)}")
assert len(notes) == 16, f"Expected 16 speaker notes, got {len(notes)}"

# 3. Slide IDs
print(f"Slide IDs: {slides}")
assert len(set(slides)) == 16, "Duplicate slide IDs detected"

# 4. Check references to old 23 slides
old_23_refs = re.findall(r'23\s*slides?', html, re.IGNORECASE)
print(f"Matches for '23 slides': {old_23_refs}")
assert len(old_23_refs) == 0, f"Found references to 23 slides: {old_23_refs}"

# 5. Check prototype elements
assert 'id="proto-body-viewport"' in html, "Missing proto-body-viewport"
assert 'id="scenario-preset-single"' in html, "Missing scenario-preset-single"
assert 'id="scenario-preset-a"' in html, "Missing scenario-preset-a"
assert 'id="scenario-preset-b"' in html, "Missing scenario-preset-b"
assert 'id="scenario-preset-c"' in html, "Missing scenario-preset-c"

# 6. Check for Appendices labels
assert 'Appendix A' in html, "Missing Appendix A"
assert 'Appendix B' in html, "Missing Appendix B"
assert 'Appendix C' in html, "Missing Appendix C"

# 7. Check Slide numbering format in pills
pills = re.findall(r'<div class="slide-number-pill">([^<]+)</div>', html)
print(f"Slide number pills count: {len(pills)}")
for i, p in enumerate(pills):
    print(f"  Slide {i+1}: {p}")

print("\n--- ALL VERIFICATIONS PASSED 100% ---")
