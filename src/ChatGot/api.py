import requests
from json import loads
import authorization
import Models



class ChatGot:
    def __init__(self, authorization_key):
        self.authorization_key = authorization_key
    
        self.json_data = {
            'model': {
                'id': 'openai/gpt-4',
                'name': 'openai/gpt-4-1106-preview',
                # 'title': 'GPT-4',
                # 'icon': '/assets/imgs/icon/4.jpg',
                # 'extra': {
                #     'title': '128k',
                #     'bgColor': '#000',
                # },
                # 'placeholder': '',
                # 'description': "The latest GPT-4 model, which is currently the world's most outstanding large language model, provided by OpenAI, can offer you high-quality answers in various aspects. It can return up to 4,096 output tokens and has a maximum context window of 128,000 tokens.",
                'order': 0,
                'unused': False,
                'isActived': True,
                'value': 'GPT-4 128k',
                'isReplying': True,
            },
            'messages': [],
        }
    
        self.model = Models.GPT4()
    def send(self, prompt):
        self.json_data['messages'] += [{
            'role': 'user',
            'content': prompt,
        }]
        
        
        for key in self.model.json:
            self.json_data['model'][key] = self.model.json[key]
    
    
        response = requests.post('https://chatgot-ai.chatgot.io/sql', 
                                 headers=authorization.headers(self.authorization_key), 
                                 json=self.json_data)
        print(response)
        
        lines=response.text.split('\n\ndata:')
        answer = ''.join([loads(x)['choices'][0]['delta']['content'] for x in lines[1:-2]])
        
        self.json_data['messages'] += [{
            'role': 'assistant',
            'content': answer,
        }]
        
        return answer
    
if __name__ == '__main__':
    authorization_key = 'authorization_key'
    cg = ChatGot(authorization_key)
    
    cg.model = Models.Claude2()
    answer = cg.send('who is the manager of the real madrid?')
    
    # asnwer2  = cg.send('who the CEO?')
