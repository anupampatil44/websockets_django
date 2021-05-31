from channels.consumer import SyncConsumer
class EchoConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("connect event")
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print("recieve event")

        self.send({
            'type': 'websocket.send',
            'text':event.get('text')
        })

    def websocket_disconnect(self,event):
        print("disconnect event")
        print(event)
