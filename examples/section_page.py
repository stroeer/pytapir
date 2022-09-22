import os

import grpc

from stroeer.core.v1.article_pb2 import Article
from stroeer.page.section.v1.section_page_service_pb2 import GetSectionPageRequest, GetSectionPageResponse
from stroeer.page.section.v1.section_page_service_pb2_grpc import SectionPageServiceStub


def handler():
    ssl = grpc.ssl_channel_credentials()

    endpoint = os.getenv('GRPC_ENDPOINT')
    # endpoint = 'localhost:8080'
    if not endpoint:
        print('\033[91mPlease provide a valid endpoint via env.GRPC_ENDPOINT.\033[0m')
        exit(1)

    if not os.getenv('GRPC_AUTHORIZATION'):
        print(
            '\033[91mYou should probably provide valid authorization via env.GRPC_AUTHORIZATION to prevent grpc/UNAUTHORIZED exceptions.\033[0m')

    # with grpc.insecure_channel(endpoint) as channel:
    with grpc.secure_channel(os.getenv('GRPC_ENDPOINT'), ssl) as channel:

        stub: SectionPageServiceStub = SectionPageServiceStub(channel)

        metadata = [('authorization', os.getenv('GRPC_AUTHORIZATION', 'VOID'))]
        response: BatchGetCurationResponse = stub.BatchGetCuration(request=BatchGetCurationRequest(ids=[1, 2, 39, 133]),
                                                                   metadata=metadata)

        curations: BatchGetCurationResponse = response.curations

        for curation in curations:
            items = "\n".join(["{:10}[{:^9s}] — {}".format(a.id, Article.Type.Name(a.type), a.fields["headline"])
                               for a in curation.articles])
            print(f"""
List {curation.id} ["{curation.label}" updated at {curation.update_time.ToDatetime()}]
items: 
{items}
            """)


def lambda_handler(event, context):
    handler()


if __name__ == '__main__':
    handler()
