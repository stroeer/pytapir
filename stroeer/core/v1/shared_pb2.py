# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/core/v1/shared.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cstroeer/core/v1/shared.proto\x12\x0fstroeer.core.v1\"\xcb\x01\n\tReference\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0c\n\x04href\x18\x03 \x01(\t\x12\x36\n\x06\x66ields\x18\x04 \x03(\x0b\x32&.stroeer.core.v1.Reference.FieldsEntry\x12,\n\x08\x63hildren\x18\x05 \x03(\x0b\x32\x1a.stroeer.core.v1.Reference\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42*Z(github.com/stroeer/go-tapir/core/v1;coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stroeer.core.v1.shared_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z(github.com/stroeer/go-tapir/core/v1;core'
  _globals['_REFERENCE_FIELDSENTRY']._options = None
  _globals['_REFERENCE_FIELDSENTRY']._serialized_options = b'8\001'
  _globals['_REFERENCE']._serialized_start=50
  _globals['_REFERENCE']._serialized_end=253
  _globals['_REFERENCE_FIELDSENTRY']._serialized_start=208
  _globals['_REFERENCE_FIELDSENTRY']._serialized_end=253
# @@protoc_insertion_point(module_scope)
