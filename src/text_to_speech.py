import json
import base64
import requests
from google.oauth2 import service_account
import google.auth.transport.requests
import os

SERVICE_ACCOUNT_FILE = ""
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOUNDS_DIR = "/var/lib/asterisk/sounds/custom"

def text_to_speech(text):
    fp = os.path.join(SOUNDS_DIR, "output.mp3")

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    token = creds.token

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    body = {
        "input": {"text": text},
        "voice": {"languageCode": "pt-BR", "ssmlGender": "NEUTRAL"},
        "audioConfig": {"audioEncoding": "LINEAR16"},
    }


    response = requests.post(
        "https://texttospeech.googleapis.com/v1/text:synthesize",
        headers=headers,
        data=json.dumps(body),
    )


    audio_base64 = response.json()["audioContent"]
    audio_bytes = base64.b64decode(audio_base64)


    with open(fp, "wb") as f:
        f.write(audio_bytes)

    return fp
