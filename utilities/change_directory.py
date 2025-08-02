import os

class ChangeDirectory:
    def __init__(self, new_directory: str):
        self.new_directory = new_directory
        self.old_directory = os.getcwd()

    def __enter__(self):
        print(f'Changing directory to {self.new_directory}')
        os.chdir(self.new_directory)

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'Returning to original directory {self.old_directory}')
        os.chdir(self.old_directory)
