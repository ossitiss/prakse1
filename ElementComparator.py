import difflib
import os
from bs4 import BeautifulSoup

class ElementComparator:
    def __init__(self, selector):
        self.selector = selector
        self.old_element_content = ""
        self.new_element_content = ""

    def extract_content(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        element = soup.select_one(self.selector)  # Use CSS selector to find the element
        return element.text if element else ""

    def detect_changes(self):
        # Print old and new content for debugging
        print("Old Element Content:", self.old_element_content)
        print("New Element Content:", self.new_element_content)
        
        diff = difflib.ndiff(self.old_element_content.splitlines(), self.new_element_content.splitlines())
        changes = [line for line in diff if line.startswith('+ ') or line.startswith('- ')]
        return '\n'.join(changes)

    def load_previous_content(self, filename):
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as file:
                file.write("")  # Create the file if it doesn't exist
        with open(filename, "r", encoding="utf-8") as file:
            self.old_element_content = self.extract_content(file.read())
        # Print loaded old content for debugging
        print("Loaded Old Content:", self.old_element_content)

    def save_current_content(self, filename, full_html_content):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(full_html_content)

    def update_content(self, new_html_content):
        self.new_element_content = self.extract_content(new_html_content)
        # Print updated new content for debugging
        print("Updated New Content:", self.new_element_content)
