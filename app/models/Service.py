from system.core.model import Model
import re
import bcrypt

class Service(Model):
    def __init__(self):
        super(Service, self).__init__()

    def get_all_services(self):
        query = 'select * from services order by updated_at desc'
        services_result = self.db.query_db(query, {})

        print 'service_result', service_result
        return {
                'status': True,
                'result': service_result
                }
