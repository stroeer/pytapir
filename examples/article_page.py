import os

import grpc

from stroeer.core.v1.article_pb2 import Article
from stroeer.core.v1.core_article_service_pb2 import GetArticleRequest
from stroeer.core.v1.core_article_service_pb2_grpc import ArticleServiceStub

from typing import List

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

        stub: ArticleServiceStub = ArticleServiceStub(channel)

        metadata = [('authorization', os.getenv('GRPC_AUTHORIZATION', 'VOID'))]

        response: Article = stub.BatchGetArticles(
            request=GetArticleRequest(id=100272296),
            metadata=metadata)

        articles: List[Article] = response.articles

        for a in articles:
            print("{:10}[{:^9s}] — {}".format(a.id, Article.Type.Name(a.type), a.fields["headline"]))


def lambda_handler(event, context):
    handler()


if __name__ == '__main__':
    handler()
