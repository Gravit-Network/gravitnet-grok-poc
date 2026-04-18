# GravitNet × Grok — Multi-LLM Verifiable Integration PoC

Official open PoC that allows **any LLM** (Grok, Claude, GPT-4o, Gemini, Llama, Mistral, Ollama, etc.) to send hypotheses to Gravit and receive verifiable, adversarially-robust, immutable decision traces.

## Quick Start

```bash
cp .env.example .env
pip install -r requirements.txt
python test_grok_api.py          # Test Grok API
python poc_example.py            # Run full Gravit verification
