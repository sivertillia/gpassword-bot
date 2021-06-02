import sqlite3

class SQLighter:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()
    
    def get_chat(self):
        """Получаем всех активных подписчиков бота"""
        with self.conn:
            return self.cursor.execute('SELECT * FROM settings', (status)).fetchall()

    def user_settings(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT * FROM settings WHERE user_id=?', (user_id,)).fetchall()
            return bool(len(result))
    def group_exists(self):
        with self.conn:
            result = self.cursor.execute('SELECT * FROM groups WHERE chat_id=?', (chat_id,)).fetchall()
            return bool(len(result))

    def get_group_status(self):
        with self.conn:
            result = self.cursor.execute('SELECT status FROM groups WHERE chat_id=?', (chat_id,)).fetchall()
            for i in result:
                for j in i:
                    result = j
            return bool(result)

    def add_users(self):
        with self.conn:
            return self.cursor.execute('INSERT INTO users (user_id, chat_id, status, fullname) VALUES(?,?,?,?)', (user_id,chat_id,status,fullname))

    def update_status_group(self):
        with self.conn:
            return self.cursor.execute('UPDATE groups SET status=? WHERE chat_id = ?', (status, chat_id))
    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()