from client.db_client import DBClient


class AbstractRepository:
    client: DBClient = DBClient("localhost", "root", "lw2")
