import os
import pprint
from typing import List

import grpc

from stroeer.core.v1.article_pb2 import Article
from stroeer.page.article.v1.article_page_pb2 import \
    ArticlePage, RelatedArticle
from stroeer.page.article.v1.article_page_service_pb2 import \
    GetArticlePageRequest, GetArticlePageResponse
from stroeer.page.article.v1.article_page_service_pb2_grpc import \
    ArticlePageServiceStub

def handler():
    ssl = grpc.ssl_channel_credentials()

    if not os.getenv('GRPC_ENDPOINT'):
        print('\033[91mPlease provide a valid endpoint via env.GRPC_ENDPOINT.\033[0m')
        exit(1)

    if not os.getenv('GRPC_AUTHORIZATION'):
        print(
            '\033[91mYou should probably provide valid authorization via env.GRPC_AUTHORIZATION to prevent grpc/UNAUTHORIZED exceptions.\033[0m')

    with grpc.secure_channel(os.getenv('GRPC_ENDPOINT'), ssl) as channel:

        stub: ArticlePageServiceStub = ArticlePageServiceStub(channel)

        metadata = [('authorization', os.getenv('GRPC_AUTHORIZATION', 'VOID'))]
        response: GetArticlePageResponse = stub.GetArticlePage(
            request=GetArticlePageRequest(id=91501530),
            metadata=metadata
        )

        article_page: ArticlePage = response.article_page

        main_article: Article = article_page.article
        related_articles: List[RelatedArticle] = article_page.related_articles

        print(f"""
main article
============
{pprint.pformat(main_article)}
    """)

        print(f"""
related articles
================
{pprint.pformat(related_articles)}
    """)


def lambda_handler(event, context):
    handler()


if __name__ == '__main__':
    handler()
