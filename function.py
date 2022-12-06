import sqlite3


class DBManager:
    def __enter__(self):
        self.con = sqlite3.connect("currency_pair.db")
        self.cursor = self.con.cursor()
        return self

    def __exit__(self):
        self.cursor.close()
        self.con.close()

    def get_query(self, query):
        result_query = self.cursor.execute(query)
        result = result_query.fetchone()
        return result









