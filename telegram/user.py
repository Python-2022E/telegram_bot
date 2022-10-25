import json


class User:
    def __init__(self,user):
        self.id = user.get('id')
        self.first_name=user.get('first_name')
        self.last_name=user.get('last_name')
        self.username = user.get('username')
        self.is_bot = user.get('is_bot')
        self.language_code = user.get('language_code')
        self.is_premium = user.get('is_premium')
        self.added_to_attachment_menu = user.get('added_to_attachment_menu')
        self.can_join_groups = user.get('can_join_groups')
        self.can_read_all_group_messages = user.get('can_read_all_group_messages')
        self.supports_inline_queries = user.get('supports_inline_queries')


    def fromDict(self)->dict:
        '''
        Convert User object to dictionary
        Returns:
            dict: dictionary of user data
        '''
        data = {
            'id':self.id,
            'last_name':self.last_name,
            'username':self.username,
            'is_bot':self.is_bot,
            "language_code":self.language_code,
            'is_premium':self.is_premium,
            'added_to_attachment_menu':self.added_to_attachment_menu,
            'can_join_groups':self.can_join_groups,
            'can_read_all_group_messages':self.can_read_all_group_messages,
            'supports_inline_queries':self.supports_inline_queries,
        }
        NewDict = {}
        for k,q in data.items():
            if q != None:
                NewDict[k] = q

        return NewDict

    #Override the __str__ method to print the user data
    def __str__(self):
        '''
        Print the user data
        '''
        return json.dumps(self.fromDict())