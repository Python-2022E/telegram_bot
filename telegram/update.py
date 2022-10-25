import json
from .message import Message
class Update:
    def __init__(self, update) -> None:
        self.update_id = update['update_id']
        self.message   = Message(update['message'])

    
    def fromDict(self)->dict:
        '''
        Convert User object to dictionary
        Returns:
            dict: dictionary of user data
        '''
        update_dict = {
            'update_id': self.update_id,
            'message': self.message.fromDict()
        }
        return update_dict

    #Override the __str__ method to print the user data
    def __str__(self):
        '''
        Print the user data
        '''
        return json.dumps(self.fromDict())