# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imp/request/request_imp.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from volcengine.imp.models.business import imp_common_pb2 as imp_dot_business_dot_imp__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='imp/request/request_imp.proto',
  package='Volcengine.Imp.Models.Request',
  syntax='proto3',
  serialized_options=b'\n(com.volcengine.service.imp.model.requestB\nImpRequestP\001Z@github.com/volcengine/volc-sdk-golang/service/imp/models/request\240\001\001\330\001\001\312\002\037Volc\\Service\\Imp\\Models\\Request\342\002#Volc\\Service\\Imp\\Models\\GPBMetadata',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dimp/request/request_imp.proto\x12\x1dVolcengine.Imp.Models.Request\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dimp/business/imp_common.proto\"}\n\x13ImpSubmitJobRequest\x12<\n\tInputPath\x18\x01 \x01(\x0b\x32).Volcengine.Imp.Models.Business.InputPath\x12\x12\n\nTemplateId\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\"\"\n\x11ImpKillJobRequest\x12\r\n\x05JobId\x18\x01 \x01(\t\"\'\n\x15ImpRetrieveJobRequest\x12\x0e\n\x06JobIds\x18\x01 \x03(\tB\xc8\x01\n(com.volcengine.service.imp.model.requestB\nImpRequestP\x01Z@github.com/volcengine/volc-sdk-golang/service/imp/models/request\xa0\x01\x01\xd8\x01\x01\xca\x02\x1fVolc\\Service\\Imp\\Models\\Request\xe2\x02#Volc\\Service\\Imp\\Models\\GPBMetadatab\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,imp_dot_business_dot_imp__common__pb2.DESCRIPTOR,])




_IMPSUBMITJOBREQUEST = _descriptor.Descriptor(
  name='ImpSubmitJobRequest',
  full_name='Volcengine.Imp.Models.Request.ImpSubmitJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='InputPath', full_name='Volcengine.Imp.Models.Request.ImpSubmitJobRequest.InputPath', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TemplateId', full_name='Volcengine.Imp.Models.Request.ImpSubmitJobRequest.TemplateId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CallbackArgs', full_name='Volcengine.Imp.Models.Request.ImpSubmitJobRequest.CallbackArgs', index=2,
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
  serialized_end=252,
)


_IMPKILLJOBREQUEST = _descriptor.Descriptor(
  name='ImpKillJobRequest',
  full_name='Volcengine.Imp.Models.Request.ImpKillJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='JobId', full_name='Volcengine.Imp.Models.Request.ImpKillJobRequest.JobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=254,
  serialized_end=288,
)


_IMPRETRIEVEJOBREQUEST = _descriptor.Descriptor(
  name='ImpRetrieveJobRequest',
  full_name='Volcengine.Imp.Models.Request.ImpRetrieveJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='JobIds', full_name='Volcengine.Imp.Models.Request.ImpRetrieveJobRequest.JobIds', index=0,
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
  serialized_start=290,
  serialized_end=329,
)

_IMPSUBMITJOBREQUEST.fields_by_name['InputPath'].message_type = imp_dot_business_dot_imp__common__pb2._INPUTPATH
DESCRIPTOR.message_types_by_name['ImpSubmitJobRequest'] = _IMPSUBMITJOBREQUEST
DESCRIPTOR.message_types_by_name['ImpKillJobRequest'] = _IMPKILLJOBREQUEST
DESCRIPTOR.message_types_by_name['ImpRetrieveJobRequest'] = _IMPRETRIEVEJOBREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImpSubmitJobRequest = _reflection.GeneratedProtocolMessageType('ImpSubmitJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPSUBMITJOBREQUEST,
  '__module__' : 'imp.request.request_imp_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Request.ImpSubmitJobRequest)
  })
_sym_db.RegisterMessage(ImpSubmitJobRequest)

ImpKillJobRequest = _reflection.GeneratedProtocolMessageType('ImpKillJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPKILLJOBREQUEST,
  '__module__' : 'imp.request.request_imp_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Request.ImpKillJobRequest)
  })
_sym_db.RegisterMessage(ImpKillJobRequest)

ImpRetrieveJobRequest = _reflection.GeneratedProtocolMessageType('ImpRetrieveJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPRETRIEVEJOBREQUEST,
  '__module__' : 'imp.request.request_imp_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Imp.Models.Request.ImpRetrieveJobRequest)
  })
_sym_db.RegisterMessage(ImpRetrieveJobRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
