import os
from db_manager import DatabaseManager
from atproto import Client
                     
def main():
    # initialise database 
    db = DatabaseManager("database.db")

    text_to_post = db.get_random_post()

    if text_to_post and text_to_post != "No posts found in database":
        # from github secrets
        username = os.environ.get("BLUESKY_USERNAME")
        password = os.environ.get("BLUESKY_PASSWORD")

        if not username or not password:
            print("Error: username and/or password not found in environment secrets.")
            return
    
        #log in
        client = Client()
        client.login(username, password)
        client.send_post(text=text_to_post)
        print("Successfully posted to Bluesky!")
    else:
        print("No quote found")

if __name__ == "__main__":
    main()