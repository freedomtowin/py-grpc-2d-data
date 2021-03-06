# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10helloworld.proto\x12\nhelloworld\"\x1e\n\x0bModelResult\x12\x0f\n\x07message\x18\x01 \x01(\t\"N\n\x0c\x44oubleMatrix\x12\x0c\n\x04rows\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ols\x18\x02 \x01(\x05\x12\x10\n\x08\x63hannels\x18\x03 \x01(\x05\x12\x10\n\x04\x64\x61ta\x18\x04 \x03(\x01\x42\x02\x10\x01\x32K\n\x07Greeter\x12@\n\tCallModel\x12\x18.helloworld.DoubleMatrix\x1a\x17.helloworld.ModelResult\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)




_MODELRESULT = _descriptor.Descriptor(
  name='ModelResult',
  full_name='helloworld.ModelResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.ModelResult.message', index=0,
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
  serialized_start=32,
  serialized_end=62,
)


_DOUBLEMATRIX = _descriptor.Descriptor(
  name='DoubleMatrix',
  full_name='helloworld.DoubleMatrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='helloworld.DoubleMatrix.rows', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cols', full_name='helloworld.DoubleMatrix.cols', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='helloworld.DoubleMatrix.channels', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='helloworld.DoubleMatrix.data', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=64,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['ModelResult'] = _MODELRESULT
DESCRIPTOR.message_types_by_name['DoubleMatrix'] = _DOUBLEMATRIX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelResult = _reflection.GeneratedProtocolMessageType('ModelResult', (_message.Message,), {
  'DESCRIPTOR' : _MODELRESULT,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ModelResult)
  })
_sym_db.RegisterMessage(ModelResult)

DoubleMatrix = _reflection.GeneratedProtocolMessageType('DoubleMatrix', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEMATRIX,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.DoubleMatrix)
  })
_sym_db.RegisterMessage(DoubleMatrix)


DESCRIPTOR._options = None
_DOUBLEMATRIX.fields_by_name['data']._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=144,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='CallModel',
    full_name='helloworld.Greeter.CallModel',
    index=0,
    containing_service=None,
    input_type=_DOUBLEMATRIX,
    output_type=_MODELRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
