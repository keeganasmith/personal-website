
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
        posts = sorted(posts, key=lambda x: x["s_key"])
        posts.reverse()
        return posts;
    
    def delete_item(self, p_key, s_key):
        try:
            response = self.table.delete_item(
                Key={
                    'p_key': p_key,
                    's_key': s_key
                }
            )
            return response
        except Exception as e:
            print(f"Error deleting item: {e}")
            return None
#my_client = Database_Client()
# my_client.get_posts()
# print(len(my_client.get_posts()))
# my_client.delete_item(my_client.get_posts()[0]['p_key'], my_client.get_posts()[0]['s_key'])
# print(len(my_client.get_posts()))