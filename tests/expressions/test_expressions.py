import unittest
from . import Expressions

class TestExpressions(unittest.TestCase):
    """
    Complete tasks one after another. Once you are done with one task, run
    the test. It it fails, find the cause and repeat until the test works.
    Proceed to the next test until the full set of tests is complete.

    Start with the first test:
    pytest -v \
        tests/expressions/test_expressions.py::TestExpressions::test_a_number_of_numbers

    Add incrementally more tests until the full set is complete:
    # 
    pytest -v \
        tests/expressions/test_expressions.py::TestExpressions::test_a_number_of_numbers \
        tests/expressions/test_expressions.py::TestExpressions::test_b_first_three_numbers \
        tests/expressions/test_expressions.py::TestExpressions::test_c_first_three_numbers \
        tests/expressions/test_expressions.py::TestExpressions::test_d_last_three_in_reverse \
        tests/expressions/test_expressions.py::TestExpressions::test_e_odd_numbers \
        tests/expressions/test_expressions.py::TestExpressions::test_f_number_of_odd_numbers \
        tests/expressions/test_expressions.py::TestExpressions::test_g_sum_of_odd_numbers \
        tests/expressions/test_expressions.py::TestExpressions::test_h_duplicates_removed \
        tests/expressions/test_expressions.py::TestExpressions::test_i_number_of_duplicate_numbers \
        tests/expressions/test_expressions.py::TestExpressions::test_j_ascending_squaredClass_no_duplicates \
        tests/expressions/test_expressions.py::TestExpressions::test_k_classify_as_odd_even_empty

    Run tests in the IDE and in the terminal.
    """

    def setUp(self):
        self.ut1 = Expressions()    # default numbers: [4, 12, 3, 8, 17, 12, 1, 8, 7]
        self.ut2 = Expressions([1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8])
        self.ut3 = Expressions([6, 67, 6, 8, 17, 3, 6, 8])
        self.ut4 = Expressions([8, 3, 9])
        self.ut5 = Expressions([1, 1, 1])
        self.ut6 = Expressions([0, 0])
        self.ut7 = Expressions([0])
        self.ut8 = Expressions([])  # empty numbers[]

    def test_a_number_of_numbers(self):
        """Test number of numbers."""
        self.assertEqual(self.ut1.a, 9)
        self.assertEqual(self.ut2.a, 22)
        self.assertEqual(self.ut3.a, 8)
        self.assertEqual(self.ut4.a, 3)
        self.assertEqual(self.ut5.a, 3)
        self.assertEqual(self.ut6.a, 2)
        self.assertEqual(self.ut7.a, 1)
        self.assertEqual(self.ut8.a, 0)

    def test_b_first_three_numbers(self):
        """Test first three numbers."""
        self.assertEqual(self.ut1.b, [4, 12, 3])
        self.assertEqual(self.ut2.b, [1, 4, 6])
        self.assertEqual(self.ut3.b, [6, 67, 6])
        self.assertEqual(self.ut4.b, [8, 3, 9])
        self.assertEqual(self.ut5.b, [1, 1, 1])
        self.assertEqual(self.ut6.b, [0, 0])
        self.assertEqual(self.ut7.b, [0])
        self.assertEqual(self.ut8.b, [])

    def test_c_first_three_numbers(self):
        """Test first three numbers."""
        self.assertEqual(self.ut1.c, [1, 8, 7])
        self.assertEqual(self.ut2.c, [67, 6, 8])
        self.assertEqual(self.ut3.c, [3, 6, 8])
        self.assertEqual(self.ut4.c, [8, 3, 9])
        self.assertEqual(self.ut5.c, [1, 1, 1])
        self.assertEqual(self.ut6.c, [0, 0])
        self.assertEqual(self.ut7.c, [0])
        self.assertEqual(self.ut8.c, [])

    def test_d_last_three_in_reverse(self):
        """Test last three in reverse."""
        self.assertEqual(self.ut1.d, [7, 8, 1])
        self.assertEqual(self.ut2.d, [8, 6, 67])
        self.assertEqual(self.ut3.d, [8, 6, 3])
        self.assertEqual(self.ut4.d, [9, 3, 8])
        self.assertEqual(self.ut5.d, [1, 1, 1])
        self.assertEqual(self.ut6.d, [0, 0])
        self.assertEqual(self.ut7.d, [0])
        self.assertEqual(self.ut8.d, [])

    def test_e_odd_numbers(self):
        """Test odd numbers."""
        self.assertEqual(self.ut1.e, [3, 17, 1, 7])
        self.assertEqual(self.ut2.e, [1, 67, 23, 49, 67, 23, 37, 67, 19, 67])
        self.assertEqual(self.ut3.e, [67, 17, 3])
        self.assertEqual(self.ut4.e, [3, 9])
        self.assertEqual(self.ut5.e, [1, 1, 1])
        self.assertEqual(self.ut6.e, [])
        self.assertEqual(self.ut7.e, [])
        self.assertEqual(self.ut8.e, [])

    def test_f_number_of_odd_numbers(self):
        """Test number of odd numbers."""
        self.assertEqual(self.ut1.f, 4)
        self.assertEqual(self.ut2.f, 10)
        self.assertEqual(self.ut3.f, 3)
        self.assertEqual(self.ut4.f, 2)
        self.assertEqual(self.ut5.f, 3)
        self.assertEqual(self.ut6.f, 0)
        self.assertEqual(self.ut7.f, 0)
        self.assertEqual(self.ut8.f, 0)

    def test_g_sum_of_odd_numbers(self):
        """Test sum of odd numbers."""
        self.assertEqual(self.ut1.g, 28)
        self.assertEqual(self.ut2.g, 420)
        self.assertEqual(self.ut3.g, 87)
        self.assertEqual(self.ut4.g, 12)
        self.assertEqual(self.ut5.g, 3)
        self.assertEqual(self.ut6.g, 0)
        self.assertEqual(self.ut7.g, 0)
        self.assertEqual(self.ut8.g, 0)

    def test_h_duplicates_removed(self):
        """Test duplicates removed."""
        self.assertEqual(set(self.ut1.h), {4, 12, 3, 8, 17, 1, 7})
        self.assertEqual(set(self.ut2.h), {1, 4, 6, 67, 8, 23, 34, 49, 37, 19})
        self.assertEqual(set(self.ut3.h), {6, 67, 8, 17, 3})
        self.assertEqual(set(self.ut4.h), {8, 3, 9})
        self.assertEqual(self.ut5.h, [1])
        self.assertEqual(self.ut6.h, [0])
        self.assertEqual(self.ut7.h, [0])
        self.assertEqual(self.ut8.h, [])

    def test_i_number_of_duplicate_numbers(self):
        """Test number of duplicate numbers."""
        self.assertEqual(self.ut1.i, 2)
        self.assertEqual(self.ut2.i, 12)
        self.assertEqual(self.ut3.i, 3)
        self.assertEqual(self.ut4.i, 0)
        self.assertEqual(self.ut5.i, 2) # [1, 1, 1] has 2 duplicates 1
        self.assertEqual(self.ut6.i, 1) # [0, 0] has one duplicate number 0
        self.assertEqual(self.ut7.i, 0)
        self.assertEqual(self.ut8.i, 0)

    def test_j_ascending_squaredClass_no_duplicates(self):
        """Test ascending squared no duplicates."""
        self.assertEqual(set(self.ut1.j), {1, 9, 16, 49, 64, 144, 289})
        self.assertEqual(set(self.ut2.j), {1, 16, 36, 64, 361, 529, 1156, 1369, 2401, 4489})
        self.assertEqual(set(self.ut3.j), {9, 36, 64, 289, 4489})
        self.assertEqual(set(self.ut4.j), {9, 64, 81})
        self.assertEqual(self.ut5.j, [1])
        self.assertEqual(self.ut6.j, [0])
        self.assertEqual(self.ut7.j, [0])
        self.assertEqual(self.ut8.j, [])

    def test_k_classify_as_odd_even_empty(self):
        """Test classify as odd even empty."""
        self.assertEqual(self.ut1.k, "ODD_LIST")
        self.assertEqual(self.ut2.k, "EVEN_LIST")
        self.assertEqual(self.ut3.k, "EVEN_LIST")
        self.assertEqual(self.ut4.k, "ODD_LIST")
        self.assertEqual(self.ut5.k, "ODD_LIST")
        self.assertEqual(self.ut6.k, "EVEN_LIST")
        self.assertEqual(self.ut7.k, "ODD_LIST")
        self.assertEqual(self.ut8.k, "EMPTY_LIST")


if __name__ == '__main__':
    unittest.main()
