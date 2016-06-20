# facebook-graph-api-python

- **About**
- **The Code**
- **Parameters**
- **The JSON output**
- **For more info**

## About

This is a Python program to generate a .json file with info about a facebook page or a facebook profile with the facebook Graph API.

## The Code

```
import json
import urllib2

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

page_id = "20531316728" # Inser the page id or name

token = "YOUR_ACCESS_TOKEN"  # Access Token

page_data = get_page_data(page_id,token,page_user_demographics,page)

```

Parameters in get_page_data:

```

page_id: id number of the page or profile (You can get this in: http://findmyfbid.com/)
access_token: Your Graph Token (You can get this in: https://developers.facebook.com/tools/explorer)
info: What info about the page you want to get, above its write all the options
page_or_profile: if you want to get info about a page, you need to type 'page', but if you want to get info about a person profile, you need to type 'profile'

```

## What info can i get?


You can enter in those sites and see all the possible info options you can get from facebook pages.

But, i will put some examples in here

* About profiles [Profile Documents](https://developers.facebook.com/docs/graph-api/reference/page/)

Since the person allow you to get theres infos, you can get whatever you want. Like id, about, artists, posts, checkins, location, fan_count, genre, birthday, photos, videos and many other things.

* About pages [Pages Documents](https://developers.facebook.com/docs/graph-api/reference/v2.6/insights)

Since the person allow you to get theres infos, you can get all kind of metrics you want. Likes, comments, posts, shares, and all types of grouping, by genre, person_preference, age, location and many other possibilitis

## The JSON output

    {
        "id": "20531316728", 
        "likes": {
            "data": [
                {
                    "id": "152917571386966", 
                    "name": "Facebook Analog Research Laboratory"
                }, 
                {
                    "id": "444271875701907", 
                    "name": "Fashion on Facebook"
                }, 
                {
                    "id": "74100576336", 
                    "name": "Facebook for Business"
                }, 
                {
                    "id": "114770288670819", 
                    "name": "Facebook Stories"
                }, 
                {
                    "id": "158736497491762", 
                    "name": "Onavo"
                }, 
                {
                    "id": "367152833370567", 
                    "name": "Instagram"
                }, 
                {
                    "id": "41130665917", 
                    "name": "Nonprofits on Facebook"
                }, 
                {
                    "id": "143483439014410", 
                    "name": "Universities on Facebook"
                }, 
                {
                    "id": "150984694912422", 
                    "name": "Influencers on Facebook"
                }, 
                {
                    "id": "10435416547", 
                    "name": "Music on Facebook"
                }, 
                {
                    "id": "125713384123802", 
                    "name": "Facebook and Privacy"
                }
            ], 
            "paging": {
                "cursors": {
                    "after": "MTI1NzEzMzg0MTIzODAy", 
                    "before": "MTUyOTE3NTcxMzg2OTY2"
                }
            }
        }, 
        "link": "https://www.facebook.com/facebook/", 
        "name": "Facebook"
    }

## For more info:

[API Documents](https://developers.facebook.com/docs/graph-api/reference/v2.6/)

[Get Your Facebook API Key](https://developers.facebook.com/tools/explorer)