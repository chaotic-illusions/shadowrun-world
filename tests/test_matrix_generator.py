"""Tests for the matrix host topology generator."""
import pytest
from app.services.matrix_generator import (
    generate,
    VALID_CONNECTIONS,
    COMPLEXITY_BANDS,
    IC_CATEGORY,
    _parse_rating,
    _available_ic,
)


# ── Rating parsing ───────────────────────────────────────────────────────────

class TestParseRating:
    def test_standard(self):
        assert _parse_rating("Orange-6") == 6

    def test_low(self):
        assert _parse_rating("Green-3") == 3

    def test_fallback(self):
        assert _parse_rating("garbage") == 6


# ── IC availability ──────────────────────────────────────────────────────────

class TestAvailableIC:
    def test_white_only(self):
        pool = _available_ic("white")
        for ic in pool:
            assert IC_CATEGORY[ic] == "white"

    def test_gray_includes_white(self):
        pool = _available_ic("gray")
        cats = {IC_CATEGORY[ic] for ic in pool}
        assert "white" in cats
        assert "gray" in cats
        assert "black" not in cats

    def test_black_includes_all(self):
        pool = _available_ic("black")
        cats = {IC_CATEGORY[ic] for ic in pool}
        assert cats == {"white", "gray", "black"}


# ── Basic generation ─────────────────────────────────────────────────────────

class TestGenerate:
    @pytest.fixture
    def simple_config(self):
        return {
            "complexity": 1,
            "base_rating": "Green-3",
            "ic_lethality": "white",
            "has_private_subnet": False,
            "owner_hint": "corp",
            "seed": 42,
        }

    def test_returns_required_keys(self, simple_config):
        result = generate(simple_config)
        assert "nodes" in result
        assert "edges" in result
        assert "subnets" in result

    def test_has_cpu(self, simple_config):
        result = generate(simple_config)
        cpu_nodes = [n for n in result["nodes"] if n["type"] == "CPU"]
        assert len(cpu_nodes) >= 1

    def test_has_san(self, simple_config):
        result = generate(simple_config)
        san_nodes = [n for n in result["nodes"] if n["type"] == "SAN"]
        assert len(san_nodes) >= 1

    def test_has_spu(self, simple_config):
        result = generate(simple_config)
        spu_nodes = [n for n in result["nodes"] if n["type"] == "SPU"]
        assert len(spu_nodes) >= 1

    def test_node_count_in_band(self, simple_config):
        result = generate(simple_config)
        lo, hi = COMPLEXITY_BANDS[1]
        assert lo <= len(result["nodes"]) <= hi

    def test_all_nodes_have_positions(self, simple_config):
        result = generate(simple_config)
        for node in result["nodes"]:
            assert "x" in node and "y" in node

    def test_all_nodes_have_ids(self, simple_config):
        result = generate(simple_config)
        ids = [n["id"] for n in result["nodes"]]
        assert len(ids) == len(set(ids)), "Node IDs should be unique"

    def test_deterministic_with_seed(self, simple_config):
        r1 = generate(simple_config)
        r2 = generate(simple_config)
        assert r1 == r2


class TestEdgeValidity:
    def test_edges_respect_connection_matrix(self):
        config = {
            "complexity": 3,
            "base_rating": "Orange-6",
            "ic_lethality": "gray",
            "has_private_subnet": False,
            "seed": 123,
        }
        result = generate(config)
        id_map = {n["id"]: n["type"] for n in result["nodes"]}
        for edge in result["edges"]:
            if edge.get("bridge"):
                continue
            src_t = id_map[edge["from"]]
            dst_t = id_map[edge["to"]]
            assert dst_t in VALID_CONNECTIONS[src_t], (
                f"Invalid edge {src_t} -> {dst_t}"
            )

    def test_all_nodes_connected(self):
        config = {
            "complexity": 2,
            "base_rating": "Green-3",
            "ic_lethality": "white",
            "has_private_subnet": False,
            "seed": 99,
        }
        result = generate(config)
        node_ids = {n["id"] for n in result["nodes"]}
        connected = set()
        for edge in result["edges"]:
            connected.add(edge["from"])
            connected.add(edge["to"])
        assert node_ids == connected, "All nodes should appear in at least one edge"


class TestPrivateSubnet:
    @pytest.fixture
    def private_config(self):
        return {
            "complexity": 3,
            "base_rating": "Red-8",
            "ic_lethality": "black",
            "has_private_subnet": True,
            "owner_hint": "military",
            "seed": 777,
        }

    def test_two_subnets(self, private_config):
        result = generate(private_config)
        assert len(result["subnets"]) == 2
        subnet_ids = {s["id"] for s in result["subnets"]}
        assert subnet_ids == {"public", "private"}

    def test_private_nodes_exist(self, private_config):
        result = generate(private_config)
        private_nodes = [n for n in result["nodes"] if n["subnet"] == "private"]
        assert len(private_nodes) >= 3

    def test_bridge_edge_exists(self, private_config):
        result = generate(private_config)
        bridge_edges = [e for e in result["edges"] if e.get("bridge")]
        assert len(bridge_edges) == 1

    def test_no_private_without_flag(self):
        config = {
            "complexity": 3,
            "base_rating": "Orange-6",
            "ic_lethality": "gray",
            "has_private_subnet": False,
            "seed": 777,
        }
        result = generate(config)
        assert len(result["subnets"]) == 1
        private_nodes = [n for n in result["nodes"] if n.get("subnet") == "private"]
        assert len(private_nodes) == 0


class TestComplexityScaling:
    @pytest.mark.parametrize("complexity", [1, 2, 3, 4, 5])
    def test_higher_complexity_more_nodes(self, complexity):
        config = {
            "complexity": complexity,
            "base_rating": "Orange-6",
            "ic_lethality": "gray",
            "has_private_subnet": False,
            "seed": 50,
        }
        result = generate(config)
        lo, hi = COMPLEXITY_BANDS[complexity]
        assert lo <= len(result["nodes"]) <= hi

    def test_complexity_clamped(self):
        config = {"complexity": 99, "base_rating": "Orange-6", "seed": 1}
        result = generate(config)
        lo, hi = COMPLEXITY_BANDS[5]
        assert lo <= len(result["nodes"]) <= hi
