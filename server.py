from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
import json

app = Flask("nanagelov Emotion Detector")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/emotionDetector')
def run_sentiment_analysis():
    text_to_analyze = request.args.get("textToAnalyze")
    resp, status_code = emotion_detector(text_to_analyze)
    resp_dict = json.loads(resp)
    if 400 == status_code and resp_dict["dominant_emotion"] == 'None':
        return {"message":"Invalid text! Please try again!"}, 400
    return resp_dict, status_code


if __name__ == "__main__":
    app.run(debug=True)
