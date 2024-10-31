"""
This module contains the Flask application for the Emotion Detector.
It serves API requests and provides emotional analysis of user input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Processes the input text from the user and returns the emotional analysis response.

    Returns:
        str: A response containing the detected emotions and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', None)

    return (
        f"For the given statement, the system response is 'anger': "
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page for the application.

    Returns:
        str: The HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
