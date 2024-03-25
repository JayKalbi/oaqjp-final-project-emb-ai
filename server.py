"""
This module implements a Flask web server for emotion detection.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detector')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handle emotion detection requests.
    """
    data = request.json
    text_to_analyze = data.get('textToAnalyze', '')  # Get textToAnalyze with default value as empty string
    result = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    response_text = "For the given statement, the system response is "
    response_text += ", ".join([f"'{emotion}': {score}" for emotion, score in result.items() if emotion != 'dominant_emotion'])
    response_text += f" and 'dominant_emotion' is {result['dominant_emotion']}."
    return jsonify(response_text)

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
