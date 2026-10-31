# Lab 7 saved answers

## mission_1.diagnosis
For normal_1, the box is on the mug, though it is larger than the cup itself. But in dim_1, the box is all over the image.  For normal_1, it could be that, considering the contour table and mask, the shadow is considered a part of the object. And for dim_1, this same effect causes the shadow to expand, as the mask considers the entire lighting part of the mug, extending the box across the image.

## mission_1.limitations
I changed the saturation, it lowered the mask's darkness and made more eligible candidates. The limitation of the shadow being considered part of the mug, which makes the object look bigger than it actually is.

## mission_2.comparison
Normal: in the classical model, the cup is found in both but the shadow is considered a part of the cup in both, and the learned model did find the cup in normal_2 but excludes the handle, and also misses the mug in normal_1. Neither makes false boxes.

Dim: Neither model gets a correct box, it could be because in dim the classical model considers lighting as part of the mug, while in learned you have the opposite problem, where the mug is a part of the lighting. This would also explain how both have a missed-mug count of 2 and how the classical model has a false box count of 2 as well.

Occluded: In this one, the classical model gets one correct box but in occluded_2 it gets one missed box. Meanwhile the learned model has 2 missed boxes.

## mission_2.choice
I would test the learned model further because it had less successes in detecting the object over the classical model. The learned model has a high mask_iou and dice, and a detailed foreground mask alone does not identify the mug as the classical model often struggled with changes in lighting. One big limit to this small image test is that the learned model requires more data to operate better than on just this single image.

## pillar_search.diagnosis
In 20261031T031351-90dfa76e, it seemed like a successful centering on the blue pillars. Changing the settings, particularly the steering gain seemed to have made it faster overall.

## pillar_search.evidence
In the four color attempt, the robot failed to center on the red pillar but centered on red and green, which may be why it is slightly pushed to the left, compared to some other attempts. The state timeline and camera show how the camera moved and where something could have gone wrong. A centered colored region and a stable hold cannot prove object identity or distance because the model must know the object beforehand and cannot tell its distance from where it is without a proper reference.

## line_following.comparison
For the practice world, I had to end the attempt due to it running infinitely. The settings were unchanged but they worked much worse for the curved segment as there was more drift with the turning. The mask in this case works really well due to the overall lack of color in the worlds but in a real world scenario would need more checks.

## line_following.limits
One stop from my attempts was the end of the practice, where it infinitely looped, it's unclear whether or not it occurred due to missing info, it could be the likely answer. But for a real delivery robot around people, this sort of thing could be fatal if it stops on a street where it could either block other people or cars could hit it while driving through, so we would need to check if something is causing the robot to stop.

## final.synthesis
These three missions taught how these models input visual evidence by taking lighting and contrast, as per classical models, or taking predefined data, as per learned models. The classical model works well with single images and take no time to deploy, but learned models rely on given data and might struggle if the data in not sufficient, this was observed in the classical and learned detector comparison. The pillar centering and line following missions shows both the benefits and the downsides of both the learned and classical models respectively. Regardless these models still face limitations when it comes to lighting as they are both reliant on colors, which are affected by light, to view the objects in their vicinity and they also need a frame of reference to tell things like distance or position, otherwise they cannot do that at all.

## final.course_reflection
This activity made me think about doing more into computer vision and would like to do more research into it. I think there should be some ethical considerations considering it requires the filming of other people and these machines need that data to operate but nevertheless this activity has really driven my motivation forward. What really stood out was the usage of different vision models and how old and new ones compared.
