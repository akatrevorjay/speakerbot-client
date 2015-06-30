from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests


LOG = logging.getLogger(__name__)
DEFAULT_TIMEOUT = 10
DEFAULT_BASE_URI = 'http://speakerbot.local'
DEFAULT_RECORD_UTTERANCE = True
DEFAULT_SOUND = 'dry-fart'
DEFAULT_SPEAKERBUCKS_AMOUNT = 500
DEFAULT_IMAGE = 'w5SlJ6q.gif'


class SpeakerbotClient(object):
    """Speakerbot Client API"""


    def __init__(self, base_uri=DEFAULT_BASE_URI, timeout=DEFAULT_TIMEOUT):
        self.base_uri = base_uri
        self.timeout = timeout


    def _absolutify_url(self, uri):
        """
        Helper to return an absolute URI. Yes, this exists.
        :param uri: Relative URI to transform
        :return: Absolute URI
        """
        return '{}/{}'.format(self.base_uri, uri)


    def _get(self, uri):
        """
        Send a GET request, yo
        :param uri: Relative URI to hit
        :return: request object
        """
        uri = self._absolutify_url(uri)
        try:
            return requests.get(uri, timeout=self.timeout)
        except:
            pass


    def _post(self, uri, data):
        """
        Send a POST request with delicious data, yo
        :param uri: Relative URI to hit
        :param data: Dictionary of POST data
        :return: request object
        """
        uri = self._absolutify_url(uri)
        try:
            return requests.post(uri, data=data, timeout=self.timeout)
        except:
            pass


    def _downgoat(self, image='w5SlJ6q.gif'):
        """
        Downvotes an image, yo
        :param image: Image filename
        :return: request object
        """
        return self._get('image/{}/downgoat'.format(image))


    _downvote = _downgoat


    def _upboat(self, image='w5SlJ6q.gif'):
        """
        Upvotes an image, yo
        :param image: Image filename
        :return: request object
        """
        return self._get('image/{}/upboat'.format(image))


    _upvote = _upboat


    def say(self, text, record_utterance=DEFAULT_RECORD_UTTERANCE):
        """
        Say a thing, yo
        :param text: Thing to say
        :param record_utterance: Bool - Slack and tweet?
        :return:
        """
        self._post('say/', {'speech-text': text, 'record_utterance': str(record_utterance).lower()})


    def play(self, sound=DEFAULT_SOUND):
        """
        Play a sound, yo
        :param sound: Sound to play
        :return:
        """
        self._get('play_sound/{}'.format(sound))


    def mine_speakerbucks(self, amount=DEFAULT_SPEAKERBUCKS_AMOUNT, image=DEFAULT_IMAGE):
        """
        Mine some speakerbucks, yo
        :param amount: Multiple of 10. Number of speakerbucks to mine
        :param image: Image to use for mining speakerbucks
        :return:
        """
        iterations = int(amount / 10)
        for _ in xrange(iterations):
            LOG.debug('Mining speakerbucks (downgoat/upboat loop)')
            self._downgoat(image)
            self._upboat(image)

    def random(self, keyword=None):
        """
        Generates a random phrase and has speakerbot say it.
        :param keyword: Keyword to include in phrase
        :return:
        """
        import speakerbotclient.text_generator as gen
        phrase = gen.generateSingle(keyword=keyword)
        LOG.debug("generated phrase:\n{}".format(phrase))
        self.say(phrase)

