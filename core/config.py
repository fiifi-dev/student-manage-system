from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = "mysql://root:testpass123@127.0.0.1:3306/student_management_system"


settings = Settings()
