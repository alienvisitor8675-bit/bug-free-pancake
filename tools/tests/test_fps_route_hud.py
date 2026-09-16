"""Protect the route HUD's bounded connection to the generated sector."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DRAW_EVENT = ROOT / "project/bugbugbug/objects/obj_fps_controller/Draw_64.gml"


class FpsRouteHudStructureTests(unittest.TestCase):
    """Keep route rendering tied to active-run state and projection markers."""

    @classmethod
    def setUpClass(cls):
        cls.draw_event = DRAW_EVENT.read_text(encoding="utf-8")

    def test_active_hud_renders_all_projected_route_markers(self):
        """The HUD consumes the projection and renders each state marker."""
        start = self.draw_event.index(
            "var _route_entries = fps_sector_route_entries("
        )
        end = self.draw_event.index("var _enemy_count =", start)
        route_block = self.draw_event[start:end]

        self.assertRegex(
            self.draw_event[:start],
            r"if \(run_state == FPS_RUN_PLAYING\) \{\s*$",
        )
        self.assertIn("run_room_index", route_block)
        self.assertIn("run_contract.room_complete", route_block)
        self.assertRegex(
            route_block,
            r"for \(var _route_index = 0; _route_index < _route_count;",
        )
        self.assertIn("_route_entry.role_name", route_block)
        self.assertIn("_route_entry.status", route_block)
        for marker in ("is_current", "is_cleared", "is_next", "is_finale"):
            with self.subTest(marker=marker):
                self.assertIn(f"_route_entry.{marker}", route_block)
        self.assertGreaterEqual(len(re.findall(r"draw_text", route_block)), 2)


if __name__ == "__main__":
    unittest.main()
