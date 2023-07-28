import secrets
import psycopg2
from apps import app

# secret key for mongo session
tokenSession = secrets.token_hex(20)
app.config["SECRET_KEY"]=tokenSession

DATABASE_URL = 'postgresql://erik1288:sasa@microservicios-postgres12:5432/db_springboot_cloud'
conn = psycopg2.connect(DATABASE_URL, sslmode='disable')

class BaseConfig(object):
    'Base configuration'
    TESTING = False
    DEBUG=True
    
class ProductionConfig(BaseConfig):
    'Production configuration'
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    'Development configuration'
    TESTING = True