# Mission 1

## bias

0.0197

## bias_vs_variance

Bias is a more consistent and rigid value while variance is more scattered and unstable. My prediction somewhat holds true as this graph has low variance and low bias, which led most of the values to be near the actual value with some outliers reaching high or low numbers way off from the actual value.

## dropouts

7

## mean

2.0197

## median

2.01

## more_samples

More samples could alleviate the issue with this sensor but considering most of the values, excluding some outliers and invalid values, are close to the actual value it would likely be better to tune the variance slightly, though more data could absolutely help.

## outliers

21

## prediction

A consistently biased sensor would have its readings off from the actual distance by a consistent amount but a noisy sensor would have its data off by completely random amounts.

## prediction_draft

A consistently biased sensor would have its mean off from the actual distance by a consistent amount and its variance would be low, but a noisy sensor would have its mean data off by completely random amounts and the variance high.

## profile

outlier_prone

## robot_consequence

Say the robot was told to move forward by 5.00m but a person appears and the robot assumes they are 7.00m away(an outlier value) but they are actually 3.00m away, it could hit that person.

## variance

0.0911
