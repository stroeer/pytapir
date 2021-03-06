# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/core/v1/core_article_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stroeer.core.v1 import article_pb2 as stroeer_dot_core_dot_v1_dot_article__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*stroeer/core/v1/core_article_service.proto\x12\x0fstroeer.core.v1\x1a\x1dstroeer/core/v1/article.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x1f\n\x11GetArticleRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"&\n\x17\x42\x61tchGetArticlesRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x03\"F\n\x18\x42\x61tchGetArticlesResponse\x12*\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x18.stroeer.core.v1.Article\"\xa7\x07\n\x13ListArticlesRequest\x12\x39\n\x05query\x18\x01 \x01(\x0b\x32*.stroeer.core.v1.ListArticlesRequest.Query\x12=\n\x07\x66ilters\x18\x02 \x01(\x0b\x32,.stroeer.core.v1.ListArticlesRequest.Filters\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x1a\xfc\x03\n\x05Query\x12\x0c\n\x04path\x18\x01 \x01(\t\x12=\n\x04type\x18\x02 \x01(\x0e\x32/.stroeer.core.v1.ListArticlesRequest.Query.Type\x12\x42\n\x07sort_by\x18\x03 \x01(\x0e\x32\x31.stroeer.core.v1.ListArticlesRequest.Query.SortBy\x12?\n\x05order\x18\x04 \x01(\x0e\x32\x30.stroeer.core.v1.ListArticlesRequest.Query.Order\x12-\n\tfrom_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07to_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"@\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cHOME_SECTION\x10\x01\x12\x10\n\x0cROOT_SECTION\x10\x02\"D\n\x06SortBy\x12\x17\n\x13SORT_BY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUPDATE_TIME\x10\x01\x12\x10\n\x0cPUBLISH_TIME\x10\x02\"=\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\x1a\xef\x01\n\x07\x46ilters\x12\x34\n\rtype_includes\x18\x01 \x03(\x0e\x32\x1d.stroeer.core.v1.Article.Type\x12\x34\n\rtype_excludes\x18\x02 \x03(\x0e\x32\x1d.stroeer.core.v1.Article.Type\x12;\n\x11sub_type_includes\x18\x03 \x03(\x0e\x32 .stroeer.core.v1.Article.SubType\x12;\n\x11sub_type_excludes\x18\x04 \x03(\x0e\x32 .stroeer.core.v1.Article.SubType\"[\n\x14ListArticlesResponse\x12*\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x18.stroeer.core.v1.Article\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"(\n\x14ListSectionsResponse\x12\x10\n\x08sections\x18\x01 \x03(\t2\xf9\x02\n\x0e\x41rticleService\x12L\n\nGetArticle\x12\".stroeer.core.v1.GetArticleRequest\x1a\x18.stroeer.core.v1.Article\"\x00\x12i\n\x10\x42\x61tchGetArticles\x12(.stroeer.core.v1.BatchGetArticlesRequest\x1a).stroeer.core.v1.BatchGetArticlesResponse\"\x00\x12]\n\x0cListArticles\x12$.stroeer.core.v1.ListArticlesRequest\x1a%.stroeer.core.v1.ListArticlesResponse\"\x00\x12O\n\x0cListSections\x12\x16.google.protobuf.Empty\x1a%.stroeer.core.v1.ListSectionsResponse\"\x00\x42@\n\x12\x64\x65.stroeer.core.v1P\x01Z(github.com/stroeer/go-tapir/core/v1;coreb\x06proto3')



_GETARTICLEREQUEST = DESCRIPTOR.message_types_by_name['GetArticleRequest']
_BATCHGETARTICLESREQUEST = DESCRIPTOR.message_types_by_name['BatchGetArticlesRequest']
_BATCHGETARTICLESRESPONSE = DESCRIPTOR.message_types_by_name['BatchGetArticlesResponse']
_LISTARTICLESREQUEST = DESCRIPTOR.message_types_by_name['ListArticlesRequest']
_LISTARTICLESREQUEST_QUERY = _LISTARTICLESREQUEST.nested_types_by_name['Query']
_LISTARTICLESREQUEST_FILTERS = _LISTARTICLESREQUEST.nested_types_by_name['Filters']
_LISTARTICLESRESPONSE = DESCRIPTOR.message_types_by_name['ListArticlesResponse']
_LISTSECTIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListSectionsResponse']
_LISTARTICLESREQUEST_QUERY_TYPE = _LISTARTICLESREQUEST_QUERY.enum_types_by_name['Type']
_LISTARTICLESREQUEST_QUERY_SORTBY = _LISTARTICLESREQUEST_QUERY.enum_types_by_name['SortBy']
_LISTARTICLESREQUEST_QUERY_ORDER = _LISTARTICLESREQUEST_QUERY.enum_types_by_name['Order']
GetArticleRequest = _reflection.GeneratedProtocolMessageType('GetArticleRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETARTICLEREQUEST,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.GetArticleRequest)
  })
_sym_db.RegisterMessage(GetArticleRequest)

BatchGetArticlesRequest = _reflection.GeneratedProtocolMessageType('BatchGetArticlesRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHGETARTICLESREQUEST,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.BatchGetArticlesRequest)
  })
_sym_db.RegisterMessage(BatchGetArticlesRequest)

BatchGetArticlesResponse = _reflection.GeneratedProtocolMessageType('BatchGetArticlesResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHGETARTICLESRESPONSE,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.BatchGetArticlesResponse)
  })
_sym_db.RegisterMessage(BatchGetArticlesResponse)

ListArticlesRequest = _reflection.GeneratedProtocolMessageType('ListArticlesRequest', (_message.Message,), {

  'Query' : _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
    'DESCRIPTOR' : _LISTARTICLESREQUEST_QUERY,
    '__module__' : 'stroeer.core.v1.core_article_service_pb2'
    # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesRequest.Query)
    })
  ,

  'Filters' : _reflection.GeneratedProtocolMessageType('Filters', (_message.Message,), {
    'DESCRIPTOR' : _LISTARTICLESREQUEST_FILTERS,
    '__module__' : 'stroeer.core.v1.core_article_service_pb2'
    # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesRequest.Filters)
    })
  ,
  'DESCRIPTOR' : _LISTARTICLESREQUEST,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesRequest)
  })
_sym_db.RegisterMessage(ListArticlesRequest)
_sym_db.RegisterMessage(ListArticlesRequest.Query)
_sym_db.RegisterMessage(ListArticlesRequest.Filters)

ListArticlesResponse = _reflection.GeneratedProtocolMessageType('ListArticlesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTARTICLESRESPONSE,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesResponse)
  })
_sym_db.RegisterMessage(ListArticlesResponse)

ListSectionsResponse = _reflection.GeneratedProtocolMessageType('ListSectionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSECTIONSRESPONSE,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListSectionsResponse)
  })
_sym_db.RegisterMessage(ListSectionsResponse)

_ARTICLESERVICE = DESCRIPTOR.services_by_name['ArticleService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022de.stroeer.core.v1P\001Z(github.com/stroeer/go-tapir/core/v1;core'
  _GETARTICLEREQUEST._serialized_start=156
  _GETARTICLEREQUEST._serialized_end=187
  _BATCHGETARTICLESREQUEST._serialized_start=189
  _BATCHGETARTICLESREQUEST._serialized_end=227
  _BATCHGETARTICLESRESPONSE._serialized_start=229
  _BATCHGETARTICLESRESPONSE._serialized_end=299
  _LISTARTICLESREQUEST._serialized_start=302
  _LISTARTICLESREQUEST._serialized_end=1237
  _LISTARTICLESREQUEST_QUERY._serialized_start=487
  _LISTARTICLESREQUEST_QUERY._serialized_end=995
  _LISTARTICLESREQUEST_QUERY_TYPE._serialized_start=798
  _LISTARTICLESREQUEST_QUERY_TYPE._serialized_end=862
  _LISTARTICLESREQUEST_QUERY_SORTBY._serialized_start=864
  _LISTARTICLESREQUEST_QUERY_SORTBY._serialized_end=932
  _LISTARTICLESREQUEST_QUERY_ORDER._serialized_start=934
  _LISTARTICLESREQUEST_QUERY_ORDER._serialized_end=995
  _LISTARTICLESREQUEST_FILTERS._serialized_start=998
  _LISTARTICLESREQUEST_FILTERS._serialized_end=1237
  _LISTARTICLESRESPONSE._serialized_start=1239
  _LISTARTICLESRESPONSE._serialized_end=1330
  _LISTSECTIONSRESPONSE._serialized_start=1332
  _LISTSECTIONSRESPONSE._serialized_end=1372
  _ARTICLESERVICE._serialized_start=1375
  _ARTICLESERVICE._serialized_end=1752
# @@protoc_insertion_point(module_scope)
