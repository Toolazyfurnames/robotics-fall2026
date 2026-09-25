# Mission 3

## Specification

Assume +x is forward, turning left is positive. Speeds must be within 0.22 m/s and 0.8 rad/s. Stops are to be made whenever commanded to, or if robot receives unclear instructions or out of bounds values(i.e move forward inf m/s, or turn 1 rad/s).

## Saved Specification

Assume +x is forward, turning left is positive. Speeds must be within 0.22 m/s and 0.8 rad/s. Stops are to be made whenever commanded to, or if robot receives unclear instructions or out of bounds values(i.e move forward inf m/s, or turn 1 rad/s).

## Assigned Pattern

l_path

## Original Prompt

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'l_path' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.

P.S Assume +x is forward, turning left is positive. Speeds must be within 0.22 m/s and 0.8 rad/s. Stops are to be made whenever commanded to, or if robot receives unclear instructions or out of bounds values(i.e move forward inf m/s, or turn 1 rad/s).

## Original Output

I updated only build_pattern() in the existing pattern.py; the course wrapper and Segment class are untouched.

The implemented L-path is:

1. Forward at 0.20 m/s for 5 s → about 1.0 m
2. Stop for 1 s
3. Turn left at +0.50 rad/s for π s → 0.5\pi \approx 1.571 rad = 90°
4. Stop for 1 s
5. Forward at 0.20 m/s for 5 s → another 1.0 m

So, assuming the robot begins at (0, 0) facing +x, the ideal path is approximately:

(0,0) → (1,0) → turn left → (1,1)

All commands satisfy the constraints: linear speed ≤ 0.22 m/s, angular speed ≤ 0.80 rad/s, every duration ≤ 30 s, and total duration is about 15.14 s. The explicit stop segments also satisfy your requirement to stop when commanded; the wrapper still handles the final zero command.

Assumptions

I assumed "l_path" means two straight legs separated by a 90° left turn, with stops before and after the turn. Since you didn’t specify exact leg lengths, I chose 1 m for each leg. I also assume the course wrapper/evaluator is responsible for rejecting malformed/non-finite commands outside build_pattern; this function itself only returns fixed, known-safe segments.

Tests I’d propose

Test that "l_path" returns the five segments in the correct order, that every segment obeys the velocity/duration bounds, that total duration is ≤ 60 s, and that the turn integrates to approximately π/2 radians. Also test that something like build_pattern("circle") raises ValueError.

For safety-oriented tests, verify the wrapper produces a final zero Twist, and—if the wrapper performs validation—that inf, nan, linear speeds above 0.22 m/s, or angular speeds above 0.80 rad/s result in stopping rather than motion.

The 3.141592653589793 second turn is intentional:

0.50\ \text{rad/s} \times \pi\ \text{s}
= \frac{\pi}{2}\ \text{rad}
= 90^\circ

So the robot makes a 90° left turn without exceeding the 0.8 rad/s limit.

## Original Source

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
    if pattern_name != "l_path":
        raise ValueError(f"Unknown pattern name: {pattern_name}")

    # L path: move straight along +x, stop, turn left 90 degrees,
    # stop again, then move straight along the new heading.
    return [
        Segment(linear_x=0.20, angular_z=0.0, duration=5.0),
        Segment(linear_x=0.0, angular_z=0.0, duration=1.0),
        Segment(linear_x=0.0, angular_z=0.50, duration=3.141592653589793),
        Segment(linear_x=0.0, angular_z=0.0, duration=1.0),
        Segment(linear_x=0.20, angular_z=0.0, duration=5.0),
    ]

## Assumptions

The AI assumed that the robot starts stationary, moves forward, stops, turns 90 degree left, stops again, and moves forward one last time. Linear_x is in m/s, angular_z is in rad/s, and duration is in seconds. Motion commands are interpreted in the base_link frame, and it did not assume a fixed global map after the robot turns. The wrapper publishes each command continuously for approximately the duration of the segment. It also assumed that commanded velocity matches actual velocity. Invalid commands are handled in the wrapper/safety layer.

## Problems

The function assumes only one pattern(even though we have other patterns), it also does not have a fixed global/map direction which can be bad depending on the environment. It also stated that commanded velocity is equal to actual velocity which is a huge error as many factors can affect the difference between these values.

## Test Plan

Pattern Behavior: Run the robot with a pattern and check distances traveled after each command and match with your predictions after each movement

Velocity Limit: Run the robot with different velocities, including values out of bounds, if the robot should run properly within the limit and should stop whenever it is outside of it

Stop test: Run the robot with commands that should allow for a stop, including error safes, and the robot should stop whenever these commands are run

## Modifications

The ai assumed it was traveling forward at 0.20 m/s when we actually need 0.40 m/s

## Live Pending

False

## Evidence Analysis

The important tests establish that the robot is moving in the direction that it should and is making the number of movements that it should, which is what I put as the student tests. However they cannot establish the margin of error and how much it will be

## Ai Disclosure

ChatGPT, I primarily used it to generate the pattern script and to do a little debugging, if I was really confused. At the same time, I did personally review my code and ensure everything worked through the tests.
