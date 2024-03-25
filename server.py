from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.json
    text_to_analyze = data['textToAnalyze']
    result = emotion_detector(text_to_analyze)
    
    # Format the response according to the example output
    response_text = "For the given statement, the system response is "
    response_text += ", ".join([f"'{emotion}': {score}" for emotion, score in result.items() if emotion != 'dominant_emotion'])
    response_text += f" and 'dominant_emotion' is {result['dominant_emotion']}."
    
    return jsonify(response_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
