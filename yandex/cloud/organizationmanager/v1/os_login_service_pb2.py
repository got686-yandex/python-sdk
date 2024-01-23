# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/os_login_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/organizationmanager/v1/os_login_service.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"B\n\x19GetOsLoginSettingsRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xc8\x01\n\x0fOsLoginSettings\x12V\n\x15user_ssh_key_settings\x18\x01 \x01(\x0b\x32\x37.yandex.cloud.organizationmanager.v1.UserSshKeySettings\x12]\n\x18ssh_certificate_settings\x18\x02 \x01(\x0b\x32;.yandex.cloud.organizationmanager.v1.SshCertificateSettings\"D\n\x12UserSshKeySettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1d\n\x15\x61llow_manage_own_keys\x18\x02 \x01(\x08\")\n\x16SshCertificateSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"\xd8\x03\n\x1cUpdateOsLoginSettingsRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12s\n\x15user_ssh_key_settings\x18\x02 \x01(\x0b\x32T.yandex.cloud.organizationmanager.v1.UpdateOsLoginSettingsRequest.UserSshKeySettings\x12z\n\x18ssh_certificate_settings\x18\x03 \x01(\x0b\x32X.yandex.cloud.organizationmanager.v1.UpdateOsLoginSettingsRequest.SshCertificateSettings\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x1a\x44\n\x12UserSshKeySettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1d\n\x15\x61llow_manage_own_keys\x18\x02 \x01(\x08\x1a)\n\x16SshCertificateSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"L\n\x1fSetDefaultOsLoginProfileRequest\x12)\n\x13os_login_profile_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"E\n\x18GetOsLoginProfileRequest\x12)\n\x13os_login_profile_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x9e\x01\n\x1aListOsLoginProfilesRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"}\n\x1bListOsLoginProfilesResponse\x12\x45\n\x08profiles\x18\x01 \x03(\x0b\x32\x33.yandex.cloud.organizationmanager.v1.OsLoginProfile\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa0\x01\n\x0eOsLoginProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\x12\x12\n\nsubject_id\x18\x03 \x01(\t\x12\r\n\x05login\x18\x04 \x01(\t\x12\x0b\n\x03uid\x18\x05 \x01(\x03\x12\x12\n\nis_default\x18\x06 \x01(\x08\x12\x16\n\x0ehome_directory\x18\x07 \x01(\t\x12\r\n\x05shell\x18\x08 \x01(\t\"\x8c\x02\n\x1bUpdateOsLoginProfileRequest\x12)\n\x13os_login_profile_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x05login\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r^[^.]*?[^~.]$\x8a\xc8\x31\x04<=32\x12&\n\x03uid\x18\x03 \x01(\x03\x42\x19\xfa\xc7\x31\x15\x31-9223372036854775807\x12!\n\x0ehome_directory\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=255\x12\x18\n\x05shell\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=255\x12/\n\x0bupdate_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"7\n\x1b\x44\x65leteOsLoginProfileRequest\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xf5\x01\n\x1b\x43reateOsLoginProfileRequest\x12%\n\x0forganization_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\nsubject_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12,\n\x05login\x18\x03 \x01(\tB\x1d\xe8\xc7\x31\x01\xf2\xc7\x31\r^[^.]*?[^~.]$\x8a\xc8\x31\x04<=32\x12&\n\x03uid\x18\x04 \x01(\x03\x42\x19\xfa\xc7\x31\x15\x31-9223372036854775807\x12!\n\x0ehome_directory\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=255\x12\x18\n\x05shell\x18\x06 \x01(\tB\t\x8a\xc8\x31\x05<=255\";\n\x1cUpdateOsLoginProfileMetadata\x12\x1b\n\x13os_login_profile_id\x18\x01 \x01(\t\";\n\x1c\x44\x65leteOsLoginProfileMetadata\x12\x1b\n\x13os_login_profile_id\x18\x01 \x01(\t\"h\n\x1c\x43reateOsLoginProfileMetadata\x12\x1b\n\x13os_login_profile_id\x18\x01 \x01(\t\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\x12\x12\n\nsubject_id\x18\x03 \x01(\t\"8\n\x1dUpdateOsLoginSettingsMetadata\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\"k\n SetDefaultOsLoginProfileMetadata\x12#\n\x1bprevious_default_profile_id\x18\x01 \x01(\t\x12\"\n\x1a\x63urrent_default_profile_id\x18\x02 \x01(\t2\xc1\x0e\n\x0eOsLoginService\x12\xd5\x01\n\x0bGetSettings\x12>.yandex.cloud.organizationmanager.v1.GetOsLoginSettingsRequest\x1a\x34.yandex.cloud.organizationmanager.v1.OsLoginSettings\"P\x82\xd3\xe4\x93\x02J\x12H/organization-manager/v1/organizations/{organization_id}/osLoginSettings\x12\x80\x02\n\x0eUpdateSettings\x12\x41.yandex.cloud.organizationmanager.v1.UpdateOsLoginSettingsRequest\x1a!.yandex.cloud.operation.Operation\"\x87\x01\xb2\xd2*0\n\x1dUpdateOsLoginSettingsMetadata\x12\x0fOsLoginSettings\x82\xd3\xe4\x93\x02M2H/organization-manager/v1/organizations/{organization_id}/osLoginSettings:\x01*\x12\xc8\x01\n\nGetProfile\x12=.yandex.cloud.organizationmanager.v1.GetOsLoginProfileRequest\x1a\x33.yandex.cloud.organizationmanager.v1.OsLoginProfile\"F\x82\xd3\xe4\x93\x02@\x12>/organization-manager/v1/osLoginProfiles/{os_login_profile_id}\x12\xc3\x01\n\x0cListProfiles\x12?.yandex.cloud.organizationmanager.v1.ListOsLoginProfilesRequest\x1a@.yandex.cloud.organizationmanager.v1.ListOsLoginProfilesResponse\"0\x82\xd3\xe4\x93\x02*\x12(/organization-manager/v1/osLoginProfiles\x12\xdb\x01\n\rCreateProfile\x12@.yandex.cloud.organizationmanager.v1.CreateOsLoginProfileRequest\x1a!.yandex.cloud.operation.Operation\"e\xb2\xd2*.\n\x1c\x43reateOsLoginProfileMetadata\x12\x0eOsLoginProfile\x82\xd3\xe4\x93\x02-\"(/organization-manager/v1/osLoginProfiles:\x01*\x12\xf1\x01\n\rUpdateProfile\x12@.yandex.cloud.organizationmanager.v1.UpdateOsLoginProfileRequest\x1a!.yandex.cloud.operation.Operation\"{\xb2\xd2*.\n\x1cUpdateOsLoginProfileMetadata\x12\x0eOsLoginProfile\x82\xd3\xe4\x93\x02\x43\x32>/organization-manager/v1/osLoginProfiles/{os_login_profile_id}:\x01*\x12\x89\x02\n\x11SetDefaultProfile\x12\x44.yandex.cloud.organizationmanager.v1.SetDefaultOsLoginProfileRequest\x1a!.yandex.cloud.operation.Operation\"\x8a\x01\xb2\xd2*2\n SetDefaultOsLoginProfileMetadata\x12\x0eOsLoginProfile\x82\xd3\xe4\x93\x02N\"I/organization-manager/v1/osLoginProfiles/{os_login_profile_id}:setDefault:\x01*\x12\xe4\x01\n\rDeleteProfile\x12@.yandex.cloud.organizationmanager.v1.DeleteOsLoginProfileRequest\x1a!.yandex.cloud.operation.Operation\"n\xb2\xd2*5\n\x1c\x44\x65leteOsLoginProfileMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02/*-/organization-manager/v1/osLoginProfiles/{id}B\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.organizationmanager.v1.os_login_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager'
  _GETOSLOGINSETTINGSREQUEST.fields_by_name['organization_id']._options = None
  _GETOSLOGINSETTINGSREQUEST.fields_by_name['organization_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEOSLOGINSETTINGSREQUEST.fields_by_name['organization_id']._options = None
  _UPDATEOSLOGINSETTINGSREQUEST.fields_by_name['organization_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _SETDEFAULTOSLOGINPROFILEREQUEST.fields_by_name['os_login_profile_id']._options = None
  _SETDEFAULTOSLOGINPROFILEREQUEST.fields_by_name['os_login_profile_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETOSLOGINPROFILEREQUEST.fields_by_name['os_login_profile_id']._options = None
  _GETOSLOGINPROFILEREQUEST.fields_by_name['os_login_profile_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTOSLOGINPROFILESREQUEST.fields_by_name['organization_id']._options = None
  _LISTOSLOGINPROFILESREQUEST.fields_by_name['organization_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTOSLOGINPROFILESREQUEST.fields_by_name['page_size']._options = None
  _LISTOSLOGINPROFILESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTOSLOGINPROFILESREQUEST.fields_by_name['page_token']._options = None
  _LISTOSLOGINPROFILESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _LISTOSLOGINPROFILESREQUEST.fields_by_name['filter']._options = None
  _LISTOSLOGINPROFILESREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['os_login_profile_id']._options = None
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['os_login_profile_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['login']._options = None
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['login']._serialized_options = b'\350\3071\001\362\3071\r^[^.]*?[^~.]$\212\3101\004<=32'
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['uid']._options = None
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['uid']._serialized_options = b'\372\3071\0251-9223372036854775807'
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['home_directory']._options = None
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['home_directory']._serialized_options = b'\212\3101\005<=255'
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['shell']._options = None
  _UPDATEOSLOGINPROFILEREQUEST.fields_by_name['shell']._serialized_options = b'\212\3101\005<=255'
  _DELETEOSLOGINPROFILEREQUEST.fields_by_name['id']._options = None
  _DELETEOSLOGINPROFILEREQUEST.fields_by_name['id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['organization_id']._options = None
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['organization_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['subject_id']._options = None
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['subject_id']._serialized_options = b'\212\3101\004<=50'
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['login']._options = None
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['login']._serialized_options = b'\350\3071\001\362\3071\r^[^.]*?[^~.]$\212\3101\004<=32'
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['uid']._options = None
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['uid']._serialized_options = b'\372\3071\0251-9223372036854775807'
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['home_directory']._options = None
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['home_directory']._serialized_options = b'\212\3101\005<=255'
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['shell']._options = None
  _CREATEOSLOGINPROFILEREQUEST.fields_by_name['shell']._serialized_options = b'\212\3101\005<=255'
  _OSLOGINSERVICE.methods_by_name['GetSettings']._options = None
  _OSLOGINSERVICE.methods_by_name['GetSettings']._serialized_options = b'\202\323\344\223\002J\022H/organization-manager/v1/organizations/{organization_id}/osLoginSettings'
  _OSLOGINSERVICE.methods_by_name['UpdateSettings']._options = None
  _OSLOGINSERVICE.methods_by_name['UpdateSettings']._serialized_options = b'\262\322*0\n\035UpdateOsLoginSettingsMetadata\022\017OsLoginSettings\202\323\344\223\002M2H/organization-manager/v1/organizations/{organization_id}/osLoginSettings:\001*'
  _OSLOGINSERVICE.methods_by_name['GetProfile']._options = None
  _OSLOGINSERVICE.methods_by_name['GetProfile']._serialized_options = b'\202\323\344\223\002@\022>/organization-manager/v1/osLoginProfiles/{os_login_profile_id}'
  _OSLOGINSERVICE.methods_by_name['ListProfiles']._options = None
  _OSLOGINSERVICE.methods_by_name['ListProfiles']._serialized_options = b'\202\323\344\223\002*\022(/organization-manager/v1/osLoginProfiles'
  _OSLOGINSERVICE.methods_by_name['CreateProfile']._options = None
  _OSLOGINSERVICE.methods_by_name['CreateProfile']._serialized_options = b'\262\322*.\n\034CreateOsLoginProfileMetadata\022\016OsLoginProfile\202\323\344\223\002-\"(/organization-manager/v1/osLoginProfiles:\001*'
  _OSLOGINSERVICE.methods_by_name['UpdateProfile']._options = None
  _OSLOGINSERVICE.methods_by_name['UpdateProfile']._serialized_options = b'\262\322*.\n\034UpdateOsLoginProfileMetadata\022\016OsLoginProfile\202\323\344\223\002C2>/organization-manager/v1/osLoginProfiles/{os_login_profile_id}:\001*'
  _OSLOGINSERVICE.methods_by_name['SetDefaultProfile']._options = None
  _OSLOGINSERVICE.methods_by_name['SetDefaultProfile']._serialized_options = b'\262\322*2\n SetDefaultOsLoginProfileMetadata\022\016OsLoginProfile\202\323\344\223\002N\"I/organization-manager/v1/osLoginProfiles/{os_login_profile_id}:setDefault:\001*'
  _OSLOGINSERVICE.methods_by_name['DeleteProfile']._options = None
  _OSLOGINSERVICE.methods_by_name['DeleteProfile']._serialized_options = b'\262\322*5\n\034DeleteOsLoginProfileMetadata\022\025google.protobuf.Empty\202\323\344\223\002/*-/organization-manager/v1/osLoginProfiles/{id}'
  _globals['_GETOSLOGINSETTINGSREQUEST']._serialized_start=268
  _globals['_GETOSLOGINSETTINGSREQUEST']._serialized_end=334
  _globals['_OSLOGINSETTINGS']._serialized_start=337
  _globals['_OSLOGINSETTINGS']._serialized_end=537
  _globals['_USERSSHKEYSETTINGS']._serialized_start=539
  _globals['_USERSSHKEYSETTINGS']._serialized_end=607
  _globals['_SSHCERTIFICATESETTINGS']._serialized_start=609
  _globals['_SSHCERTIFICATESETTINGS']._serialized_end=650
  _globals['_UPDATEOSLOGINSETTINGSREQUEST']._serialized_start=653
  _globals['_UPDATEOSLOGINSETTINGSREQUEST']._serialized_end=1125
  _globals['_UPDATEOSLOGINSETTINGSREQUEST_USERSSHKEYSETTINGS']._serialized_start=539
  _globals['_UPDATEOSLOGINSETTINGSREQUEST_USERSSHKEYSETTINGS']._serialized_end=607
  _globals['_UPDATEOSLOGINSETTINGSREQUEST_SSHCERTIFICATESETTINGS']._serialized_start=609
  _globals['_UPDATEOSLOGINSETTINGSREQUEST_SSHCERTIFICATESETTINGS']._serialized_end=650
  _globals['_SETDEFAULTOSLOGINPROFILEREQUEST']._serialized_start=1127
  _globals['_SETDEFAULTOSLOGINPROFILEREQUEST']._serialized_end=1203
  _globals['_GETOSLOGINPROFILEREQUEST']._serialized_start=1205
  _globals['_GETOSLOGINPROFILEREQUEST']._serialized_end=1274
  _globals['_LISTOSLOGINPROFILESREQUEST']._serialized_start=1277
  _globals['_LISTOSLOGINPROFILESREQUEST']._serialized_end=1435
  _globals['_LISTOSLOGINPROFILESRESPONSE']._serialized_start=1437
  _globals['_LISTOSLOGINPROFILESRESPONSE']._serialized_end=1562
  _globals['_OSLOGINPROFILE']._serialized_start=1565
  _globals['_OSLOGINPROFILE']._serialized_end=1725
  _globals['_UPDATEOSLOGINPROFILEREQUEST']._serialized_start=1728
  _globals['_UPDATEOSLOGINPROFILEREQUEST']._serialized_end=1996
  _globals['_DELETEOSLOGINPROFILEREQUEST']._serialized_start=1998
  _globals['_DELETEOSLOGINPROFILEREQUEST']._serialized_end=2053
  _globals['_CREATEOSLOGINPROFILEREQUEST']._serialized_start=2056
  _globals['_CREATEOSLOGINPROFILEREQUEST']._serialized_end=2301
  _globals['_UPDATEOSLOGINPROFILEMETADATA']._serialized_start=2303
  _globals['_UPDATEOSLOGINPROFILEMETADATA']._serialized_end=2362
  _globals['_DELETEOSLOGINPROFILEMETADATA']._serialized_start=2364
  _globals['_DELETEOSLOGINPROFILEMETADATA']._serialized_end=2423
  _globals['_CREATEOSLOGINPROFILEMETADATA']._serialized_start=2425
  _globals['_CREATEOSLOGINPROFILEMETADATA']._serialized_end=2529
  _globals['_UPDATEOSLOGINSETTINGSMETADATA']._serialized_start=2531
  _globals['_UPDATEOSLOGINSETTINGSMETADATA']._serialized_end=2587
  _globals['_SETDEFAULTOSLOGINPROFILEMETADATA']._serialized_start=2589
  _globals['_SETDEFAULTOSLOGINPROFILEMETADATA']._serialized_end=2696
  _globals['_OSLOGINSERVICE']._serialized_start=2699
  _globals['_OSLOGINSERVICE']._serialized_end=4556
# @@protoc_insertion_point(module_scope)
