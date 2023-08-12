import json
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = datetime.now()