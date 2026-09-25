import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PointStamped
from tf2_ros import Buffer, TransformListener, TransformException
from tf2_geometry_msgs import do_transform_point


class CameraPointTransformer(Node):

    def __init__(self):
        super().__init__('camera_point_transformer')

        # TF2 buffer stores known coordinate-frame transforms.
        self.tf_buffer = Buffer()

        # Listens to /tf and /tf_static and fills the buffer.
        self.tf_listener = TransformListener(
            self.tf_buffer,
            self
        )

        # Point detected by the hallway camera.
        self.subscription = self.create_subscription(
            PointStamped,
            '/hallway_camera/detected_point',
            self.point_callback,
            10
        )

        # Optional: publish the transformed point.
        self.publisher = self.create_publisher(
            PointStamped,
            '/detected_point_base_link',
            10
        )

    def point_callback(self, point_msg):

        try:
            # Get the transform:
            #
            # camera frame --> base_link
            #
            # Using the point's timestamp is important if the robot/camera
            # may be moving.
            transform = self.tf_buffer.lookup_transform(
                'base_link',                   # target frame
                point_msg.header.frame_id,     # source frame
                point_msg.header.stamp
            )

            # Apply the transform to the detected point.
            point_in_base = do_transform_point(
                point_msg,
                transform
            )

            self.get_logger().info(
                f'Point in base_link: '
                f'x={point_in_base.point.x:.3f}, '
                f'y={point_in_base.point.y:.3f}, '
                f'z={point_in_base.point.z:.3f}'
            )

            self.publisher.publish(point_in_base)

        except TransformException as ex:
            self.get_logger().warn(
                f'Could not transform point to base_link: {ex}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = CameraPointTransformer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()