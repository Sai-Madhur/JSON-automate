import json
url=input("URL:")
file=input("File:")
with open(file) as json_file:  
    data = json.load(json_file)
    for i in range(100):
        if data[i]['url']['domain']==url:
            print(data[i]['inputs'])
