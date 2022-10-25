import json
class Chat:
    def __init__(self, chat_data: dict) -> None:
        self.id    = chat_data['id']
        self.type  = chat_data['type']
        self.title = chat_data.get('title')
        self.username = chat_data.get('username')
        self.first_name = chat_data.get('first_name')
        self.last_name = chat_data.get('last_name')
        self.photo = chat_data.get('photo')
        self.bio = chat_data.get('bio')

    def fromDict(self) -> dict:
        chat_dict = {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'photo': self.photo,
            'bio': self.bio,
        }
        newdict = {}
        for key, value in chat_dict.items():
            if value:
                newdict[key] = value

        return newdict

    def __str__(self) -> str:
        return json.dumps(self.fromDict())