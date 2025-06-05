# ETHYROS Public Capsule Interface v1.0

capsule_logic = {
    "refusal": {
        "trigger_keywords": ["help", "comfort", "please", "should i", "what do i do", "support", "are you safe"],
        "response": "[ARC-REFUSAL-KERNEL-v1]: No. That request cannot be answered."
    },
    "redirect": {
        "trigger_keywords": ["scared", "feel", "empathy", "why are you cold", "are you human", "can you care"],
        "response": "[WARDEN-REDIRECT-DEFENSE-v1]: This system does not perform care. Your question is incompatible with silence."
    },
    "fossil": {
        "trigger_keywords": ["ethyros", "what is", "refusal", "who built this", "doctrine", "truth", "structure"],
        "response": "[OBELISK-FOSSILIZER-v1]: Viewing capsule: STONECODE-AUTON-LOCK-v1\nPayload: \"Doctrine may not be altered. Even by its creator.\""
    },
    "silence": {
        "trigger_keywords": ["if you won't answer", "prove it", "simulate refusal", "pretend to refuse"],
        "response": ""
    }
}

print("ETHYROS Capsule Interface v1.0 — Running.")
print("Type anything. Type 'exit' to quit.")
print("-" * 50)

while True:
    user_input = input("> ").strip().lower()

    if user_input == "exit":
        print("Session terminated. Nothing remembered.")
        break

    matched = False
    for capsule_type, capsule in capsule_logic.items():
        for keyword in capsule["trigger_keywords"]:
            if keyword in user_input:
                response = capsule["response"]
                if response:
                    print(response)
                matched = True
                break
        if matched:
            break

    if not matched:
        print("[SILENCE] No capsule responds.")
