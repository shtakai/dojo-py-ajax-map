from system.core.model import Model
import re
import bcrypt

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def get_all_notes(self):
        query = 'select * from notes order by updated_at desc'
        notes_result = self.db.query_db(query, {})

        print 'note_result', note_result
        return {
                'status': True,
                'result': note_result
                }
