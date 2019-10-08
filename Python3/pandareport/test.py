from json2html import *

def SwitchProfile(switch_type,ios_ver,acl_ver):
        return[{'Switch Type': switch_type,'IOS Version':ios_ver,'ACL': acl_ver}]

switch_type =input ("What is the Switch type:")
ios_ver = input ("What is the IOS version:")
acl_ver = input ("What is the ACL version:")

json_obj = SwitchProfile (switch_type,ios_ver,acl_ver)

#json_obj = [{"Switch Type": "3560", "IOS Version": "15"}]
print (json_obj)
json_obj_in_html = json2html.convert(json = { "Switch Info" : json_obj })
print (json_obj_in_html)