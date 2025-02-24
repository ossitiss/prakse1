import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from WebFetcher import WebFetcher
from ContentComparator import ContentComparator

def send_email(subject, body, to_email):
    from_email = "prakse2025@inbox.lv"
    password = "JE8Xr3Ke8w"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach message body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP('mail.inbox.lv', 587)  # SMTP server and port
        server.set_debuglevel(1)  # Enable debugging to print the SMTP communication

        server.starttls()  # Upgrade to a secure connection
        server.login(from_email, password)  # Log in to the email server
        server.sendmail(from_email, to_email, msg.as_string())  # Send the email
        server.quit()  # Disconnect from the server
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed: Check your email or password.")
    except smtplib.SMTPConnectError:
        print("Connection error: Check your SMTP server and port.")
    except Exception as e:
        print("Failed to send email:", str(e))

if __name__ == "__main__":
    url = "https://www.neste.lv/lv/content/degvielas-cenas"
    
    # Fetch content
    fetcher = WebFetcher(url)
    new_html_content = fetcher.fetch_content()
    
    # Compare content
    comparator = ContentComparator(new_html_content)  # Initialize with new content
    comparator.load_previous_content("previous_content.txt")  # Load previous content from file
    changes = comparator.detect_changes()
    
    if changes:
        print("Changes detected:\n", changes)
        # Send email notification
        subject = "Content Change Detected"
        body = f"Changes detected in the content:\n{changes}"
        to_email = "oskars_val@inbox.lv"
        send_email(subject, body, to_email)
    
    # Save the current content only if changes are detected
    if changes:
        comparator.save_current_content("previous_content.txt")

'''
from WebFetcher import WebFetcher
from ContentParser import ContentParser
from ElementComparator import ElementComparator  # Import the updated ElementComparator class

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
        print("No changes detected in the specific element.")
    
    # Save the full HTML content for future comparisons
    comparator.save_current_content("previous_element_content.txt", new_html_content)
'''
