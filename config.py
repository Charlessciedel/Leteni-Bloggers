import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 588
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:123@localhost/blogger'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
    
    

# class TestConfig(Config):
#     '''
#     Testing configuration child class
#     Args:Config: The parent configuration class with General configuration settings 
#     '''
    
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:123@localhost/blogger'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    # 'test': TestConfig
}