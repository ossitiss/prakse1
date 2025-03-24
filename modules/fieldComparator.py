class fieldComparator:
    def __init__(self, selector, condition, target_value):
        self.selector = selector  # CSS Selector or XPath for the specific area
        self.condition = condition  # e.g., "less than", "greater than"
        self.target_value = target_value

    def check_change(self, page_content):
        # Extract the value from the specified area (using BeautifulSoup, for example)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page_content, 'html.parser')
        field = soup.select_one(self.selector)
        if field:
            current_value = float(field.get_text().strip())
            if self.evaluate_condition(current_value):
                return f"Target condition met: Current value {current_value}"
        return "No change detected"

    def evaluate_condition(self, current_value):
        if self.condition == "less than":
            return current_value < self.target_value
        elif self.condition == "greater than":
            return current_value > self.target_value
        return False
