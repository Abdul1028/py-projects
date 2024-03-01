import firebase_admin
from firebase_admin import credentials,auth
import requests

cred = credentials.Certificate("wit-reality-firebase-adminsdk-fipta-3a5614c527.json")
firebase_admin.initialize_app(cred)

# try:
#     user = auth.create_user(email="rasoolas2003@gmail.com", password="123456")
#     print(user)
# except Exception as e:
#     print(e)

firebase_api_key = "AIzaSyDqFTgBTs10Qx3Km2eVWASTum-1Eoy64xo"

def signin_with_password(email, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
    api_key = "AIzaSyDqFTgBTs10Qx3Km2eVWASTum-1Eoy64xo"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    params = {"key": api_key}

    try:
        response = requests.post(url, params=params, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        data = response.json()
        if "idToken" in data:
            # Authentication successful, return the secure token
            return data["idToken"]
        else:
            # Authentication failed, handle error
            return None
    except requests.exceptions.RequestException as e:
        # Handle request errors
        print("Error:", e)
        return None
#
#
# # Example usage
email = "rasoolas2003@gmail.com"
password = "123456"
token = signin_with_password(email, password)
if token:
    print("successfully signed in")
    print("Secure Token:", token)
else:
    print("Authentication failed.")

def get_google_profile_picture(id_token):
    url = "https://www.googleapis.com/oauth2/v3/tokeninfo"
    params = {"id_token": id_token}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        data = response.json()
        if "picture" in data:
            # User's profile picture URL
            return data["picture"]
        else:
            # Profile picture not found
            return None
    except requests.exceptions.RequestException as e:
        # Handle request errors
        print("Error:", e)
        return None

profile_picture_url = get_google_profile_picture(token)
if profile_picture_url:
    print("Profile Picture URL:", profile_picture_url)
else:
    print("Profile picture not found.")


