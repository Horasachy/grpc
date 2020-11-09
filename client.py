import grpc

from generated import purchase_campaign_pb2_grpc, purchase_campaign_pb2, test_pb2_grpc, test_pb2


def client():
    with grpc.insecure_channel('localhost:6066') as conn:
        stub = purchase_campaign_pb2_grpc.PurchaseCampaingStub(conn)
        # stub = test_pb2_grpc.TestStub(conn)
        # foo = test_pb2.Foo()
        # bar = foo.bars.add()  # Adds a Bar then modify
        # bar.i = 15
        # bar.j = 12

        # foo = test_pb2.Foo(  # Creates Foo
        #     bars=[  # with its field bars set to a list
        #         test_pb2.Bar(i=15, j=17),  # where each list member is also initialized during creation.
        #         test_pb2.Bar(i=32),
        #         test_pb2.Bar(i=47, j=77),
        #     ]
        # )
        # stub = purchase_campaign_pb2_grpc.PurchaseCampaingStub(conn)

        # rq.suppliers_to_request.id = '1'

        # sup = rq.suppliers_to_request.add()
        # print(sup)
        # sup.id = '1'
        # del rq.suppliers_to_request[:]
        # rq.suppliers_to_request.extend(sup)

        # sup = purchase_campaign_pb2.SupplierToRequest()
        # sup.id = '1'
        # sup.contacts['full_name'] = "test"
        # sup.contacts['company_name'] = "test"
        # sup.contacts['email'] = "test"
        # sup.metadata['info'] = "test"

        # rq.suppliers_to_request.MergeFrom(sup)
        # rq.suppliers_to_request.contacts['full_name'] = sup.contacts['full_name']
        # rq.suppliers_to_request.contacts['company_name'] = sup.contacts['company_name']
        # rq.suppliers_to_request.contacts['email'] = sup.contacts['email']
        # rq.suppliers_to_request.metadata['info'] = sup.metadata['info']

        rq = purchase_campaign_pb2.PurchaseCampaignVerified()
        rq.id = 1
        rq.anfrage.id = 1
        rq.anfrage.name = 'product1'
        rq.schedule.start_at = '12-12-2010'
        rq.schedule.end_at = '12-12-2010'

        response = stub.CreatePurchaseCampanies(rq)
        print(response)


if __name__ == "__main__":
    client()
