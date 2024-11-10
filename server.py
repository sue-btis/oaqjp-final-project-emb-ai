"""
Emotion Detection Server

THIS SCRIP DEFINES AN EMOTION DETECTOR BASED IN FLASK

Author(Learner): [SUE-BTIS]
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")  # Flask app instance

def run_app() -> None:
    """
    Starts the Flask application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def detect_emotion() -> str:
    """
    Endpoint to detect emotions from the provided text.

    Returns:
        str: Formatted response based on detected emotions or an error message if invalid.
    """
    text_to_detect = request.args.get('textToAnalyze')
    if not text_to_detect:
        return "No text provided! Please try again."

    formatted_response = emotion_detector(text_to_detect)

    if formatted_response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is: 'anger': {formatted_response['anger']}, "
        f"'disgust': {formatted_response['disgust']}, 'fear': {formatted_response['fear']}, "
        f"'joy': {formatted_response['joy']}, and 'sadness': {formatted_response['sadness']}. "
        f"The dominant emotion is {formatted_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page() -> str:
    """
    Renders the main index page of the application.

    Returns:
        HTML: The rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_app()
