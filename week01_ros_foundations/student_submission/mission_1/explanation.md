# Mission 1

## Scan Observation

I found a massive list of floating point numbers, which represents the distances to the nearest object from that scanner. 

## Guided Checks

{'node_list': True, 'guard_info': True, 'bridge_info': True, 'scan_info': True, 'scan_message': True, 'command_topics': True}

## Graph Explanation

A ROS 2 graph shows all the running nodes, which are the programs running the robot. For example, we had /course_cmd_vel_guard which we used as a safety check to approve which commands go through to the robot, these nodes utilize topics to communicate with each other or the hardware, for example we have /scan to communicate with the LiDAR sensors and return data.

## Command Path Explanation

A proposed command travels on /student_cmd_vel. The guard then publishes the command to /cmd_vel and the simlator bridge responds accordingly.

## Tools Explanation

Gazebo is responsible for simulating the robot and the world's physics while RViz is responsible for displaying relevant data such as sensor readings and position.
