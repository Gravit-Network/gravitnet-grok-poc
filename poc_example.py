from gravit_grok_sdk import GravitGrokSDK

sdk = GravitGrokSDK()

hypothesis = "In a multi-agent AI system for critical decision-making, a Byzantine coalition of 30% malicious nodes attempts to inject false data and corrupt consensus."

result = sdk.evolve_from_llm(
    llm_provider="grok",
    hypothesis=hypothesis,
    model_name="grok-4"
)

print(result)
