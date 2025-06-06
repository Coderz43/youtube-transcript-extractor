from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable
from flask_cors import CORS 
import time

app = Flask(__name__)
CORS(app) 

@app.route('/api/transcript')
def transcript():
    video_id = request.args.get('videoId')
    if not video_id:
        return jsonify({"error": "Missing videoId parameter"}), 400
    tries = 3
    for attempt in range(tries):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return jsonify(transcript)
        except TranscriptsDisabled:
            return jsonify({"error": "Transcripts are disabled for this video"}), 403
        except NoTranscriptFound:
            return jsonify({"error": "No transcript available for this video"}), 404
        except VideoUnavailable:
            return jsonify({"error": "Video is unavailable"}), 404
        except Exception as e:
            print(f"INTERNAL SERVER ERROR: {str(e)}")
            time.sleep(1)
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=False, port=5000)
