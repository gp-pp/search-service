from pprint import pprint
import pymongo
import meilisearch


url = "mongodb+srv://gradcapital:gradcapital@cluster0.zeq17pz.mongodb.net/?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(url)

mydb = myclient["test"]
mycol = mydb["users"]

data = []
for x in mycol.find():
  data.append(x)


print(data[0])



client = meilisearch.Client('http://meilisearch:7700')
index = client.index('data_new')

# print('odsfipsvajipfnjnvfnldf--------------------------------------kfdamvfkdvl')

x = 0
data_meili = []

for i in data:

  del i['_id']

  publications = i.get('publications')
  for k in publications:
     del k['_id']
     

  name = i.get('name')
  print(name)
     
  dictt = {
    'id':x,
    'name': name,
    'email':i.get('email'),
    'username':i.get('username'),
    'bio':i.get('bio'),
    'affiliations':i.get('affiliations'),
    'gscholar_url':i.get('gscholar_url'),
    'interests':i.get('interests'),
    'publications':publications,
    'skills':i.get('skills')
    }
  # print(dictt)
  print('\n')
  
  x = x+1
  data_meili.append(dictt)

   

# print(data[0])

print(type(data_meili))
# print(data_meili)
# print(data_meili)

index.add_documents(data_meili)

import io
import requests
import PyPDF2


index = client.index('papers')


common_url = "https://cited-file-storage.s3.ap-south-1.amazonaws.com/"
pdfs = [
  '10.1002x9781118371985.pdf',
  '10.1007x978-3-319-66119-3.pdf',
  '10.1080x13691066.2019.1599188.pdf',
  '10.1111xcorg.12259.pdf',
  '10.1111xjoes.12274.pdf',
  '10.5465xamp.2017.0208.pdf'
  ]

id_no = 0
final_data_papers = []
for i in pdfs:
  url = common_url + i
  r = requests.get(url)
  f = io.BytesIO(r.content)

  reader = PyPDF2.PdfReader(f)
  print(reader)
  pages = reader.pages
  
  y = ''
  for i in pages:
      x = i.extract_text()
      y = y + x
  dictt = {
    'id': id_no,
    'text': y,
    'url':url
  }

  id_no = id_no + 1
  final_data_papers.append(dictt)

index.add_documents(final_data_papers)


