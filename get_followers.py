#!/usr/bin/env python
""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run
import sys

# login credentials
insta_username = ''
insta_password = ''
with open("logs/working_user.lst") as input_file:
    line = input_file.readline().strip()
    insta_username = line.split(':')[0]
    insta_password = line.split(':')[1]
    print("username :"+insta_username)
    print("password :"+insta_password)
    sys.stdout.flush()

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  disable_image_load=True,
                  multi_logs=True)

with smart_run(session):
    """ Activity flow """
    with open("logs/target_list.lst", 'r') as input_file:
        for line in input_file:
            account = line.strip()
            if account[0] != '#':
                all_followers = session.grab_followers(
                    username=account, amount="full", live_match="False", store_locally= False)
