import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Step 1: Authentication
def authenticate():
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    client_secrets_file = "account1_credentials.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_local_server(port=0)

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return youtube

# Step 2: Post a comment on a live stream
def post_comment(youtube, video_id, comment_text):
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

# Example of posting
youtube = authenticate()
post_comment(youtube, "your_live_video_id", "This is a great stream! :)")
