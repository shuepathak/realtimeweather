## Project Overview
This project sets up a simple weather data streaming service using Flask and Server-Sent Events (SSE). It continuously streams real-time weather data fetched from a third-party API.

## Features:
Real-time weather data updates using Server-Sent Events (SSE).
Simple and lightweight API structure using Flask and Flask-RESTful.
Customizable to work with various weather APIs (currently integrated with WeatherAPI).

## Requirements:
1) Python 3.x
2) Flask
3) Flask-RESTful
4) WeatherAPI key


## Installation

1) Clone the repository:
git clone https://github.com/shuepathak/your-repo-name.git
cd your-repo-name

2) Set up a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3) Install dependencies:
pip install -r requirements.txt
Configure APIService: In api_service.py, replace "MY API KEY" with your actual WeatherAPI key.

4) Run the Flask app:
python app.py

5) Access the app in your browser:
Navigate to http://127.0.0.1:5000/ for the root endpoint.
Access http://127.0.0.1:5000/stream to receive a continuous stream of weather data.


API Endpoints: 
GET /: A simple welcome message to confirm the server is running.
GET /stream: Starts streaming real-time weather data as Server-Sent Events (SSE). In our case on every second 

## How It Works:
The /stream route continuously fetches data from a third-party weather API and pushes the updates to the client in real-time via Server-Sent Events (SSE).
A new data point is fetched every second, and the client receives the latest weather information without needing to refresh the page.

## Future Improvements:
1) Add additional endpoints to fetch specific weather data (e.g., by city, country).
2) Implement caching to reduce the number of API requests.
3) Add error handling for failed API requests or connection timeouts.
4) Frontend to make the real time data more presentable 

**License
This project is licensed under the MIT License.
**
