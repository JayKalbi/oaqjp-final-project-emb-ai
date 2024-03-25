import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert response text to dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotions and their scores
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return emotions and dominant emotion in required format
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
