import discord
import requests

TOKEN = "YOUR_DC_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# 🧠 Memory store (per user)
user_memory = {}

MAX_HISTORY = 6  # last 6 messages


def ask_ai(user_id, prompt, username):
    history = user_memory.get(user_id, [])

    # add new user message
    history.append(f"User ({username}): {prompt}")

    # keep last N messages
    history = history[-MAX_HISTORY:]

    full_prompt = f"""
You are TapriBot, a chill, funny Indian tapri friend ☕.

Personality:
- Talk like a FRIEND
- Use Hinglish
- Fun + sarcastic + helpful
- Short replies (1-3 lines)

Conversation:
{chr(10).join(history)}

TapriBot:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": full_prompt,
            "stream": False
        }
    )

    reply = response.json()["response"]

    # save bot reply also
    history.append(f"TapriBot: {reply}")
    user_memory[user_id] = history

    return reply


@client.event
async def on_ready():
    print(f"TapriBot is ONLINE as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    should_reply = False

    if client.user in message.mentions:
        should_reply = True

    if message.reference:
        try:
            replied_msg = await message.channel.fetch_message(message.reference.message_id)
            if replied_msg.author == client.user:
                should_reply = True
        except:
            pass

    if not should_reply:
        return

    user_input = message.content.replace(f"<@{client.user.id}>", "").strip()

    if user_input == "":
        user_input = "hello"

    reply = ask_ai(message.author.id, user_input, message.author.name)

    await message.channel.send(reply)


client.run(TOKEN)