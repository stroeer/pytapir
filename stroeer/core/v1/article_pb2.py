# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/core/v1/article.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from stroeer.core.v1 import shared_pb2 as stroeer_dot_core_dot_v1_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dstroeer/core/v1/article.proto\x12\x0fstroeer.core.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cstroeer/core/v1/shared.proto\"\x97\x18\n\x07\x41rticle\x12\n\n\x02id\x18\x01 \x01(\x03\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.stroeer.core.v1.Article.Type\x12\x32\n\x08sub_type\x18\x03 \x01(\x0e\x32 .stroeer.core.v1.Article.SubType\x12\x30\n\x0csection_tree\x18\x04 \x01(\x0b\x32\x1a.stroeer.core.v1.Reference\x12\x34\n\x06\x66ields\x18\x05 \x03(\x0b\x32$.stroeer.core.v1.Article.FieldsEntry\x12-\n\x06\x62odies\x18\x06 \x03(\x0b\x32\x1d.stroeer.core.v1.Article.Body\x12\x33\n\x08metadata\x18\x07 \x01(\x0b\x32!.stroeer.core.v1.Article.Metadata\x12\x32\n\x08\x65lements\x18\x08 \x03(\x0b\x32 .stroeer.core.v1.Article.Element\x12\x32\n\x08keywords\x18\t \x03(\x0b\x32 .stroeer.core.v1.Article.Keyword\x12\x0f\n\x07onwards\x18\n \x03(\x03\x12\x38\n\x08variants\x18\x0b \x03(\x0b\x32&.stroeer.core.v1.Article.VariantsEntry\x12(\n\x07\x61uthors\x18\x0c \x03(\x0b\x32\x17.stroeer.core.v1.Author\x12\x14\n\x08\x65ntities\x18\x64 \x03(\tB\x02\x18\x01\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aI\n\rVariantsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.stroeer.core.v1.Article:\x02\x38\x01\x1a\x97\x06\n\x07\x45lement\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.stroeer.core.v1.Article.Element.Type\x12<\n\trelations\x18\x02 \x03(\x0e\x32).stroeer.core.v1.Article.Element.Relation\x12\x36\n\x06\x61ssets\x18\x03 \x03(\x0b\x32&.stroeer.core.v1.Article.Element.Asset\x12\x32\n\x08\x63hildren\x18\x04 \x03(\x0b\x32 .stroeer.core.v1.Article.Element\x1a\xca\x02\n\x05\x41sset\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32+.stroeer.core.v1.Article.Element.Asset.Type\x12\x42\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x32.stroeer.core.v1.Article.Element.Asset.FieldsEntry\x12\x33\n\x08metadata\x18\x03 \x01(\x0b\x32!.stroeer.core.v1.Article.Metadata\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"^\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\t\n\x05VIDEO\x10\x02\x12\x12\n\x0e\x45XTERNAL_VIDEO\x10\x03\x12\x0c\n\x08METADATA\x10\x04\x12\x08\n\x04LINK\x10\x05\"\x95\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x41RTICLE\x10\x01\x12\t\n\x05IMAGE\x10\x02\x12\t\n\x05VIDEO\x10\x03\x12\x0b\n\x07GALLERY\x10\x04\x12\n\n\x06OEMBED\x10\x05\x12\n\n\x06\x41UTHOR\x10\x06\x12\n\n\x06\x41GENCY\x10\x07\x12\x15\n\x11\x45\x44GE_SIDE_INCLUDE\x10\x08\x12\x0c\n\x08\x43ITATION\x10\t\"H\n\x08Relation\x12\x18\n\x14RELATION_UNSPECIFIED\x10\x00\x12\n\n\x06OPENER\x10\x01\x12\n\n\x06TEASER\x10\x02\x12\n\n\x06SOCIAL\x10\x03\x1a\xef\x03\n\x04\x42ody\x12\x38\n\x08\x63hildren\x18\x01 \x03(\x0b\x32&.stroeer.core.v1.Article.Body.BodyNode\x12\x30\n\x04type\x18\x02 \x01(\x0e\x32\".stroeer.core.v1.Article.Body.Type\x1a\x87\x02\n\x08\x42odyNode\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x42\n\x06\x66ields\x18\x03 \x03(\x0b\x32\x32.stroeer.core.v1.Article.Body.BodyNode.FieldsEntry\x12\x38\n\x08\x63hildren\x18\x04 \x03(\x0b\x32&.stroeer.core.v1.Article.Body.BodyNode\x12\x32\n\x08\x65lements\x18\x05 \x03(\x0b\x32 .stroeer.core.v1.Article.Element\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"q\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x42ODY\x10\x01\x12\x13\n\x0f\x41RTICLE_SOURCES\x10\x02\x12\x0e\n\nDISCLAIMER\x10\x03\x12\r\n\tTRUST_BOX\x10\x04\x12\x15\n\x11TABLE_OF_CONTENTS\x10\x05\x1a\xab\x05\n\x08Metadata\x12\x36\n\x05state\x18\x01 \x01(\x0e\x32\'.stroeer.core.v1.Article.Metadata.State\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cpublish_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x13transformation_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x15transformation_errors\x18\x07 \x01(\x03\x12:\n\x16last_modification_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x0c\x65vent_source\x18\t \x01(\x0e\x32-.stroeer.core.v1.Article.Metadata.EventSource\x12\x11\n\tseo_score\x18\n \x01(\x01\x12\x16\n\x0epublication_id\x18\x0b \x01(\x03\"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tPUBLISHED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\t\n\x05\x44RAFT\x10\x03\"[\n\x0b\x45ventSource\x12\x1c\n\x18\x45VENT_SOURCE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PRIMARY\x10\x01\x12\r\n\tSECONDARY\x10\x02\x12\x12\n\x0e\x43ONTENT_ENGINE\x10\x03\x1a\x35\n\x07Keyword\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x02\"\x93\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x41RTICLE\x10\x01\x12\r\n\x05IMAGE\x10\x02\x1a\x02\x08\x01\x12\t\n\x05VIDEO\x10\x03\x12\x0b\n\x07GALLERY\x10\x04\x12\t\n\x05\x45MBED\x10\x05\x12\n\n\x06\x41UTHOR\x10\x06\x12\x0e\n\x06\x41GENCY\x10\x07\x1a\x02\x08\x01\x12\x0c\n\x08\x45XTERNAL\x10\x08\x12\x0c\n\x08INTERNAL\x10\x64\"\xde\x01\n\x07SubType\x12\x18\n\x14SUB_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04NEWS\x10\x01\x12\n\n\x06\x43OLUMN\x10\x02\x12\x0e\n\nCOMMENTARY\x10\x03\x12\r\n\tINTERVIEW\x10\x04\x12\x0f\n\x0b\x43ONTROVERSY\x10\x05\x12\x10\n\x0cTAGESANBRUCH\x10\x06\x12\r\n\tEVERGREEN\x10\x07\x12\x11\n\rAGENCY_IMPORT\x10\x08\x12\x0f\n\x0b\x41\x44VERTORIAL\x10\t\x12\x08\n\x04QUIZ\x10\n\x12\x08\n\x04GAME\x10\x0b\x12\x0e\n\nCOMPLIANCE\x10\x0c\x12\n\n\x06RECIPE\x10\r\"\xfd\x03\n\x06\x41uthor\x12\n\n\x02id\x18\x01 \x01(\x03\x12*\n\x04type\x18\x02 \x01(\x0e\x32\x1c.stroeer.core.v1.Author.Type\x12\x33\n\x06\x66ields\x18\x03 \x03(\x0b\x32#.stroeer.core.v1.Author.FieldsEntry\x12\x32\n\x08\x65lements\x18\x04 \x03(\x0b\x32 .stroeer.core.v1.Article.Element\x12:\n\x0cwork_history\x18\x05 \x03(\x0b\x32$.stroeer.core.v1.Author.HistoryEntry\x12-\n\teducation\x18\x06 \x03(\x0b\x32\x1a.stroeer.core.v1.Reference\x12\x33\n\x0fsocial_profiles\x18\x07 \x03(\x0b\x32\x1a.stroeer.core.v1.Reference\x12\x1a\n\x12\x61reas_of_expertise\x18\x08 \x03(\t\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0cHistoryEntry\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"4\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41UTHOR\x10\x01\x12\n\n\x06\x41GENCY\x10\x02\x42*Z(github.com/stroeer/go-tapir/core/v1;coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stroeer.core.v1.article_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(github.com/stroeer/go-tapir/core/v1;core'
  _ARTICLE_FIELDSENTRY._options = None
  _ARTICLE_FIELDSENTRY._serialized_options = b'8\001'
  _ARTICLE_VARIANTSENTRY._options = None
  _ARTICLE_VARIANTSENTRY._serialized_options = b'8\001'
  _ARTICLE_ELEMENT_ASSET_FIELDSENTRY._options = None
  _ARTICLE_ELEMENT_ASSET_FIELDSENTRY._serialized_options = b'8\001'
  _ARTICLE_BODY_BODYNODE_FIELDSENTRY._options = None
  _ARTICLE_BODY_BODYNODE_FIELDSENTRY._serialized_options = b'8\001'
  _ARTICLE_TYPE.values_by_name["IMAGE"]._options = None
  _ARTICLE_TYPE.values_by_name["IMAGE"]._serialized_options = b'\010\001'
  _ARTICLE_TYPE.values_by_name["AGENCY"]._options = None
  _ARTICLE_TYPE.values_by_name["AGENCY"]._serialized_options = b'\010\001'
  _ARTICLE.fields_by_name['entities']._options = None
  _ARTICLE.fields_by_name['entities']._serialized_options = b'\030\001'
  _AUTHOR_FIELDSENTRY._options = None
  _AUTHOR_FIELDSENTRY._serialized_options = b'8\001'
  _globals['_ARTICLE']._serialized_start=114
  _globals['_ARTICLE']._serialized_end=3209
  _globals['_ARTICLE_FIELDSENTRY']._serialized_start=681
  _globals['_ARTICLE_FIELDSENTRY']._serialized_end=726
  _globals['_ARTICLE_VARIANTSENTRY']._serialized_start=728
  _globals['_ARTICLE_VARIANTSENTRY']._serialized_end=801
  _globals['_ARTICLE_ELEMENT']._serialized_start=804
  _globals['_ARTICLE_ELEMENT']._serialized_end=1595
  _globals['_ARTICLE_ELEMENT_ASSET']._serialized_start=1039
  _globals['_ARTICLE_ELEMENT_ASSET']._serialized_end=1369
  _globals['_ARTICLE_ELEMENT_ASSET_FIELDSENTRY']._serialized_start=681
  _globals['_ARTICLE_ELEMENT_ASSET_FIELDSENTRY']._serialized_end=726
  _globals['_ARTICLE_ELEMENT_ASSET_TYPE']._serialized_start=1275
  _globals['_ARTICLE_ELEMENT_ASSET_TYPE']._serialized_end=1369
  _globals['_ARTICLE_ELEMENT_TYPE']._serialized_start=1372
  _globals['_ARTICLE_ELEMENT_TYPE']._serialized_end=1521
  _globals['_ARTICLE_ELEMENT_RELATION']._serialized_start=1523
  _globals['_ARTICLE_ELEMENT_RELATION']._serialized_end=1595
  _globals['_ARTICLE_BODY']._serialized_start=1598
  _globals['_ARTICLE_BODY']._serialized_end=2093
  _globals['_ARTICLE_BODY_BODYNODE']._serialized_start=1715
  _globals['_ARTICLE_BODY_BODYNODE']._serialized_end=1978
  _globals['_ARTICLE_BODY_BODYNODE_FIELDSENTRY']._serialized_start=681
  _globals['_ARTICLE_BODY_BODYNODE_FIELDSENTRY']._serialized_end=726
  _globals['_ARTICLE_BODY_TYPE']._serialized_start=1980
  _globals['_ARTICLE_BODY_TYPE']._serialized_end=2093
  _globals['_ARTICLE_METADATA']._serialized_start=2096
  _globals['_ARTICLE_METADATA']._serialized_end=2779
  _globals['_ARTICLE_METADATA_STATE']._serialized_start=2617
  _globals['_ARTICLE_METADATA_STATE']._serialized_end=2686
  _globals['_ARTICLE_METADATA_EVENTSOURCE']._serialized_start=2688
  _globals['_ARTICLE_METADATA_EVENTSOURCE']._serialized_end=2779
  _globals['_ARTICLE_KEYWORD']._serialized_start=2781
  _globals['_ARTICLE_KEYWORD']._serialized_end=2834
  _globals['_ARTICLE_TYPE']._serialized_start=2837
  _globals['_ARTICLE_TYPE']._serialized_end=2984
  _globals['_ARTICLE_SUBTYPE']._serialized_start=2987
  _globals['_ARTICLE_SUBTYPE']._serialized_end=3209
  _globals['_AUTHOR']._serialized_start=3212
  _globals['_AUTHOR']._serialized_end=3721
  _globals['_AUTHOR_FIELDSENTRY']._serialized_start=681
  _globals['_AUTHOR_FIELDSENTRY']._serialized_end=726
  _globals['_AUTHOR_HISTORYENTRY']._serialized_start=3618
  _globals['_AUTHOR_HISTORYENTRY']._serialized_end=3667
  _globals['_AUTHOR_TYPE']._serialized_start=3669
  _globals['_AUTHOR_TYPE']._serialized_end=3721
# @@protoc_insertion_point(module_scope)
