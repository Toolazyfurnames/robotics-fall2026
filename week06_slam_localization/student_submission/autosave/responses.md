# Week 6: SLAM and Localization

- name: Nahil Rashid
- email: nahil.rashid41@login.cuny.edu
- course_id: 26

## concepts.prediction

One symptom of poor odometry will be wrong or exaggerated distances and one symptom of weak scan geometry will be the robot trying to travel to places that don't exist in the physical world. Poor odometry could be found in Gazebo and VSLAM will be useful for finding weak scan geometry.

## final.course_reflection

On my interests in robotics and etc I found this more exciting as a task because it involved actual trial and error compared to some of the last few labs, which makes it more of a "lab" in that sense. This activity was also one of the most rigorous and process heavy assignments to date (I lost 50% of my battery in 1 hour) so indeed I am a little scared for my computer regarding my motivation but I still would love to keep going with this class. Using RViz to create a map, and even seeing that map as a PGM, was definitely the most standout feature of this lab as it gives a glimpse into how these machines actually interpret its concept of location.

## final.synthesis

For this robot to know where it is, it utilizes a map as a representation of its environment to determine its location. Using SLAM, a robot can construct a map and estimate its own position within it. Whenever a robot returns to a previously visited location, it can recognize that environment and correct any errors from that return, that is loop closure, and it can be determined by examining odometry and seeing if the robot connects that odometry back to the map. The robot also needs to know where it started, initial pose, as a reference for localization, and as we saw, having an incorrect starting pose causes the robot to misinterpret its location on the map. We saw in our tests that the robot had a much higher convergence time and pose jump in the incorrect initial pose trial over the correct initial pose trial, meaning the robot had less confidence and was trying to correct itself frequently. With sensor quality, we observed that poor sensors can lead to errors similar to incorrect initial position, which makes sense as with bad sensors the robot can reduce localization accuracy which also happens with bad initial pose. But overall, for a robot to know where it is does not mean that the robot needs to know exactly where it is down to the atom, rather it needs a precise estimate of its location, and to correct itself if necessary.

## mission_1.limitations

The robot did not observe the boundaries well, as we have doubled walls. This could be caused by the fact that I consistently drove the robot around at 0.05 forward velocity, which may be too fast for the scan, or it could be rotational geometry as a hexagon can look similar when rotating so the map created another hexagon over it.

## mission_1.map_interpretation

The known fraction of the map is strange, because most of the map seems to appear on the pgm, but the map still does look strange and seems to layer over itself, so that data could be reliable. But, Speckle, and especially Border Contact, fraction should describe a higher number than what is given considering this fact, there is a lot of data that exists outside so border contact should be higher. Quality Score, may be the fairest value, since the map, while not good, does describe everything but has a lot of noise and other issues.

## mission_1.system_observation

Scan would often show different points and these points likely align with the red diagram that RViz creates as some points are grouped together which matches with the pillars on the map. Odometry had changes that were most visible whenever I ran it while moving the robot where it would describe different translations depending on the directions I made it go. TF seems to be pretty messy and gives seemingly random numbers even when the robot isn't moving. The only change that Map seems to give is just printing out the positition, the actual map details seems to stay the same across runs.

## mission_2.comparison

Looking at the map, it seems that we fixed the double walls that appeared in the first map, the map even came out as much smaller than the original because of this. It seems our prediction was correct in this regard as going slower, not making stops, or going backwards helped prevent double walls and with loop closure. Unsurprisingly our new map has less speckle than our first map but surprisingly we had more border contact, despite the fact that we barely traveled to the border in our run. Also on the pillars, in the original map, the pillars were all rotated and were messy, in our new map, the pillars appear more cleaner with the exception of two pillars on the top right and bottom right. But overall my prediction was correct.

## mission_2.loop_closure

The second map itself could be evidence of a loop closure, as it is much more coherent compared to the first map, so we could have had a loop closure. But this cannot be confirmation as to truly confirm a loop closure we would need to examine odometry further and compare it with map readings. Loop closure would be a change in existing data, map growth is the addition of new data.

## mission_2.strategy_prediction

For this second run, I intend to go across more parts of the map while also avoiding the edges, this should help alleviate the double walls that appear. I also want to avoid going backwards and avoid stopping, which should also help with continuity and loop closure.

## mission_3.deployment_limit

One dangerous false confidence case is that the robot has the correct position which could lead the robot to try go to places that it thinks aren't obstacles but are leading to the robot to face damage and/or potentially hit a pedestrian.

## mission_3.knowing_where

Using pose, the robot is aware to an extent where it is, covariance/particle spread describes the variance of that pose, constantly changing but regardless, the points will converge to a single area that accurately describes the robots location.

## mission_3.recovery

The biggest differences between the good and incorrect initial pose trials is convergence time and pose_jump. Its clear that in the incorrect trial, it was far less confident, but the pose jump parameter tells us that it made many corrections.

## mission_3.sensor_effect

The degraded sensor had a notably higher covariance than the normal but aside from that it also had a higher convergence time and pose jump over the other correct initial poses, which is similar to the incorrect initial pose trial but less so. So the issues with the degraded sensor are similar to if the initial pose was incorrect.
