import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    baseUrl = os.getenv("BASEURL")
    userName = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

