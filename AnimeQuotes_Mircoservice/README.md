# Anime Quote Microservice

This microservice provides users to request a random anime quote and optionally provide the specific anime.

NO API KEY IS NEEDED

# Installation
**After cloning:**
pip install -r requirements.txt 

.\.venv\Scripts\Activate to use on powershell

This will install all the dependecies you need to run it.

# Get route
You need to type after /quotes/'animename'
If just quotes it will return a random quote from the full pool

# Sample Request:
http://127.0.0.1:5003/api/quotes/yu-gi-oh

# Response:
```json
{
  "summary_length": "medium",
  "additional_info": "yes",
  "content": [
    { 
      "text": "Frieren: Beyond Journey's End is a Japanese manga series written by Kanehito Yamada and illustrated by Tsukasa Abe. It follows Frieren, an elven mage on a journey to reunite with her former comrade Himmel."
    },
    // You can add more text blocks here if needed
    {
      "text": "The story takes place over a long time, as Frieren's elven lifespan makes years seem ephemeral."
    }
  ]
}
```