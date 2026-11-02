# Files

- [Slugify Behavior](behavior.md) - The slugify(text) contract in slugify.py — German umlaut/ß transliteration before NFKD-to-ASCII normalization, lowercasing, non-alphanumeric collapse to single hyphens, and edge-case behavior for empty, whitespace-only, special-characters-only, and already-slugified input.
- [Slugify Tests](testing.md) - The pytest suite in test_slugify.py that pins the slugify() contract — twelve hand-written test methods in one TestSlugify class, grouped by concern from basic ASCII through umlaut and sharp-s transliteration to Unicode normalization, boundary hyphens, and idempotency — with a mapping from each pipeline stage to the assertions that must change when behavior changes.
