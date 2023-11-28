from channels.consumer import SyncConsumer, AsyncConsumer


# sync consumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('connected....sync')
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print('received....sync',event)

    def websocket_disconnect(self, event):
        print('disconnect....sync', event)


# async consumer
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected....async", event)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print("Received....async", event)
    
    async def websocket_disconnect(self, event):
        print("disconnected....async", event)