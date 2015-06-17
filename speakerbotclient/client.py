import sys
import requests


class SpeakerbotClient(object):


    def __init__(self, base_uri='http://speakerbot.local'):
        self.base_uri = base_uri


    def _absolutify_url(self, uri):
        return '{}/{}'.format(self.base_uri, uri)


    def _downgoat(self, image='w5SlJ6q.gif'):
        self._get('image/{}/downgoat'.format(image))


    def _get(self, uri):
        uri = self._absolutify_url(uri)
        return requests.get(uri)


    def _post(self, uri, data):
        uri = self._absolutify_url(uri)
        return requests.post(uri, data=data)


    def _upboat(self, image='w5SlJ6q.gif'):
        self._get('image/{}/upboat'.format(image))


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
        iterations = amount / 10
        i = 0
        while i < iterations:
            self._downgoat(image)
            self._upboat(image)
            i += 1
