# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntest.proto\"&\n\x04test\x12\r\n\x05\x62rake\x18\x03 \x01(\x02\x12\x0f\n\x07\x63ounter\x18\x04 \x01(\x05\x62\x06proto3'
)




_TEST = _descriptor.Descriptor(
  name='test',
  full_name='test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='brake', full_name='test.brake', index=0,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counter', full_name='test.counter', index=1,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=14,
  serialized_end=52,
)

DESCRIPTOR.message_types_by_name['test'] = _TEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

test = _reflection.GeneratedProtocolMessageType('test', (_message.Message,), {
  'DESCRIPTOR' : _TEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:test)
  })
_sym_db.RegisterMessage(test)


# @@protoc_insertion_point(module_scope)