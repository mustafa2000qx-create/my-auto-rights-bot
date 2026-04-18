requirements.txt
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# التوكن الخاص بك
TOKEN = "8182600073:AAHtTADHbhXxNoTk0lJzVYf-3vDw4eTZ0ps"

bot = telebot.TeleBot(TOKEN, threaded=True, num_threads=50)

# إنشاء الأزرار الشفافة
markup = InlineKeyboardMarkup()
markup.row(
    InlineKeyboardButton("Gift for sale", url="https://t.me/zuzzz"),
    InlineKeyboardButton("Gift Chat", url="https://t.me/+_hfHwc8ZW-AzNTQ5")
)
markup.row(
    InlineKeyboardButton("Emoji Premium", url="https://t.me/ccc80")
)

# معالج للمنشورات في القنوات
@bot.channel_post_handler(content_types=['photo', 'video', 'text'])
def add_button(message):
    if message.reply_markup:
        return

    try:
        bot.edit_message_reply_markup(
            chat_id=message.chat.id,
            message_id=message.message_id,
            reply_markup=markup
        )
    except Exception as e:
        print(f"Error: {e}")

# معالج للرسائل الموجهة في الخاص (حسب طلبك الأول)
@bot.message_handler(content_types=['photo', 'video', 'text'])
def handle_private(message):
    try:
        # إعادة إرسال المحتوى مع الحقوق
        if message.text:
            bot.send_message(message.chat.id, message.text, reply_markup=markup)
        else:
            bot.copy_message(message.chat.id, message.chat.id, message.message_id, reply_markup=markup)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("البوت يعمل الآن بنجاح...")
    bot.infinity_polling(
        skip_pending=True, 
        timeout=10, 
        long_polling_timeout=5
    )
