
import urllib.request
import json
import ssl
import pandas as pd


user_names = []
comment_bodies = []


def json_parser(url):
    context = ssl._create_unverified_context()
    x = urllib.request.urlopen(url, context=context)
    doc = x.read()
    json_object = json.loads(doc)

    comments = json_object["comments"]

    for i in range(len(json_object["comments"])):
        for key, value in json_object["comments"][i].items():
            if key == "user":
                user_names.append(value['username'])
            if key == "body":
                comment_bodies.append(value)


    Dict = {'User': user_names, 'Commments': comment_bodies}
    
    df = pd.DataFrame(data=Dict)

    return df


print(json_parser("https://dummyjson.com/comments"))
  