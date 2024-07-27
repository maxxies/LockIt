from fastapi import FastAPI
import pyrebase
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()  

# Set up app
app = FastAPI()

# Retrieve Firebase configuration from environment variables
firebase_config = {
    "apiKey": os.getenv("APIKEY"),
    "authDomain": os.getenv("AUTHDOMAIN"),
    "databaseURL": os.getenv("DATABASEURL"),
    "projectId": os.getenv("PROJECTID"),
    "storageBucket": os.getenv("STORAGEBUCKET"),
    "messagingSenderId": os.getenv("MESSAGINGSENDERID"),
    "appId": os.getenv("APPID"),
    "measurementId": os.getenv("MEASUREMENTID")
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

@app.get("/confirm_room")
async def confirm_room(card: str):
    # Retrieve the allowed rooms
    allowed_rooms = db.child("alloweRooms").get().val()

    # Check if the card is allowed for any room
    for room, numbers in allowed_rooms.items():
        if card in numbers:
            return {"room": room, "access": True}

    return {"room": None, "access": False}
