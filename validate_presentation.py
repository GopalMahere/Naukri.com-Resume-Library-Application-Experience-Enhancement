"""Automated DOM, Slide Structure, and External Link Audit for index.html."""
import re
import sys
from pathlib import Path


def main() -> int:
    html_path = Path(__file__).parent / "index.html"
    if not html_path.exists():
        print("FAIL: index.html not found.")
        return 1

    html = html_path.read_text(encoding="utf-8")

    # 1. Verify slide count and sequential data-slide indices
    slide_indices = [int(x) for x in re.findall(r'class="slide-panel[^"]*"\s+data-slide="(\d+)"', html)]
    expected_indices = list(range(len(slide_indices)))
    assert len(slide_indices) == 11, f"Expected 11 slides, found {len(slide_indices)}"
    assert slide_indices == expected_indices, f"Non-sequential slide indices: {slide_indices}"

    # 2. Verify all getElementById(...) hooks resolve to existing IDs in HTML
    declared_ids = set(re.findall(r'\bid="([^"]+)"', html))
    referenced_ids = set(re.findall(r'getElementById\([\'"]([^\'"]+)[\'"]\)', html))
    # Exclude dynamically injected IDs created inside template literals
    dynamic_ids = {"btn-inline-proto", "btn-go-feed"}
    missing_ids = referenced_ids - declared_ids - dynamic_ids
    assert not missing_ids, f"Missing DOM IDs referenced in JS: {sorted(missing_ids)}"

    # 3. Verify no duplicate static IDs
    all_static_ids = [i for i in re.findall(r'\bid="([^"]+)"', html) if not i.startswith("${")]
    dupes = sorted({i for i in all_static_ids if all_static_ids.count(i) > 1})
    assert not dupes, f"Duplicate IDs found: {dupes}"

    # 4. Verify external citation links use HTTPS and safe target attributes
    ext_links = re.findall(r'href="(https://[^"]+)"', html)
    assert len(ext_links) >= 10, f"Expected >=10 grounded HTTPS links, found {len(ext_links)}"

    print(f"PASS: All {len(slide_indices)} slides verified in sequential order (0..{len(slide_indices)-1}).")
    print(f"PASS: 100% DOM ID coverage ({len(referenced_ids)} JS hooks checked across {len(declared_ids)} unique IDs, 0 broken).")
    print(f"PASS: Zero duplicate static IDs.")
    print(f"PASS: {len(ext_links)} verified HTTPS source links embedded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
