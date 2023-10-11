# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\t\"6\n\x0b\x42ookingData\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x17\n\x04\x64\x61te\x18\x02 \x03(\x0b\x32\t.DateData\")\n\x08\x44\x61teData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07movieid\x18\x02 \x03(\t\"\x07\n\x05\x45mpty2\\\n\x07\x42ooking\x12$\n\nGetBooking\x12\x06.Empty\x1a\x0c.BookingData\"\x00\x12+\n\x10GetBookingByUser\x12\x07.UserId\x1a\x0c.BookingData\"\x00\x62\x06proto3')



_USERID = DESCRIPTOR.message_types_by_name['UserId']
_BOOKINGDATA = DESCRIPTOR.message_types_by_name['BookingData']
_DATEDATA = DESCRIPTOR.message_types_by_name['DateData']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
UserId = _reflection.GeneratedProtocolMessageType('UserId', (_message.Message,), {
  'DESCRIPTOR' : _USERID,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:UserId)
  })
_sym_db.RegisterMessage(UserId)

BookingData = _reflection.GeneratedProtocolMessageType('BookingData', (_message.Message,), {
  'DESCRIPTOR' : _BOOKINGDATA,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:BookingData)
  })
_sym_db.RegisterMessage(BookingData)

DateData = _reflection.GeneratedProtocolMessageType('DateData', (_message.Message,), {
  'DESCRIPTOR' : _DATEDATA,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:DateData)
  })
_sym_db.RegisterMessage(DateData)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_BOOKING = DESCRIPTOR.services_by_name['Booking']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERID._serialized_start=17
  _USERID._serialized_end=37
  _BOOKINGDATA._serialized_start=39
  _BOOKINGDATA._serialized_end=93
  _DATEDATA._serialized_start=95
  _DATEDATA._serialized_end=136
  _EMPTY._serialized_start=138
  _EMPTY._serialized_end=145
  _BOOKING._serialized_start=147
  _BOOKING._serialized_end=239
# @@protoc_insertion_point(module_scope)
