import telebot

API_TOKEN = '1857097343:AAHxz60AZF-g8aOtxClomy24fC_qpDdzEgM'
shoping_bot = telebot.TeleBot(API_TOKEN)

commands = ["Add to list", "Get from list "]
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row(*commands)


shopping_list = []
current_operation = None

@shoping_bot.message_handler(commands=['start'])
def start(message):
    shoping_bot.reply_to(message, 'Welcome to shoping bot', reply_markup=keyboard)
    
    


@shoping_bot.message_handler(content_types=['text'])
def command(message):
    global current_operation
    global shopping_list
    if message.text == "Add to list":
        current_operation = 'Add'
    elif message.text == "Get from list":
        current_operation = 'Get'
        shoping_bot.reply_to(message, ", ".join(shopping_list))
    else:
        if current_operation == "Add":
            shopping_list.append(message.text)
            shoping_bot.reply_to(message, f"successfully added {message.text}")
        
shoping_bot.polling()