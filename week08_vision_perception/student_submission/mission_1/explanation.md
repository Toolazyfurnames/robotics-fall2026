# mission_1

## diagnosis
For normal_1, the box is on the mug, though it is larger than the cup itself. But in dim_1, the box is all over the image.  For normal_1, it could be that, considering the contour table and mask, the shadow is considered a part of the object. And for dim_1, this same effect causes the shadow to expand, as the mask considers the entire lighting part of the mug, extending the box across the image.

## limitations
I changed the saturation, it lowered the mask's darkness and made more eligible candidates. The limitation of the shadow being considered part of the mug, which makes the object look bigger than it actually is.
