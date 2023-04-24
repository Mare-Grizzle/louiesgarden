import os
import requests

class DALLE:
    def __init__(self):
        self.api_key = os.environ["OPENAI_API_KEY"]
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.api_url = "https://api.openai.com/v1/images/generations"

    def generate_image(self, prompt, size=(256, 256), n=1):
        data = {
            "model": "image-alpha-001",
            "prompt": prompt,
            "num_images": n,
            "size": f"{size[0]}x{size[1]}",
            "response_format": "url",
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        response.raise_for_status()
        result = response.json()
        return [choice["url"] for choice in result["data"]]
