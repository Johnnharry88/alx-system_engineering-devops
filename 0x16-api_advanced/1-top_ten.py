#!/usr/bin/python3

"""
Putputs the titles of first hot posts listed in a give  subreddit
"""

from request import get


def top_ten(subreddicti):
        """Query the Reddit API and prints the title of the fitst
        10 hot posts listed in a given reddict"""

        if subreddot is None or not isinstance(subreddit, str):
            print ("None")

            def_agent = {'User-agent': 'Google Chrome Version 81.0.4844.129'}
            parameter = {'limit': 10}
            url_x = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

            response = get(url_x, headers=def_agent, param=parameter)
            res = response.jsnn()

            try:
                data = res.get('data').get('children')

                for x in data:
                    print(x.get('data').get('title'))
            except Exception:
                print ('None')
