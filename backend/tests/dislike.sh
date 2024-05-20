#!/bin/bash
curl -X POST http://192.168.4.187:5000/post_interaction \
     -H "Content-Type: application/json" \
     -d '{
           "access_token": "ya29.a0AXooCgvin0EzNvPgWEWxpSgXKaSlqhsGmIaPZC4tmbjs1Q4HqnSVyrkYrzUlawVMRvl3Bf8BsqzGaMuCazrmQ1pc-YZeE796pCTC0cNM_PZK2AM9y4v3ZLbrkuUPQFz5T2TrS10-xQyhVOJ2kWEBWndbOA8MtIe713xeaCgYKAUASARASFQHGX2MiQU_7NchiWog8qjPSbG72uw0171",
           "refresh_token": "This is the content of my new blog post.",
           "type": "dislike",
           "s_key": "1715977348.034613"
         }'