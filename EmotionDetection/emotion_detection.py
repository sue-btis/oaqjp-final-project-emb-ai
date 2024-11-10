import requests
import json

def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputjson= { "raw_document": { "text": text_to_analyze } }

    response=requests.post(URL,json=inputjson,headers=Header)

    if response.status_code==200:
        response=response.json()
        formated_response=modify_response(response)
        return formated_response
    elif response.status_code==400:
        formated_response = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None}
        return formated_response

def modify_response(response):
    emotions = response['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    max_emotion = max(emotions, key=emotions.get)
    formated_response = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': max_emotion} 
    return formated_response