import re
import json

class FileParser:
    """A class to parse markdown front matter and JSON files"""

    def parse_front_matter(self, file_contents) -> dict:
        file_lines = file_contents.readlines()

        if len(file_lines) == 0:
            raise ValueError("File is empty")

        match = re.search("---", file_lines.pop(0))

        if not match:
            raise ValueError('File does not begin with front matter')

        front_matter = {}
        for line in file_lines:
            front_matter_end = re.search("---", line)

            if front_matter_end:
                break

            match = re.split(": ", line)
            front_matter[match[0]] = match[1].rstrip("\n")

        return front_matter

    def parse_json(self, file_contents) -> dict:
        return json.load(file_contents)

