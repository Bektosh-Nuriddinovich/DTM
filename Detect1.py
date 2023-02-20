import telebot
import cv2
import Check1

bot_token = '5554349522:AAEfZP0qsPCErmUfEJDvxIiea6wQL8YKTdc'
bot = telebot.TeleBot(bot_token, parse_mode='html')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Hello...{message.from_user.first_name}\nBot yaratuvchisi:Bektosh Nuriddinov')


@bot.message_handler(content_types=['photo'])
def photo(message):
    print("message.chat",message.from_user.first_name)
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    picture=cv2.imread("image.jpg")
    result=Check1.checker(picture)
    bot.send_message(message.from_user.id,result)
bot.polling()