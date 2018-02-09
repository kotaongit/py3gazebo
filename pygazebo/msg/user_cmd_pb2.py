# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_cmd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import light_pb2
from . import model_pb2
from . import world_control_pb2
from . import wrench_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_cmd.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\x0euser_cmd.proto\x12\x0bgazebo.msgs\x1a\x0blight.proto\x1a\x0bmodel.proto\x1a\x13world_control.proto\x1a\x0cwrench.proto\"\xc5\x02\n\x07UserCmd\x12\n\n\x02id\x18\x01 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x02 \x02(\t\x12\'\n\x04type\x18\x03 \x02(\x0e\x32\x19.gazebo.msgs.UserCmd.Type\x12!\n\x05model\x18\x04 \x03(\x0b\x32\x12.gazebo.msgs.Model\x12!\n\x05light\x18\x05 \x03(\x0b\x32\x12.gazebo.msgs.Light\x12\x13\n\x0b\x65ntity_name\x18\x06 \x01(\t\x12\x30\n\rworld_control\x18\x07 \x01(\x0b\x32\x19.gazebo.msgs.WorldControl\x12#\n\x06wrench\x18\x08 \x01(\x0b\x32\x13.gazebo.msgs.Wrench\">\n\x04Type\x12\n\n\x06MOVING\x10\x01\x12\x11\n\rWORLD_CONTROL\x10\x02\x12\n\n\x06WRENCH\x10\x03\x12\x0b\n\x07SCALING\x10\x04')
  ,
  dependencies=[light_pb2.DESCRIPTOR,model_pb2.DESCRIPTOR,world_control_pb2.DESCRIPTOR,wrench_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_USERCMD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='gazebo.msgs.UserCmd.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOVING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORLD_CONTROL', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRENCH', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCALING', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=356,
  serialized_end=418,
)
_sym_db.RegisterEnumDescriptor(_USERCMD_TYPE)


_USERCMD = _descriptor.Descriptor(
  name='UserCmd',
  full_name='gazebo.msgs.UserCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.UserCmd.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='gazebo.msgs.UserCmd.description', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='gazebo.msgs.UserCmd.type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='gazebo.msgs.UserCmd.model', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='light', full_name='gazebo.msgs.UserCmd.light', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entity_name', full_name='gazebo.msgs.UserCmd.entity_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world_control', full_name='gazebo.msgs.UserCmd.world_control', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wrench', full_name='gazebo.msgs.UserCmd.wrench', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERCMD_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=418,
)

_USERCMD.fields_by_name['type'].enum_type = _USERCMD_TYPE
_USERCMD.fields_by_name['model'].message_type = model_pb2._MODEL
_USERCMD.fields_by_name['light'].message_type = light_pb2._LIGHT
_USERCMD.fields_by_name['world_control'].message_type = world_control_pb2._WORLDCONTROL
_USERCMD.fields_by_name['wrench'].message_type = wrench_pb2._WRENCH
_USERCMD_TYPE.containing_type = _USERCMD
DESCRIPTOR.message_types_by_name['UserCmd'] = _USERCMD

UserCmd = _reflection.GeneratedProtocolMessageType('UserCmd', (_message.Message,), dict(
  DESCRIPTOR = _USERCMD,
  __module__ = 'user_cmd_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.UserCmd)
  ))
_sym_db.RegisterMessage(UserCmd)


# @@protoc_insertion_point(module_scope)
