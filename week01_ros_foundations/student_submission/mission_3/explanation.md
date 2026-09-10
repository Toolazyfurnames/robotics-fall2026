# Mission 3

## Data To Command

The front_distance() function looks for the closest front distance by isolating the distances on the list of ranges to only those within the front(half-width-radians), then the next function decide_velocity() makes the actual decision of whether or not the robot should move, if the robot is too close to an object in front of it or if no good readings were found then don't move, otherwise move.

## Missing Data Safety

The robot does not move when there is no valid front measurement as we cannot be certain whether or not there is an object there or not, so the safest option is to not move.

## System Layers

The decision functions take the information from the /scan node, and they make the calculations as to what is in front of the robot and if it is safe to move, this information then goes to the command guard to finalize the decision.
