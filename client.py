import grpc
import logging

from generated import test_pb2_grpc, test_pb2


def run():
    with grpc.insecure_channel('localhost:6066') as conn:
        stub = test_pb2_grpc.TestStub(conn)

        helloRepeatedRequest = test_pb2.HelloRepeatedRequest()
        helloRepeatedRequest.name = 'gfhdhgfdh'
        helloRepeatedRequest.bars.add().i = 15
        helloRepeatedRequest.bars.add().i = 16
        helloRepeatedRequest.bars.add().i = 17
        print("TestRepeate client prepared: " + str(helloRepeatedRequest))

        response = stub.SayRepeated(helloRepeatedRequest)
        print("TestRepeate client received: " + str(response))


if __name__ == "__main__":
    logging.basicConfig()
    run()
