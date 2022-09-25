import serial
from pymongo import MongoClient
import uuid
from datetime import datetime
import urllib

CONNECTION_STRING = "mongodb+srv://vsaraff:"+urllib.parse.quote("??????")+"@cluster0.timjy8c.mongodb.net/test"
#
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)

# Create the database for our example (we will use the same database throughout the tutorial
db = client['aurdino']['stats']
data_db = {}

with serial.Serial('COM3', 9600, timeout=1) as ser:
    while True:
        line = str(ser.readline())
        if len(line) > 55:
            line = line[2:-5]
            myuuid = str(uuid.uuid4())
            # ts = str(time.time())
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            linefields = line.split(",")
            field1 = linefields[0].split(":")
            field2 = linefields[1].split(":")
            field3 = linefields[2].split(":")
            data_db["ID"] = myuuid
            data_db[field1[0]] = field1[1]
            data_db[field2[0]] = float(field2[1].strip())
            data_db[field3[0]] = float(field3[1].strip())
            data_db["TimeStamp"] = date_time
            print(data_db)
            db.insert_one(data_db)
            data_db = {}


