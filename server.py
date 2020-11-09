import time
from concurrent import futures

import grpc
from generated import test_pb2, test_pb2_grpc

class TestServicer(test_pb2_grpc.TestServicer):
    def SayRepeated(self, request, context):
        print(f'TestServicer has got this request with repeated Message as field: {request}')

        response = test_pb2.HelloRepeatedReply()
        response.name = 'adsfafsad'
        response.bars.add().i=25
        response.bars.add().i = 26
        response.bars.add().i = 27

        print(f'TestServicer has prepared this response with repeated Message as field: {response}')

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    test_pb2_grpc.add_TestServicer_to_server(TestServicer(), server)
    print('Starting server on port 6066.')
    server.add_insecure_port('[::]:6066')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
