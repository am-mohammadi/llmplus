from keycrypt import get_secret, set_secret
from pandas.io import clipboard
from time import sleep



    
    
class API:
    def __init__(self):
        self.chats = []
        self.WIN_VAR_NAME = "llmState"
        self.timeout = 120
        
    def set_switch(self, state):
        set_secret(self.WIN_VAR_NAME, state)
        
    def get_switch(self):
        return get_secret(self.WIN_VAR_NAME)
    
    def send(self, text):
        if self.get_switch() != 'PA_ready':
            raise Exception("llmService is not running!")
            
        clipboard.copy(text)
        self.set_switch("python_waiting")
        print("Wating for PA response...")
        
        c = 0
        while self.get_switch() != 'PA_done':
            c += 1
            if c > self.timeout:
                raise Exception("PA timeout")
            sleep(1)
        
        print("PA done.")
        answer = clipboard.paste()
        self.chats += [{"human": text}, {"ai": answer}]
        self.set_switch('PA_ready')
        return answer
    
    def close(self):
        self.set_switch('close')
        
        
        
if __name__ == '__main__':
    llm = API()
    answer = llm.send('what is 3+3?')
    print(answer)