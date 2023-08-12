import json
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Заметка {self.note_id}: {self.title} - {self.body} ({self.timestamp})"

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != int(note_id)]
    
    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == int(note_id):
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now()
                break
    
    def filter_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note.timestamp.date() == date]
        return filtered_notes

    def save_notes_to_file(self, filename):
        notes_data = []
        for note in self.notes:
            note_data = {
                'note_id': note.note_id,
                'title': note.title,
                'body': note.body,
                'timestamp': note.timestamp.isoformat()
            }
            notes_data.append(note_data)
        
        with open(filename, 'w') as file:
            file.write(json.dumps(notes_data, indent=4))

    def load_notes_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                notes_data = json.load(file)
        except FileNotFoundError:
            notes_data = []
        
        self.notes = []
        for note_data in notes_data:
            note = Note(
                note_data['note_id'],
                note_data['title'],
                note_data['body']
            )
            note.timestamp = datetime.fromisoformat(note_data['timestamp'])
            self.notes.append(note)

def main():
    note_manager = NoteManager()
    note_manager.load_notes_from_file('notes.json')

    while True:
        print('1. Добавить заметку')
        print('2. Удалить заметку')
        print('3. Редактировать заметку')
        print('4. Просмотреть заметки по дате')
        print('5. Сохранить изменения')
        print('6. Выйти из программы')
        choice = input('Введите номер операции: ')

        if choice == '1':
            note_id = input('Введите идентификатор заметки: ')
            title = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')
            note = Note(note_id, title, body)
            note_manager.add_note(note)
        elif choice == '2':
            note_id = input('Введите идентификатор заметки для удаления: ')
            note_manager.delete_note(note_id)
        elif choice == '3':
            note_id = input('Введите идентификатор заметки для редактирования: ')
            new_title = input('Введите новый заголовок заметки: ')
            new_body = input('Введите новый текст заметки: ')
            note_manager.edit_note(note_id, new_title, new_body)
        elif choice == '4':
            date_str = input('Введите дату для фильтрации заметок (в формате ГГГГ-ММ-ДД): ')
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            filtered_notes = note_manager.filter_notes_by_date(date)
            for note in filtered_notes:
                print(note)
        elif choice == '5':
            note_manager.save_notes_to_file('notes.json')
            print('Изменения сохранены.')
        elif choice == '6':
            break
        else:
            print('Некорректный выбор. Попробуйте еще раз.')

if __name__ == '__main__':
    main()