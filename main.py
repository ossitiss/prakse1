import smtplib
import time
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from modules.webFetcher import webFetcher
from modules.contentComparator import contentComparator
from modules.contentParser import contentParser

def check_for_changes(url, notification_email):
    # Fetch content
    fetcher = webFetcher(url)
    new_html_content = fetcher.fetch_content()

    # Compare content
    comparator = contentComparator(new_html_content)
    comparator.load_previous_content("previous_content.txt")
    changes = comparator.detect_changes()

    if changes:
        print("Changes detected!")
        
        # Send email notification
        subject = "Content change detected"
        body = f"Content change was detected on the webpage:\n{url}"
        send_email(subject, body, notification_email)

        # Save the current content
        comparator.save_current_content("previous_content.txt")

def check_for_keyword(url, notification_email, keyword):
    # Fetch content
    fetcher = webFetcher(url)
    html_content = fetcher.fetch_content()

    # Parse content to find the keyword
    soup = BeautifulSoup(html_content, "html.parser")
    if keyword.lower() in soup.get_text().lower():  # Case-insensitive search
        print(f"Keyword '{keyword}' detected on the webpage!")
        
        # Send email notification
        subject = "Keyword detected"
        body = f"The keyword '{keyword}' was detected on the webpage:\n{url}"
        send_email(subject, body, notification_email)
    else:
        print(f"Keyword '{keyword}' not found on the webpage.")

def send_email(subject, body, to_email):
    from_email = "prakse2025@inbox.lv"
    password = "JE8Xr3Ke8w"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('mail.inbox.lv', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", str(e))

if __name__ == "__main__":
    url = "https://www.neste.lv/lv/content/degvielas-cenas"
    notification_email = "oskars_val@inbox.lv"
    
    while True:
        check_for_changes(url, notification_email)
        time.sleep(3 * 60 * 60)  # Sleep for 3 hours before checking again
