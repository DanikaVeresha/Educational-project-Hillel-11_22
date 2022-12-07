import sqlite3


class DataConn:

    def __enter__(self):
        """Открываем подключение с базой данных"""
        self.db = sqlite3.connect("currency_pair.db")
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрываем подключение"""
        self.db.close()


if __name__ == '__main__':
    db = 'currency_pair.db'







