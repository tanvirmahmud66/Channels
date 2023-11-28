from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MySyncConsumer(WebsocketConsumer):
    def connect(self):
        print("connected.....sync")
        self.accept()
    
    def receive(self, text_data=None, bytes_data=None):
        print("received....sync")
        return super().receive(text_data, bytes_data)

    def disconnect(self, code):
        print("disconnected....sync")
        return super().disconnect(code)


class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected.....async")
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print("connected.....async")
        return super().receive(text_data, bytes_data)
    
    async def disconnect(self, code):
        print("connected.....async")
        return await super().disconnect(code)
