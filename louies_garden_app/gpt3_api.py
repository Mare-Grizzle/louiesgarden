import openai
import os

class GPT3:
    def __init__(self):
        self.api_key = os.environ["OPENAI_API_KEY"]
        openai.api_key = self.api_key

    def generate_text(self, prompt, max_tokens=300):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
