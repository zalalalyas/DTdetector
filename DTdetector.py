import telebot
import datetime

# Replace 'YOUR_TOKEN' with your actual bot token
bot = telebot.TeleBot('6929570993:AAHGy5i2_BEMyqh5SsdR1CIb8kARjHtn1os')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "hello")

# Dictionary to store the last sent photo time for each user
user_last_photo_time = {}

# Define a handler for incoming photo messages
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the sender is an admin, creator, or owner
    chat_member = bot.get_chat_member(chat_id, user_id)
    status = chat_member.status
    if status in ['administrator', 'creator', 'owner']:
        return

    # Check if the user has sent a photo before
    if user_id in user_last_photo_time:
        # Get the last sent photo time
        last_photo_time = user_last_photo_time[user_id]

        # Get the current time
        current_time = datetime.datetime.now()

        # Calculate the time difference
        time_difference = current_time - last_photo_time

        # If less than 24 hours have passed, delete the extra photo
        if time_difference < datetime.timedelta(days=1):
            bot.delete_message(chat_id, message.message_id)
            bot.send_message(chat_id, f"@{message.from_user.username}, ببورە ناتوانی لە وێنەیێک زیادتر بنێری❗️")
          # bot.reply_to(chat_id, "ببورە ناتوانی لە وێنەیێک زیادتر بنێری❗️")
            return

    # Update the last sent photo time for the user
    user_last_photo_time[user_id] = datetime.datetime.now()

# Start the bot
bot.polling()
