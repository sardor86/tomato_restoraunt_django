from dataclasses import dataclass
from environs import Env


@dataclass
class DataBase:
    host: str
    port: int
    user: str
    password: str
    database: str


@dataclass
class Django:
    secret_key: str


@dataclass
class Email:
    email: str
    password: str


@dataclass
class Config:
    db: DataBase
    django: Django
    email: Email


def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        db=DataBase(
            host=env.str('DB_HOST'),
            port=env.int('DB_PORT'),
            user=env.str('DB_USER'),
            password=env.str('DB_PASSWORD'),
            database=env.str('DB_NAME'),
        ),
        django=Django(
            secret_key=env.str('SECRET_KET')
        ),
        email=Email(
            email=env.str('MAIL'),
            password=env.str('MAIL_PASSWORD')
        )
    )
