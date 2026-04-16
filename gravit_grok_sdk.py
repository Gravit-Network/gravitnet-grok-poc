import requests
import json

class GravitGrokSDK:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def evolve(self, hypothesis: str):
        """Send Grok hypothesis to Gravit and receive verified anchor"""
        payload = {"hypothesis": hypothesis}
        response = requests.post(f"{self.base_url}/grok_evolve", json=payload)
        return response.json()
