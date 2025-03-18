from datetime import timedelta

class Config:
    SECRET_KEY = "12345"
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)