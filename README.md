# llmplus
Usage
```python
from llmplus.ChatGot.api import API, Models
authorization_key = 'your authorization key from website headers'
api = API(authorization_key)
    
api.model = Models.GPT4()
answer = api.send('who is the manager of the real madrid?')

asnwer2  = api.send('who is the CEO?')
```

Models
```python
Models.GPT4
Models.GPT3
Models.Claude2
```

Acsess to the chat history
```python
API.json_data['messages']
```
