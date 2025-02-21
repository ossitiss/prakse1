import difflib
import os

class ContentComparator:
    def __init__(self, old_content, new_content):
        self.old_content = old_content
        self.new_content = new_content

    def detect_changes(self):
        diff = difflib.ndiff(self.old_content.splitlines(), self.new_content.splitlines())
        changes = [line for line in diff if line.startswith('+ ') or line.startswith('- ')]
        return '\n'.join(changes)

    def load_previous_content(self, filename):
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as file:
                file.write("")  # Create the file if it doesn't exist
        with open(filename, "r", encoding="utf-8") as file:
            self.old_content = file.read()

    def save_current_content(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.new_content)

