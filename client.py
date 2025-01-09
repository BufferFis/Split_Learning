import grpc
import message_service_pb2
import message_service_pb2_grpc

def run():
    with grpc.insecure_channel('SERVER_IP:50051') as channel:  # Replace SERVER_IP with the server's IP address
        stub = message_service_pb2_grpc.MessageServiceStub(channel)
        request = message_service_pb2.MessageRequest(message='World')
        response = stub.SendMessage(request)
        print('Client received: ' + response.reply)

if __name__ == '__main__':
    run()