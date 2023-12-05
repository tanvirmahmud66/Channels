from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected...sync", event)
        print("Channels Layer...", self.channel_layer)
        print("Channels Name...", self.channel_name)
        print("group name....", self.scope['url_route']['kwargs']['group_name'])
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print("received from client....sync", event['text'])
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type':'chat.message',
            'message': event['text']
        })
    
    def chat_message(self, event):
        print("chat_message....sync", event)
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    
    def websocket_disconnect(self, event):
        print("disconnected....sync", event)
        print("Channels Layer...", self.channel_layer)
        print("Channels Name...", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        raise StopConsumer()




class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected...async", event)
        print("Channels Layer...", self.channel_layer)
        print("Channels Name...", self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print("received from client....sync", event['text'])
        await self.channel_layer.group_send(self.group_name,{
            'type':'chat.message',
            'message': event['text']
        })
    
    async def chat_message(self, event):
        print("chat_message....sync", event)
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    
    async def websocket_disconnect(self, event):
        print("disconnected....sync", event)
        print("Channels Layer...", self.channel_layer)
        print("Channels Name...", self.channel_name)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()
