"""Tests for slugify helper function."""

import pytest
from slugify import slugify


class TestSlugify:
    """Test cases for slugify function."""

    def test_basic_ascii_text(self):
        """Test basic ASCII text conversion."""
        assert slugify("Hello World") == "hello-world"
        assert slugify("Hello  World") == "hello-world"
        assert slugify("  Hello World  ") == "hello-world"

    def test_umlaut_transliteration(self):
        """Test German umlaut transliteration."""
        assert slugify("Müller") == "mueller"
        assert slugify("Größe") == "groesse"
        assert slugify("Bäckerei") == "baeckerei"
        assert slugify("Straße") == "strasse"
        assert slugify("für") == "fuer"
        assert slugify("Über") == "ueber"

    def test_sharp_s_transliteration(self):
        """Test ß transliteration."""
        assert slugify("Straße") == "strasse"
        assert slugify("Weiß") == "weiss"
        assert slugify("Maß") == "mass"

    def test_mixed_case(self):
        """Test mixed case handling."""
        assert slugify("MÜLLER") == "mueller"
        assert slugify("müller") == "mueller"
        assert slugify("Müller") == "mueller"

    def test_special_characters_removed(self):
        """Test that special characters are removed/replaced."""
        assert slugify("Hello@World") == "hello-world"
        assert slugify("Hello#World") == "hello-world"
        assert slugify("Hello$World") == "hello-world"
        assert slugify("Hello!World") == "hello-world"

    def test_numbers_preserved(self):
        """Test that numbers are preserved."""
        assert slugify("Version 2.0") == "version-2-0"
        assert slugify("Item 42") == "item-42"

    def test_multiple_spaces_collapsed(self):
        """Test that multiple spaces/hyphens are collapsed."""
        assert slugify("Hello    World") == "hello-world"
        assert slugify("Hello---World") == "hello-world"
        assert slugify("Hello - - World") == "hello-world"

    def test_empty_string(self):
        """Test empty string handling."""
        assert slugify("") == ""
        assert slugify("   ") == ""

    def test_only_special_chars(self):
        """Test string with only special characters."""
        assert slugify("@#$%") == ""
        assert slugify("!!!") == ""

    def test_unicode_normalization(self):
        """Test unicode normalization (e.g., accented characters)."""
        assert slugify("café") == "cafe"
        assert slugify("naïve") == "naive"
        assert slugify("résumé") == "resume"

    def test_no_leading_trailing_hyphens(self):
        """Test no leading or trailing hyphens."""
        assert slugify("-Hello-") == "hello"
        assert slugify("---Hello---") == "hello"
        assert slugify(" Hello ") == "hello"

    def test_already_slugified(self):
        """Test already slugified text stays the same."""
        assert slugify("hello-world") == "hello-world"
        assert slugify("already-a-slug") == "already-a-slug"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])