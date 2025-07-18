from app.model_gpt4 import run_gpt4_comparator

def compare_outputs_with_gpt4(original_text: str, local: str, gpt: str) -> dict:
    prompt = f"""
Given the following Jenkins pipeline:
{original_text}
Two YAML translations were generated. Choose the better one based on correctness and formatting.

YAML A:
{local}

YAML B:
{gpt}

Reply only with:
- A (if YAML A is better)
- B (if YAML B is better)
"""

    choice = run_gpt4_comparator(prompt)
    if "A" in choice.upper():
        return {"best": local, "source": "local"}
    elif "B" in choice.upper():
        return {"best": gpt, "source": "gpt4mini"}
    else:
        return {"best": gpt, "source": "gpt4mini"}  # fallback

