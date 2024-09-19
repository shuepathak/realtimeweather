from flask import Flask, Response
from flask_restful import Api
from api_service import APIService
import json
import time

app = Flask(__name__)
api = Api(app)

# Your API Details 
api_service = APIService("OPENSOURCE WEATHER.COM", "YOUR API KEY")

@app.route('/')
def hello():
    return "Hello, Weather Data Streaming!"

@app.route('/stream')
def stream():
    def generate():
        while True:
            data = api_service.get_data()
            if data:
                yield f"data: {json.dumps(data)}\n\n"
            time.sleep(1)  # Wait for 1 sec before next request

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
