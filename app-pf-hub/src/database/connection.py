import pymongo

url_database = 'mongodb+srv://rafaelcorrea:KH3im0bgAqsB1YgQ@cluster0.5tbir.mongodb.net/'

banco = pymongo.MongoClient(url_database)
#db = banco['db_produto']
db = banco['Grupo_2']

Produtos = db.Produtos
