'''
from WebFetcher import WebFetcher
from ContentParser import ContentParser
from ContentComparator import ContentComparator

if __name__ == "__main__":
    url = "https://www.neste.lv/lv/content/degvielas-cenas"
    
    # Fetch content
    fetcher = WebFetcher(url)
    new_html_content = fetcher.fetch_content()
    
    # Parse content
    parser = ContentParser(new_html_content)
    prices = parser.parse_prices()
    print(f"Prices: {prices}")
    
    # Compare content
    comparator = ContentComparator("", new_html_content)
    comparator.load_previous_content("previous_content.txt")
    changes = comparator.detect_changes()
    
    if changes:
        print("Changes detected:\n", changes)
    
    comparator.save_current_content("previous_content.txt")
'''
from WebFetcher import WebFetcher
from ContentParser import ContentParser
from ElementComparator import ElementComparator  # Import the new class

if __name__ == "__main__":
    url = "https://www.neste.lv/lv/content/degvielas-cenas"
    
    # Fetch content
    fetcher = WebFetcher(url)
    new_html_content = fetcher.fetch_content()
    
    # Parse content (if needed for other purposes)
    parser = ContentParser(new_html_content)
    prices = parser.parse_prices()
    print(f"Prices: {prices}")
    
    # Compare content of a specific element
    selector = "strong"  # Update this selector to target the specific part of the page
    comparator = ElementComparator(selector)
    comparator.load_previous_content("previous_element_content.txt")
    comparator.update_content(new_html_content)
    changes = comparator.detect_changes()
    
    if changes:
        print("Changes detected in the specific element:\n", changes)
    else:
        print("No changes detected in the specific element.")  # Debug statement
    
    # Save the full HTML content
    comparator.save_current_content("previous_element_content.txt", new_html_content)
