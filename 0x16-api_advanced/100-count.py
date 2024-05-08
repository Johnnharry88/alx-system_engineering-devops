#!/usr/bin/python3
"""api for rddit"""

import json
import requests


def count_words(subreddit, word_list, after="", rec=[]):
    """count all words"""

    if after == "":
        rec = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        rec[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        rec[i] += rec[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (rec[j] > rec[i] or
                            (word_list[i] > word_list[j] and
                             rec[j] == rec[i])):
                        aux = rec[i]
                        rec[i] = rec[j]
                        rec[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (rec[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), rec[i]))
        else:
            count_words(subreddit, word_list, after, rec)
