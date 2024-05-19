from flask import Flask, jsonify, request
from Database import Database_Client
from flask_cors import CORS
from google_client.GoogleClient import GoogleClient
app = Flask(__name__)
CORS(app)
@app.route('/get_posts')
def get_posts():
    client = Database_Client()
    my_posts= client.get_posts()
    return jsonify(my_posts)
@app.route('/new_post', methods = ['POST'])
def new_post():
    client = Database_Client()
    data = request.get_json()
    response = client.new_post(data)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return jsonify({"status": "success", "message": "Post created successfully!"}), 200
    else:
        return jsonify({"status": "error", "message": "Failed to create post", "details": response}), 500
    
@app.route('/delete_post', methods= ['POST'])
def del_post():
    client = Database_Client()
    data = request.get_json()
    response = client.delete_item(p_key=data["p_key"], s_key=data["s_key"])
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return jsonify({"status": "success", "message": "Post deleted successfully!"}), 200
    else:
        return jsonify({"status": "error", "message": "Failed to delete post", "details": response}), 500

@app.route('/get_email', methods= ['GET'])
def get_email():
    print(request.args)
    access_token = request.args["access_token"]
    refresh_token = request.args["refresh_token"]
    google = GoogleClient(access_token=access_token, refresh_token=refresh_token)
    try:
        my_email = google.get_email()
        return jsonify({"status": "success", "message": my_email}), 200
    except:
        return jsonify({"status": "error", "message": "Token invalid"}), 401
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")