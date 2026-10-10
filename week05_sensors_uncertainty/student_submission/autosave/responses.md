# Week 5: Sensors, Noise, and Uncertainty

- course_id: 25
- email: nahil.rashid41@myhunter.cuny.edu
- name: Nahil Rashid

## concepts.observation

When I increased noise the values on the measurement sequence and the distribution graphs became less scattered. On the other hand, changing bias moved the all the points overall upwards or downwards on the measurement sequence or leftwards or rightwards on the distribution graph.

## final.course_reflection



## final.synthesis



## mission_1.bias

0.0197

## mission_1.bias_vs_variance

Bias is a more consistent and rigid value while variance is more scattered and unstable. My prediction somewhat holds true as this graph has low variance and low bias, which led most of the values to be near the actual value with some outliers reaching high or low numbers way off from the actual value.

## mission_1.dropouts

7

## mission_1.mean

2.0197

## mission_1.median

2.01

## mission_1.more_samples

More samples could alleviate the issue with this sensor but considering most of the values, excluding some outliers and invalid values, are close to the actual value it would likely be better to tune the variance slightly, though more data could absolutely help.

## mission_1.outliers

21

## mission_1.prediction

A consistently biased sensor would have its readings off from the actual distance by a consistent amount but a noisy sensor would have its data off by completely random amounts.

## mission_1.prediction_draft

A consistently biased sensor would have its mean off from the actual distance by a consistent amount and its variance would be low, but a noisy sensor would have its mean data off by completely random amounts and the variance high.

## mission_1.profile

outlier_prone

## mission_1.robot_consequence

Say the robot was told to move forward by 5.00m but a person appears and the robot assumes they are 7.00m away(an outlier value) but they are actually 3.00m away, it could hit that person.

## mission_1.variance

0.0911

## mission_2.comparison

The given settings of moving average and median have varying effects on error and response delay. With moving average, increasing the window generally increases error until 7, then it slightly reduces, then a small increase to response delay after a window size of 5(consistently 0.9-1.1). With median, Increasing weight has a positively linear effect on error and positively negative effect on delay.

## mission_2.fusion_choice

The weights are equally separated by 0.25, and the weights work for each sensor as the weights for A push the outlier values much higher to compensate for its outlier prone nature. The weights for B also compensate for the missing values since B is much slower.

## mission_2.manual_average

4.17

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

I think the error and response delay will have a positively linear relationship across configurations, error and response delay with increasing any value.

## mission_2.responsiveness

Smoothing averages samples to cancel noise, the more the samples the later it reacts, which creates delay, and this is what is observed in the experiments as we increase the window size. For a nearby person, delay would consider a person that is there, and is recognized by the robot, but will assume that that person is in a position that they were actually in before.

## mission_2.selected

1

## mission_3.Assistive.prediction_draft

Now by increasing weight and changing to moving avg we can get even more error than before, and potentially a dangerous command. Like the last test, this scenario would be challenged by the baseline.

## mission_3.Warehouse.prediction_draft

Last run, will try one more time to reduce delay and unnecessary stop, and by using the same settings as the first run but with a moving average threshold, it might help reduce the dangerous commands.

## mission_3.context_comparison

in the second to last policy of the warehouse robot, we got 2 dangerous commands and high delay which may have caused injury to any operators or may have damaged to equipment. The final policy of warehouse robot's results closely resembles the baseline, despite the fact that it is in a moving average configuration with a slightly lower sensor weight than the baseline. 

## mission_3.error_costs

Different people bear false safe and unnecessary stop costs. In all results of the warehouse simulation, we can see that unnecessary stopping was constantly on 0.0408, but this didn't necessarily lead to any dangerous commands, so at worst we have the company potentially losing money for slow warehouse flow. But when we made changes to configuration and window size, then we started getting dangerous commands, so there could be some damage to inventory/equipment.

## mission_3.limitations

The seven tests establish how each sensor reacts in different scenarios, and they also allow us to infer what could go wrong at certain times during these scenarios. However they do not establish the desired outcomes and for that we need to consult the client/user, and for testing we need to choose which one resembles the user's desired outcome, or create a new motion test all together.
