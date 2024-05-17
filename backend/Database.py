
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
class Database_Client:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
        if(os.environ["PROD"] == "False"):
            self.table = self.dynamodb.Table('Website')
        else:
            self.table = self.dynamodb.Table('Blog')

    def new_post(self, data):
        item = {
            'title': data["title"],
            'msg': data["msg"],
            'likes': 0,
            'dislikes': 0,
            'p_key': "post",
            's_key': str(datetime.now().timestamp())
        }
        response = self.table.put_item(Item=item)
        return response
    
    def scan_db(self):
        print(self.table.scan())
    
    def get_posts(self):
        posts = self.table.scan()["Items"]
        for post in posts:
            post["likes"] = int(post["likes"])
            post["dislikes"] = int(post["dislikes"])
        return posts;
# my_client = Database_Client()
# my_client.get_posts()
# print(my_client.get_posts())