from unittest import TestCase
from main import update_headings


class TestUpdateHeadings(TestCase):
    def test_remove_empty_properties(self):
        input_lines = [
            "* Diary",
            "\t:PROPERTIES:",
            "\t:END:",
            "* Diary2"
        ]
        expected_output = [
            "* Diary",
            "* Diary2"
        ]

        self.assertEqual(expected_output,
                         list(update_headings(input_lines)))

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

        expected_output = [
            "* Diary",
            "** 2022",
            "*** <2022-01-01 Mon 12:12> Today's entry",
            "",
            "Diary content line 1",
            "Diary content line 2"
        ]

        self.assertEqual(expected_output,
                         list(update_headings(input_lines)))

    def test_preserve_trailing_whitespace(self):
        input_lines = [
            "* Diary",
            "** 2022",
            "*** Today's entry\t\n",
            "\t:PROPERTIES:",
            "\t:CREATED:  [2022-01-01 Mon 12:12]",
            "\t:END:",
            "",
            "Diary content line 1",
            "Diary content line 2"
        ]
        expected_output = [
            "* Diary",
            "** 2022",
            "*** <2022-01-01 Mon 12:12> Today's entry\t\n",
            "",
            "Diary content line 1",
            "Diary content line 2"
        ]

        self.assertEqual(expected_output,
                         list(update_headings(input_lines)))

    def test_multi_heading_change(self):
        input_lines = [
            "* Diary",
            "** 2022",
            "*** Today's entry",
            "\t:PROPERTIES:",
            "\t:CREATED:  [2022-01-01 Mon 12:12]",
            "\t:END:",
            "",
            "Diary content line 1",
            "Diary content line 2",
            "*** Today's entry",
            "\t:PROPERTIES:",
            "\t:CREATED:  [2022-01-02 Tue 13:13]",
            "\t:END:",
            "",
            "Diary content line 1",
        ]
        expected_output = [
            "* Diary",
            "** 2022",
            "*** <2022-01-01 Mon 12:12> Today's entry",
            "",
            "Diary content line 1",
            "Diary content line 2",
            "*** <2022-01-02 Tue 13:13> Today's entry",
            "",
            "Diary content line 1",
        ]

        self.assertEqual(expected_output,
                         list(update_headings(input_lines)))

    def test_subheadings_inside_diary(self):
        input_lines = [
            "* Diary",
            "** 2022",
            "*** Today's entry",
            "\t:PROPERTIES:",
            "\t:CREATED:  [2022-01-01 Mon 12:12]",
            "\t:END:",
            "",
            "**** Inner heading",
            "***** Inner heading 2"
            "Diary content line 2"
        ]

        expected_output = [
            "* Diary",
            "** 2022",
            "*** <2022-01-01 Mon 12:12> Today's entry",
            "",
            "**** Inner heading",
            "***** Inner heading 2"
            "Diary content line 2"
        ]

        self.assertEqual(expected_output,
                         list(update_headings(input_lines)))