from json2html import *
json_obj = [{"Agent Status": "status1", "Last backup": "", "hostId": 1234567, "hostfqdn": "test1.example.com", "username": "user1"}, {"Agent Status": "status2", "Last backup": "", "hostId": 2345678, "hostfqdn": "test2.example.com", "username": "user2"}]
print (json_obj)
json_obj_in_html = json2html.convert(json = { "Switch Info" : json_obj })
print (json_obj_in_html)