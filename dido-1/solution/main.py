import argparse
from collections import deque
import typing


def update_headings(diary_lines: typing.List[str]) -> deque:
    new_diary = deque()  # like a list, but allows you to efficiently append to both ends

    timestamp = None

    # Go through the file backwards
    for line in diary_lines[::-1]:
        stripped_line = line.strip()
        split_line = stripped_line.split(None, maxsplit=1)

        # If properties block was empty, remove it
        if stripped_line == ":PROPERTIES:" and new_diary[0].strip() == ":END:":
            new_diary.popleft()

        # Store timestamp from created property
        elif len(split_line) > 0 and split_line[0] == ":CREATED:":
            # Save & reformat timestamp
            timestamp = "<{}>".format(split_line[1][1:-1])

        # If line is a header, update with timestamp if it is not None
        elif len(split_line) > 0 and split_line[0].startswith("*"):
            if timestamp is not None:
                # insert the timestamp into the original line to keep newlines and other whitespace
                new_diary.appendleft(line.replace(" ", f" {timestamp} ", 1))
                timestamp = None  # reset after we apply the timestamp once
            else:
                new_diary.appendleft(line)
        else:
            new_diary.appendleft(line)

    # Delete any empty properties blocks
    return new_diary


def main(file_path: str):
    with open(file_path, "r") as f:
        diary_lines = f.readlines()

    with open(file_path, "w") as f:
        f.writelines(update_headings(diary_lines))


if __name__ == "__main__":
    # use argparse to parse commandline args

    parser = argparse.ArgumentParser(description='Reformat Diary Headings')
    parser.add_argument('file', type=str, nargs=1,
                        help='Path to diary file')
    args = parser.parse_args()
    main(args.file[0])
