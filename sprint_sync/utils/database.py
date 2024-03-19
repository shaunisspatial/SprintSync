import psycopg2
from configparser import ConfigParser


class Database():
    def __init__(self, config_file=None, section=None):
        self.config_file = '/Users/shaunpersonal/PycharmProjects/SprintSync/database.ini'
        self.section = 'postgresql'
        self.username = None
        self.password = None


    def _load_config(self):
        filename = self.config_file
        section = self.section
        parser = ConfigParser()
        parser.read(filename)

        # get section, default to postgresql
        config = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                config[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return config
    def connect(self,username = None, password = None):
        config = self._load_config()
        config['username'] = username
        config['password'] = password
        # todo: add username and password here
        try:
            # connecting to the PostgreSQL server
            with psycopg2.connect(**config) as conn:
                print('Connected to the PostgreSQL server.')
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def write(self, table, data: list[dict]):
        columns = data[0].keys()
        vals = [[i[x] for x in columns] for i in data]

        insert_statement = f'''INSERT INTO {table}({col_string}) VALUES ({vals_str})'''
        config = self._load_config()
        config['user'] = self.username
        config['password'] = self.password
        try:
            # connecting to the PostgreSQL server
            with psycopg2.connect(**config) as conn:
                print('Connected to the PostgreSQL server.')

                cur = conn.cursor()
                cur.executemany(insert_statement, table)

        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
