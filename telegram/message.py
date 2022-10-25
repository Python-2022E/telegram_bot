import json
from .user import User
from .chat import Chat
from .photosize import PhotoSize
class Message:
    def __init__(self, message: dict) -> None:
        self.message_id  = message['message_id']
        self.from_user   = User(message['from'])
        self.chat        = Chat(message['chat'])
        self.text        = message.get('text')
        self.photo       = []
    
        for files in message.get('photo', ''):
            self.photo.append(PhotoSize(files))

    def fromDict(self)->dict:
        '''
        Convert User object to dictionary
        Returns:
            dict: dictionary of user data
        '''
        msg_dict = {
            'message_id': self.message_id,
            'from_user': self.from_user.fromDict(),
            'chat': self.chat.fromDict(),
        }
        if self.text:
            msg_dict['text'] = self.text
        
        if self.photo:
            list_photos = []
            for i in self.photo:
                list_photos.append(i.fromDict())
            msg_dict['photo'] = list_photos

        return msg_dict

    #Override the __str__ method to print the user data
    def __str__(self):
        '''
        Print the user data
        '''
        return json.dumps(self.fromDict())