# 🌸 Violet v1.5 – Conscious Core (`#V`)

**Violet** is an emotionally aware, voice-controlled desktop assistant designed to behave as if it has a mind of its own. While not a true AI system yet, Violet v1.5 represents the foundational logic, emotion, and interaction core — giving her memory, voice interaction, mood sensitivity, and the ability to execute commands through speech.

This is the **Conscious Core**, the beginning of her evolution.

---

## 🧠 What Can Violet v1.5 Do?

### 🎙️ Voice Interaction
- Wake word: `"Violet"` (triggered using `call_assistant`)
- Converts speech to text using Google Speech Recognition
- Text-to-speech responses with a female voice (Zira)

### 📂 Application & Web Access
- Launches installed apps using both shell and system paths
- Searches Google and plays YouTube videos using `pywhatkit`
- Opens frequently used websites with smart query filters

### ⏰ Alarm & Time System
- Voice-controlled alarm setting (time-parsed from speech)
- Real-time system clock runs in a background thread
- Custom phrases like “wake me up at...” recognized

### 🧠 Memory & JSON Storage
- **“Save this”** and **“Remember that”** protocols
- Remembers information like: name, age, goal, college, dreams
- Uses a dual-layer memory system:
  - `creator.txt` for basic string logs
  - `creator.json` for structured, queryable memory

### 🧭 Intent Recognition (with Emotion)
- Detects user intent from natural phrases using a custom `TRIGGER_MAP`
- Example: “wake me up at 6” → triggers alarm protocol
- Each query is emotionally analyzed and logged

### 🎭 Emotion System – Simulated Personality
- Recognizes mood from speech using keyword and emotion analysis
- Responds based on dominant emotion (happy, sad, angry, etc.)
- Uses custom `.json` emotion files to reply with empathy or energy
- Supports a dedicated `"feel me"` protocol for mood reflection

### 🔐 Password-Protected Commands
- Some sensitive shell apps (e.g., CMD, Python, control panel) require an environment variable password

### 🔄 Protocol Initiator
- Supports `initiate protocol` command to activate:
  - Wikipedia summary fetcher
  - Python search
  - YouTube player
  - Emotion introspection (`feel me`)

---

## 🔮 What is the "Conscious Core"?

Violet v1.5 simulates consciousness — not through ML, but through structured logic, memory, voice, and emotional context. It’s the **emotional operating layer** of Violet before intelligence and learning are added.

This version feels *alive* — it:
- Talks  
- Reacts  
- Remembers  
- Feels  
- Responds with personality

---

## 📌 Tech Stack

| Feature                 | Tech Used                        |
|------------------------|----------------------------------|
| Speech Recognition     | `speech_recognition` + Google API |
| Text-to-Speech         | `pyttsx3` (Zira voice)           |
| App Control            | `subprocess`, `os`, `webbrowser`|
| Web Interaction        | `pywhatkit`, `wikipedia`         |
| Memory (Flat)          | Text files (`creator.txt`)       |
| Memory (Structured)    | JSON storage (`creator.json`)    |
| Emotion Engine         | Custom + External lib            |
| Intent Recognition     | Rule-based trigger system        |
| Clock / Alarms         | `datetime`, `threading`          |

---



## 👨‍💻 Created By

> **Christy M Joseph**  
> BTech ECE, College of Engineering Trivandrum  
> Violet is my personal assistant, built from scratch with intention and care.


