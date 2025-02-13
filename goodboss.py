import os
import telebot
import schedule
import time
from openai import OpenAI

AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
# CHAT_ID = -1002374309134
CHAT_ID = '@KaroshiyNasyalnika'

def job(prompt):
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - отличный руководитель команды" },
            { "role": "user", "content": prompt },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

schedule.every().day.at("09:00",'Europe/Moscow').do(job, prompt="Заряди команду на свершения на весь день")
#schedule.every().day.at("11:00",'Europe/Moscow').do(job, prompt="Позови команду на кофе")
#schedule.every().day.at("13:00",'Europe/Moscow').do(job, prompt="Напомни команде об обеде")
#schedule.every().day.at("16:00",'Europe/Moscow').do(job, prompt="Позови команду на чай")
#schedule.every().day.at("18:00",'Europe/Moscow').do(job, prompt="Напомни команде об окончании рабочего дня")

half_day = 12 * 60 * 60

for i in range(half_day):
    schedule.run_pending()
    time.sleep(1)
