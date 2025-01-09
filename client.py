import grpc
import message_service_pb2
import message_service_pb2_grpc

def client():
    with grpc.insecure_channel('SERVER_IP:50051') as channel:
        stub = message_service_pb2_grpc.MessageServiceStub(channel)
        request = message_service_pb2.MessageRequest(message=':DDDDD')
        response = stub.SendMEssage(request)
        print('Client received: ' + response.reply)

if __name__ == '__main__':
    client()