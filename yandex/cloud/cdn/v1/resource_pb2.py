# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/cdn/v1/resource.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'yandex/cloud/cdn/v1/resource.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"yandex/cloud/cdn/v1/resource.proto\x12\x13yandex.cloud.cdn.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"$\n\x12SecondaryHostnames\x12\x0e\n\x06values\x18\x01 \x03(\t\"\x96\x04\n\x08Resource\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\r\n\x05\x63name\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x61\x63tive\x18\x06 \x01(\x08\x12\x35\n\x07options\x18\x07 \x01(\x0b\x32$.yandex.cloud.cdn.v1.ResourceOptions\x12\x1b\n\x13secondary_hostnames\x18\x08 \x03(\t\x12\x17\n\x0forigin_group_id\x18\t \x01(\x03\x12\x19\n\x11origin_group_name\x18\n \x01(\t\x12<\n\x0forigin_protocol\x18\x0b \x01(\x0e\x32#.yandex.cloud.cdn.v1.OriginProtocol\x12<\n\x0fssl_certificate\x18\x0c \x01(\x0b\x32#.yandex.cloud.cdn.v1.SSLCertificate\x12\x39\n\x06labels\x18\r \x03(\x0b\x32).yandex.cloud.cdn.v1.Resource.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe6\x1f\n\x0fResourceOptions\x12\x46\n\rdisable_cache\x18\x01 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOption\x12S\n\x13\x65\x64ge_cache_settings\x18\x02 \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.EdgeCacheSettings\x12P\n\x16\x62rowser_cache_settings\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.cdn.v1.ResourceOptions.Int64Option\x12R\n\x12\x63\x61\x63he_http_headers\x18\x04 \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.StringsListOption\x12U\n\x14query_params_options\x18\x05 \x01(\x0b\x32\x37.yandex.cloud.cdn.v1.ResourceOptions.QueryParamsOptions\x12>\n\x05slice\x18\x06 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOption\x12T\n\x13\x63ompression_options\x18\x07 \x01(\x0b\x32\x37.yandex.cloud.cdn.v1.ResourceOptions.CompressionOptions\x12N\n\x10redirect_options\x18\x08 \x01(\x0b\x32\x34.yandex.cloud.cdn.v1.ResourceOptions.RedirectOptions\x12\x46\n\x0chost_options\x18\t \x01(\x0b\x32\x30.yandex.cloud.cdn.v1.ResourceOptions.HostOptions\x12M\n\x0estatic_headers\x18\n \x01(\x0b\x32\x35.yandex.cloud.cdn.v1.ResourceOptions.StringsMapOption\x12\x44\n\x04\x63ors\x18\x0b \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.StringsListOption\x12\x45\n\x05stale\x18\x0c \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.StringsListOption\x12T\n\x14\x61llowed_http_methods\x18\r \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.StringsListOption\x12P\n\x17proxy_cache_methods_set\x18\x0e \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOption\x12S\n\x1a\x64isable_proxy_force_ranges\x18\x0f \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOption\x12U\n\x16static_request_headers\x18\x10 \x01(\x0b\x32\x35.yandex.cloud.cdn.v1.ResourceOptions.StringsMapOption\x12M\n\x12\x63ustom_server_name\x18\x11 \x01(\x0b\x32\x31.yandex.cloud.cdn.v1.ResourceOptions.StringOption\x12\x46\n\rignore_cookie\x18\x12 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOption\x12\x43\n\x07rewrite\x18\x13 \x01(\x0b\x32\x32.yandex.cloud.cdn.v1.ResourceOptions.RewriteOption\x12H\n\nsecure_key\x18\x14 \x01(\x0b\x32\x34.yandex.cloud.cdn.v1.ResourceOptions.SecureKeyOption\x12O\n\x0eip_address_acl\x18\x15 \x01(\x0b\x32\x37.yandex.cloud.cdn.v1.ResourceOptions.IPAddressACLOption\x1a,\n\nBoolOption\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x08\x1a.\n\x0cStringOption\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\t\x1a-\n\x0bInt64Option\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x03\x1a\x33\n\x11StringsListOption\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x03(\t\x1a\xa2\x01\n\x10StringsMapOption\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12O\n\x05value\x18\x02 \x03(\x0b\x32@.yandex.cloud.cdn.v1.ResourceOptions.StringsMapOption.ValueEntry\x1a,\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xb5\x01\n\x0c\x43\x61\x63hingTimes\x12\x14\n\x0csimple_value\x18\x01 \x01(\x03\x12Z\n\rcustom_values\x18\x02 \x03(\x0b\x32\x43.yandex.cloud.cdn.v1.ResourceOptions.CachingTimes.CustomValuesEntry\x1a\x33\n\x11\x43ustomValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x93\x01\n\x11\x45\x64geCacheSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32\x31.yandex.cloud.cdn.v1.ResourceOptions.CachingTimesH\x00\x12\x17\n\rdefault_value\x18\x03 \x01(\x03H\x00\x42\x10\n\x0evalues_variant\x1a\xa9\x03\n\x17StringVariableMapOption\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12V\n\x05value\x18\x02 \x03(\x0b\x32G.yandex.cloud.cdn.v1.ResourceOptions.StringVariableMapOption.ValueEntry\x1a\xac\x01\n\x0bOneofString\x12\x42\n\x05value\x18\x01 \x01(\x0b\x32\x31.yandex.cloud.cdn.v1.ResourceOptions.StringOptionH\x00\x12H\n\x06values\x18\x02 \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.StringsListOptionH\x00\x42\x0f\n\rstring_option\x1av\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12W\n\x05value\x18\x02 \x01(\x0b\x32H.yandex.cloud.cdn.v1.ResourceOptions.StringVariableMapOption.OneofString:\x02\x38\x01\x1a\xb0\x02\n\x12QueryParamsOptions\x12N\n\x13ignore_query_string\x18\x01 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOptionH\x00\x12X\n\x16query_params_whitelist\x18\x02 \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.StringsListOptionH\x00\x12X\n\x16query_params_blacklist\x18\x03 \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.StringsListOptionH\x00\x42\x16\n\x14query_params_variant\x1a\xcb\x01\n\x0fRedirectOptions\x12Q\n\x16redirect_http_to_https\x18\x01 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOptionH\x00\x12Q\n\x16redirect_https_to_http\x18\x02 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOptionH\x00\x42\x12\n\x10redirect_variant\x1a\xb0\x01\n\x0bHostOptions\x12\x41\n\x04host\x18\x01 \x01(\x0b\x32\x31.yandex.cloud.cdn.v1.ResourceOptions.StringOptionH\x00\x12N\n\x13\x66orward_host_header\x18\x02 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOptionH\x00\x42\x0e\n\x0chost_variant\x1a\x92\x02\n\x12\x43ompressionOptions\x12K\n\x10\x66\x65tch_compressed\x18\x01 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOptionH\x00\x12\x42\n\x07gzip_on\x18\x02 \x01(\x0b\x32/.yandex.cloud.cdn.v1.ResourceOptions.BoolOptionH\x00\x12T\n\x12\x62rotli_compression\x18\x03 \x01(\x0b\x32\x36.yandex.cloud.cdn.v1.ResourceOptions.StringsListOptionH\x00\x42\x15\n\x13\x63ompression_variant\x1a^\n\rRewriteOption\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12.\n\x04\x66lag\x18\x03 \x01(\x0e\x32 .yandex.cloud.cdn.v1.RewriteFlag\x1a\x64\n\x0fSecureKeyOption\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x33\n\x04type\x18\x03 \x01(\x0e\x32%.yandex.cloud.cdn.v1.SecureKeyURLType\x1at\n\x12IPAddressACLOption\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x34\n\x0bpolicy_type\x18\x02 \x01(\x0e\x32\x1f.yandex.cloud.cdn.v1.PolicyType\x12\x17\n\x0f\x65xcepted_values\x18\x03 \x03(\t\"\x84\x01\n\x14SSLTargetCertificate\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.yandex.cloud.cdn.v1.SSLCertificateType\x12\x35\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\'.yandex.cloud.cdn.v1.SSLCertificateData\"\xb9\x01\n\x0eSSLCertificate\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.yandex.cloud.cdn.v1.SSLCertificateType\x12\x39\n\x06status\x18\x02 \x01(\x0e\x32).yandex.cloud.cdn.v1.SSLCertificateStatus\x12\x35\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\'.yandex.cloud.cdn.v1.SSLCertificateData\"m\n\x12SSLCertificateData\x12\x37\n\x02\x63m\x18\x01 \x01(\x0b\x32).yandex.cloud.cdn.v1.SSLCertificateCMDataH\x00\x42\x1e\n\x1cssl_certificate_data_variant\"\"\n\x14SSLCertificateCMData\x12\n\n\x02id\x18\x01 \x01(\t*Q\n\x0eOriginProtocol\x12\x1f\n\x1bORIGIN_PROTOCOL_UNSPECIFIED\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTPS\x10\x02\x12\t\n\x05MATCH\x10\x03*]\n\x0bRewriteFlag\x12\x1c\n\x18REWRITE_FLAG_UNSPECIFIED\x10\x00\x12\x08\n\x04LAST\x10\x01\x12\t\n\x05\x42REAK\x10\x02\x12\x0c\n\x08REDIRECT\x10\x03\x12\r\n\tPERMANENT\x10\x04*f\n\x10SecureKeyURLType\x12#\n\x1fSECURE_KEY_URL_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x45NABLE_IP_SIGNING\x10\x01\x12\x16\n\x12\x44ISABLE_IP_SIGNING\x10\x02*V\n\nPolicyType\x12\x1b\n\x17POLICY_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11POLICY_TYPE_ALLOW\x10\x01\x12\x14\n\x10POLICY_TYPE_DENY\x10\x02*l\n\x12SSLCertificateType\x12$\n SSL_CERTIFICATE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44ONT_USE\x10\x01\x12\x1a\n\x12LETS_ENCRYPT_GCORE\x10\x02\x1a\x02\x08\x01\x12\x06\n\x02\x43M\x10\x03*[\n\x14SSLCertificateStatus\x12&\n\"SSL_CERTIFICATE_STATUS_UNSPECIFIED\x10\x00\x12\t\n\x05READY\x10\x01\x12\x10\n\x08\x43REATING\x10\x02\x1a\x02\x08\x01\x42V\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cdn.v1.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _globals['_SSLCERTIFICATETYPE'].values_by_name["LETS_ENCRYPT_GCORE"]._loaded_options = None
  _globals['_SSLCERTIFICATETYPE'].values_by_name["LETS_ENCRYPT_GCORE"]._serialized_options = b'\010\001'
  _globals['_SSLCERTIFICATESTATUS'].values_by_name["CREATING"]._loaded_options = None
  _globals['_SSLCERTIFICATESTATUS'].values_by_name["CREATING"]._serialized_options = b'\010\001'
  _globals['_RESOURCE_LABELSENTRY']._loaded_options = None
  _globals['_RESOURCE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_RESOURCEOPTIONS_STRINGSMAPOPTION_VALUEENTRY']._loaded_options = None
  _globals['_RESOURCEOPTIONS_STRINGSMAPOPTION_VALUEENTRY']._serialized_options = b'8\001'
  _globals['_RESOURCEOPTIONS_CACHINGTIMES_CUSTOMVALUESENTRY']._loaded_options = None
  _globals['_RESOURCEOPTIONS_CACHINGTIMES_CUSTOMVALUESENTRY']._serialized_options = b'8\001'
  _globals['_RESOURCEOPTIONS_STRINGVARIABLEMAPOPTION_VALUEENTRY']._loaded_options = None
  _globals['_RESOURCEOPTIONS_STRINGVARIABLEMAPOPTION_VALUEENTRY']._serialized_options = b'8\001'
  _globals['_ORIGINPROTOCOL']._serialized_start=5210
  _globals['_ORIGINPROTOCOL']._serialized_end=5291
  _globals['_REWRITEFLAG']._serialized_start=5293
  _globals['_REWRITEFLAG']._serialized_end=5386
  _globals['_SECUREKEYURLTYPE']._serialized_start=5388
  _globals['_SECUREKEYURLTYPE']._serialized_end=5490
  _globals['_POLICYTYPE']._serialized_start=5492
  _globals['_POLICYTYPE']._serialized_end=5578
  _globals['_SSLCERTIFICATETYPE']._serialized_start=5580
  _globals['_SSLCERTIFICATETYPE']._serialized_end=5688
  _globals['_SSLCERTIFICATESTATUS']._serialized_start=5690
  _globals['_SSLCERTIFICATESTATUS']._serialized_end=5781
  _globals['_SECONDARYHOSTNAMES']._serialized_start=92
  _globals['_SECONDARYHOSTNAMES']._serialized_end=128
  _globals['_RESOURCE']._serialized_start=131
  _globals['_RESOURCE']._serialized_end=665
  _globals['_RESOURCE_LABELSENTRY']._serialized_start=620
  _globals['_RESOURCE_LABELSENTRY']._serialized_end=665
  _globals['_RESOURCEOPTIONS']._serialized_start=668
  _globals['_RESOURCEOPTIONS']._serialized_end=4738
  _globals['_RESOURCEOPTIONS_BOOLOPTION']._serialized_start=2334
  _globals['_RESOURCEOPTIONS_BOOLOPTION']._serialized_end=2378
  _globals['_RESOURCEOPTIONS_STRINGOPTION']._serialized_start=2380
  _globals['_RESOURCEOPTIONS_STRINGOPTION']._serialized_end=2426
  _globals['_RESOURCEOPTIONS_INT64OPTION']._serialized_start=2428
  _globals['_RESOURCEOPTIONS_INT64OPTION']._serialized_end=2473
  _globals['_RESOURCEOPTIONS_STRINGSLISTOPTION']._serialized_start=2475
  _globals['_RESOURCEOPTIONS_STRINGSLISTOPTION']._serialized_end=2526
  _globals['_RESOURCEOPTIONS_STRINGSMAPOPTION']._serialized_start=2529
  _globals['_RESOURCEOPTIONS_STRINGSMAPOPTION']._serialized_end=2691
  _globals['_RESOURCEOPTIONS_STRINGSMAPOPTION_VALUEENTRY']._serialized_start=2647
  _globals['_RESOURCEOPTIONS_STRINGSMAPOPTION_VALUEENTRY']._serialized_end=2691
  _globals['_RESOURCEOPTIONS_CACHINGTIMES']._serialized_start=2694
  _globals['_RESOURCEOPTIONS_CACHINGTIMES']._serialized_end=2875
  _globals['_RESOURCEOPTIONS_CACHINGTIMES_CUSTOMVALUESENTRY']._serialized_start=2824
  _globals['_RESOURCEOPTIONS_CACHINGTIMES_CUSTOMVALUESENTRY']._serialized_end=2875
  _globals['_RESOURCEOPTIONS_EDGECACHESETTINGS']._serialized_start=2878
  _globals['_RESOURCEOPTIONS_EDGECACHESETTINGS']._serialized_end=3025
  _globals['_RESOURCEOPTIONS_STRINGVARIABLEMAPOPTION']._serialized_start=3028
  _globals['_RESOURCEOPTIONS_STRINGVARIABLEMAPOPTION']._serialized_end=3453
  _globals['_RESOURCEOPTIONS_STRINGVARIABLEMAPOPTION_ONEOFSTRING']._serialized_start=3161
  _globals['_RESOURCEOPTIONS_STRINGVARIABLEMAPOPTION_ONEOFSTRING']._serialized_end=3333
  _globals['_RESOURCEOPTIONS_STRINGVARIABLEMAPOPTION_VALUEENTRY']._serialized_start=3335
  _globals['_RESOURCEOPTIONS_STRINGVARIABLEMAPOPTION_VALUEENTRY']._serialized_end=3453
  _globals['_RESOURCEOPTIONS_QUERYPARAMSOPTIONS']._serialized_start=3456
  _globals['_RESOURCEOPTIONS_QUERYPARAMSOPTIONS']._serialized_end=3760
  _globals['_RESOURCEOPTIONS_REDIRECTOPTIONS']._serialized_start=3763
  _globals['_RESOURCEOPTIONS_REDIRECTOPTIONS']._serialized_end=3966
  _globals['_RESOURCEOPTIONS_HOSTOPTIONS']._serialized_start=3969
  _globals['_RESOURCEOPTIONS_HOSTOPTIONS']._serialized_end=4145
  _globals['_RESOURCEOPTIONS_COMPRESSIONOPTIONS']._serialized_start=4148
  _globals['_RESOURCEOPTIONS_COMPRESSIONOPTIONS']._serialized_end=4422
  _globals['_RESOURCEOPTIONS_REWRITEOPTION']._serialized_start=4424
  _globals['_RESOURCEOPTIONS_REWRITEOPTION']._serialized_end=4518
  _globals['_RESOURCEOPTIONS_SECUREKEYOPTION']._serialized_start=4520
  _globals['_RESOURCEOPTIONS_SECUREKEYOPTION']._serialized_end=4620
  _globals['_RESOURCEOPTIONS_IPADDRESSACLOPTION']._serialized_start=4622
  _globals['_RESOURCEOPTIONS_IPADDRESSACLOPTION']._serialized_end=4738
  _globals['_SSLTARGETCERTIFICATE']._serialized_start=4741
  _globals['_SSLTARGETCERTIFICATE']._serialized_end=4873
  _globals['_SSLCERTIFICATE']._serialized_start=4876
  _globals['_SSLCERTIFICATE']._serialized_end=5061
  _globals['_SSLCERTIFICATEDATA']._serialized_start=5063
  _globals['_SSLCERTIFICATEDATA']._serialized_end=5172
  _globals['_SSLCERTIFICATECMDATA']._serialized_start=5174
  _globals['_SSLCERTIFICATECMDATA']._serialized_end=5208
# @@protoc_insertion_point(module_scope)
