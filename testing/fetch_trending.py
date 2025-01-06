import time
import random
import json
import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import uuid

# MongoDB Atlas setup
client = pymongo.MongoClient("mongodb+srv://Random123:Random123@selenium.mflpa.mongodb.net/?retryWrites=true&w=majority&appName=Selenium")
db = client["twitter_trends"]
collection = db["trends"]

# Function to fetch trending topics from the homepage
def fetch_trending_topics():
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode for faster execution
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize the WebDriver
    service = Service('path/to/chromedriver')  # Update with your path to chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Navigate to Twitter homepage
    driver.get("https://twitter.com/")
    time.sleep(5)  # Wait for the page to load

    # Fetch trending topics
    trends = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]')
    trending_topics = [trend.text for trend in trends[:5]]

    # Close the driver
    driver.quit()

    # Create a unique ID and timestamp
    unique_id = str(uuid.uuid4())
    timestamp = datetime.now()

    # Store in MongoDB Atlas
    record = {
        "_id": unique_id,
        "trend1": trending_topics[0] if len(trending_topics) > 0 else None,
        "trend2": trending_topics[1] if len(trending_topics) > 1 else None,
        "trend3": trending_topics[2] if len(trending_topics) > 2 else None,
        "trend4": trending_topics[3] if len(trending_topics) > 3 else None,
        "trend5": trending_topics[4] if len(trending_topics) > 4 else None,
        "timestamp": timestamp,
        "ip_address": "N/A"  # No proxy used in this case
    }
    collection.insert_one(record)

    return unique_id, trending_topics, timestamp

if __name__ == "__main__":
    fetch_trending_topics()