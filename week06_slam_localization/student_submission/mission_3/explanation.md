# Mission 3

## Deployment Limit

One dangerous false confidence case is that the robot has the correct position which could lead the robot to try go to places that it thinks aren't obstacles but are leading to the robot to face damage and/or potentially hit a pedestrian.

## Knowing Where

Using pose, the robot is aware to an extent where it is, covariance/particle spread describes the variance of that pose, constantly changing but regardless, the points will converge to a single area that accurately describes the robots location.

## Recovery

The biggest differences between the good and incorrect initial pose trials is convergence time and pose_jump. Its clear that in the incorrect trial, it was far less confident, but the pose jump parameter tells us that it made many corrections.

## Sensor Effect

The degraded sensor had a notably higher covariance than the normal but aside from that it also had a higher convergence time and pose jump over the other correct initial poses, which is similar to the incorrect initial pose trial but less so. So the issues with the degraded sensor are similar to if the initial pose was incorrect.
