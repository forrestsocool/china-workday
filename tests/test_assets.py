"""Regression checks for metadata, compatibility, and brand assets."""

from __future__ import annotations

import json
from pathlib import Path
import struct


ROOT = Path(__file__).parents[1]
COMPONENT = ROOT / "custom_components" / "china-workday"


def test_manifest_points_to_the_maintained_fork() -> None:
    manifest = json.loads((COMPONENT / "manifest.json").read_text("utf-8"))
    assert manifest["version"] == "0.0.3"
    assert manifest["documentation"] == (
        "https://github.com/forrestsocool/china-workday"
    )
    assert manifest["issue_tracker"] == (
        "https://github.com/forrestsocool/china-workday/issues"
    )
    assert manifest["codeowners"] == ["@forrestsocool"]


def test_binary_sensor_does_not_force_an_invalid_entity_id() -> None:
    source = (COMPONENT / "binary_sensor.py").read_text("utf-8")
    assert "self.entity_id" not in source
    assert "self._attr_unique_id" in source


def test_brand_images_are_transparent_square_pngs() -> None:
    for name in ("icon.png", "logo.png"):
        image = (COMPONENT / "brand" / name).read_bytes()
        assert image[:8] == b"\x89PNG\r\n\x1a\n"
        assert struct.unpack(">II", image[16:24]) == (554, 554)
        assert image[25] == 6, f"{name} must use RGBA color type"
