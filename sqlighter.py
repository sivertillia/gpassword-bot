import sqlite3

class SQLighter:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()
    
    def get_chat(self):
        """Получаем всех активных подписчиков бота"""
        with self.conn:
            return self.cursor.execute('SELECT * FROM settings').fetchall()
    def user_settings(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT * FROM settings WHERE user_id=?', (user_id,)).fetchall()
            return result
    def add_user_settings(self, user_id, length=15, upper=True, lower=True, number=False, symbol=False):
        with self.conn:
            return self.cursor.execute('INSERT INTO settings (user_id, length, upper, lower, number, symbol) VALUES(?,?,?,?,?,?)', (user_id,length,upper,lower,number,symbol))
    def update_user_settings(self, user_id, col, row):
        with self.conn:
            print(user_id, col, row)
            return self.cursor.execute(f'UPDATE settings SET {col}=? WHERE user_id = ?', (row, user_id))   
    def user_exists(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT * FROM settings WHERE user_id=?', (user_id,)).fetchall()
            return bool(len(result))
    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()