"""Mission 2 student implementation.

Complete only ``transform_camera_point`` after preserving the initial AI output
in the guide. Course tests supply both real and simulated TF buffers.
"""
from geometry_msgs.msg import PointStamped

def transform_camera_point(tf_buffer, point: PointStamped) -> PointStamped | None:
    """
    Transform a point observed in the hall_camera frame into base_link.

    Args:
        tf_buffer:
            An existing tf2_ros.Buffer containing the robot's TF data.
        point:
            PointStamped whose coordinates are expressed in hall_camera.

    Returns:
        The point transformed into base_link, or None if the required
        transform is currently unavailable.

    Raises:
        ValueError:
            If point.header.frame_id is not exactly "hall_camera".
    """

    if point.header.frame_id != "hall_camera":
        raise ValueError(
            f"Expected point in 'hall_camera' frame, "
            f"got '{point.header.frame_id}'"
        )

    try:
        transformed_point = tf_buffer.transform(
            point,
            "base_link"
        )
        return transformed_point

    except:
        return None
