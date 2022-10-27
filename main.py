import telegram

bot = telegram.Bot(token='5297954693:AAGmz8OqL9EBPsfJ4S_R9AqgOtV67vkNtY4')
bosh = ''
while True:
    update = bot.getUpdates()

    chat_id = update.message.chat.id
    text = update.message.text
    current_id = update.message.message_id

    if current_id!=bosh:
        bot.sendMessage(chat_id, text)
        bosh = current_id









# last_id = -1
# while True:
#     update = bot.getUpdates()

#     current_id = update.message.message_id

#     if last_id != current_id:
#         chat_id = update.message.chat.id
#         text = update.message.text
#         bot.sendMessage(chat_id, text)
#         last_id = current_id


# update = bot.getUpdates()

# data = Update(update)

# message = data.message
# msg = Message(message)
# print(msg.text)



# chat_id = update['message']['chat']['id']
# text = update['message']['text']
# bot.sendMessage(chat_id, text)



# bot = telegram.Bot(TOKEN)

# updates = bot.getUpdates()

# chat_id = updates[-1].message.chat.id
# text = updates[-1].message.text

# bot.sendMessage(chat_id, text)

# class Person:
#     ism = 'sanjarbek'
    
#     def __init__(self, age, height):
#         self.age = age
#         self.height = height
    
#     def speak(self):
#         print('gapir')
    
#     def hi(self, name):
#         print('hello ' + name)
    
# samandar = Person(17, 180)
# print(samandar.hi('sanjarbek'))