# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/page/section/v1/section_page_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stroeer.page.section.v1 import section_page_pb2 as stroeer_dot_page_dot_section_dot_v1_dot_section__page__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2stroeer/page/section/v1/section_page_service.proto\x12\x17stroeer.page.section.v1\x1a*stroeer/page/section/v1/section_page.proto\";\n\x15GetSectionPageRequest\x12\x14\n\x0csection_path\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\"\x97\x02\n\x16GetSectionPageResponse\x12:\n\x0csection_page\x18\x01 \x01(\x0b\x32$.stroeer.page.section.v1.SectionPage\x12\x13\n\x0btotal_pages\x18\x02 \x01(\x05\x12W\n\x0fpagination_type\x18\x03 \x01(\x0e\x32>.stroeer.page.section.v1.GetSectionPageResponse.PaginationType\"S\n\x0ePaginationType\x12\x1f\n\x1bPAGINATION_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x46IXED_BLOCK\x10\x01\x12\x0f\n\x0bGHOST_BLOCK\x10\x02\x32\x89\x01\n\x12SectionPageService\x12s\n\x0eGetSectionPage\x12..stroeer.page.section.v1.GetSectionPageRequest\x1a/.stroeer.page.section.v1.GetSectionPageResponse\"\x00\x42\x35Z3github.com/stroeer/go-tapir/page/section/v1;sectionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stroeer.page.section.v1.section_page_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/stroeer/go-tapir/page/section/v1;section'
  _globals['_GETSECTIONPAGEREQUEST']._serialized_start=123
  _globals['_GETSECTIONPAGEREQUEST']._serialized_end=182
  _globals['_GETSECTIONPAGERESPONSE']._serialized_start=185
  _globals['_GETSECTIONPAGERESPONSE']._serialized_end=464
  _globals['_GETSECTIONPAGERESPONSE_PAGINATIONTYPE']._serialized_start=381
  _globals['_GETSECTIONPAGERESPONSE_PAGINATIONTYPE']._serialized_end=464
  _globals['_SECTIONPAGESERVICE']._serialized_start=467
  _globals['_SECTIONPAGESERVICE']._serialized_end=604
# @@protoc_insertion_point(module_scope)
