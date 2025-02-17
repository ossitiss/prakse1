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