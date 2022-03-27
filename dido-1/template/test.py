from unittest import TestCase
from main import update_headings


class TestUpdateHeadings(TestCase):
    def test_single_heading_change(self):
        input_lines = [
            "* Diary",
            "** 2022",
            "*** Today's entry",
            "\t:PROPERTIES:",
            "\t:CREATED:  [2022-01-01 Mon 12:12]",
            "\t:END:",
            "",
            "Diary content line 1",
            "Diary content line 2"
        ]

        # copy the list & create a nwe one
        expected_output = input_lines[:]
        expected_output[2] = "*** <2022-01-01 Mon 12:12> Today's entry"
        del expected_output[3:6]  # delete properties block

        self.assertEqual(expected_output,
                         update_headings(input_lines))

    # TODO:
    # def test_multi_heading_change(self):

    # TODO:
    # def test_subheadings_inside_diary(self):
    
