#!/usr/bin/env python

import sys
import requests


class SpeakerbotClient(object):
    base_uri = 'http://speakerbot.local'

    def __init__(self):
        pass

    def _absolutify_url(self, uri):
        return '{}/{}'.format(self.base_uri, uri)

    def get(self, uri):
        uri = self._absolutify_url(uri)
        return requests.get(uri)

    def post(self, uri, data):
        uri = self._absolutify_url(uri)
        return requests.post(uri, data=data)

    def say(self, text, record_utterance=True):
        self.post('say/', {'speech-text': text, 'record_utterance': str(record_utterance).lower()})

    #def fget(self, uri_format, *args, **kwargs):
    #    uri = uri_format.format(
    #    uri = '{base_uri}/{uri}

    def play_sound(self, sound='dry-fart'):
        self.get('play_sound/{}'.format(sound))

    def downgoat(self, image='w5SlJ6q.gif'):
        self.get('image/{}/downgoat'.format(image))

    #def __getattr__(self, name):
    #    def meth_wrap(self, name, *args, **kwargs):
    #        if isinstance(args, [list, tuple]):
    #            if not isinstance(args, list):
    #                args = list(args)
    #            args.insert(0, name)
    #
    #        return self.get(*args, **kwargs)


if __name__ == '__main__':
    sp = SpeakerbotClient()
    #sp.play_sound(sys.argv[1])
    sp.say(sys.argv[1])
