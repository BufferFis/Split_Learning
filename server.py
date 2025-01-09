import grpc
from concurrent import futures
import message_service_pb2
import message_service_pb2_grpc

class MessageServiceServicer(message_service_pb2_grpc.MessageServiceServicer):
    def SendMessage(self, request, context):
        print(f"Received: {request.message}")
        return message_service_pb2.MessageResponse(reply='Hello, ' + request.message)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_service_pb2_grpc.add_MessageServiceServicer_to_server(MessageServiceServicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()