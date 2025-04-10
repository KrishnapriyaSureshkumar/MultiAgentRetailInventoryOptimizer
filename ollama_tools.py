import requests

class LLMQueryAgent:
    def __init__(self, model="phi"):  
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def query(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(self.url, json=payload, timeout=90)  
            response.raise_for_status() 
            return response.json().get("response", "LLM Error: Empty response").strip()
        
        except requests.exceptions.Timeout:
            return "LLM Timeout/Error: LLM took too long to respond. Try increasing timeout or warming up the model."

        except requests.exceptions.ConnectionError:
            return "LLM Error: Couldn't connect to Ollama. Did you run 'ollama serve' and 'ollama run phi'?"

        except requests.exceptions.RequestException as e:
            return f"LLM Error: {str(e)}"
