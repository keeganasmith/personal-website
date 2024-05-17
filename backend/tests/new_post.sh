#!/bin/bash
curl -X POST http://192.168.4.187:5000/new_post \
     -H "Content-Type: application/json" \
     -d '{
           "title": "My New Blog Post",
           "msg": "This is the content of my new blog post."
         }'