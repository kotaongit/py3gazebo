# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: friction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import vector3d_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='friction.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\x0e\x66riction.proto\x12\x0bgazebo.msgs\x1a\x0evector3d.proto\"\xcd\x02\n\x08\x46riction\x12\n\n\x02mu\x18\x01 \x01(\x01\x12\x0b\n\x03mu2\x18\x02 \x01(\x01\x12$\n\x05\x66\x64ir1\x18\x03 \x01(\x0b\x32\x15.gazebo.msgs.Vector3d\x12\r\n\x05slip1\x18\x04 \x01(\x01\x12\r\n\x05slip2\x18\x05 \x01(\x01\x12\x32\n\ttorsional\x18\x06 \x01(\x0b\x32\x1f.gazebo.msgs.Friction.Torsional\x1a\xaf\x01\n\tTorsional\x12\x13\n\x0b\x63oefficient\x18\x01 \x01(\x01\x12\x18\n\x10use_patch_radius\x18\x02 \x01(\x08\x12\x14\n\x0cpatch_radius\x18\x03 \x01(\x01\x12\x16\n\x0esurface_radius\x18\x04 \x01(\x01\x12\x30\n\x03ode\x18\x05 \x01(\x0b\x32#.gazebo.msgs.Friction.Torsional.ODE\x1a\x13\n\x03ODE\x12\x0c\n\x04slip\x18\x01 \x01(\x01')
  ,
  dependencies=[vector3d_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FRICTION_TORSIONAL_ODE = _descriptor.Descriptor(
  name='ODE',
  full_name='gazebo.msgs.Friction.Torsional.ODE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slip', full_name='gazebo.msgs.Friction.Torsional.ODE.slip', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=381,
)

_FRICTION_TORSIONAL = _descriptor.Descriptor(
  name='Torsional',
  full_name='gazebo.msgs.Friction.Torsional',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coefficient', full_name='gazebo.msgs.Friction.Torsional.coefficient', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_patch_radius', full_name='gazebo.msgs.Friction.Torsional.use_patch_radius', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patch_radius', full_name='gazebo.msgs.Friction.Torsional.patch_radius', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surface_radius', full_name='gazebo.msgs.Friction.Torsional.surface_radius', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ode', full_name='gazebo.msgs.Friction.Torsional.ode', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FRICTION_TORSIONAL_ODE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=381,
)

_FRICTION = _descriptor.Descriptor(
  name='Friction',
  full_name='gazebo.msgs.Friction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mu', full_name='gazebo.msgs.Friction.mu', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mu2', full_name='gazebo.msgs.Friction.mu2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fdir1', full_name='gazebo.msgs.Friction.fdir1', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slip1', full_name='gazebo.msgs.Friction.slip1', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slip2', full_name='gazebo.msgs.Friction.slip2', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='torsional', full_name='gazebo.msgs.Friction.torsional', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FRICTION_TORSIONAL, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=381,
)

_FRICTION_TORSIONAL_ODE.containing_type = _FRICTION_TORSIONAL
_FRICTION_TORSIONAL.fields_by_name['ode'].message_type = _FRICTION_TORSIONAL_ODE
_FRICTION_TORSIONAL.containing_type = _FRICTION
_FRICTION.fields_by_name['fdir1'].message_type = vector3d_pb2._VECTOR3D
_FRICTION.fields_by_name['torsional'].message_type = _FRICTION_TORSIONAL
DESCRIPTOR.message_types_by_name['Friction'] = _FRICTION

Friction = _reflection.GeneratedProtocolMessageType('Friction', (_message.Message,), dict(

  Torsional = _reflection.GeneratedProtocolMessageType('Torsional', (_message.Message,), dict(

    ODE = _reflection.GeneratedProtocolMessageType('ODE', (_message.Message,), dict(
      DESCRIPTOR = _FRICTION_TORSIONAL_ODE,
      __module__ = 'friction_pb2'
      # @@protoc_insertion_point(class_scope:gazebo.msgs.Friction.Torsional.ODE)
      ))
    ,
    DESCRIPTOR = _FRICTION_TORSIONAL,
    __module__ = 'friction_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.Friction.Torsional)
    ))
  ,
  DESCRIPTOR = _FRICTION,
  __module__ = 'friction_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Friction)
  ))
_sym_db.RegisterMessage(Friction)
_sym_db.RegisterMessage(Friction.Torsional)
_sym_db.RegisterMessage(Friction.Torsional.ODE)


# @@protoc_insertion_point(module_scope)
