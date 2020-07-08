# Necessary imports
import config
import os
import praw
import selenium


# Authentication function
def authenticate():
    print("Authenticating...")
    session = praw.Reddit(user_agent = 'Foundation\'s Edge\'s first Robot!',
                    username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret)
    print("Authenticated.")
    return session


# Driver for the script
def main():
    # Authenticates bot
    session = authenticate()

    # Gets comments
    replies = replied_comments()

    # Replues to all appropriate comments
    while True:
        reply(session, replies)


# Finds comments with "mule" in it and then replies to them
def reply(session, replies):
    # Searches /r/FoundationsEdge for comments to reply to
    sub = session.subreddit('FoundationsEdge')
    comments = sub.stream.comments()
    
    # Looks through comments for the name "mule"
    for comment in comments:
        text = comment.body

        # If it contains mule, replies to comment
        if "mule" in text.lower() and comment.id not in replies:
            print ("User Indoctrinated")
            comment.reply("Hail the First Citizen!")
            replies.append(comment.id)
            with open('C:/Users/caleb/Documents/Computer Science/PythonProjects/replies.txt', 'a') as f:
                f.write (comment.id + "\n")


# Opens replies that are in a file and formats them
def replied_comments():
    with open('C:/Users/caleb/Documents/Computer Science/PythonProjects/replies.txt') as f:
        replies = f.read().splitlines()
    return replies


# Main check
if __name__ == "__main__":
    pass

username = ""
password = ""
client_id = ""
client_secret = ""


/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div[8]/div/div[1]/div[1]/text()[1]

/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div[10]/div[1]/div[1]/div[1]/text()[1]
/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div[10]/div[2]/div[1]/div[1]/text()[1]
