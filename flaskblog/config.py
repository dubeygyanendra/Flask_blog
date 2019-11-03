import os

class Config:
	SECRET_KEY='e8bc62141da651bc5cba8383979babce'
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	Mail_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')