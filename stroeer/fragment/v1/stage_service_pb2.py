# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/fragment/v1/stage_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stroeer.page.stage.v1 import stage_pb2 as stroeer_dot_page_dot_stage_dot_v1_dot_stage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'stroeer/fragment/v1/stage_service.proto\x12\x13stroeer.fragment.v1\x1a!stroeer/page/stage/v1/stage.proto\"\x1f\n\x10GetStagesRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\",\n\x1bGetArticleCompanionsRequest\x12\r\n\x05token\x18\x01 \x03(\t\"U\n\x1cGetArticleCompanionsResponse\x12\x35\n\ncompanions\x18\x01 \x03(\x0b\x32!.stroeer.page.stage.v1.Stage.Item\"A\n\x11GetStagesResponse\x12,\n\x06stages\x18\x01 \x03(\x0b\x32\x1c.stroeer.page.stage.v1.Stage2\xeb\x01\n\x0cStageService\x12\\\n\tGetStages\x12%.stroeer.fragment.v1.GetStagesRequest\x1a&.stroeer.fragment.v1.GetStagesResponse\"\x00\x12}\n\x14GetArticleCompanions\x12\x30.stroeer.fragment.v1.GetArticleCompanionsRequest\x1a\x31.stroeer.fragment.v1.GetArticleCompanionsResponse\"\x00\x42L\n\x16\x64\x65.stroeer.fragment.v1P\x01Z0github.com/stroeer/go-tapir/fragment/v1;fragmentb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stroeer.fragment.v1.stage_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026de.stroeer.fragment.v1P\001Z0github.com/stroeer/go-tapir/fragment/v1;fragment'
  _GETSTAGESREQUEST._serialized_start=99
  _GETSTAGESREQUEST._serialized_end=130
  _GETARTICLECOMPANIONSREQUEST._serialized_start=132
  _GETARTICLECOMPANIONSREQUEST._serialized_end=176
  _GETARTICLECOMPANIONSRESPONSE._serialized_start=178
  _GETARTICLECOMPANIONSRESPONSE._serialized_end=263
  _GETSTAGESRESPONSE._serialized_start=265
  _GETSTAGESRESPONSE._serialized_end=330
  _STAGESERVICE._serialized_start=333
  _STAGESERVICE._serialized_end=568
# @@protoc_insertion_point(module_scope)
