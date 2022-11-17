# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12game_service.proto\x12\x06protos\"\x18\n\x08New_game\x12\x0c\n\x04name\x18\x01 \x01(\x05\"-\n\x04Game\x12\x0c\n\x04stat\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\x05\"\x1f\n\x0fNew_game_status\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x16\n\x06Status\x12\x0c\n\x04stat\x18\x01 \x01(\x05\"\x94\x02\n\x11\x46orward_to_server\x12\x0f\n\x07gold_up\x18\x01 \x01(\x05\x12\x0f\n\x07tech_up\x18\x02 \x01(\x05\x12\x0c\n\x04gold\x18\x03 \x01(\x05\x12\x0c\n\x04tech\x18\x04 \x01(\x05\x12\x13\n\x0bup_foot_att\x18\x05 \x01(\x05\x12\x13\n\x0bup_foot_def\x18\x06 \x01(\x05\x12\x13\n\x0bup_arch_att\x18\x07 \x01(\x05\x12\x13\n\x0bup_arch_def\x18\x08 \x01(\x05\x12\x12\n\nup_cav_att\x18\t \x01(\x05\x12\x12\n\nup_cav_def\x18\n \x01(\x05\x12\x0c\n\x04\x66oot\x18\x0b \x01(\x05\x12\x0c\n\x04\x61rch\x18\x0c \x01(\x05\x12\x0b\n\x03\x63\x61v\x18\r \x01(\x05\x12\x0c\n\x04name\x18\x0e \x01(\t\x12\x0e\n\x06player\x18\x0f \x01(\x05\"\xc4\x02\n\x11\x46orward_to_player\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x05\x12\r\n\x05\x66ield\x18\x02 \x01(\x05\x12\x0b\n\x03war\x18\x03 \x01(\x08\x12\x0c\n\x04gold\x18\x04 \x01(\x05\x12\x0c\n\x04tech\x18\x05 \x01(\x05\x12\x14\n\x0c\x66oot_att_min\x18\x06 \x01(\x05\x12\x14\n\x0c\x66oot_att_max\x18\x07 \x01(\x05\x12\x12\n\nfoot_armor\x18\x08 \x01(\x05\x12\x14\n\x0c\x61rch_att_min\x18\t \x01(\x05\x12\x14\n\x0c\x61rch_att_max\x18\n \x01(\x05\x12\x12\n\narch_armor\x18\x0b \x01(\x05\x12\x13\n\x0b\x63\x61v_att_min\x18\x0c \x01(\x05\x12\x13\n\x0b\x63\x61v_att_max\x18\r \x01(\x05\x12\x11\n\tcav_armor\x18\x0e \x01(\x05\x12\x0e\n\x06winner\x18\x0f \x01(\x05\x12\r\n\x05\x65nemy\x18\x10 \x03(\x05\x12\x0e\n\x06player\x18\x11 \x03(\x05\"\'\n\x0bGame_status\x12\x0b\n\x03gid\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x61y\x18\x02 \x01(\x05\"-\n\x0eNext_Turn_Info\x12\x0b\n\x03gid\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\x05\x32\xd9\x02\n\x03TTT\x12\x31\n\x0fJoinMatchmaking\x12\x10.protos.New_game\x1a\x0c.protos.Game\x12<\n\x11Matchmaking_Ready\x12\x17.protos.New_game_status\x1a\x0e.protos.Status\x12\x35\n\x08\x45nd_Turn\x12\x19.protos.Forward_to_server\x1a\x0e.protos.Status\x12\x37\n\x10Next_Turn_Status\x12\x13.protos.Game_status\x1a\x0e.protos.Status\x12>\n\tNext_Turn\x12\x16.protos.Next_Turn_Info\x1a\x19.protos.Forward_to_player\x12\x31\n\x0fTest_Clear_Game\x12\x0e.protos.Status\x1a\x0e.protos.Statusb\x06proto3')



_NEW_GAME = DESCRIPTOR.message_types_by_name['New_game']
_GAME = DESCRIPTOR.message_types_by_name['Game']
_NEW_GAME_STATUS = DESCRIPTOR.message_types_by_name['New_game_status']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
_FORWARD_TO_SERVER = DESCRIPTOR.message_types_by_name['Forward_to_server']
_FORWARD_TO_PLAYER = DESCRIPTOR.message_types_by_name['Forward_to_player']
_GAME_STATUS = DESCRIPTOR.message_types_by_name['Game_status']
_NEXT_TURN_INFO = DESCRIPTOR.message_types_by_name['Next_Turn_Info']
New_game = _reflection.GeneratedProtocolMessageType('New_game', (_message.Message,), {
  'DESCRIPTOR' : _NEW_GAME,
  '__module__' : 'game_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.New_game)
  })
_sym_db.RegisterMessage(New_game)

Game = _reflection.GeneratedProtocolMessageType('Game', (_message.Message,), {
  'DESCRIPTOR' : _GAME,
  '__module__' : 'game_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.Game)
  })
_sym_db.RegisterMessage(Game)

New_game_status = _reflection.GeneratedProtocolMessageType('New_game_status', (_message.Message,), {
  'DESCRIPTOR' : _NEW_GAME_STATUS,
  '__module__' : 'game_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.New_game_status)
  })
_sym_db.RegisterMessage(New_game_status)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'game_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.Status)
  })
_sym_db.RegisterMessage(Status)

Forward_to_server = _reflection.GeneratedProtocolMessageType('Forward_to_server', (_message.Message,), {
  'DESCRIPTOR' : _FORWARD_TO_SERVER,
  '__module__' : 'game_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.Forward_to_server)
  })
_sym_db.RegisterMessage(Forward_to_server)

Forward_to_player = _reflection.GeneratedProtocolMessageType('Forward_to_player', (_message.Message,), {
  'DESCRIPTOR' : _FORWARD_TO_PLAYER,
  '__module__' : 'game_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.Forward_to_player)
  })
_sym_db.RegisterMessage(Forward_to_player)

Game_status = _reflection.GeneratedProtocolMessageType('Game_status', (_message.Message,), {
  'DESCRIPTOR' : _GAME_STATUS,
  '__module__' : 'game_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.Game_status)
  })
_sym_db.RegisterMessage(Game_status)

Next_Turn_Info = _reflection.GeneratedProtocolMessageType('Next_Turn_Info', (_message.Message,), {
  'DESCRIPTOR' : _NEXT_TURN_INFO,
  '__module__' : 'game_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.Next_Turn_Info)
  })
_sym_db.RegisterMessage(Next_Turn_Info)

_TTT = DESCRIPTOR.services_by_name['TTT']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEW_GAME._serialized_start=30
  _NEW_GAME._serialized_end=54
  _GAME._serialized_start=56
  _GAME._serialized_end=101
  _NEW_GAME_STATUS._serialized_start=103
  _NEW_GAME_STATUS._serialized_end=134
  _STATUS._serialized_start=136
  _STATUS._serialized_end=158
  _FORWARD_TO_SERVER._serialized_start=161
  _FORWARD_TO_SERVER._serialized_end=437
  _FORWARD_TO_PLAYER._serialized_start=440
  _FORWARD_TO_PLAYER._serialized_end=764
  _GAME_STATUS._serialized_start=766
  _GAME_STATUS._serialized_end=805
  _NEXT_TURN_INFO._serialized_start=807
  _NEXT_TURN_INFO._serialized_end=852
  _TTT._serialized_start=855
  _TTT._serialized_end=1200
# @@protoc_insertion_point(module_scope)
