import psycopg2
import os
from dotenv import load_dotenv

class Database:
    
    def create_table(self):
        with psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
                                      password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT")) as connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Users (
                                user_id varchar(50) PRIMARY KEY,
                                user_full_name varchar(50)
                            );
                    """)
                    print('бд создана успешно')
            except psycopg2.DatabaseError as e:
                print('что-то пошло нетак')
                  
    def insert_user(self, id, name):
        with psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
                                      password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT")) as connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                            INSERT INTO Users VALUES ('{}','{}');
                    """.format(id, name))
                    return 'Вы подписались на матчи Милана!'
            except psycopg2.DatabaseError as e:
                return 'ошибочка в работе с базой данных'
            except:
                return 'Вы уже подписаны'
            
    def delete_user(self, id):
        with psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
                              password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT")) as connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                            DELETE FROM Users WHERE user_id='{}';
                    """.format(id))
                    return 'Вы больше не подписаны!'
            except psycopg2.DatabaseError as e:
                return 'ошибка в работе с базой данных'

    def select_subscribers(self):
        with psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
                              password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT")) as connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                            SELECT * FROM Users;
                    """ )
                    return cursor.fetchall()
            except psycopg2.DatabaseError as e:
                return 'ошибка в работе с базой данных' 
