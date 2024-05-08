#!/usr/bin/python3
""" Gat the number of subscribers for a given subreddit"""

from requests import get


def number_of_subscribers(subreddit):
    """Quieries API
    Return: Number of subscribes (not active users, total subscriber)
    for a give subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    agent_def = {'User-agent': 'Google Chrome Version 81.0.4844.129'}
    url_x = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url_x, headers=agent_def)
    res = response.json()
    try:
        return res.get('data').get('subscribers')
    except Exception:
        return 0
