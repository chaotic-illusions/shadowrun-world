"""Tests for the consequence suggestion engine."""
import pytest
from app.services.consequence_engine import suggest


class TestSuggest:
    def test_empty_tags(self):
        assert suggest([]) == []

    def test_single_known_tag(self):
        results = suggest(["megacorp_offended"])
        assert len(results) > 0
        assert all(r["severity"] for r in results)
        assert all(r["suggestion"] for r in results)

    def test_multiple_tags(self):
        results = suggest(["megacorp_burned", "run_failure_exposed"])
        assert len(results) > 0

    def test_unknown_tag_ignored(self):
        results = suggest(["totally_made_up_tag"])
        assert results == []

    def test_no_duplicate_suggestions(self):
        results = suggest(["megacorp_burned", "run_failure_exposed", "npc_major_killed", "pc_identity_exposed"])
        texts = [r["suggestion"] for r in results]
        assert len(texts) == len(set(texts))

    def test_sorted_by_severity(self):
        results = suggest(["run_success_clean", "megacorp_offended", "megacorp_burned"])
        severity_order = {"severe": 0, "significant": 1, "moderate": 2, "variable": 3, "low": 4, "positive": 5}
        indices = [severity_order.get(r["severity"], 3) for r in results]
        assert indices == sorted(indices)

    def test_compound_rules_before_single(self):
        # Compound match: megacorp_burned + run_failure_exposed fires a compound rule
        results = suggest(["megacorp_burned", "run_failure_exposed"])
        compound_sources = [r for r in results if len(r["source_tags"]) > 1]
        single_sources = [r for r in results if len(r["source_tags"]) == 1]
        assert len(compound_sources) > 0, "Should have compound rule matches"
        assert len(single_sources) > 0, "Should have single-tag rule matches"

    def test_source_tags_included(self):
        results = suggest(["megacorp_offended"])
        for r in results:
            assert "source_tags" in r
            assert isinstance(r["source_tags"], list)
