import urllib2
import json

#Create and write the return into a json.
def write_json(file_name, data):
	with open(file_name, 'w') as outfile:
		json.dump(data, outfile)

#Print the json return on terminal.
def print_json(page_data):
	print json.dumps(page_data, indent=4, sort_keys=True)

#Get the info about a page or profile
def get_page_data(page_id,access_token,info,page_or_profile):
    api_endpoint = "https://graph.facebook.com/v2.6/"
    if page_or_profile == 1:
    	fb_graph_url = api_endpoint+page_id+"/insights"+info+"?access_token="+access_token
    else:
    	fb_graph_url = api_endpoint+page_id+"?fields="+info+"&access_token="+access_token
    try:
    	print fb_graph_url
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)

        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page = 1;
profile = 2;

profile_info = "id,name,likes,link"
page_user_demographics = "/page_fans,page_fans_locale,page_fans_city,page_fans_country,page_fans_gender_age,page_fan_adds,page_fan_adds_unique,page_fans_by_like_source,page_fans_by_like_source_unique,page_fan_removes,page_fan_removes_unique,page_fans_by_unlike_source_unique"

page_id = "facebook" # Inser the page id or name

token = "EAACEdEose0cBADGuex87nTy9vuEDQEA2C4WzEWDWyZALy48HneKzRh5ACVN67grtJLlISggFQHew7v7mPJNGQUabqkSyhgUjKxEnyZCs4xnXmfWiisU1zbNfG4zotJ4Ikpqimd5Vu8XQUh4RyiCYWCZBZAXh8CYX43IaHTFlzwZDZD"  # Access Token

page_data = get_page_data(page_id,token,profile_info,profile)

print_json(page_data)
write_json("facebook2.json", page_data)