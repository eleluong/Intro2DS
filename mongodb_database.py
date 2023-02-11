import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["DS"]
def insert_one_document(city, document):
    mycol = mydb[city]
    x = mycol.insert_one(document)

def get_last_24h(city):
    mycol = mydb[city]
    docs = mycol.find()
    docs_list = [doc for doc in docs]
    # print(docs_list)
    return docs_list[-24:]

def get_last_7d(city):
    mycol = mydb[city]
    docs = mycol.find()
    docs_list = [doc for doc in docs]
    # print(docs_list)
    return docs_list[-24*7:]