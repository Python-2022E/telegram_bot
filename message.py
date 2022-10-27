class Message:
    def __init__(self, message: dict) -> None:
        self.message_id  = message['message_id']
        self.chat        = message['chat']
        self.text        = message.get('text')