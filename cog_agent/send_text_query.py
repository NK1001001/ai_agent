#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import argparse
from intent import Intent
import json
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

""" You can use this program to send any text query.
Args: -tok: the authentication token taken from your created doamin in Dialogflow website console:
            https://console.dialogflow.com/api-client/#/login
            Enter your agent settings on the lest and take the: "Client access token"
      -text: The text you want to send, for example: "I want pizza"
"""

def main():
    """
        Get the token from the Dialogue Flow  WebSite, you should create an account and get it from you the agent
    """
    parser = argparse.ArgumentParser("cog agent - ")
    parser.add_argument('-text', '--text_to_query', help='The text to send', required=True)
    parser.add_argument('-token', '--auth_token', help='The token to authenticate on Dialogflow', required=True)
    args = parser.parse_args()
    ai = apiai.ApiAI(args.auth_token)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

   # request.query = "who is albert einstein?"
#Who was Albert Einstein?
    # request.query = "play sia"
    request.query = args.text_to_query
    response = request.getresponse()
    intent = Intent(response.read())
    #intent.createIntentFromJson(response.read())
    print ('intent name is: ',intent.getIntentName())
    intent.handleIntent()

    #print (response.read())
	

if __name__ == '__main__':
    main()
