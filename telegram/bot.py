import requests
from .user import User
from .update import Update

class Bot:
    def __init__(self, token:str)->None:
        self.base_url = f'https://api.telegram.org/bot{token}'

    def getMe(self)-> User:
        """A simple method for testing your bot's auth token.
         Returns:
          A telegram.User instance representing that bot if the
          credentials are valid, None otherwise.
        """
        url = f'{self.base_url}/getMe'
        r = requests.get(url)
        user_data = r.json()['result']
        
        return User(user_data)

    def sendMessage(self,chat_id,text):
        """Use this method to send text messages.
        Args:
          chat_id:
            Unique identifier for the message recipient — telegram.User or
            telegram.GroupChat id.
          text:
            Text of the message to be sent.
        Returns:
          A telegram.Message instance representing the message posted.
        """