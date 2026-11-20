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

# 4. Check for absence of old 23 slides references
old_23_refs = re.findall(r'23\s*slides?', html, re.IGNORECASE)
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

# 7. Check Slide 1 status badge
assert 'PROJECT INTRODUCTION' in html, "Missing [PROJECT INTRODUCTION] badge on Slide 1"

# 8. Check that survey count is 100+ and NOT N=45
assert 'N=100+' in html, "Missing N=100+ in html"
assert 'N=45' not in html, "Found deprecated N=45 in html"
assert '45 college' not in html, "Found deprecated '45 college' in html"
assert '45 respondents' not in html, "Found deprecated '45 respondents' in html"

# 9. Check that unsupported statistics/assumptions have been removed
unsupported_strings = [
    "3.2 versions",
    "3.2 resumes",
    "65% Google Drive",
    "75% worried",
    "60% exited an application",
    "70% volunteered",
    "Google Forms",
    "September – October 2024",
    "September - October 2024",
    "prevent keyword rejections",
    "executive-CV-versus-analyst-CV",
    "must search for the job again"
]
for s in unsupported_strings:
    assert s not in html, f"Found unsupported string: '{s}'"

# 10. Check verified competitor URLs in Appendix B
competitor_urls = [
    "https://resume.naukri.com/faqs",
    "https://www.linkedin.com/help/linkedin/answer/a512405",
    "https://www.linkedin.com/help/linkedin/answer/a506680",
    "https://in.indeed.com/help/job-seekers/articles/11314976176141-faqs-creating-uploading-and-managing-a-resume-file?co=IN&hl=en",
    "https://in.indeed.com/help/job-seekers/articles/204652920-applying-for-a-job-on-indeed?co=IN&hl=en"
]
for url in competitor_urls:
    assert url in html, f"Missing competitor URL: {url}"

# 11. Check Q1-Q13 restored findings
for q in ["Q1:", "Q2:", "Q3:", "Q4:", "Q5:", "Q6:", "Q7:", "Q8:", "Q9:", "Q10:", "Q11:", "Q12:", "Q13:"]:
    assert q in html, f"Missing question {q} in HTML"

# 12. Check illustrative proposals labeling in Slide 13
assert "Illustrative Proposal" in html, "Missing 'Illustrative Proposal' label in Slide 13"

# 13. Check proposed capacity assumption for 5 resumes
assert "proposed MVP capacity assumption requiring validation" in html, "Missing proposed capacity assumption label"

print("\n--- ALL VERIFICATIONS PASSED 100% ---")
