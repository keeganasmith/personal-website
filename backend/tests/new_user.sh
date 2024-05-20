#!/bin/bash
curl -X POST http://192.168.4.187:5000/new_user \
     -H "Content-Type: application/json" \
     -d '{
           "access_token": "ya29.a0AXooCgtAj5Kcmr9UdKN9tWcghv7j7ROWYJYpqtpcY42MHYMd_oevgSAtcFfz-7JEzP43q8yFcWWxSWkPjo8lkbedR-l6wldNLP38w8HjJmMytDKIEkazUfMDeXRc5pJTdchHHbnOvtXz9m0FwKlINfXt9x2j8kWP_RfXaCgYKAdsSARASFQHGX2Mi9PagO92oH1YKrKgxv_GNsw0171",
           "refresh_token": "1//04F-cZmHKvCpGCgYIARAAGAQSNwF-L9Ir3fLRXVPsArb7C5gwcOT2KxRon-2ZbC5HlQ6v5ez9N8kFl_I2Pep-7i27F6RrpREO_KI"
         }'