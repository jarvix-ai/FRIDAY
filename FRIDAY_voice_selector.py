import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Try to find a female voice automatically
female_voice = None

for voice in voices:
    if "female" in voice.name.lower() or "woman" in voice.name.lower():
        female_voice = voice
        break

# Set the voice
if female_voice:
    engine.setProperty('voice', female_voice.id)
    print(f"✅ Female voice selected: {female_voice.name}")
else:
    print("⚠️ No female voice found. Using default voice.")

# Test it
engine.say("Hello Sir, I'm FRIDAY. Ready for your command.")
engine.runAndWait()
