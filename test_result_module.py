import unittest

from result_module import calculate_gpa, calculate_total_score, generate_result


class TestCalculateTotalScore(unittest.TestCase):
    def test_valid_scores_are_summed(self):
        self.assertEqual(calculate_total_score(18, 17, 52), 87)

    def test_maximum_scores_produce_one_hundred(self):
        self.assertEqual(calculate_total_score(20, 20, 60), 100)

    def test_scores_above_each_component_maximum_are_rejected(self):
        cases = [
            (21, 0, 0),
            (0, 21, 0),
            (0, 0, 61),
        ]

        for assignment, test, examination in cases:
            with self.subTest(
                assignment=assignment, test=test, examination=examination
            ):
                with self.assertRaises(ValueError):
                    calculate_total_score(assignment, test, examination)

    def test_negative_scores_are_rejected(self):
        cases = [
            (-1, 0, 0),
            (0, -1, 0),
            (0, 0, -1),
        ]

        for assignment, test, examination in cases:
            with self.subTest(
                assignment=assignment, test=test, examination=examination
            ):
                with self.assertRaises(ValueError):
                    calculate_total_score(assignment, test, examination)

    def test_non_numeric_score_is_rejected(self):
        with self.assertRaises(TypeError):
            calculate_total_score("18", 17, 52)


class TestGenerateResult(unittest.TestCase):
    def test_valid_result_strips_name_and_registration_whitespace(self):
        result = generate_result(
            name="  Ada Lovelace  ",
            registration_number="  CSC/2026/001  ",
            course_code="CSC 101",
            assignment=18,
            test=17,
            examination=52,
        )

        self.assertEqual(
            result,
            {
                "student_name": "Ada Lovelace",
                "registration_number": "CSC/2026/001",
                "course_code": "CSC 101",
                "total": 87,
                "grade": "A",
                "grade_point": 5,
            },
        )

    def test_score_above_component_maximum_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_result("Ada", "CSC/2026/001", "CSC 101", 21, 17, 52)


class TestCalculateGpa(unittest.TestCase):
    def test_valid_course_results_return_credit_weighted_gpa(self):
        courses = [
            {"grade_point": 5, "credit_unit": 3},
            {"grade_point": 4, "credit_unit": 2},
            {"grade_point": 2, "credit_unit": 1},
        ]

        self.assertAlmostEqual(calculate_gpa(courses), 25 / 6)

    def test_empty_course_list_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_gpa([])

    def test_grade_points_outside_valid_range_are_rejected(self):
        for grade_point in (-1, 6):
            with self.subTest(grade_point=grade_point):
                with self.assertRaises(ValueError):
                    calculate_gpa(
                        [{"grade_point": grade_point, "credit_unit": 3}]
                    )

    def test_non_numeric_grade_point_is_rejected(self):
        with self.assertRaises(TypeError):
            calculate_gpa([{"grade_point": "5", "credit_unit": 3}])

    def test_non_positive_credit_units_are_rejected(self):
        for credit_unit in (0, -1):
            with self.subTest(credit_unit=credit_unit):
                with self.assertRaises(ValueError):
                    calculate_gpa(
                        [{"grade_point": 5, "credit_unit": credit_unit}]
                    )

    def test_non_numeric_credit_unit_is_rejected(self):
        with self.assertRaises(TypeError):
            calculate_gpa([{"grade_point": 5, "credit_unit": "3"}])


if __name__ == "__main__":
    unittest.main()