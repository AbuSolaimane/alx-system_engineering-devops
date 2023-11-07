#!/usr/bin/python3

"""
this is a module
"""

from requests import get


def top_ten(subreddit):
    """
    this is function
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    parameters = {'limit': 10}
    my_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    results = get(my_url, headers=agent, params=parameters).json()

    try:
        my_data = results.get('data').get('children')
        for i in my_data:
            print(i.get('data').get('title'))
    except Exception:
        print("None")
