import telegram

TOKEN='5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'

bot = telegram.Bot(TOKEN)

updates = bot.getUpdates()

chat_id = updates[-1].message.chat.id
text = updates[-1].message.text

bot.sendMessage(chat_id, text)