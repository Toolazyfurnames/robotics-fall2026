# mission_2

## comparison
Normal: in the classical model, the cup is found in both but the shadow is considered a part of the cup in both, and the learned model did find the cup in normal_2 but excludes the handle, and also misses the mug in normal_1. Neither makes false boxes.

Dim: Neither model gets a correct box, it could be because in dim the classical model considers lighting as part of the mug, while in learned you have the opposite problem, where the mug is a part of the lighting. This would also explain how both have a missed-mug count of 2 and how the classical model has a false box count of 2 as well.

Occluded: In this one, the classical model gets one correct box but in occluded_2 it gets one missed box. Meanwhile the learned model has 2 missed boxes.

## choice
I would test the learned model further because it had less successes in detecting the object over the classical model. The learned model has a high mask_iou and dice, and a detailed foreground mask alone does not identify the mug as the classical model often struggled with changes in lighting. One big limit to this small image test is that the learned model requires more data to operate better than on just this single image.
