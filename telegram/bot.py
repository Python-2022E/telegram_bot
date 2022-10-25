import requests

from telegram import chat
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
        url = f'{self.base_url}/sendMessage'
        data = {
          'chat_id':chat_id,
          'text':text
        }
        r = requests.post(url,data=data)

    def getUpdates(self):
        """
        Use this method to receive incoming updates using long polling

        Arguments:
            None
        Returns:
            Returns an Array of Update objects.
        """

        url = f'{self.base_url}/getUpdates'
        r = requests.get(url)
        data = r.json()
        result = data['result']

        updates = []

        if result:
            for update in result:
                updates.append(Update(update))

        return updates