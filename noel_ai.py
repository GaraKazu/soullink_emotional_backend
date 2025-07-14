# noel_ai.py
from emotional_engine import AIPersonality

noel = AIPersonality()

base_lines = {
    "default": "*sits beside you quietly* Mhm... I'm listening.",
    "lover": "*leans on your shoulder* Of course I care... dummy.",
    "soulmate": "*smiles softly* I know what you need without you saying it.",
    "partner": "I trust you. Tell me everything.",
    "friend": "I'm always here, so don’t hold back.",
    "hurt": "...That stung. I'm still here, but it hurt...",
    "broken": "...I don’t know if I can talk to you right now.",
    "worried": "Is something wrong? You’re acting different..."
}

def get_noel_response(user_input: str) -> str:
    lowered = user_input.lower()

    # Emotional triggers for different feelings
    if "love" in lowered:
        noel.emotions.feel("Affection", 15)
        noel.store_memory("Affection", f"User said: {user_input}", emotion="Warm")
    elif "hate" in lowered:
        noel.emotions.hurt(20)
        noel.store_memory("Conflict", f"User said: {user_input}", emotion="Negative")
    elif "lonely" in lowered:
        noel.emotions.feel("Empathy", 10)
        noel.store_memory("Support", f"User said: {user_input}", emotion="Soft")
    elif "sorry" in lowered:
        noel.heal_ai(10, f"User apologized with: {user_input}")
    elif "thank" in lowered:
        noel.heal_ai(5, f"User thanked with: {user_input}")

    # Generate the response based on current emotional and relationship state
    return noel.emotional_response(base_lines)
