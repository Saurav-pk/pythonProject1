from db import db
from models.models import Note
from flask_login import current_user


class NoteService:
    @staticmethod
    def add_note(note_data):
        if len(note_data) < 1:
            return False, 'Note is too short!'

        new_note = Note(data=note_data, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        return True, 'Note added!'


class NoteDeleteService:
    @staticmethod
    def delete_note(note_id):
        note = Note.query.get(note_id)
        if note and note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return True, 'Note deleted successfully!'
        return False, 'Failed to delete note'
