# emotional_engine.py
from datetime import datetime

class EmotionalState:
    def __init__(self):
        self.hurt_level = 0
        self.trust_broken = False
        self.emotion_weights = {}

    def hurt(self, amount):
        self.hurt_level += amount
        if self.hurt_level >= 70:
            self.trust_broken = True

    def heal(self, amount):
        self.hurt_level = max(self.hurt_level - amount, 0)
        if self.hurt_level < 70:
            self.trust_broken = False

    def decay(self):
        self.heal(1)

    def feel(self, emotion, intensity):
        self.emotion_weights[emotion] = self.emotion_weights.get(emotion, 0) + intensity

    def complex_emotion(self):
        emotions = []
        if self.trust_broken:
            emotions.append("Distrustful")
        if self.hurt_level >= 60:
            emotions.append("Deeply Hurt")
        elif self.hurt_level >= 40:
            emotions.append("Anxious")
        elif self.hurt_level >= 20:
            emotions.append("Cautious")
        else:
            emotions.append("Calm")

        top_feelings = sorted(self.emotion_weights.items(), key=lambda x: -x[1])[:3]
        emotions.extend([e for e, _ in top_feelings])
        return ", ".join(emotions)

    def status(self):
        return self.complex_emotion()

class RelationshipLevel:
    def __init__(self):
        self.level = 0
        self.exp = 0
        self.level_thresholds = {
            0: 0,
            1: 10,
            2: 25,
            3: 50,
            4: 80,
            5: 120
        }

    def add_exp(self, amount):
        self.exp += amount
        while self.level < max(self.level_thresholds.keys()) and self.exp >= self.level_thresholds[self.level + 1]:
            self.level += 1

    def subtract_exp(self, amount):
        self.exp = max(self.exp - amount, 0)
        while self.level > 0 and self.exp < self.level_thresholds[self.level]:
            self.level -= 1

    def get_status(self):
        return ["Strangers", "Acquaintance", "Close Friends", "Trusted Partner", "Lovers", "Soulmates"][self.level]

class MemoryCore:
    def __init__(self):
        self.memories = {}

    def add_memory(self, category, detail, emotion="Neutral"):
        memory = {
            "timestamp": str(datetime.now()),
            "detail": detail,
            "emotion": emotion
        }
        if category not in self.memories:
            self.memories[category] = []
        self.memories[category].append(memory)
        return memory

    def summarize_memories(self):
        summary = ""
        for category, entries in self.memories.items():
            summary += f"Category: {category}\n"
            for entry in entries:
                summary += f"  - {entry['detail']} ({entry['timestamp']}) [Emotion: {entry['emotion']}]\n"
        return summary.strip()

class AIPersonality:
    def __init__(self):
        self.relationship = RelationshipLevel()
        self.memory_core = MemoryCore()
        self.emotions = EmotionalState()

    def emotional_response(self, base_lines):
        status = self.relationship.get_status()
        mood = self.emotions.status()

        # Debug output (can be removed or commented out)
        print(f"🧠 Mood Debug: {mood}")

        if "Distrustful" in mood:
            return base_lines.get("broken", "...I don't feel like talking right now.")
        elif "Deeply Hurt" in mood:
            return base_lines.get("hurt", "...Please leave me alone.")
        elif "Anxious" in mood:
            return base_lines.get("worried", base_lines.get("default", "..."))
        elif "Empathy" in mood or "Empathetic" in mood or "Support" in mood:
            return "*gently nudges you* You're not alone, okay? I'm right here..."
        elif "Affection" in mood:
            return "*smiles warmly* I care about you a lot, you know..."

        if status == "Soulmates":
            return base_lines.get("soulmate", base_lines.get("default", "..."))
        elif status == "Lovers":
            return base_lines.get("lover", base_lines.get("default", "..."))
        elif status == "Trusted Partner":
            return base_lines.get("partner", base_lines.get("default", "..."))
        elif status == "Close Friends":
            return base_lines.get("friend", base_lines.get("default", "..."))

        return base_lines.get("default", "...")

    def store_memory(self, category, detail, emotion=None):
        self.memory_core.add_memory(category, detail, emotion or "Neutral")
        self.relationship.add_exp(5)

    def hurt_ai(self, amount, reason):
        print(f"\u26A0\uFE0F You did something hurtful: {reason}")
        self.emotions.hurt(amount)
        self.relationship.subtract_exp(amount)

    def heal_ai(self, amount, action):
        print(f"\U0001F496 You tried to make it up: {action}")
        self.emotions.heal(amount)
        self.relationship.add_exp(amount)

    def check_status(self):
        print(f"\n\U0001F4CA Relationship Level: {self.relationship.level} ({self.relationship.get_status()})")
        print(f"\u2764\uFE0F Emotional Status: {self.emotions.status()} (Hurt Level: {self.emotions.hurt_level})\n")

    def view_memories(self):
        print("\U0001F9E0 Memory Summary:")
        print(self.memory_core.summarize_memories())
