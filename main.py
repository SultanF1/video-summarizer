from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

import transformers








app = Flask(__name__)


cors = CORS(app)





def generate_transcript(url):
    id = url[url.index("=")+1:]
        
    transcript = YouTubeTranscriptApi.get_transcript(id)
    script = ""

    for text in transcript:
        t = text["text"]
        if t != '[Music]':
            script += t + " "
		
    return script























@app.route("/post", methods=["POST"])
def getME():
    url = request.get_json()['mes']
    print(url)
    summarization = pipeline(model='sshleifer/distilbart-cnn-12-6')
    res = summarization(generate_transcript(url), truncation=True)[0]['summary_text']
    print(res)
    return jsonify(res)



@app.route("/rec", methods=["GET","POST"])
def postME():
    summarization = pipeline(model='sshleifer/distilbart-cnn-12-6')
    res = summarization(generate_transcript('https://www.youtube.com/watch?v=0oBi8OmjLIg'), truncation=True)[0]['summary_text']
    return res
    
    

    


@app.route('/')
def index():
    return render_template('index.html')