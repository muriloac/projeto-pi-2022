import mysql.connector


class Mysql:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.mysql = None
        self.cursor = None

    def connect(self):
        try:
            self.mysql = mysql.connector.connect(
                user=self.user, password=self.password, host=self.host, database=self.database)
            print(self.mysql)
            self.cursor = self.mysql.cursor()
        except Exception as err:
            print(err)
            raise

    def insert(self, values):
        query = (
            "INSERT INTO dados (valor, espacoMemoria, tempoExecucao) VALUES (%s, %s, %s)"
        )
        try:
            print('Inserindo Valores')
            self.cursor.execute(query, values)
            self.mysql.commit()
        except Exception as err:
            print(err)
            self.mysql.rollback()
            self.close()

    def truncate(self):
        query = "TRUNCATE dados"
        try:
            self.cursor.execute(query)
            self.mysql.commit()
            return True
        except Exception as err:
            print(err)
            self.mysql.rollback()
            self.close()
            return False

    def close(self):
        self.cursor.close()
        self.mysql.close()
