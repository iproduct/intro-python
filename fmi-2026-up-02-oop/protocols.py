from typing import Protocol

class Connection(Protocol):
    def connect(self) -> None:
        ...  # Ellipsis indicates an abstract method

    def disconnect(self) -> None:
        ...

class Database:
    def connect(self) -> None:
        print("Connected to DB")

    def disconnect(self) -> None:
        print("Disconnected from DB")

def start_service(conn: Connection):
    conn.connect()

if __name__ == "__main__":
    conn = Connection()
    start_service(conn)
    # Database satisfies the Connection protocol without inheriting from it
    db = Database()
    start_service(db)