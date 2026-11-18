import unittest
from grading import calculate_grade, calculate_grade_point


class TestGrading(unittest.TestCase):
    def test_grade_boundaries_and_transitions(self):
        cases = [
            (39, "F"),
            (40, "E"),
            (44, "E"),
            (45, "D"),
            (49, "D"),
            (50, "C"),
            (59, "C"),
            (60, "B"),
            (69, "B"),
            (70, "A"),
        ]

        for score, expected_grade in cases:
            with self.subTest(score=score):
                self.assertEqual(calculate_grade(score), expected_grade)

    def test_grade_point_boundaries_and_transitions(self):
        cases = [
            (39, 0),
            (40, 1),
            (44, 1),
            (45, 2),
            (49, 2),
            (50, 3),
            (59, 3),
            (60, 4),
            (69, 4),
            (70, 5),
        ]

        for score, expected_grade_point in cases:
            with self.subTest(score=score):
                self.assertEqual(calculate_grade_point(score), expected_grade_point)

    def test_valid_score_endpoints(self):
        cases = [
            (0, "F", 0),
            (1, "F", 0),
            (99, "A", 5),
            (100, "A", 5),
        ]

        for score, expected_grade, expected_grade_point in cases:
            with self.subTest(score=score):
                self.assertEqual(calculate_grade(score), expected_grade)
                self.assertEqual(calculate_grade_point(score), expected_grade_point)

    def test_out_of_range_scores_raise_value_error(self):
        for score in (-1, 101):
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    calculate_grade(score)
                with self.assertRaises(ValueError):
                    calculate_grade_point(score)

    def test_non_numeric_scores_raise_type_error(self):
        for score in ("75", True, None):
            with self.subTest(score=score):
                with self.assertRaises(TypeError):
                    calculate_grade(score)
                with self.assertRaises(TypeError):
                    calculate_grade_point(score)

if __name__ == "__main__":
    unittest.main()
