from dotenv import load_dotenv
import os
load_dotenv()

from sqlalchemy import create_engine





dbConnectionString=os.getenv("dbConnectionString")
engine =  create_engine(
    dbConnectionString, 
    connect_args={
    "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    }
    })

