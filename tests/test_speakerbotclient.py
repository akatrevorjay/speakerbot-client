from speakerbotclient import SpeakerbotClient
from mock import Mock, patch
from unittest import TestCase

class SpeakerbotClientTest(TestCase):
    """ Provides an instantiated SpeakerbotClient
    """


    def setUp(self):
        self.client = SpeakerbotClient()


class TestInit(SpeakerbotClientTest):
    """ Test __init__()
    """


    def test_defaults_base_uri(self):
        self.assertEqual('http://speakerbot.local', self.client.base_uri)


    def test_allows_base_uri_override(self):
        base_uri = 'foo'
        self.client = SpeakerbotClient(base_uri)
        self.assertEqual(base_uri, self.client.base_uri)


class TestAbsolutifyUrl(SpeakerbotClientTest):
    """ Test _absolutify_url()
    """


    def test_formats_url_correctly(self):
        uri = 'foo'
        self.assertEqual('{}/{}'.format(self.client.base_uri, uri),
                         self.client._absolutify_url(uri))


class TestDowngoat(SpeakerbotClientTest):
    """ Test _downgoat
    """


    def setUp(self):
        super(TestDowngoat, self).setUp()
        self.client._get = Mock()


    def test_calls_get_with_correct_arguments(self):
        image = 'foo'
        self.client._downgoat(image)
        self.client._get.assert_called_once_with('image/{}/downgoat'.format(image))


    def test_defaults_image(self):
        self.client._downgoat()
        self.client._get.assert_called_once_with('image/w5SlJ6q.gif/downgoat')


class TestGet(SpeakerbotClientTest):
    """ Test get()
    """


    @patch('speakerbotclient.client.requests')
    def test_calls_proper_methods(self, mock_requests):
        uri = 'foo'
        self.client._absolutify_url = Mock(return_value=uri)
        self.client._get(uri)
        self.client._absolutify_url.assert_called_once_with(uri)
        mock_requests.get.assert_called_once_with(uri)


class TestPost(SpeakerbotClientTest):
    """ Test post()
    """


    @patch('speakerbotclient.client.requests')
    def test_calls_proper_methods(self, mock_requests):
        uri = 'foo'
        data = {'foo': 'bar'}
        self.client._absolutify_url = Mock(return_value=uri)
        self.client._post(uri, data)
        self.client._absolutify_url.assert_called_once_with(uri)
        mock_requests.post.assert_called_once_with(uri, data=data)


class TestUpboat(SpeakerbotClientTest):
    """ Test _upboat
    """


    def setUp(self):
        super(TestUpboat, self).setUp()
        self.client._get = Mock()


    def test_calls_get_with_correct_arguments(self):
        image = 'foo'
        self.client._upboat(image)
        self.client._get.assert_called_once_with('image/{}/upboat'.format(image))


    def test_defaults_image(self):
        self.client._upboat()
        self.client._get.assert_called_once_with('image/w5SlJ6q.gif/upboat')


class TestSay(SpeakerbotClientTest):
    """ Test say()
    """


    def setUp(self):
        super(TestSay, self).setUp()
        self.client._post = Mock()


    def test_calls_post_with_correct_arguments(self):
        arg_dicts = [
            {
                'text': 'foo',
                'record_utterance': False
            },
            {
                'text': 'foo',
                'record_utterance': True
            }
        ]
        for arg_dict in arg_dicts:
            self.client._post = Mock()
            self.client.say(arg_dict['text'], arg_dict['record_utterance'])
            self.client._post.assert_called_once_with('say/',
                {
                    'speech-text': arg_dict['text'],
                    'record_utterance': str(arg_dict['record_utterance']).lower()
                })


    def test_defaults_record_utterance(self):
        text = 'foo'
        self.client.say(text)
        self.client._post.assert_called_once_with('say/',
            {
                'speech-text': text,
                'record_utterance': 'true'
            })


class TestPlay(SpeakerbotClientTest):
    """ Test play()
    """


    def setUp(self):
        super(TestPlay, self).setUp()
        self.client._get = Mock()


    def test_calls_get_with_correct_arguments(self):
        sound = 'foo'
        self.client.play(sound)
        self.client._get.assert_called_once_with('play_sound/{}'.format(sound))


    def test_defaults_sound(self):
        self.client.play()
        self.client._get.assert_called_once_with('play_sound/dry-fart')


class TestMineSpeakerbucks(SpeakerbotClientTest):
    """ Test mine_speakerbucks
    """


    def setUp(self):
        super(TestMineSpeakerbucks, self).setUp()
        self.client._downgoat = Mock()
        self.client._upboat = Mock()


    def test_calls_methods_correct_number_of_times(self):
        for amount in [10, 30, 50, 100]:
            self.client._downgoat = Mock()
            self.client._upboat = Mock()
            self.client.mine_speakerbucks(amount, 'foo')
            self.assertEqual(amount / 10, self.client._downgoat.call_count)
            self.assertEqual(amount / 10, self.client._upboat.call_count)


    def test_defaults_amount_and_image(self):
        self.client.mine_speakerbucks()
        self.assertEqual(100, self.client._downgoat.call_count)
        self.assertEqual(100, self.client._upboat.call_count)
        self.client._downgoat.assert_called_with('w5SlJ6q.gif')
        self.client._upboat.assert_called_with('w5SlJ6q.gif')
