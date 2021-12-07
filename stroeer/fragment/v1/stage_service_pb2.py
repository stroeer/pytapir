# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/fragment/v1/stage_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stroeer.page.stage.v1 import stage_pb2 as stroeer_dot_page_dot_stage_dot_v1_dot_stage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stroeer/fragment/v1/stage_service.proto',
  package='stroeer.fragment.v1',
  syntax='proto3',
  serialized_options=b'\n\026de.stroeer.fragment.v1P\001Z0github.com/stroeer/go-tapir/fragment/v1;fragment',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'stroeer/fragment/v1/stage_service.proto\x12\x13stroeer.fragment.v1\x1a!stroeer/page/stage/v1/stage.proto\"\x1f\n\x10GetStagesRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\"A\n\x11GetStagesResponse\x12,\n\x06stages\x18\x01 \x03(\x0b\x32\x1c.stroeer.page.stage.v1.Stage2l\n\x0cStageService\x12\\\n\tGetStages\x12%.stroeer.fragment.v1.GetStagesRequest\x1a&.stroeer.fragment.v1.GetStagesResponse\"\x00\x42L\n\x16\x64\x65.stroeer.fragment.v1P\x01Z0github.com/stroeer/go-tapir/fragment/v1;fragmentb\x06proto3'
  ,
  dependencies=[stroeer_dot_page_dot_stage_dot_v1_dot_stage__pb2.DESCRIPTOR,])




_GETSTAGESREQUEST = _descriptor.Descriptor(
  name='GetStagesRequest',
  full_name='stroeer.fragment.v1.GetStagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='stroeer.fragment.v1.GetStagesRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=99,
  serialized_end=130,
)


_GETSTAGESRESPONSE = _descriptor.Descriptor(
  name='GetStagesResponse',
  full_name='stroeer.fragment.v1.GetStagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stages', full_name='stroeer.fragment.v1.GetStagesResponse.stages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=132,
  serialized_end=197,
)

_GETSTAGESRESPONSE.fields_by_name['stages'].message_type = stroeer_dot_page_dot_stage_dot_v1_dot_stage__pb2._STAGE
DESCRIPTOR.message_types_by_name['GetStagesRequest'] = _GETSTAGESREQUEST
DESCRIPTOR.message_types_by_name['GetStagesResponse'] = _GETSTAGESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetStagesRequest = _reflection.GeneratedProtocolMessageType('GetStagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTAGESREQUEST,
  '__module__' : 'stroeer.fragment.v1.stage_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.fragment.v1.GetStagesRequest)
  })
_sym_db.RegisterMessage(GetStagesRequest)

GetStagesResponse = _reflection.GeneratedProtocolMessageType('GetStagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTAGESRESPONSE,
  '__module__' : 'stroeer.fragment.v1.stage_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.fragment.v1.GetStagesResponse)
  })
_sym_db.RegisterMessage(GetStagesResponse)


DESCRIPTOR._options = None

_STAGESERVICE = _descriptor.ServiceDescriptor(
  name='StageService',
  full_name='stroeer.fragment.v1.StageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=199,
  serialized_end=307,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStages',
    full_name='stroeer.fragment.v1.StageService.GetStages',
    index=0,
    containing_service=None,
    input_type=_GETSTAGESREQUEST,
    output_type=_GETSTAGESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STAGESERVICE)

DESCRIPTOR.services_by_name['StageService'] = _STAGESERVICE

# @@protoc_insertion_point(module_scope)