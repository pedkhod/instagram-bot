# import the moudle
from instaloader import instaloader
#crate an instancenof instaloder class
bot = instaloader.Instaloader()
#load a profile from instagram handel
profile= instaloader.Profile.from_username(bot.context ,'pkhoddami')
print(type(profile))
print(profile)
