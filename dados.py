
import pymysql
import dotenv
import os
import bcrypt


class Dados: 
    @staticmethod
    def chama_arquivo():
        dotenv.load_dotenv()
        connection = pymysql.connect( 
            host= os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'],
    )   
        return connection
