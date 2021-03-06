#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function

import random

from six.moves.urllib import error

from zulip_bots.test_lib import BotTestCase

class TestGoogleSearchBot(BotTestCase):
    bot_name = 'googlesearch'

    # Simple query
    def test_normal(self):
        with self.mock_http_conversation('test_normal'):
            self.assert_bot_response({'content': 'zulip'}, {'content': 'Found Result: [Zulip](https://www.google.com/url?url=https%3A%2F%2Fzulipchat.com%2F)'}, 'send_reply')

    # Help without typing anything
    def test_bot_help_none(self):
        help_message = "To use this bot, start messages with @mentioned-bot, \
                    followed by what you want to search for. If \
                    found, Zulip will return the first search result \
                    on Google.\
                    \
                    An example message that could be sent is:\
                    '@mentioned-bot zulip' or \
                    '@mentioned-bot how to create a chatbot'."
        self.assert_bot_response({'content': ''}, {'content': help_message}, 'send_reply')

    # Help from typing 'help'
    def test_bot_help(self):
        help_message = "To use this bot, start messages with @mentioned-bot, \
                    followed by what you want to search for. If \
                    found, Zulip will return the first search result \
                    on Google.\
                    \
                    An example message that could be sent is:\
                    '@mentioned-bot zulip' or \
                    '@mentioned-bot how to create a chatbot'."
        self.assert_bot_response({'content': 'help'}, {'content': help_message}, 'send_reply')

    def test_bot_no_results(self):
        with self.mock_http_conversation('test_no_result'):
            self.assert_bot_response({'content': 'no res'}, {'content': 'Found no results.'}, 'send_reply')
