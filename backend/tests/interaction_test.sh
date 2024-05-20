#!/bin/bash
curl -X POST http://192.168.4.187:5000/post_interaction \
     -H "Content-Type: application/json" \
     -d '{
           "access_token": "ya29.a0AXooCgtEJyR7oCi2dnt3j9aWAPd6ZZCtVFyaIJ-xaHBPR6dEu2-dXqNo6TtfZCOfRkMAJOJxTOqKvUq64kHEVaWGkiIcn8eKgXh3ivErbSHKCQ2gcrWE2GC8AuYGOh9w1tsx06UYyrbB-HAxe6GV3oR5lBtZdzFnD8RqaCgYKAa8SARASFQHGX2MivRx-m-ugxzrBp4AIZYvEWQ0171",
           "refresh_token": "This is the content of my new blog post.",
           "type": "like",
           "s_key": "1715977348.034613"
         }'