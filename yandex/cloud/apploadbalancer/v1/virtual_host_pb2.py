# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/apploadbalancer/v1/virtual_host.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from yandex.cloud.apploadbalancer.v1 import payload_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_payload__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/apploadbalancer/v1/virtual_host.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1egoogle/protobuf/duration.proto\x1a-yandex/cloud/apploadbalancer/v1/payload.proto\x1a\x1dyandex/cloud/validation.proto\"\xdd\x02\n\x0bVirtualHost\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tauthority\x18\x02 \x03(\t\x12\x36\n\x06routes\x18\x03 \x03(\x0b\x32&.yandex.cloud.apploadbalancer.v1.Route\x12S\n\x16modify_request_headers\x18\x04 \x03(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.HeaderModification\x12T\n\x17modify_response_headers\x18\x05 \x03(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.HeaderModification\x12\x44\n\rroute_options\x18\x06 \x01(\x0b\x32-.yandex.cloud.apploadbalancer.v1.RouteOptions\"\x8b\x02\n\x0cRouteOptions\x12S\n\x16modify_request_headers\x18\x01 \x03(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.HeaderModification\x12T\n\x17modify_response_headers\x18\x02 \x03(\x0b\x32\x33.yandex.cloud.apploadbalancer.v1.HeaderModification\x12\x33\n\x04rbac\x18\x03 \x01(\x0b\x32%.yandex.cloud.apploadbalancer.v1.RBAC\x12\x1b\n\x13security_profile_id\x18\x04 \x01(\t\"\xcb\x01\n\x04RBAC\x12\x42\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32,.yandex.cloud.apploadbalancer.v1.RBAC.ActionB\x04\xe8\xc7\x31\x01\x12H\n\nprincipals\x18\x02 \x03(\x0b\x32+.yandex.cloud.apploadbalancer.v1.PrincipalsB\x07\x82\xc8\x31\x03>=1\"5\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\t\n\x05\x41LLOW\x10\x01\x12\x08\n\x04\x44\x45NY\x10\x02\"Y\n\nPrincipals\x12K\n\x0e\x61nd_principals\x18\x01 \x03(\x0b\x32*.yandex.cloud.apploadbalancer.v1.PrincipalB\x07\x82\xc8\x31\x03>=1\"\xf1\x01\n\tPrincipal\x12J\n\x06header\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.apploadbalancer.v1.Principal.HeaderMatcherH\x00\x12\x13\n\tremote_ip\x18\x02 \x01(\tH\x00\x12\r\n\x03\x61ny\x18\x03 \x01(\x08H\x00\x1a`\n\rHeaderMatcher\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.yandex.cloud.apploadbalancer.v1.StringMatchB\x12\n\nidentifier\x12\x04\xc0\xc1\x31\x01\"x\n\x12HeaderModification\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x06\x61ppend\x18\x02 \x01(\tH\x00\x12\x11\n\x07replace\x18\x03 \x01(\tH\x00\x12\x10\n\x06remove\x18\x04 \x01(\x08H\x00\x12\x10\n\x06rename\x18\x05 \x01(\tH\x00\x42\x0b\n\toperation\"\xe8\x01\n\x05Route\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12:\n\x04http\x18\x02 \x01(\x0b\x32*.yandex.cloud.apploadbalancer.v1.HttpRouteH\x00\x12:\n\x04grpc\x18\x03 \x01(\x0b\x32*.yandex.cloud.apploadbalancer.v1.GrpcRouteH\x00\x12\x44\n\rroute_options\x18\x04 \x01(\x0b\x32-.yandex.cloud.apploadbalancer.v1.RouteOptionsB\r\n\x05route\x12\x04\xc0\xc1\x31\x01\"\xb5\x02\n\tHttpRoute\x12>\n\x05match\x18\x01 \x01(\x0b\x32/.yandex.cloud.apploadbalancer.v1.HttpRouteMatch\x12\x41\n\x05route\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.apploadbalancer.v1.HttpRouteActionH\x00\x12\x43\n\x08redirect\x18\x03 \x01(\x0b\x32/.yandex.cloud.apploadbalancer.v1.RedirectActionH\x00\x12P\n\x0f\x64irect_response\x18\x04 \x01(\x0b\x32\x35.yandex.cloud.apploadbalancer.v1.DirectResponseActionH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\"\xf4\x01\n\tGrpcRoute\x12>\n\x05match\x18\x01 \x01(\x0b\x32/.yandex.cloud.apploadbalancer.v1.GrpcRouteMatch\x12\x41\n\x05route\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.apploadbalancer.v1.GrpcRouteActionH\x00\x12T\n\x0fstatus_response\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.apploadbalancer.v1.GrpcStatusResponseActionH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\"a\n\x0eHttpRouteMatch\x12\x13\n\x0bhttp_method\x18\x01 \x03(\t\x12:\n\x04path\x18\x02 \x01(\x0b\x32,.yandex.cloud.apploadbalancer.v1.StringMatch\"L\n\x0eGrpcRouteMatch\x12:\n\x04\x66qmn\x18\x01 \x01(\x0b\x32,.yandex.cloud.apploadbalancer.v1.StringMatch\"b\n\x0bStringMatch\x12\x15\n\x0b\x65xact_match\x18\x01 \x01(\tH\x00\x12\x16\n\x0cprefix_match\x18\x02 \x01(\tH\x00\x12\x15\n\x0bregex_match\x18\x03 \x01(\tH\x00\x42\r\n\x05match\x12\x04\xc0\xc1\x31\x01\"\xfa\x02\n\x0eRedirectAction\x12\x16\n\x0ereplace_scheme\x18\x01 \x01(\t\x12\x14\n\x0creplace_host\x18\x02 \x01(\t\x12\x14\n\x0creplace_port\x18\x03 \x01(\x03\x12\x16\n\x0creplace_path\x18\x04 \x01(\tH\x00\x12\x18\n\x0ereplace_prefix\x18\x05 \x01(\tH\x00\x12\x14\n\x0cremove_query\x18\x06 \x01(\x08\x12[\n\rresponse_code\x18\x07 \x01(\x0e\x32\x44.yandex.cloud.apploadbalancer.v1.RedirectAction.RedirectResponseCode\"w\n\x14RedirectResponseCode\x12\x15\n\x11MOVED_PERMANENTLY\x10\x00\x12\t\n\x05\x46OUND\x10\x01\x12\r\n\tSEE_OTHER\x10\x02\x12\x16\n\x12TEMPORARY_REDIRECT\x10\x03\x12\x16\n\x12PERMANENT_REDIRECT\x10\x04\x42\x06\n\x04path\"k\n\x14\x44irectResponseAction\x12\x1b\n\x06status\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31\x30\x30-599\x12\x36\n\x04\x62ody\x18\x02 \x01(\x0b\x32(.yandex.cloud.apploadbalancer.v1.Payload\"\x82\x02\n\x18GrpcStatusResponseAction\x12P\n\x06status\x18\x01 \x01(\x0e\x32@.yandex.cloud.apploadbalancer.v1.GrpcStatusResponseAction.Status\"\x93\x01\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x14\n\x10INVALID_ARGUMENT\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\x12\x15\n\x11PERMISSION_DENIED\x10\x03\x12\x13\n\x0fUNAUTHENTICATED\x10\x04\x12\x11\n\rUNIMPLEMENTED\x10\x05\x12\x0c\n\x08INTERNAL\x10\x06\x12\x0f\n\x0bUNAVAILABLE\x10\x07\"\x8c\x02\n\x0fHttpRouteAction\x12\x1e\n\x10\x62\x61\x63kend_group_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12*\n\x07timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0cidle_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x16\n\x0chost_rewrite\x18\x04 \x01(\tH\x00\x12\x1b\n\x11\x61uto_host_rewrite\x18\x05 \x01(\x08H\x00\x12\x16\n\x0eprefix_rewrite\x18\x06 \x01(\t\x12\x15\n\rupgrade_types\x18\x07 \x03(\tB\x18\n\x16host_rewrite_specifier\"\xe1\x01\n\x0fGrpcRouteAction\x12\x1e\n\x10\x62\x61\x63kend_group_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12.\n\x0bmax_timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0cidle_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x16\n\x0chost_rewrite\x18\x04 \x01(\tH\x00\x12\x1b\n\x11\x61uto_host_rewrite\x18\x05 \x01(\x08H\x00\x42\x18\n\x16host_rewrite_specifierBz\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.apploadbalancer.v1.virtual_host_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _VIRTUALHOST.fields_by_name['name']._options = None
  _VIRTUALHOST.fields_by_name['name']._serialized_options = b'\350\3071\001'
  _RBAC.fields_by_name['action']._options = None
  _RBAC.fields_by_name['action']._serialized_options = b'\350\3071\001'
  _RBAC.fields_by_name['principals']._options = None
  _RBAC.fields_by_name['principals']._serialized_options = b'\202\3101\003>=1'
  _PRINCIPALS.fields_by_name['and_principals']._options = None
  _PRINCIPALS.fields_by_name['and_principals']._serialized_options = b'\202\3101\003>=1'
  _PRINCIPAL_HEADERMATCHER.fields_by_name['name']._options = None
  _PRINCIPAL_HEADERMATCHER.fields_by_name['name']._serialized_options = b'\350\3071\001'
  _PRINCIPAL.oneofs_by_name['identifier']._options = None
  _PRINCIPAL.oneofs_by_name['identifier']._serialized_options = b'\300\3011\001'
  _ROUTE.oneofs_by_name['route']._options = None
  _ROUTE.oneofs_by_name['route']._serialized_options = b'\300\3011\001'
  _ROUTE.fields_by_name['name']._options = None
  _ROUTE.fields_by_name['name']._serialized_options = b'\350\3071\001'
  _HTTPROUTE.oneofs_by_name['action']._options = None
  _HTTPROUTE.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _GRPCROUTE.oneofs_by_name['action']._options = None
  _GRPCROUTE.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _STRINGMATCH.oneofs_by_name['match']._options = None
  _STRINGMATCH.oneofs_by_name['match']._serialized_options = b'\300\3011\001'
  _DIRECTRESPONSEACTION.fields_by_name['status']._options = None
  _DIRECTRESPONSEACTION.fields_by_name['status']._serialized_options = b'\372\3071\007100-599'
  _HTTPROUTEACTION.fields_by_name['backend_group_id']._options = None
  _HTTPROUTEACTION.fields_by_name['backend_group_id']._serialized_options = b'\350\3071\001'
  _GRPCROUTEACTION.fields_by_name['backend_group_id']._options = None
  _GRPCROUTEACTION.fields_by_name['backend_group_id']._serialized_options = b'\350\3071\001'
  _globals['_VIRTUALHOST']._serialized_start=198
  _globals['_VIRTUALHOST']._serialized_end=547
  _globals['_ROUTEOPTIONS']._serialized_start=550
  _globals['_ROUTEOPTIONS']._serialized_end=817
  _globals['_RBAC']._serialized_start=820
  _globals['_RBAC']._serialized_end=1023
  _globals['_RBAC_ACTION']._serialized_start=970
  _globals['_RBAC_ACTION']._serialized_end=1023
  _globals['_PRINCIPALS']._serialized_start=1025
  _globals['_PRINCIPALS']._serialized_end=1114
  _globals['_PRINCIPAL']._serialized_start=1117
  _globals['_PRINCIPAL']._serialized_end=1358
  _globals['_PRINCIPAL_HEADERMATCHER']._serialized_start=1242
  _globals['_PRINCIPAL_HEADERMATCHER']._serialized_end=1338
  _globals['_HEADERMODIFICATION']._serialized_start=1360
  _globals['_HEADERMODIFICATION']._serialized_end=1480
  _globals['_ROUTE']._serialized_start=1483
  _globals['_ROUTE']._serialized_end=1715
  _globals['_HTTPROUTE']._serialized_start=1718
  _globals['_HTTPROUTE']._serialized_end=2027
  _globals['_GRPCROUTE']._serialized_start=2030
  _globals['_GRPCROUTE']._serialized_end=2274
  _globals['_HTTPROUTEMATCH']._serialized_start=2276
  _globals['_HTTPROUTEMATCH']._serialized_end=2373
  _globals['_GRPCROUTEMATCH']._serialized_start=2375
  _globals['_GRPCROUTEMATCH']._serialized_end=2451
  _globals['_STRINGMATCH']._serialized_start=2453
  _globals['_STRINGMATCH']._serialized_end=2551
  _globals['_REDIRECTACTION']._serialized_start=2554
  _globals['_REDIRECTACTION']._serialized_end=2932
  _globals['_REDIRECTACTION_REDIRECTRESPONSECODE']._serialized_start=2805
  _globals['_REDIRECTACTION_REDIRECTRESPONSECODE']._serialized_end=2924
  _globals['_DIRECTRESPONSEACTION']._serialized_start=2934
  _globals['_DIRECTRESPONSEACTION']._serialized_end=3041
  _globals['_GRPCSTATUSRESPONSEACTION']._serialized_start=3044
  _globals['_GRPCSTATUSRESPONSEACTION']._serialized_end=3302
  _globals['_GRPCSTATUSRESPONSEACTION_STATUS']._serialized_start=3155
  _globals['_GRPCSTATUSRESPONSEACTION_STATUS']._serialized_end=3302
  _globals['_HTTPROUTEACTION']._serialized_start=3305
  _globals['_HTTPROUTEACTION']._serialized_end=3573
  _globals['_GRPCROUTEACTION']._serialized_start=3576
  _globals['_GRPCROUTEACTION']._serialized_end=3801
# @@protoc_insertion_point(module_scope)
