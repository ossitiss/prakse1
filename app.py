from flask import Flask, render_template, request, jsonify
import threading
import time
from main import check_for_changes, check_for_keyword  # Import functions to detect full changes and keyword

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Assumes your HTML file is named 'index.html'

# Handle the "Run" button request
@app.route('/run_row', methods=['POST'])
def run_row():
    data = request.get_json()
    url = data.get('url')
    regularity = int(data.get('regularity'))
    notification = data.get('notification')
    method = data.get('method')
    value = data.get('value')  # This will hold the keyword if the method is 'keyword'

    if not url or not notification or not regularity:
        return jsonify({'success': False, 'message': 'Missing required fields.'})

    # Start a new thread to handle the request
    def run_detection():
        while True:
            if method == "keyword":
                check_for_keyword(url, notification, value)
            else:
                check_for_changes(url, notification)
            time.sleep(regularity * 60 * 60)

    thread = threading.Thread(target=run_detection, daemon=True)
    thread.start()

    return jsonify({'success': True, 'message': 'Change detection is running.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
