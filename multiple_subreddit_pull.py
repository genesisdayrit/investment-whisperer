import os
import praw
from dotenv import load_dotenv
from datetime import datetime
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables
load_dotenv()

# List of subreddits to fetch posts from
subreddits_list = [
    'stocks',
    'investing',
    'wallstreetbets',
    'SecurityAnalysis',
    'StockMarket',
    'RobinHood',
    'pennystocks',
    'dividends'
]
num_posts = 15  # You can adjust the number of posts per subreddit if needed

# Gmail configuration
GMAIL_ACCOUNT = os.getenv("GMAIL_ACCOUNT")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USERNAME")
)

email_body = ""

for subreddit_name in subreddits_list:
    hot_posts = list(reddit.subreddit(subreddit_name).hot(limit=100))
    
    # Randomly select posts from hot posts
    selected_posts = random.sample(hot_posts, num_posts)
    
    email_body += f"Subreddit: r/{subreddit_name}\n"
    email_body += "-" * 30 + "\n"  # separator
    
    for post in selected_posts:
        email_body += f"Title: {post.title}\n"
        email_body += f"URL: https://www.reddit.com{post.permalink}\n"
        post_time = datetime.utcfromtimestamp(post.created_utc)
        email_body += f"Posted on: {post_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    email_body += "\n"  # extra space between subreddits

msg = MIMEMultipart()
msg['From'] = GMAIL_ACCOUNT
msg['To'] = GMAIL_ACCOUNT
msg['Subject'] = f"Random Reddit posts from finance and stock subreddits"
msg.attach(MIMEText(email_body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(GMAIL_ACCOUNT, GMAIL_PASSWORD)
server.sendmail(GMAIL_ACCOUNT, GMAIL_ACCOUNT, msg.as_string())
server.quit()

print("Email sent successfully")
