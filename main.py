import telebot

bot = telebot.TeleBot(r"6941460819:AAFVcD9jvpnpQHLH3EpUra7BHmzdBgW2zNg")
chat_id = 5401218650

t = 12

HELP_MSG = """Here are all commands to work with licenses:

/settings - bot settings
/new - creates new license
/rem - deletes license
/see - sends all available and expired licenses
/edit - edits license

Bot will send you warning messages about licenses that have expired. You can set the time when it will do it.
"""

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "Welcome to MyCar! It's license tracking bot. For more information, send /help.")


@bot.message_handler(commands=["help"])
def help(msg):
    bot.send_message(msg.chat.id, HELP_MSG)


@bot.message_handler(commands=["settings"])
def settings(msg):
    bot.send_message(msg.chat.id, "Alright, now give me the hour (just a number, 24-h format) when I can send you messages about expired licenses.")
    bot.register_next_step_handler(msg, settime)

def settime(mesg):
    global time
    temp = None
    print(mesg.text)
    try:
        temp = int(mesg.text)
    except Exception:
        bot.send_message(mesg.chat.id, "It's not a number. Try again")
        return

    if not (temp >= 0 and temp <= 23):
        bot.send_message(mesg.chat.id, "Incorrect time format. Try again")
        return

    time = temp
    bot.send_message(mesg.chat.id, "New sending time set!")


bot.polling(non_stop=True)
