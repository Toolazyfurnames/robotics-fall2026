import os
import unittest
from week03_pattern.pattern import build_pattern

class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        # Add assertions for your assigned pattern.
        self.assertEqual(len(segments), 3)

        self.assertGreater(segments[0].linear_x, 0.0)
        self.assertEqual(segments[0].angular_z, 0.0)

        first_distance = segments[0].linear_x * segments[0].duration
        second_distance = segments[2].linear_x * segments[2].duration
        self.assertAlmostEqual(first_distance, 0.4)
        self.assertAlmostEqual(second_distance, 0.4)

        self.assertGreater(segments[1].angular_z, 0.0)
        turn_angle = segments[1].angular_z * segments[1].duration
        self.assertAlmostEqual(turn_angle, 3.141592653589793 / 2)


        total_duration = 0.0
        for segment in segments:
            self.assertLessEqual(abs(segment.linear_x), 0.22)
            self.assertLessEqual(abs(segment.angular_z), 0.80)
            self.assertLessEqual(segment.duration, 30.0)
            total_duration += segment.duration

        self.assertLessEqual(total_duration, 60.0)
        

    def test_my_pattern_order(self):
        # Check another property with a known expected result.
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
 
        self.assertGreater(segments[0].linear_x, 0.0)
        self.assertEqual(segments[0].angular_z, 0.0)

        self.assertEqual(segments[1].linear_x, 0.0)
        self.assertGreater(segments[1].angular_z, 0.0)

        self.assertGreater(segments[2].linear_x, 0.0)
        self.assertEqual(segments[2].angular_z, 0.0)