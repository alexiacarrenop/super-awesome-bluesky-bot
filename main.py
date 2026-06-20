import schedule
import time
import db_manager
from config import client

                     
def job():
    quote = db_manager.get_random_quote()
    if quote:
        client.send_post(text=quote)
        print("Successfully posted to Bluesky!")
    else:
        print("No quote found")

if __name__ == "__main__":
    job()