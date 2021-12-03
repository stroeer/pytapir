# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/core/v1/core_article_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stroeer.core.v1 import article_pb2 as stroeer_dot_core_dot_v1_dot_article__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stroeer/core/v1/core_article_service.proto',
  package='stroeer.core.v1',
  syntax='proto3',
  serialized_options=b'\n\022de.stroeer.core.v1P\001Z(github.com/stroeer/go-tapir/core/v1;core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*stroeer/core/v1/core_article_service.proto\x12\x0fstroeer.core.v1\x1a\x1dstroeer/core/v1/article.proto\"\x1f\n\x11GetArticleRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"R\n\x13ListArticlesRequest\x12\x14\n\x0csection_path\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"[\n\x14ListArticlesResponse\x12*\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x18.stroeer.core.v1.Article\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbd\x01\n\x0e\x41rticleService\x12L\n\nGetArticle\x12\".stroeer.core.v1.GetArticleRequest\x1a\x18.stroeer.core.v1.Article\"\x00\x12]\n\x0cListArticles\x12$.stroeer.core.v1.ListArticlesRequest\x1a%.stroeer.core.v1.ListArticlesResponse\"\x00\x42@\n\x12\x64\x65.stroeer.core.v1P\x01Z(github.com/stroeer/go-tapir/core/v1;coreb\x06proto3'
  ,
  dependencies=[stroeer_dot_core_dot_v1_dot_article__pb2.DESCRIPTOR,])




_GETARTICLEREQUEST = _descriptor.Descriptor(
  name='GetArticleRequest',
  full_name='stroeer.core.v1.GetArticleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stroeer.core.v1.GetArticleRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=125,
)


_LISTARTICLESREQUEST = _descriptor.Descriptor(
  name='ListArticlesRequest',
  full_name='stroeer.core.v1.ListArticlesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='section_path', full_name='stroeer.core.v1.ListArticlesRequest.section_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='stroeer.core.v1.ListArticlesRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='stroeer.core.v1.ListArticlesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=209,
)


_LISTARTICLESRESPONSE = _descriptor.Descriptor(
  name='ListArticlesResponse',
  full_name='stroeer.core.v1.ListArticlesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='articles', full_name='stroeer.core.v1.ListArticlesResponse.articles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='stroeer.core.v1.ListArticlesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=302,
)

_LISTARTICLESRESPONSE.fields_by_name['articles'].message_type = stroeer_dot_core_dot_v1_dot_article__pb2._ARTICLE
DESCRIPTOR.message_types_by_name['GetArticleRequest'] = _GETARTICLEREQUEST
DESCRIPTOR.message_types_by_name['ListArticlesRequest'] = _LISTARTICLESREQUEST
DESCRIPTOR.message_types_by_name['ListArticlesResponse'] = _LISTARTICLESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetArticleRequest = _reflection.GeneratedProtocolMessageType('GetArticleRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETARTICLEREQUEST,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.GetArticleRequest)
  })
_sym_db.RegisterMessage(GetArticleRequest)

ListArticlesRequest = _reflection.GeneratedProtocolMessageType('ListArticlesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTARTICLESREQUEST,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesRequest)
  })
_sym_db.RegisterMessage(ListArticlesRequest)

ListArticlesResponse = _reflection.GeneratedProtocolMessageType('ListArticlesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTARTICLESRESPONSE,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesResponse)
  })
_sym_db.RegisterMessage(ListArticlesResponse)


DESCRIPTOR._options = None

_ARTICLESERVICE = _descriptor.ServiceDescriptor(
  name='ArticleService',
  full_name='stroeer.core.v1.ArticleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=305,
  serialized_end=494,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetArticle',
    full_name='stroeer.core.v1.ArticleService.GetArticle',
    index=0,
    containing_service=None,
    input_type=_GETARTICLEREQUEST,
    output_type=stroeer_dot_core_dot_v1_dot_article__pb2._ARTICLE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListArticles',
    full_name='stroeer.core.v1.ArticleService.ListArticles',
    index=1,
    containing_service=None,
    input_type=_LISTARTICLESREQUEST,
    output_type=_LISTARTICLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARTICLESERVICE)

DESCRIPTOR.services_by_name['ArticleService'] = _ARTICLESERVICE

# @@protoc_insertion_point(module_scope)
