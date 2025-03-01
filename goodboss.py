import os
import telebot
import schedule
import time
from openai import OpenAI

AI_TEXT_MODEL = 'deepseek-chat'
CHAT_TOKEN_NAME = "DEEPSEEK_API_KEY"
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@KaroshiyNasyalnika'

def job(CHAT_ID=CHAT_ID):
    client = OpenAI(api_key=os.environ.get(CHAT_TOKEN_NAME), base_url="https://api.deepseek.com")
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - технический директор, лидер команды с 100% харизмой" },
            { "role": "user", "content": "Заряди команду на свершения на весь день, не используй 'Конечно'" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

if __name__ == '__main__':
    schedule.every().day.at("09:00",'Europe/Moscow').do(job)

    half_day = 12 * 60 * 60

    for i in range(half_day):
        schedule.run_pending()
        time.sleep(1)
