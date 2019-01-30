#!/usr/bin/env python
""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = 'stevednd'
insta_password = 'yyX^QFP9na7*&Y&q'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  disable_image_load=True,
                  multi_logs=True)

with smart_run(session):
    """ Activity flow """
    #account = "urlaubsguru"
    list1 = ('urlaubspiraten', 'firstclassandmore', 'urlaubstracker')
    for account in list1:
        all_followers = session.grab_followers(
            username=account, amount="full", live_match="False", store_locally=True)