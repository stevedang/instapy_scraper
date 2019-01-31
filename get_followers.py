#!/usr/bin/env python
""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = 'steve.dang.050'
insta_password = 'lavina123'

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
    #list1 = ('abindenurlaub', 'reiseuhu', 'travador','globaltraveler.tv' )
    #list1 = ('airberlin', 'condorairlines', 'tuideutschland')
    list1 = ('capital_bra')
    #list1 = ('heuteshow', 'tagesschau', 'gzsz' )
    #list1 = ('extra3', 'szmagazin', 'bild', 'spiegelonline' )
    for account in list1:
        all_followers = session.grab_followers(
            username=account, amount="full", live_match="False", store_locally= False)
