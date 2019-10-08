import json
from json2html import *
def PlayerProfile(switch_type,ios_ver):
        return[{'Switch Type': switch_type,'IOS Version':ios_ver}]

switch_type =input ("What is the Switch type:")
ios_ver = input ("What is the IOS version:")

answer = PlayerProfile (switch_type,ios_ver)

jdump =json.dumps(answer)
print (jdump)
json_obj_in_html = json2html.convert(json = { "Switch Info" : jdump })
print (json_obj_in_html)
