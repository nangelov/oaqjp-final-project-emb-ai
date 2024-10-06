import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions
from ibm_cloud_sdk_core.api_exception import ApiException
import os

ibm_watson_api_key = os.environ.get('MY_IBM_WATSON_API_KEY')
ibm_watson_service_id = os.environ.get('MY_IBM_WATSON_SERVICE_ID')

if ibm_watson_api_key is None or ibm_watson_service_id is None:
    raise ValueError("API key not found. Make sure MY_IBM_WATSON_API_KEY and MY_IBM_WATSON_SERVICE_ID environment variables are set.")

NO_EMOTIONS = {
    'anger': 'None',
    'disgust': 'None',
    'fear': 'None',
    'joy': 'None',
    'sadness': 'None',
    'dominant_emotion': 'None'
    }

def emotions_extractor(emotions):
    dominant_emotion = max(emotions, key=emotions.get)

    emotion_dict = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return emotion_dict

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    if not text_to_analyse:
        return json.dumps(NO_EMOTIONS, indent=4, sort_keys=False), 400
    try:
        authenticator = IAMAuthenticator(ibm_watson_api_key)
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2022-04-07',
            authenticator=authenticator)

        # URL of the emotion detection analysis service
        natural_language_understanding.set_service_url(ibm_watson_service_id)

        response = natural_language_understanding.analyze(
            text=text_to_analyse,
            features=Features(emotion=EmotionOptions())).get_result()

        emotions = response['emotion']['document']['emotion']
        emotion_dict = emotions_extractor(emotions)

        return json.dumps(emotion_dict, indent=4, sort_keys=False), 200
    except ApiException as e:
        return json.dumps({"message": f"Error: {e.message}, Status code: {e.code}"}), e.code

