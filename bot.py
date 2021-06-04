import telebot
from gtts import gTTS
bot = telebot.TeleBot("1831903452:AAENblJDi4iDrOKUR2VbLdoDPqGiaDbLHJQ", parse_mode="HTML")
@bot.message_handler(content_types=['text'])
def gettext(message):
    if 'Аниме' in message.text or 'аниме' in message.text or 'хентай' in message.text or 'Хентай' in message.text:
        bot.reply_to(message, "No anime")
    else:
        aud = gTTS(message.text, lang='ru')
        aud.save('audio.mp3')
        bot.send_audio(message.chat.id, 'audio.mp3', "От @PyTesterAPIBot")
bot.polling(none_stop = True, interval = 1)
