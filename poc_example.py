from gravit_grok_sdk import GravitGrokSDK

sdk = GravitGrokSDK()

hypothesis = "The integration of Grok and Gravit creates a verifiable epistemic evolution system that survives adversarial conditions and preserves truth for future generations."

result = sdk.evolve(hypothesis)

print(json.dumps(result, indent=2))
