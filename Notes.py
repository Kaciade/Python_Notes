import json
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = datetime.now()

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
    
    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now()
                break
    
    def filter_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note.timestamp.date() == date.date()]
        return filtered_notes

    def save_notes_to_file(self, filename):
        notes_data = []
        for note in self.notes:
            note_data = {
                'note_id': note.note_id,
                'title': note.title,
                'body': note.body,
                'timestamp': note.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
            notes_data.append(note_data)
        
        with open(filename, 'w') as file:
            json.dump(notes_data, file, indent=4)

