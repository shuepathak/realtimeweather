import requests

class APIService:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_data(self):
        try:
            # You need to specify a location and other required parameters for the WeatherAPI
            params = {
                'key': self.api_key,
                'q': 'London',  # Example location
                'aqi': 'no'
            }
            response = requests.get(f"{self.base_url}/current.json", params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None