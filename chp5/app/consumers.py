from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected...sync", event)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print("received....sync", event['text'])
        for i in range(20):
            self.send({
                'type':'websocket.send',
                'text': json.dumps({'count':i+1})
            })
            sleep(1)
    
    def websocket_disconnect(self, event):
        print("disconnected....sync", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected...sync", event)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print("received....sync", event['text'])
        for i in range(20):
            await self.send({
                'type':'websocket.send',
                'text':json.dumps({'count':i+1})
            })
            await asyncio.sleep(1)
    
    async def websocket_disconnect(self, event):
        print("disconnected....sync", event)
        raise StopConsumer()