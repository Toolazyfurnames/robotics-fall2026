# Mission 2

## comparison

The given settings of moving average and median have varying effects on error and response delay. With moving average, increasing the window generally increases error until 7, then it slightly reduces, then a small increase to response delay after a window size of 5(consistently 0.9-1.1). With median, Increasing weight has a positively linear effect on error and positively negative effect on delay.

## fusion_choice

The weights are equally separated by 0.25, and the weights work for each sensor as the weights for A push the outlier values much higher to compensate for its outlier prone nature. The weights for B also compensate for the missing values since B is much slower.

## manual_average

4.17

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

I think the error and response delay will have a positively linear relationship across configurations, error and response delay with increasing any value.

## responsiveness

Smoothing averages samples to cancel noise, the more the samples the later it reacts, which creates delay, and this is what is observed in the experiments as we increase the window size. For a nearby person, delay would consider a person that is there, and is recognized by the robot, but will assume that that person is in a position that they were actually in before.

## selected

1
