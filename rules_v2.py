"""EAS 510 - Project 1 - Phase 2: the V2 rule set.

Rules 1-3 are kept exactly as in `rules.py`. Your job is to ADD Rule 4 that
targets the systematic weakness you diagnosed from results_v1_hard.txt.

Constraint: the rules' `out_of` weights must still sum to 100 so the Final
Score stays on a /100 scale (the format validator enforces "Final Score:
<s>/100" equals the sum of the block's rule scores).

Example split that keeps the original spirit: Rules 1-3 -> 25/25/40 and
Rule 4 -> 10 (or trim the losers more aggressively).
"""

import rules
import cv2
import numpy as np

#: Define our custom rule set with rescaled weights summing to 100
RULES = ("rule1_v2", "rule2_v2", "rule3_v2", "rule4_edges")


def _scale(res, new_out_of):
    """Helper to rescale rule score to new weight."""
    if res["out_of"] > 0:
        res["score"] = int(round(res["score"] * (new_out_of / res["out_of"])))
    res["out_of"] = new_out_of
    return res


def rule1_v2(target, input_path):
    return _scale(rules.rule1(target, input_path), 25)


def rule2_v2(target, input_path):
    return _scale(rules.rule2(target, input_path), 25)


def rule3_v2(target, input_path):
    return _scale(rules.rule3(target, input_path), 40)


def rule4_edges(target, input_path):
    """Rule 4: Edge-based comparison (out_of = 10)."""
    try:
        img1 = cv2.imread(target, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        
        if img1 is None or img2 is None:
            return {
                "rule": 4, "name": "Edges", "fired": False,
                "score": 0, "out_of": 10, "note": "Image error", "metric": 0.0
            }
            
        img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

        edges1 = cv2.Canny(img1, 100, 200)
        edges2 = cv2.Canny(img2_resized, 100, 200)

        diff = np.absdiff(edges1, edges2)
        metric = float(np.mean(diff))

        fired = metric < 25.0
        score = 10 if fired else 0

        return {
            "rule": 4,
            "name": "Edges",
            "fired": fired,
            "score": score,
            "out_of": 10,
            "note": f"Edge diff: {metric:.2f}",
            "metric": metric,
        }
    except Exception as e:
        return {
            "rule": 4, "name": "Edges", "fired": False,
            "score": 0, "out_of": 10, "note": str(e), "metric": 0.0
        }