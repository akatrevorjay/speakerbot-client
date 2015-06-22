from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from speakerbotclient.client import SpeakerbotClient

import click


@click.group()
@click.option('-h', default='http://speakerbot.local', help='The host for speakerbot.')
@click.pass_context
def speakerbot(ctx, h):
    ctx.obj = SpeakerbotClient(base_uri=h)


@speakerbot.command()
@click.argument('text')
@click.option('--record/--no-record', default=True, help='Whether speakerbot will record the utterance')
@click.pass_context
def say(ctx, text, record):
    spkr = ctx.obj
    spkr.say(text, record_utterance=record)


@speakerbot.command()
@click.option('--keyword', default=None, help='Whether speakerbot will include the word in the random phrase')
@click.pass_context
def random(ctx, keyword):
    spkr = ctx.obj
    spkr.random(keyword=keyword)


@speakerbot.command()
@click.option('--sound', default='dry-fart', help='What sound do you want speakerbot to play?')
@click.pass_context
def play(ctx, sound):
    spkr = ctx.obj
    spkr.play(sound=sound)


@speakerbot.command()
@click.option('--amount', default=1000, type=int, help='How many speakerbucks do you want?')
@click.option('--image', default='w5SlJ6q.gif', help='The image to up and down vote.')
@click.pass_context
def mine(ctx, amount, image):
    spkr = ctx.obj
    spkr.mine_speakerbucks(amount=amount, image=image)


if __name__ == '__main__':
    speakerbot()
