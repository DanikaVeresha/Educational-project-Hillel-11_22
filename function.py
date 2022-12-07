import sqlite3


# class DBManager:
#     def __enter__(self):
#         self.con = sqlite3.connect("currency_pair.db")
#         self.cursor = self.con.cursor()
#         return self
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         self.cursor.close()
#         self.con.close()
#
#     def get_query(self, query):
#         result_query = self.cursor.execute(query)
#         result = result_query.fetchone()
#         return result


class DataConn:

    def __enter__(self):
        """Открываем подключение с базой данных"""
        self.con = sqlite3.connect("currency_pair.db")
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрываем подключение"""
        self.con.close()


if __name__ == '__main__':
    db = 'currency_pair.db'






