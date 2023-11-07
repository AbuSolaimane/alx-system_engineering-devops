#!/usr/bin/python3
"""
this is a module
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    this is a function
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    my_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    results = get(my_url, headers=agent).json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
