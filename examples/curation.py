import os
import pprint
from typing import List

import grpc

from stroeer.core.v1.article_pb2 import Article
from stroeer.curation.v1.core_curation_service_pb2 import \
    BatchGetCurationRequest, BatchGetCurationResponse
from stroeer.curation.v1.core_curation_service_pb2_grpc import \
    CurationServiceStub


def handler():
    ssl = grpc.ssl_channel_credentials()

    if not os.getenv('GRPC_ENDPOINT'):
        print('\033[91mPlease provide a valid endpoint via env.GRPC_ENDPOINT.\033[0m')
        exit(1)

    if not os.getenv('GRPC_AUTHORIZATION'):
        print(
            '\033[91mYou should probably provide valid authorization via env.GRPC_AUTHORIZATION to prevent grpc/UNAUTHORIZED exceptions.\033[0m')

    with grpc.secure_channel(os.getenv('GRPC_ENDPOINT'), ssl) as channel:

        stub: CurationServiceStub = CurationServiceStub(channel)

        metadata = [('authorization', os.getenv('GRPC_AUTHORIZATION', 'VOID'))]
        response: GetArticlePageResponse = stub.BatchGetCuration(
            request=BatchGetCurationRequest(ids=[1, 2]),
            metadata=metadata
        )

        curations: BatchGetCurationResponse = response.curations

        print(curations)
        # main_article: Article = article_page.article
        # related_articles: List[RelatedArticle] = article_page.related_articles
        #
        # print(f"""
# main article
# ============
# {pprint.pformat(main_article)}
#     """)
#
#         print(f"""
# related articles
# ================
# {pprint.pformat(related_articles)}
#     """)


def lambda_handler(event, context):
    handler()


if __name__ == '__main__':
    handler()
