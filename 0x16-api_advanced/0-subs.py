#!/usr/bin/python3
"""
Function to query Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Ubuntu:0x16.api.advanced:v1.0.0 (by u/Evalase85)"
            }
    response = requests.get(url,  headers=headers)
    if (not response.ok):
        return 0
    results = response.json().get("data").get("subscribers")
    return results
