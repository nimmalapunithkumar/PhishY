from flask import Flask, request, jsonify, render_template
from threading import Thread
from pipeline import URLClassifier

app = Flask(__name__)
classifier = URLClassifier()

def start_flask_app():
    app.run(debug=True, use_reloader=False)  # Set use_reloader=False to avoid threading issues

# Home route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to classify the URL or text
@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()

    if 'url' in data:
        url = data['url']
        result = classifier.classify_url(url)
    else:
        result = None  # Handle case where no URL is provided

    if 'text' in data:
        text = data['text']
        text_result = classifier.classify_text(text)
    else:
        text_result = None  # Handle case where no text is provided

    return jsonify({'url_result': result, 'text_result': text_result})

if __name__ == '__main__':
    # Start Flask app in a separate thread
    Thread(target=start_flask_app).start()
