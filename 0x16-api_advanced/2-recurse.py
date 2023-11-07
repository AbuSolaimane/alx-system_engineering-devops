#!/usr/bin/python3
"""
this is a module
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    func
    """
    global after
    agent = {'User-Agent': 'api_advanced-project'}
    my_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    results = requests.get(my_url, params=params, headers=agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
