import time
from concurrent import futures

import grpc
from generated import purchase_campaign_pb2, purchase_campaign_pb2_grpc, test_pb2, test_pb2_grpc


class PurchaseCompaingServicer(purchase_campaign_pb2_grpc.PurchaseCampaingServicer):

    def CreatePurchaseCampanies(self, request, context):
        response = purchase_campaign_pb2.PurchaseCampaignVerified()
        response.id = request.id
        response.anfrage.id = request.anfrage.id
        response.anfrage.name = request.anfrage.name
        # response.suppliers_to_request = request.suppliers_to_request
        # response.suppliers_to_request.contacts = request.suppliers_to_request.contacts
        # response.suppliers_to_request.contacts['company_name'] = request.suppliers_to_request.contacts['company_name']
        # response.suppliers_to_request.contacts['email'] = request.suppliers_to_request.contacts['email']
        # response.suppliers_to_request.metadata['info'] = request.suppliers_to_request.metadata['info']
        response.schedule.start_at = request.schedule.start_at
        response.schedule.end_at = request.schedule.end_at

        return response


class TestServicer(purchase_campaign_pb2_grpc.PurchaseCampaingServicer):
    def CreateFoo(self, request, context):
        response = test_pb2.Foo()
        response.i = request.bars

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    purchase_campaign_pb2_grpc.add_PurchaseCampaingServicer_to_server(PurchaseCompaingServicer(), server)
    test_pb2_grpc.add_TestServicer_to_server(TestServicer(), server)
    print('Starting server on port 6066.')
    server.add_insecure_port('[::]:6066')
    server.start()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
