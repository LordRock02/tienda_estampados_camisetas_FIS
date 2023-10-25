class Config:
    DEBUG = True
    SECRET_KEY = "dev"

    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:admin@localhost:5432/project"