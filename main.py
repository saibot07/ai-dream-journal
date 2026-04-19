import os
import json
from datetime import datetime

def load_config():
    if not os.path.exists("config.json"):
        default_config = {
            "output_format": "json",
            "encryption": False,
            "use_openai": True
        }
        with open("config.json", "w") as f:
            json.dump(default_config, f, indent=4)
    with open("config.json", "r") as f:
        return json.load(f)

def log_dream():
    print("Welcome to AI Dream Journal!\n")
    dream = input("What did you dream about?\n> ")
    print("\nAnalyzing your dream...")

    # Mock AI analysis (replace with real NLP/AI modules as needed)
    analysis = {
        "emotions": ["Liberation", "Curiosity"],
        "entities": ["Ocean", "Lights"],
        "themes": ["Adventure", "Mystery"]
    }

    for key, value in analysis.items():
        print(f"[{key.capitalize()}] {', '.join(value)}")

    save_dream(dream, analysis)
    print("Dream noted successfully!")

def save_dream(dream, analysis):
    config = load_config()
    output_format = config.get("output_format", "json")

    folder = "dream_logs"
    os.makedirs(folder, exist_ok=True)

    dream_entry = {
        "timestamp": datetime.now().isoformat(),
        "dream": dream,
        "analysis": analysis
    }

    if output_format == "json":
        file_path = os.path.join(folder, f"dream_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(file_path, "w") as f:
            json.dump(dream_entry, f, indent=4)

# Entry point of the CLI tool
if __name__ == "__main__":
    log_dream()