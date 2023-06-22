import instaloader 
import re

bot = instaloader.Instaloader() 
profile1 = instaloader.Profile.from_username(bot.context, 'cristiano')
profile2 = instaloader.Profile.from_username(bot.context, 'fabriziorom')
for post in profile1.get_posts():
    match = re.search(r'<Post\s+(\S+)>', str(post))
    if match:
        post_id = match.group(1)
        print(f'fabrizio\'s new post: https://www.instagram.com/p/{post_id}/?hl=en')
    else:
        print("error")
    break