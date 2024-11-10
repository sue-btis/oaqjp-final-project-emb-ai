import flask from flask
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detection")

def runapp():
    app.run(host="0.0.0.0",port=5000)

@app.route("/emotionDetector")

if __name__ == "__main__":
    run_emotion_detection()