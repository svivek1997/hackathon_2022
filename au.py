import serial
from pymongo import MongoClient
import uuid
import time
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
            print(line)
            myuuid = str(uuid.uuid4())
            ts = str(time.time())
            linefields = line.split(",")
            field1 = linefields[0].split(":")
            field2 = linefields[1].split(":")
            field3 = linefields[2].split(":")
            data_db["ID"] = myuuid
            data_db[field1[0]] = field1[1]
            data_db[field2[0]] = field2[1]
            data_db[field3[0]] = field3[1]
            data_db["TimeStamp"] = ts
            print(data_db)
            db.insert_one(data_db)
            data_db = {}


    # x = ser.read()          # read one byte
    # s = ser.read(10)        # read up to ten bytes (timeout)
    # line = ser.readline()

    # db_values = {}
