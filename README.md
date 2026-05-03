# 🤖 TapriBot – AI Discord Bot (LLaMA3)

TapriBot is an AI-powered Discord chatbot built using a local LLaMA3 model (Ollama).
It responds like a chill tapri friend using Hinglish, with short, fun, and context-aware replies.

---

## 🧠 Features

- Real-time AI responses in Discord  
- Per-user memory (context-aware chat)  
- Custom Hinglish personality (fun + sarcastic tone)  
- Runs locally using Ollama (no external API required)  
- Maintains recent chat history for better replies  

---

## 🛠️ Tech Stack

- Python  
- discord.py  
- Ollama (LLaMA3)  
- requests  

---

## 🚀 Setup

### 1. Clone the repository
git clone https://github.com/articblue3452/tapribot.git  
cd tapribot  

### 2. Install dependencies
pip install discord requests  

### 3. Run LLaMA3 using Ollama
ollama run llama3  

### 4. Set your Discord bot token

import os  
TOKEN = os.getenv("DISCORD_TOKEN")  

### 5. Run the bot
python bot.py  

---

## ⚙️ How It Works

- Bot listens when mentioned or replied to  
- Stores last few messages per user  
- Generates responses using LLaMA3 via Ollama  
- Sends reply back to Discord  


---

## 🔮 Future Improvements

- Add !reset command (clear memory)  
- Multiple personality modes  
- Improved memory handling  

---

## 👨‍💻 Author

ARTIC BLUE  
GitHub: https://github.com/articblue3452
