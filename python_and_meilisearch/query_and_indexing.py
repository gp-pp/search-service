from pprint import pprint
import pymongo
import meilisearch

url = "mongodb://harshxtanwar:db12345@ac-zdnook2-shard-00-00.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-01.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-02.dvbpycz.mongodb.net:27017/?ssl=true&replicaSet=atlas-83le6q-shard-0&authSource=admin&retryWrites=true&w=majority"
myclient = pymongo.MongoClient(url)

mydb = myclient["gp_profiles"]
mycol = mydb["proff_data"]

data = []
for x in mycol.find():
  data.append(x)

# print(data[0])



client = meilisearch.Client('http://meilisearch:7700')
index = client.index('data')

# print('odsfipsvajipfnjnvfnldf--------------------------------------kfdamvfkdvl')

x = 0
data_meili = []

for i in data:
  dictt = {
    'id':x,
    'name': i.get('name'),
    'thumbnail':i.get('thumbnail'),
    'link':i.get('link'),
    'author_id':i.get('author_id'),
    'email':i.get('email'),
    'affiliations':i.get('affiliations'),
    'cited_by':i.get('cited_by'),
    'interests':i.get('interests'),
    'articles':i.get('articles')
    }
  # print(dictt)
  print('\n')
  
  x = x+1
  data_meili.append(dictt)

   

# print(data[0])

print(type(data_meili))
# print(data_meili)

index.add_documents(data_meili)
