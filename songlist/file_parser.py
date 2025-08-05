import re

class FileParser:
    """A class to parse markdown front matter and JSON files"""

    def parse_front_matter(file_contents) -> dict:
        file_lines = file_contents.readlines()
        match = re.search("---", file_lines.pop(0))

        if not match:
            raise ValueError('File does not begin with front matter')

        for line in file_lines:
            front_matter_end = re.search("---", line)

            if front_matter_end:
                break

            match = re.split(": ", line)
            print(match)
