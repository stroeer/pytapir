# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/curation/v1/core_curation_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from stroeer.core.v1 import article_pb2 as stroeer_dot_core_dot_v1_dot_article__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/stroeer/curation/v1/core_curation_service.proto\x12\x13stroeer.curation.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dstroeer/core/v1/article.proto\" \n\x12GetCurationRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\x8d\x01\n\x13GetCurationResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05label\x18\x02 \x01(\t\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x08\x61rticles\x18\x04 \x03(\x0b\x32\x18.stroeer.core.v1.Article\"&\n\x17\x42\x61tchGetCurationRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x03\"W\n\x18\x42\x61tchGetCurationResponse\x12;\n\tcurations\x18\x01 \x03(\x0b\x32(.stroeer.curation.v1.GetCurationResponse2\xe8\x01\n\x0f\x43urationService\x12\x62\n\x0bGetCuration\x12\'.stroeer.curation.v1.GetCurationRequest\x1a(.stroeer.curation.v1.GetCurationResponse\"\x00\x12q\n\x10\x42\x61tchGetCuration\x12,.stroeer.curation.v1.BatchGetCurationRequest\x1a-.stroeer.curation.v1.BatchGetCurationResponse\"\x00\x42.Z,github.com/stroeer/go-tapir/curation/v1;coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stroeer.curation.v1.core_curation_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/stroeer/go-tapir/curation/v1;core'
  _globals['_GETCURATIONREQUEST']._serialized_start=136
  _globals['_GETCURATIONREQUEST']._serialized_end=168
  _globals['_GETCURATIONRESPONSE']._serialized_start=171
  _globals['_GETCURATIONRESPONSE']._serialized_end=312
  _globals['_BATCHGETCURATIONREQUEST']._serialized_start=314
  _globals['_BATCHGETCURATIONREQUEST']._serialized_end=352
  _globals['_BATCHGETCURATIONRESPONSE']._serialized_start=354
  _globals['_BATCHGETCURATIONRESPONSE']._serialized_end=441
  _globals['_CURATIONSERVICE']._serialized_start=444
  _globals['_CURATIONSERVICE']._serialized_end=676
# @@protoc_insertion_point(module_scope)
