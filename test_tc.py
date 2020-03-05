from unittest import TestCase

import tc


class Test(TestCase):

    def test_csv_reader_printing(self):
        """This function tests whether the CSV reader can read the csv file.

                       """

        filename = "test-data/test.csv"
        result = tc.csv_reader(filename)
        print(result)

    def test_csv_reader_empty_input(self):
        """This function tests whether the csv_reader can handle invalid input.

                       """

        filename = "nonsense"
        with self.assertRaises(Exception) as context:
            tc.csv_reader(filename)

        self.assertTrue('Invalid input' in str(context.exception))

    def test_csv_reader_basic_results_check(self):
        """This function tests whether the csv_reader outputs a valid dictionary.

                               """
        filename = "test-data/test.csv"
        result = tc.csv_reader(filename)
        expected_result = {1: {1, 2}, 2: {1, 2}, 3: {1, 3}, 4: {4}}
        self.assertEqual(expected_result, result)

    def test_kill_count(self):
        """This function tests whether the kill_count outputs a valid dictionary.

                               """
        test_input = {1: {1, 2}, 2: {1, 2}, 3: {1, 3}, 4: {4}}
        result = tc.kill_count(test_input)
        expected_result = {1: 2, 2: 2, 3: 2, 4: 1}
        self.assertEqual(expected_result, result)

    def test_sorter(self):
        """This function tests whether the sorter outputs a valid list of tuples.

                               """
        test_input = {1: 2, 2: 2, 3: 2, 4: 1}
        result = tc.sorter(test_input)
        expected_result = [(1, 2), (2, 2), (3, 2), (4, 1)]
        self.assertEqual(expected_result, result)



    def test_plot(self):
        """This function tests whether the plot actually plots the input coordinates.
                                      """
        test_input = ([[0, 0], [1, 2], [2, 3], [3, 4]])
        test_input2 = {1: {1, 2}, 2: {1, 2}, 3: {1, 3}, 4: {4}}
        test_input3 = [1, 2, 3, 4]
        tc.plot(test_input, test_input2, test_input3)

    def test_dominator_calculation_returns_empty_set_from_empty_kill_map(self):
        self.assertEqual(tc.calculate_dominating_mutants({}), {})

    def test_dominator_calculation_on_simple_graph(self):
        kill_map = {1: {1, 2, 4}, 2: {1, 3}, 3: {4}, 4: {2, 4}, 5: {1, 3, 4}}
        self.assertEqual(tc.calculate_dominating_mutants(kill_map), {2, 3})
