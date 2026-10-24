# Mission 1

## Limitations

The robot did not observe the boundaries well, as we have doubled walls. This could be caused by the fact that I consistently drove the robot around at 0.05 forward velocity, which may be too fast for the scan, or it could be rotational geometry as a hexagon can look similar when rotating so the map created another hexagon over it.

## Map Interpretation

The known fraction of the map is strange, because most of the map seems to appear on the pgm, but the map still does look strange and seems to layer over itself, so that data could be reliable. But, Speckle, and especially Border Contact, fraction should describe a higher number than what is given considering this fact, there is a lot of data that exists outside so border contact should be higher. Quality Score, may be the fairest value, since the map, while not good, does describe everything but has a lot of noise and other issues.

## System Observation

Scan would often show different points and these points likely align with the red diagram that RViz creates as some points are grouped together which matches with the pillars on the map. Odometry had changes that were most visible whenever I ran it while moving the robot where it would describe different translations depending on the directions I made it go. TF seems to be pretty messy and gives seemingly random numbers even when the robot isn't moving. The only change that Map seems to give is just printing out the positition, the actual map details seems to stay the same across runs.
