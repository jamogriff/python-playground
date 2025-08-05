class FrontMatterMixin:
    """Provides methods to format a class into Markdown Front Matter"""

    def to_front_matter(self):
        front_matter = "---\n"
        for key, value in self.__dict__.items():
            front_matter += f"{key}: {value}\n"

        front_matter += "---\n"
        return front_matter
