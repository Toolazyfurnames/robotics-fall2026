# Mission 2

## Predictions

{'straight': "I predict the robot will finish 0.45m in front from it's starting point.", 'rotation': "I predict the robot's position will not change but the direction will turn it slightly to the left.", 'curve': 'I predict a right swinging curve because the robot is moving right while turning right, a negative radian turn.', 'curve_modified': 'This curve should be tighter because the radian turning speed is much higher and the forward speed is also higher.'}

## Prediction Locks

{'straight': '2026-09-09T16:41:03.977271+00:00', 'rotation': '2026-09-09T16:45:18.970391+00:00', 'curve': '2026-09-09T16:52:41.127020+00:00', 'curve_modified': '2026-09-09T17:02:27.104793+00:00'}

## Motion Comparison

On the curve trial, I was correct in that the turn would make a right swinging curve as the direction changed by -44.5 degrees, at the same time I was surprised that the robot only traveled 0.28m.

## Measurement Explanation

On the curve modified trial, the estimated travel path is higher than the start to end distance because the start to end distance describes the straight path from the robot's start position to end position while the travel path describes the actual path the robot traveled over, which would be the hypotenuse of the ste distance.

## Safety Explanation

The command guard checks every movement command given before the robot responds. The final zero command ends the trial by setting the forward speed and turning speed to 0. The timeout is needed if a program crashes or communication is lost, so the guard must send the stop command after 0.5 seconds of no new command.

## Modified Settings

{'linear_x': 0.15, 'angular_z': 0.8, 'duration': 4.0}
