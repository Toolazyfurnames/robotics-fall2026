# mission_3 Submission

- Name: (not provided)
- Section: (not provided)

## Explanations

### heading

The PID checks it's current heading and the direction of the goal point, and after making the calculations, adjusts its angle to make a steer towards the next goal point.

### integration

A well-tuned controller can still fail when odometry is wrong because the controller only sees the odometry not the physical environment, so even a well tuned controller will be off by a consistent amount if odometry is off.