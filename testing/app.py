from flask import Flask, render_template, jsonify
from fetch_trending import fetch_trending_topics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    unique_id, trending_topics, timestamp = fetch_trending_topics()
    return {
        "unique_id": unique_id,
        "trending_topics": trending_topics,
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "mongo_record": {
            "_id": unique_id,
            "trend1": trending_topics[0],
            "trend2": trending_topics[1],
            "trend3": trending_topics[2],
            "trend4": trending_topics[3],
            "trend5": trending_topics[4],
        }
    }

if __name__ == '__main__':
    app.run(debug=True)