
#encoding UFT8  sqlite manager
import sqlite3
import datetime


class Geodata_plotting:
    def __init__(self):
        self.data_output = []       
        self.DB = "geodata.db"
        self.table = "GEO"
        self.connexion = sqlite3.connect(self.DB)
       
       

    def db_create_table(self):
        self.connexion = sqlite3.connect(self.DB)
        self.connexion.execute("CREATE TABLE GEO(DATETIME TEXT NOT NULL, LATITUDE REAL NOT NULL, LONGITUDE REAL NOT NULL, ALTITUDE REAL NOT NULL)")
        self.connexion.commit()
        self.connexion.close()

    def db_write_data(self, x, y, z):
        self.connexion = sqlite3.connect(self.DB)
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #Dict format --> {"latitude": self.latitude, "longitude" : self.longitude, "satelites": self.satellites, "time":self.GPStime}
        request = f"INSERT INTO GEO (DATETIME, LATITUDE, LONGITUDE, ALTITUDE) VALUES (\"{t}\", {x}, {y}, {z})"
        self.connexion.execute(request)
        self.connexion.commit()
        self.connexion.close()

        
    def db_read_data(self):
        pass
        


    def db_if_table_exist(self):
        self.connexion = sqlite3.connect(self.DB)
        cursor = self.connexion.cursor()	
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='GEO' ''')
        if cursor.fetchone()[0]==1 : {
	        print('Table exists.')
        }
        else : 
            self.db_create_table()



        
        
      
       


