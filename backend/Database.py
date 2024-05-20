
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv
from boto3.dynamodb.conditions import Key, Attr
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
    
    def new_user(self, user_info):
        duplicate_users = self.table.query(KeyConditionExpression=Key("p_key").eq("user"), FilterExpression=Attr("email").eq(user_info["email"]))["Items"]
        if(len(duplicate_users) > 0):
            return;
        item = {
            'name': user_info['name'],
            'email': user_info['email'],
            'liked_posts': [],
            'disliked_posts': [],
            'p_key': 'user',
            's_key': str(datetime.now().timestamp())
        }
        self.table.put_item(Item=item)
        
    def scan_db(self):
        print(self.table.scan())
    
    def get_posts(self):
        posts = self.table.query(KeyConditionExpression=Key("p_key").eq("post"))["Items"]
        for post in posts:
            post["likes"] = int(post["likes"])
            post["dislikes"] = int(post["dislikes"])
        posts = sorted(posts, key=lambda x: x["s_key"])
        posts.reverse()
        return posts;
    
    def like_post(self, user_email, post_key):
        user = self.table.query(KeyConditionExpression=Key("p_key").eq("user"), FilterExpression=Attr("email").eq(user_email))["Items"][0]
        post = self.table.query(KeyConditionExpression=Key("p_key").eq("post") & Key("s_key").eq(post_key))["Items"][0]
        liked_posts = user["liked_posts"]
        disliked_posts = user["disliked_posts"]
        
        if post_key in liked_posts:
            return False
        new_post_dislikes = post["dislikes"]
        if post_key in disliked_posts:
            disliked_posts.remove(post_key)
            new_post_dislikes = post["dislikes"] - 1
        
        liked_posts.append(post_key)
        self.table.update_item(
            Key={
                's_key': user["s_key"],
                'p_key': "user"
            },
            UpdateExpression="SET liked_posts = :newLiked, SET disliked_posts = :new_post_dislikes",
            ExpressionAttributeValues={
                ':newLiked': liked_posts,
                ':new_post_dislikes': new_post_dislikes
            },
            ReturnValues="UPDATED_NEW"
        )
        self.table.update_item(
            Key = {
                's_key': post_key,
                'p_key': "post"
            },
            UpdateExpression="SET likes = :new_likes, SET dislikes = :new_dislikes",
            ExpressionAttributeValues={
                ':new_likes': post["likes"] + 1,
                ':new_dislikes': new_post_dislikes  
            },
            ReturnValues = "UPDATE_NEW"
        )
    #def dislike_post(self, user_email, post_key):
        
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