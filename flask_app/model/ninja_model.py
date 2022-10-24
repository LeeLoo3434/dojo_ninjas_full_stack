from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'mydb'


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self):
        return f'<Ninja: {self.first_name}>'

    # create a ninja
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_id

    # find all ninjas (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from ninjas;'
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for result in results:
            ninjas.append(Ninja(result))
        return ninjas

    # find one ninja by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from ninjas WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        ninja = Ninja(results[0])
        return ninja

    # update one ninja by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s,dojo_id = %(dojo_id)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one ninja by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True