from typing import Protocol

class Connectable(Protocol):
    def connect(self) -> None:
        ...  # Ellipsis indicates an abstract method

    def disconnect(self) -> None:
        ...

class Database:
    def connect(self) -> None:
        print("Connected to DB")

    def disconnect(self) -> None:
        print("Disconnected from DB")

def get_data_from_service(conn: Connectable) -> None:
    conn.connect()
    # do smthg
    conn.disconnect()

if __name__ == "__main__":
    # Database satisfies the Connection protocol without inheriting from it
    db = Database()
    get_data_from_service(db)