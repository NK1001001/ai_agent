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

CLIENT_ACCESS_TOKEN = ''


def main():
    parser = argparse.ArgumentParser("cog agent - ")
    parser.add_argument('-text', '--text_to_query', help='The text to send')
    parser.add_argument('-token', '--auth_token', help='The token to authenticate on Dialogflow')

    ai = apiai.ApiAI(parser.auth_token)

    argparser = argparse.ArgumentParser()

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

   # request.query = "who is albert einstein?"
#Who was Albert Einstein?
    request.query = "play rihanna"
    response = request.getresponse()
    intent = Intent(response.read())
    #intent.createIntentFromJson(response.read())
    print ' intent name is: ' ,intent.getIntentName()
    intent.handleIntent()

    #print (response.read())
	

if __name__ == '__main__':
    main()
