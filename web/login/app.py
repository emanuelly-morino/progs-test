from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
import os
import jwt
import datetime
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")


CORS(app, supports_credentials=True)



# Configure Google OAuth
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'}
)

@app.route('/')
def index():
    user = session.get('user')
    if user:
        return f"""
            <h1>Welcome {user['name']}!</h1>
            <p>Email: {user['email']}</p>
            <img src="{user['picture']}" width="100">
            <br><a href="/logout">Logout</a>
        """
    return '<a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)



# new callback working with frontend using JWT
@app.route('/login/callback')
def authorize():
    token = google.authorize_access_token()
    user_info = google.get('https://openidconnect.googleapis.com/v1/userinfo').json()

    # Create our own JWT for the frontend
    payload = {
        "sub": user_info["email"],  # user ID or email
        "name": user_info["name"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # expires in 1 hour
        "iat": datetime.datetime.utcnow()
    }

    jwt_token = jwt.encode(payload, app.secret_key, algorithm="HS256")

    # Option A: send token as JSON (for API)
    response = ({"token": jwt_token, "user": user_info})
    return jsonify({"result":"ok", "details": response}), 200
    
    # return {"token": jwt_token, "user": user_info}

    # Option B: (if you serve HTML) redirect to front-end with token in query string:
    # return redirect(f"http://localhost:3000?token={jwt_token}")

      
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
