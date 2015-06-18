from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import gevent.monkey
gevent.monkey.patch_all()

import logging
log = logging.getLogger(__name__)

import gevent


class SpeakerbotParallelMiner(gevent.Greenlet):
    """
    Parallel Speakerbuck Miner
    """

    def __init__(self, client, amount):
        """
        Init
        :param client: SpeakerbotClient instance
        :param amount: Amount of speakerbucks to mine
        """
        self.client = client
        self.amount = amount

        gevent.Greenlet.__init__(self)

    def run(self):
        """Run miner from within greenlet"""
        log.info('Starting %s', self)
        self.client.mine_speakerbucks(amount=self.amount)
        log.info('Done %s', self)


def mine(client, amount=1000, image='w5SlJ6q.gif', concurrency=10):
    """
    Mine some speakerbucks concurrently, yo
    :param client: SpeakerbotClient instance
    :param amount: Multiple of 10. Number of speakerbucks to mine
    :param image: Image to use for mining speakerbucks
    :param concurrency: Number of parallel requests
    :return:
    """
    per_miner = int(amount / concurrency)
    log.info('Starting parallel gevent miner: amount=%s image=%s concurrency=%s per_miner=%s',
             amount, image, concurrency, per_miner)

    miners = []
    for _ in xrange(concurrency):
        miner = SpeakerbotParallelMiner(client, per_miner)
        miners.append(miner)
    for miner in miners:
        miner.start()

    log.info('Running gevent loop')
    gevent.sleep(0)


def main():
    from . import SpeakerbotClient
    client = SpeakerbotClient()
    mine(client)


if __name__ == '__main__':
    main()
