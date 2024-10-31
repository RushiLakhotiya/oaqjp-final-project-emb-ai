import requests
def emotion_detector(text):
    if not text or text.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    response = call_to_emotion_detection_api(text)  # Replace with actual API call logic
    # Check the response status code
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # If everything is fine, extract the relevant data from the response
    json_response = response.json()
    return {
        'anger': json_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': json_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': json_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': json_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': json_response['emotionPredictions'][0]['emotion']['sadness'],
        'dominant_emotion': json_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']
    }
