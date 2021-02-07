import psycopg2
import os
from dotenv import load_dotenv

class Database:
    
    def create_table(self):
        connection = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
                                      password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
        cursor = connection.cursor()
        try:
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Users (
                        user_id varchar(50) PRIMARY KEY,
                        user_full_name varchar(50)
                    );
            """)
            print('бд создана успешно')
        except:
            print('бд уже создана')
        finally:
            connection.commit()
            cursor.close()
            connection.close()
        

    def insert_user(self, id, name):
        connection = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
                                      password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
        cursor = connection.cursor()
        try:
            cursor.execute("""
                    INSERT INTO Users VALUES ('{}','{}');
            """.format(id, name))
            print('пользователь добавлен успешно')
        except:
            print('такой пользователь уже существует в базе данных')
        finally:
            connection.commit()
            cursor.close()
            connection.close()
