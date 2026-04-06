import os
import secrets

import requests
from flask import Flask, redirect, request, session, url_for, jsonify
from google_auth_oauthlib.flow import Flow

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", secrets.token_hex(32))

# Для локального HTTP-теста
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

CLIENT_SECRETS_FILE = "client_secret.json"

SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

REDIRECT_URI = "http://127.0.0.1:5000/callback"


def create_flow() -> Flow:
    return Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )


@app.route("/")
def index():
    user = session.get("user")
    if user:
        return f"""
        <h2>Вы вошли через Google</h2>
        <p><b>Имя:</b> {user.get("name")}</p>
        <p><b>Email:</b> {user.get("email")}</p>
        <img src="{user.get("picture", "")}" width="100" />
        <br><br>
        <a href="/logout">Выйти</a>
        """
    return '<a href="/login">Войти через Google</a>'


@app.route("/login")
def login():
    flow = create_flow()
    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    state = session.get("state")
    if not state:
        return "State отсутствует в сессии", 400

    flow = create_flow()
    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials
    session["google_token"] = credentials.token

    # Получаем профиль пользователя
    resp = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {credentials.token}"},
        timeout=10,
    )
    resp.raise_for_status()
    user_info = resp.json()

    session["user"] = {
        "id": user_info.get("id"),
        "email": user_info.get("email"),
        "name": user_info.get("name"),
        "picture": user_info.get("picture"),
    }

    return redirect(url_for("index"))


@app.route("/me")
def me():
    user = session.get("user")
    if not user:
        return jsonify({"error": "not authenticated"}), 401
    return jsonify(user)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)