# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Nahil Rashid
- Email: nahil.rashid41@login.cuny.edu

## final.architecture_evidence

The node can be considered reactive as its behavior is determined by the sensor data and makes the decision, however to make a real hybrid system we would need a planning or mapping component.

## final.course_reflection

This activity really changed my perspective on robotics as I am not super familiar with this field in computer science but was still curious as to how software is made for these kind of machines. But still knowing more about robotics now, I would like to learn more and understand better how to structure software for robots.

## final.hardware_next

I would test the actual movement, because I am unsure as to how the units within the Gazebo translate to real world movement.

## final.middleware_debugging

It would allow you to get an idea as to where that command could have failed or if it was rejected by the command guard.

## final.system_synthesis

Robotics software is difficult because it requires the usage of numerous different software components and must translate software(and hardware) with certainties into real world actions with uncertainties. These software components have different tasks and must interact with each other in order for the machine to run its components. In this lab, I implemented a sense decide act architecture where the robot receives information from sensors then processes that information to make a decision, and lastly finalizes that decision by moving or not. It is relatively simple but the quality and timing of that sensor data is vital to making it work. If the sensor data was off, then something could go wrong with the decision making process and we would need additional safety mechanisms if a component failed. In fact, the robot must interpret missing data as a stop as we cannot say whether the path is really clear or if the sensor incorrectly interpreted that data. For this reason, front_distance() should ignore invalid measurements such as non-positive or non-finite distances, while decide_velocity() should stop the robot when we have no valid distance. And to restrict unsafe motion, we can use the command-guard as a safety layer, so that even if the controller requests an excessive or unsafe velocity, we can limit or reject that command before it reaches the robot.
ROS 2 connected the components of the system using publishers and subscribers. For example, /scan is the topic that connected the publisher, ros_gz_bridge, to the subscriber, course_evidence_collector, and this is how sensory data is transmitted. Through the topic /cmd_vel, ros_gz_bridge is also connected as a publisher to course_cmd_vel_guard (the command guard) which is how the commands given will be checked before going to the robot. ROS 2 middleware allows these components to communicate through topics without each component needing to know the implementation of the others.

## final.timing_evidence

I would say the fact that whenever invalid data arrives then we do not move the robot changed my understanding, initially I believed that an infinite reading would mean the area is clear as the closest object would be really far away but in reality we cannot exactly prove that the area in front of the robot is safe to travel towards.

## mission_1.command_path_explanation

A proposed command travels on /student_cmd_vel. The guard then publishes the command to /cmd_vel and the simlator bridge responds accordingly.

## mission_1.graph_explanation

A ROS 2 graph shows all the running nodes, which are the programs running the robot. For example, we had /course_cmd_vel_guard which we used as a safety check to approve which commands go through to the robot, these nodes utilize topics to communicate with each other or the hardware, for example we have /scan to communicate with the LiDAR sensors and return data.

## mission_1.guided_checks

{'node_list': True, 'guard_info': True, 'bridge_info': True, 'scan_info': True, 'scan_message': True, 'command_topics': True}

## mission_1.scan_observation

I found a massive list of floating point numbers, which represents the distances to the nearest object from that scanner. 

## mission_1.tools_explanation

Gazebo is responsible for simulating the robot and the world's physics while RViz is responsible for displaying relevant data such as sensor readings and position.

## mission_2.measurement_explanation

On the curve modified trial, the estimated travel path is higher than the start to end distance because the start to end distance describes the straight path from the robot's start position to end position while the travel path describes the actual path the robot traveled over, which would be the hypotenuse of the ste distance.

## mission_2.modified_settings

{'linear_x': 0.15, 'angular_z': 0.8, 'duration': 4.0}

## mission_2.motion_comparison

On the curve trial, I was correct in that the turn would make a right swinging curve as the direction changed by -44.5 degrees, at the same time I was surprised that the robot only traveled 0.28m.

## mission_2.prediction_locks

{'straight': '2026-09-09T16:41:03.977271+00:00', 'rotation': '2026-09-09T16:45:18.970391+00:00', 'curve': '2026-09-09T16:52:41.127020+00:00', 'curve_modified': '2026-09-09T17:02:27.104793+00:00'}

## mission_2.predictions

{'straight': "I predict the robot will finish 0.45m in front from it's starting point.", 'rotation': "I predict the robot's position will not change but the direction will turn it slightly to the left.", 'curve': 'I predict a right swinging curve because the robot is moving right while turning right, a negative radian turn.', 'curve_modified': 'This curve should be tighter because the radian turning speed is much higher and the forward speed is also higher.'}

## mission_2.safety_explanation

The command guard checks every movement command given before the robot responds. The final zero command ends the trial by setting the forward speed and turning speed to 0. The timeout is needed if a program crashes or communication is lost, so the guard must send the stop command after 0.5 seconds of no new command.

## mission_3.data_to_command

The front_distance() function looks for the closest front distance by isolating the distances on the list of ranges to only those within the front(half-width-radians), then the next function decide_velocity() makes the actual decision of whether or not the robot should move, if the robot is too close to an object in front of it or if no good readings were found then don't move, otherwise move.

## mission_3.missing_data_safety

The robot does not move when there is no valid front measurement as we cannot be certain whether or not there is an object there or not, so the safest option is to not move.

## mission_3.system_layers

The decision functions take the information from the /scan node, and they make the calculations as to what is in front of the robot and if it is safe to move, this information then goes to the command guard to finalize the decision.

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
