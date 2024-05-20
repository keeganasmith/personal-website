from flask import Flask, jsonify, request
from Database import Database_Client
from flask_cors import CORS
from google_client.GoogleClient import GoogleClient
app = Flask(__name__)
CORS(app)

def valid_token(access_token, refresh_token):
    google = GoogleClient(access_token=access_token, refresh_token=refresh_token)
    try:
        google.get_email()
        return True
    except:
        return False
    
def admin(access_token, refresh_token):
    google = GoogleClient(access_token=access_token, refresh_token=refresh_token)
    try:
        email= google.get_email()
        return email == "keeganasmith2003@gmail.com"
    except:
        return False
    
@app.route('/get_posts')
def get_posts():
    access_token = request.args["access_token"]
    refresh_token = request.args.get("refresh_token", None)
    if(valid_token(access_token, refresh_token)):
        client = Database_Client()
        my_posts= client.get_posts()
        return jsonify(my_posts)
    else:
        return jsonify({"status": "error", "message": "Token invalid"}), 401

@app.route('/new_post', methods = ['POST'])
def new_post():
    data = request.get_json()
    access_token = data['access_token']
    refresh_token = data.get('refresh_token', None)
    if(not admin(access_token, refresh_token)):
        return jsonify({"status": "error", "message": "Token invalid"}), 401
    client = Database_Client()
    response = client.new_post(data)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return jsonify({"status": "success", "message": "Post created successfully!"}), 200
    else:
        return jsonify({"status": "error", "message": "Failed to create post", "details": response}), 500
    
@app.route('/delete_post', methods= ['POST'])
def del_post():
    data = request.get_json()
    access_token = data['access_token']
    refresh_token = data.get('refresh_token', None)
    if(not admin(access_token, refresh_token)):
        return jsonify({"status": "error", "message": "Token invalid"}), 401
    client = Database_Client()
    response = client.delete_item(p_key=data["p_key"], s_key=data["s_key"])
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return jsonify({"status": "success", "message": "Post deleted successfully!"}), 200
    else:
        return jsonify({"status": "error", "message": "Failed to delete post", "details": response}), 500

@app.route('/get_email', methods= ['GET'])
def get_email():
    access_token = request.args["access_token"]
    refresh_token = request.args.get("refresh_token", None)
    google = GoogleClient(access_token=access_token, refresh_token=refresh_token)
    try:
        my_email = google.get_email()
        return jsonify({"status": "success", "message": my_email}), 200
    except:
        return jsonify({"status": "error", "message": "Token invalid"}), 401

@app.route('/new_user', methods=['POST'])
def new_user():
    data = request.get_json()
    google = GoogleClient(access_token=data["access_token"], refresh_token=data.get("refresh_token", None))
    try:
        user_info = google.get_user_info()
        client = Database_Client()
        client.new_user(user_info)
        return jsonify({"status": "success", "message": "user created"}), 200
    except:
        return jsonify({"status": "error", "message": "Token invalid"}), 401
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")