import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-7e3dffba-9af3-11ea-9123-e6a08f73ae22'
pnconfig.publish_key = 'pub-c-da801c01-82e0-4e28-b4b5-133335a467a3'

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(
            f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')


class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """

    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Blockcast a block object to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())


def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})


if __name__ == '__main__':
    main()
