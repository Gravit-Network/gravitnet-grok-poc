"""
llm_adapter.py - Universal adapter for any LLM to connect to Gravit
Use this file to integrate Gravit with Claude, GPT-4o, Gemini, Llama, etc.
"""

from gravit_grok_sdk import GravitGrokSDK

sdk = GravitGrokSDK()

def send_to_gravit(llm_provider: str, hypothesis: str, model_name: str = None):
    """
    Simple one-line function for any developer.
    Example: result = send_to_gravit("claude", "My hypothesis...")
    """
    result = sdk.evolve_from_llm(
        llm_provider=llm_provider,
        hypothesis=hypothesis,
        model_name=model_name
    )
    return result
