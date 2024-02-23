import os
from dotenv import load_dotenv


class Environment:

    instance = None

    def __init__(self):
        load_dotenv()

        self.MODE = os.getenv('MODE', 'production')
        self.DATABASE_URL = (
            'clientpulse_db:3306'
            if self.MODE == 'development' else os.getenv(
                'DATABASE_URL', 'clientpulse_db:3306'
            )
        )
        self.DATABASE_NAME = (
            'clientpulse'
            if self.MODE == 'development' else os.getenv(
                'DATABASE_NAME',
                'clientpulse'
            )
        )
        self.DATABASE_USER = (
            'root'
            if self.MODE == 'development' else os.getenv(
                'DATABASE_USER',
                'root'
            )
        )
        self.DATABASE_PASSWORD = (
            '123456'
            if self.MODE == 'development' else os.getenv(
                'DATABASE_PASSWORD'
            )
        )

        self.url_connection = (
            f"mysql+mysqlconnector://{self.DATABASE_USER}"
            f":{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_URL}"
        )

        self.database_connection = (
            f"{self.url_connection}/{self.DATABASE_NAME}"
        )

    def __str__(self) -> str:
        return (
            f"MODE: {self.MODE}\n"
            f"DATABASE_URL: {self.DATABASE_URL}\n"
            f"DATABASE_NAME: {self.DATABASE_NAME}\n"
            f"DATABASE_USER: {self.DATABASE_USER}\n"
            f"DATABASE_PASSWORD: {self.DATABASE_PASSWORD}\n"
            f"database_connection: {self.database_connection}\n"
        )

    @classmethod
    @property
    def get_instance(cls) -> 'Environment':
        if cls.instance is None:
            cls.instance = Environment()
        print(cls.instance)
        return cls.instance
