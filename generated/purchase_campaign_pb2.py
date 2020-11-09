# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: purchase_campaign.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
import generated.anfrage_pb2 as anfrage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='purchase_campaign.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17purchase_campaign.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\ranfrage.proto\"u\n\x11SupplierToRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12)\n\x08\x63ontacts\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"4\n\x10\x43\x61mpaignSchedule\x12\x10\n\x08start_at\x18\x01 \x01(\t\x12\x0e\n\x06\x65nd_at\x18\x02 \x01(\t\"8\n\rCampaignState\x12\'\n\x06states\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xae\x01\n\x18PurchaseCampaignVerified\x12\n\n\x02id\x18\x01 \x01(\x03\x12 \n\x07\x61nfrage\x18\x02 \x01(\x0b\x32\x0f.pce.bo.Anfrage\x12\x30\n\x14suppliers_to_request\x18\x03 \x03(\x0b\x32\x12.SupplierToRequest\x12#\n\x08schedule\x18\x04 \x01(\x0b\x32\x11.CampaignSchedule\x12\r\n\x05state\x18\x05 \x01(\x03\"n\n\x1aPurchaseCampaingUnverified\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x11\x66ree_text_anfrage\x18\x02 \x01(\t\x12)\n\x08metadata\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\"\r\n\x0bVoidRequest2\xa8\x01\n\x10PurchaseCampaing\x12Q\n\x17\x43reatePurchaseCampanies\x12\x19.PurchaseCampaignVerified\x1a\x19.PurchaseCampaignVerified\"\x00\x12\x41\n\x14GetPurchaseCampanies\x12\x0c.VoidRequest\x1a\x19.PurchaseCampaignVerified\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,anfrage__pb2.DESCRIPTOR,])




_SUPPLIERTOREQUEST = _descriptor.Descriptor(
  name='SupplierToRequest',
  full_name='SupplierToRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SupplierToRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contacts', full_name='SupplierToRequest.contacts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='SupplierToRequest.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=72,
  serialized_end=189,
)


_CAMPAIGNSCHEDULE = _descriptor.Descriptor(
  name='CampaignSchedule',
  full_name='CampaignSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_at', full_name='CampaignSchedule.start_at', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_at', full_name='CampaignSchedule.end_at', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=191,
  serialized_end=243,
)


_CAMPAIGNSTATE = _descriptor.Descriptor(
  name='CampaignState',
  full_name='CampaignState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='states', full_name='CampaignState.states', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=245,
  serialized_end=301,
)


_PURCHASECAMPAIGNVERIFIED = _descriptor.Descriptor(
  name='PurchaseCampaignVerified',
  full_name='PurchaseCampaignVerified',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PurchaseCampaignVerified.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anfrage', full_name='PurchaseCampaignVerified.anfrage', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='suppliers_to_request', full_name='PurchaseCampaignVerified.suppliers_to_request', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='PurchaseCampaignVerified.schedule', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='PurchaseCampaignVerified.state', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=304,
  serialized_end=478,
)


_PURCHASECAMPAINGUNVERIFIED = _descriptor.Descriptor(
  name='PurchaseCampaingUnverified',
  full_name='PurchaseCampaingUnverified',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PurchaseCampaingUnverified.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='free_text_anfrage', full_name='PurchaseCampaingUnverified.free_text_anfrage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='PurchaseCampaingUnverified.metadata', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=480,
  serialized_end=590,
)


_VOIDREQUEST = _descriptor.Descriptor(
  name='VoidRequest',
  full_name='VoidRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=592,
  serialized_end=605,
)

_SUPPLIERTOREQUEST.fields_by_name['contacts'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SUPPLIERTOREQUEST.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CAMPAIGNSTATE.fields_by_name['states'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_PURCHASECAMPAIGNVERIFIED.fields_by_name['anfrage'].message_type = anfrage__pb2._ANFRAGE
_PURCHASECAMPAIGNVERIFIED.fields_by_name['suppliers_to_request'].message_type = _SUPPLIERTOREQUEST
_PURCHASECAMPAIGNVERIFIED.fields_by_name['schedule'].message_type = _CAMPAIGNSCHEDULE
_PURCHASECAMPAINGUNVERIFIED.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['SupplierToRequest'] = _SUPPLIERTOREQUEST
DESCRIPTOR.message_types_by_name['CampaignSchedule'] = _CAMPAIGNSCHEDULE
DESCRIPTOR.message_types_by_name['CampaignState'] = _CAMPAIGNSTATE
DESCRIPTOR.message_types_by_name['PurchaseCampaignVerified'] = _PURCHASECAMPAIGNVERIFIED
DESCRIPTOR.message_types_by_name['PurchaseCampaingUnverified'] = _PURCHASECAMPAINGUNVERIFIED
DESCRIPTOR.message_types_by_name['VoidRequest'] = _VOIDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SupplierToRequest = _reflection.GeneratedProtocolMessageType('SupplierToRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUPPLIERTOREQUEST,
  '__module__' : 'purchase_campaign_pb2'
  # @@protoc_insertion_point(class_scope:SupplierToRequest)
  })
_sym_db.RegisterMessage(SupplierToRequest)

CampaignSchedule = _reflection.GeneratedProtocolMessageType('CampaignSchedule', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNSCHEDULE,
  '__module__' : 'purchase_campaign_pb2'
  # @@protoc_insertion_point(class_scope:CampaignSchedule)
  })
_sym_db.RegisterMessage(CampaignSchedule)

CampaignState = _reflection.GeneratedProtocolMessageType('CampaignState', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNSTATE,
  '__module__' : 'purchase_campaign_pb2'
  # @@protoc_insertion_point(class_scope:CampaignState)
  })
_sym_db.RegisterMessage(CampaignState)

PurchaseCampaignVerified = _reflection.GeneratedProtocolMessageType('PurchaseCampaignVerified', (_message.Message,), {
  'DESCRIPTOR' : _PURCHASECAMPAIGNVERIFIED,
  '__module__' : 'purchase_campaign_pb2'
  # @@protoc_insertion_point(class_scope:PurchaseCampaignVerified)
  })
_sym_db.RegisterMessage(PurchaseCampaignVerified)

PurchaseCampaingUnverified = _reflection.GeneratedProtocolMessageType('PurchaseCampaingUnverified', (_message.Message,), {
  'DESCRIPTOR' : _PURCHASECAMPAINGUNVERIFIED,
  '__module__' : 'purchase_campaign_pb2'
  # @@protoc_insertion_point(class_scope:PurchaseCampaingUnverified)
  })
_sym_db.RegisterMessage(PurchaseCampaingUnverified)

VoidRequest = _reflection.GeneratedProtocolMessageType('VoidRequest', (_message.Message,), {
  'DESCRIPTOR' : _VOIDREQUEST,
  '__module__' : 'purchase_campaign_pb2'
  # @@protoc_insertion_point(class_scope:VoidRequest)
  })
_sym_db.RegisterMessage(VoidRequest)



_PURCHASECAMPAING = _descriptor.ServiceDescriptor(
  name='PurchaseCampaing',
  full_name='PurchaseCampaing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=608,
  serialized_end=776,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreatePurchaseCampanies',
    full_name='PurchaseCampaing.CreatePurchaseCampanies',
    index=0,
    containing_service=None,
    input_type=_PURCHASECAMPAIGNVERIFIED,
    output_type=_PURCHASECAMPAIGNVERIFIED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPurchaseCampanies',
    full_name='PurchaseCampaing.GetPurchaseCampanies',
    index=1,
    containing_service=None,
    input_type=_VOIDREQUEST,
    output_type=_PURCHASECAMPAIGNVERIFIED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PURCHASECAMPAING)

DESCRIPTOR.services_by_name['PurchaseCampaing'] = _PURCHASECAMPAING

# @@protoc_insertion_point(module_scope)
