from channels.consumer import SyncConsumer, AsyncConsumer

# --------------------------------------- Sync Consumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("websocket connected...", event)
        self.send({
            'type':'websocket.accept'
        })
    
    # this function will fire up while server receive data form client side
    def websocket_receive(self, event):
        print("websocket received...",event)

    def websocket_disconnect(self, event):
        print("websoceket disconnected...", event)





# -------------------------------------- Async Consumer
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket connected...", event)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self,event):
        print("websocket received...", event)

    async def websocket_disconnect(self,event):
        print("websocket disconnected...",event)