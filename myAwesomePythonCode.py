import time
import random
import pyrebase
from datetime import datetime


config = {
    "apiKey": "AIzaSyDPm6nFp3x8zyWBgEzTcApGWRTHDBkxFrE",
    "authDomain": "aquaponics-system.firebaseapp.com",
"databaseURL": "https://aquaponics-system.firebaseio.com",
"projectId": "aquaponics-system",
"storageBucket": "aquaponics-system.appspot.com",
"messagingSenderId": "698142730339"
}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("hrghauri@hotmail.com", "jamesgreen")


db = firebase.database()


ph = round(random.uniform(4.0,7.5),1)

data = {
    "PH": str(ph),
    "Time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "Image":{
        "Image_Title": "DummyName",
        "Image_URL": "DummyURL"
    }
}

results = db.child("Readings").push(data, user['idToken'])


print(ph)
