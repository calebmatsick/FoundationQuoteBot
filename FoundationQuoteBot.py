#!/usr/bin/python

# Necessary imports
import os
import praw
import secrets
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


# Authenticates bot to Reddit
def authenticate():
    print("Authenticating...")

    # Creates reddit using Praw and secrets
    reddit = praw.Reddit(user_agent = 'Foundation\'s Edge\'s first Robot!',
                    username = secrets.username,
                    password = secrets.password,
                    client_id = secrets.client_id,
                    client_secret = secrets.client_secret)

    print("Authenticated.")
    return reddit


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
    reddit = authenticate()

    # Gets the quote to post
    quote = getQuote()

    # Gets the number of times the script has been run
    timesRun = getTimesRun()

    # Posts the quote to the subreddit
    postQuote(reddit, quote, timesRun)


# Finds comments with "mule" in it and then replies to them
def postQuote(reddit, quote, timesRun):
    # Selects /r/FoundationsEdge as the subreddit to post to
    sub = reddit.subreddit('FoundationsEdge')

    # Variables needed to make the post
    title = 'QOTD #' + timesRun
    selftext = quote

    # Makes the post
    reddit.subreddit(sub).submit(title, selftext)


# Main check
if __name__ == "__main__":
    pass
