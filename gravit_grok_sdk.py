import os
import requests
from typing import Optional, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class GravitGrokSDK:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.grok_client = OpenAI(
            api_key=os.getenv("XAI_API_KEY"),
            base_url="https://api.x.ai/v1"
        )

    def evolve_from_llm(self,
                        llm_provider: str,
                        hypothesis: str,
                        model_name: Optional[str] = None,
                        temperature: float = 0.7) -> Dict[str, Any]:
        """
        Universal method: Any LLM → Gravit verification pipeline
        """
        # Optional: Let the LLM refine the hypothesis first
        if llm_provider.lower() in ["grok", "xai"]:
            response = self.grok_client.chat.completions.create(
                model=model_name or "grok-4",
                messages=[{"role": "user", "content": hypothesis}],
                temperature=temperature,
                max_tokens=1024
            )
            hypothesis = response.choices[0].message.content
# Send to Gravit for full GQRVP processing
        payload = {
            "llm_provider": llm_provider,
            "model_name": model_name,
            "hypothesis": hypothesis,
            "temperature": temperature
        }

        response = requests.post(f"{self.base_url}/evolve_from_llm", json=payload)
        return response.json()
