import json
import yaml

with open('c:/My/Github/09-devnetpython-KDubicki/src/parsing/myfile.json','r') as json_file:
    ourjson = json.load(json_file)

print(ourjson)
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

print("\n\n---")
print(yaml.dump(ourjson))