import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import time

# Function to authenticate and get a YouTube API client
def authenticate(account_credentials):
    # Define the scopes for the YouTube Data API
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    
    # Path to your account's credentials file
    client_secrets_file = account_credentials
    
    # Start OAuth 2.0 authentication flow
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return youtube

# Function to post a comment on a specific live video
def post_comment(youtube, video_id, comment_text):
    try:
        # Make the request to post a comment on the live stream
        request = youtube.commentThreads().insert(
            part="snippet",
            body={
                "snippet": {
                    "videoId": video_id,
                    "topLevelComment": {
                        "snippet": {
                            "textOriginal": comment_text
                        }
                    }
                }
            }
        )
        response = request.execute()
        print(f"Comment posted: {response['snippet']['topLevelComment']['snippet']['textOriginal']}")
    except Exception as e:
        print(f"Error posting comment: {e}")

# Main function to run the script
def main():
    # List of account credential files (OAuth 2.0 credentials for different accounts)
    accounts = ["account1_credentials.json", "account2_credentials.json"]  # Add your credential file names here
    video_id = "https://www.youtube.com/live/D6YTrHai1rw?si=v9Z2Pl7tVBN823ZI"  # Replace with your live video ID
    comment = "HACKER HACKER HACKER HEHEHEHE"

    # Loop through each account and post a comment
    for account in accounts:
        print(f"Authenticating account: {account}")
        youtube = authenticate(account)  # Authenticate the account
        post_comment(youtube, video_id, comment)  # Post the comment
        time.sleep(5)  # Adding a small delay between actions to avoid flags

# Run the main function
if __name__ == "__main__":
    main()
