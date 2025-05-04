# mistral_runner.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load once at import time
model_name = "mistralai/Mistral-7B-Instruct-v0.1"

print("🔧 Loading Mistral model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)
model.eval()
print("✅ Mistral loaded.\n")

def generate_answer(prompt: str) -> str:
    print("\n🧪 PROMPT SENT TO MISTRAL:\n")
    print(prompt)
    print("\n🧪 END OF PROMPT\n")

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Optional: clean the output if prompt is echoed back
    if "Answer:" in decoded:
        return decoded.split("Answer:")[-1].strip()
    return decoded.strip()
