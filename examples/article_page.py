import os

import grpc

from stroeer.core.v1.article_pb2 import Article
from stroeer.page.article.v1.article_page_pb2 import ArticlePage
from stroeer.page.article.v1.article_page_service_pb2 import GetArticlePageRequest, GetArticlePageResponse
from stroeer.page.article.v1.article_page_service_pb2_grpc import  ArticlePageServiceStub

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

        stub: ArticlePageServiceStub = ArticlePageServiceStub(channel)

        metadata = [('authorization', os.getenv('GRPC_AUTHORIZATION', 'VOID'))]

        response: GetArticlePageResponse = stub.GetArticlePage(
            request=GetArticlePageRequest(id=100300282),
            metadata=metadata)

        ids: set[int] = set()
        page: GetArticlePageResponse = response.article_page
        a = page.article
        ids.add(a.id)
        related = page.related_articles

        print("{:10}[{:^9s}] — {}".format(a.id, Article.Type.Name(a.type), a.fields["headline"]))
        for a in related:
            print(f"related: source {a.source}")
            a = a.article
            print("{:10}[{:^9s}] — {}".format(a.id, Article.Type.Name(a.type), a.fields["headline"]))
            ids.add(a.id)

        for id in ids:
            print(f"aws sqs send-message --queue-url https://sqs.eu-west-1.amazonaws.com/053041861227/cms-updates-secondary.fifo --message-deduplication-id '{id}' --message-group-id '{id}' --message-body '{id}'")


def lambda_handler(event, context):
    handler()


if __name__ == '__main__':
    handler()
