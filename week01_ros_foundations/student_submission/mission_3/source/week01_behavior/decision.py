"""Pure decision helpers for Mission 3.

Complete both functions. Keeping this logic independent of ROS makes it possible
to test safety decisions before running the simulated robot.
"""

from __future__ import annotations

from collections.abc import Sequence

import math

def front_distance(
    ranges: Sequence[float],
    angle_min: float,
    angle_increment: float,
    half_width_radians: float,
) -> float | None:
    """Return the nearest finite, positive reading in the front sector.

    Return ``None`` when the sector has no valid reading. Angles are measured in
    radians and the front direction is zero radians.
    """
    nearest = float('inf')
    angle = angle_min
    for r in ranges:
        if (r < nearest and r > 0.0) and (angle <= half_width_radians and angle >= -half_width_radians):
            nearest = r
        else:
            pass
        angle += angle_increment

    if math.isinf(nearest):
        return None
    
    return nearest
    #raise NotImplementedError("Mission 3: select and validate the front-sector readings")


def decide_velocity(
    distance: float | None,
    stop_distance: float,
    forward_speed: float,
) -> float:
    """Return a bounded forward velocity; missing data must produce a stop."""
    if distance == None or distance <= stop_distance:
        return 0.0

    return forward_speed
    #raise NotImplementedError("Mission 3: implement the move/stop safety rule, idk lol")

