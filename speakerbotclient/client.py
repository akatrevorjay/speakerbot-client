from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests


class SpeakerbotClient(object):
    """Speakerbot Client API"""

    def __init__(self, base_uri='http://speakerbot.local'):
        self.base_uri = base_uri

    def _absolutify_url(self, uri):
        return '{}/{}'.format(self.base_uri, uri)

    def _get(self, uri):
        uri = self._absolutify_url(uri)
        return requests.get(uri)

    def _post(self, uri, data):
        uri = self._absolutify_url(uri)
        return requests.post(uri, data=data)

    def _downvote(self, image='w5SlJ6q.gif'):
        """Downvotes an image, yo
        :param image: Image filename
        :return:
        """
        self._get('image/{}/downgoat'.format(image))

    _downgoat = _downvote

    def _upvote(self, image='w5SlJ6q.gif'):
        """Upvotes an image, yo
        :param image: Image filename
        :return:
        """
        self._get('image/{}/upboat'.format(image))

    _upboat = _upvote

    def say(self, text, record_utterance=True):
        """
        Say a thing, yo
        :param text: Thing to say
        :param record_utterance: Bool - Slack and tweet?
        :return:
        """
        self._post('say/', {'speech-text': text, 'record_utterance': str(record_utterance).lower()})

    def play(self, sound='dry-fart'):
        """
        Play a sound, yo
        :param sound: Sound to play
        :return:
        """
        self._get('play_sound/{}'.format(sound))

    def mine_speakerbucks(self, amount=1000, image='w5SlJ6q.gif'):
        """
        Mine some speakerbucks, yo
        :param amount: Multiple of 10. Number of speakerbucks to mine
        :param image: Image to use for mining speakerbucks
        :return:
        """
        iterations = int(amount / 10)
        for _ in xrange(iterations):
            self._downgoat(image)
            self._upboat(image)
