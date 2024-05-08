#!/usr/bin/python3
"""
Using Reddit APi recusrively
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returnut top ten posts titles"""
    global after
    ded_agent = {'User-agent': 'api_advanced-project'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after}
    res = requests.get(url, params=params, headers=ded_agent,
                       allow_redirects=False)

    if res.status_code == 200:
        after_x = res.json().get('data').get('after')
        if after_x is not None:
            after = after_x
            recurse(subreddit, hot_list)
            all_titles = res.json().get('data').get('children')
            for title in all_titles:
                hot_list.appent(title.get('data').get('title'))
            return hot_list
        else:
            return (None)
