#!/usr/bin/python

# Necessary imports
import secrets
import os
import praw

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Authentication function
def authenticate():
    print("Authenticating...")
    session = praw.Reddit(user_agent = 'Foundation\'s Edge\'s first Robot!',
                    username = secrets.username,
                    password = secrets.password,
                    client_id = secrets.client_id,
                    client_secret = secrets.client_secret)
    print("Authenticated.")
    return session


# Scrapes quotes from the Goodreads website
def getQuote():
    # Use headless browser
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    
    # Use chrome to drive the scrape
    DRIVER_PATH = '/home/firstcitizen/Documents/Dev/GitHub/FoundationQuoteBot/'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    # Gets the Goodreads website
    driver.get('https://www.goodreads.com/work/quotes/1783981-foundation')

    # Iterates to get subsequent quotes from Goodreads
    quoteNumber = 1
    
    # Get element and print value
    elem = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div[10]/div[' + quoteNumber + ']/div[1]/div[1]/text()[1]')
    quote = elem.text

    # Return the scraped quote
    return quote


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


# Counts the number of times the script is run to know which quote to scrape
def getTimesRun(filename="timesRun.dat"):
        # Opens data file
        with open(filename, "a+") as f:
            f.seek(0)
            timesRun = int(f.read() or 0) + 1
            f.seek(0)
            f.truncate()
            f.write(str(timesRun))

        # Returns the total times the script has been run
        return timesRun


# Main check
if __name__ == "__main__":
    pass
