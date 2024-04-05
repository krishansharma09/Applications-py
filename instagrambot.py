from instabot import Bot
bot=Bot()
bot.login(username='hello4565925',password='denusharma5656')
bot.follow('xx.__kanha__.xx__')
bot.upload_photo("path",caption="i love python")
bot.unfollow('xx.__kanha__.xx__')
bot.send_message("i love python with [username]")
followers=bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))
bot.logout()