from db_password import password
import mysql.connector


class DBClient:
    def __init__(self, host: str, user: str, database: str) -> None:
        self.__host: str = host
        self.__user: str = user
        self.__password: str = password
        self.__database: str = database

    def execute_without_output(self, query: str) -> None:
        try:
            with mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    connection.commit()
        except mysql.connector.Error as e:
            print(e)

    def execute_with_output(self, query: str) -> list[tuple]:
        try:
            with mysql.connector.connect(
                    host=self.__host,
                    user=self.__user,
                    password=self.__password,
                    database=self.__database
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
