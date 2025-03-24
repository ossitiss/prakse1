import difflib
import os

class contentComparator:
    def __init__(self, new_content):
        self.old_content = ""
        self.new_content = new_content

    def detect_changes(self):
        # If old content is still empty, no need to detect changes
        if not self.old_content:
            return "No previous content available for comparison."
    
        diff = difflib.ndiff(self.old_content.splitlines(), self.new_content.splitlines())
        changes = [line[2:] for line in diff if (line.startswith('+ ') or line.startswith('- ')) and line[2:].strip()]
        return '\n'.join(changes) if changes else "No changes detected."

    def load_previous_content(self, filename):
        # Create the file if it doesn't exist
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as file:
                file.write("")  # Create the file if it doesn't exist
        with open(filename, "r", encoding="utf-8") as file:
            self.old_content = file.read()  # Read the previous content

    def save_current_content(self, filename):
        # Save the new content to the file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.new_content)
