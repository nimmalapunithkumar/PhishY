# app.py

from flask import Flask, request, jsonify, render_template
from pipeline import URLClassifier

app = Flask(__name__)
classifier = URLClassifier()

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
    app.run(debug=True)
