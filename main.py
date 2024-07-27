from fastapi import FastAPI
import pyrebase
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()  

# Set up app
app = FastAPI()

APIKEY = os.getenv("APIKEY")
AUTHDOMAIN = os.getenv("AUTHDOMAIN")
DATABASEURL = os.getenv("DATABASEURL")
PROJECTID = os.getenv("PROJECTID")
STORAGEBUCKET = os.getenv("STORAGEBUCKET")
MESSAGINGSENDERID = os.getenv("MESSAGINGSENDERID")
APPID = os.getenv("APPID")
MEASUREMENTID = os.getenv("MEASUREMENTID")

# Firebase configuration
firebaseConfig = {
  "apiKey": APIKEY,
  "authDomain": AUTHDOMAIN,
  "databaseURL": DATABASEURL,
  "projectId": PROJECTID,
  "storageBucket": STORAGEBUCKET,
  "messagingSenderId": MESSAGINGSENDERID,
  "appId": APPID,
  "measurementId": MEASUREMENTID
}

# Set up database
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


@app.get("/confirm_room")
async def confirm(card: str):
    # Get the allowed rooms
    room, numbers  = db.child("alloweRooms").get().pyres[0].item

    # Check if the card is allowed for room
    if card in numbers:
        return True

    return False
    
