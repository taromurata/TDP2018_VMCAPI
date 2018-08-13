# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.sddcs.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class Clusters(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClustersStub)


    def create(self,
               org,
               sddc,
               cluster_config,
               ):
        """
        Add a cluster in the target sddc

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  cluster_config: :class:`com.vmware.vmc.model_client.ClusterConfig`
        :param cluster_config: clusterConfig (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The sddc is not in a state that's valid for updates
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the cluster with the given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'sddc': sddc,
                            'cluster_config': cluster_config,
                            })

    def delete(self,
               org,
               sddc,
               cluster,
               ):
        """
        This is a force operation which will delete the cluster even if there
        can be a data loss. Before calling this operation, all the VMs should
        be powered off.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  cluster: :class:`str`
        :param cluster: cluster identifier (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The sddc is not in a state that's valid for updates
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the cluster with the given id
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'sddc': sddc,
                            'cluster': cluster,
                            })
class Convert(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ConvertStub)


    def create(self,
               org,
               sddc,
               ):
        """
        This API converts a one host SDDC to a four node DEFAULT SDDC. It takes
        care of configuring and upgrading the vCenter configurations on the
        SDDC for high availability and data redundancy.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
            The sddc is not in a state that's valid for updates, Method not
            allowed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'sddc': sddc,
                            })
class Esxs(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _EsxsStub)


    def create(self,
               org,
               sddc,
               esx_config,
               action=None,
               ):
        """
        Add/Remove one or more ESX hosts in the target cloud

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  esx_config: :class:`com.vmware.vmc.model_client.EsxConfig`
        :param esx_config: esxConfig (required)
        :type  action: :class:`str` or ``None``
        :param action: If = 'add', will add the esx. If = 'remove', will delete the
            esx/esxs bound to a single cluster (Cluster Id is mandatory for non
            cluster 1 esx remove). If = 'force-remove', will delete the esx
            even if it can lead to data loss (This is an privileged operation).
            If = 'addToAll', will add esxs to all clusters in the SDDC (This is
            an privileged operation). If = 'removeFromAll', will delete the
            esxs from all clusters in the SDDC (This is an privileged
            operation). Default behaviour is 'add' (optional)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The sddc is not in a state that's valid for updates
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with the given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'sddc': sddc,
                            'esx_config': esx_config,
                            'action': action,
                            })
class Publicips(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PublicipsStub)


    def create(self,
               org,
               sddc,
               spec,
               ):
        """
        Allocate public IPs for a SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  spec: :class:`com.vmware.vmc.model_client.SddcAllocatePublicIpSpec`
        :param spec: allocation spec (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The sddc is not in a state that's valid for updates
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'sddc': sddc,
                            'spec': spec,
                            })

    def delete(self,
               org,
               sddc,
               id,
               ):
        """
        Free one public IP for a SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  id: :class:`str`
        :param id: ip allocation id (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The sddc is not in a state that's valid for updates
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the public IP with given IP address
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'sddc': sddc,
                            'id': id,
                            })

    def get(self,
            org,
            sddc,
            id,
            ):
        """
        Get one public IP for a SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  id: :class:`str`
        :param id: ip allocation id (required)
        :rtype: :class:`com.vmware.vmc.model_client.SddcPublicIp`
        :return: com.vmware.vmc.model.SddcPublicIp
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the public IP with given IP address
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            'id': id,
                            })

    def list(self,
             org,
             sddc,
             ):
        """
        list all public IPs for a SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.SddcPublicIp`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('list',
                            {
                            'org': org,
                            'sddc': sddc,
                            })

    def update(self,
               org,
               sddc,
               id,
               action,
               sddc_public_ip_object,
               ):
        """
        Attach or detach a public IP to workload VM for a SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  id: :class:`str`
        :param id: ip allocation id (required)
        :type  action: :class:`str`
        :param action: Type of action as 'attach', 'detach', 'reattach', or 'rename'. For
            'attch', the public IP must not be attached and
            'associated_private_ip' in the payload needs to be set with a
            workload VM private IP. For 'detach', the public IP must be
            attached and 'associated_private_ip' in the payload should not be
            set with any value. For 'reattach', the public IP must be attached
            and 'associated_private_ip' in the payload needs to be set with a
            new workload VM private IP. For 'rename', the 'name' in the payload
            needs to have a new name string. (required)
        :type  sddc_public_ip_object: :class:`com.vmware.vmc.model_client.SddcPublicIp`
        :param sddc_public_ip_object: SddcPublicIp object to update (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The sddc is not in a state that's valid for updates
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the public IP with given IP address
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('update',
                            {
                            'org': org,
                            'sddc': sddc,
                            'id': id,
                            'action': action,
                            'sddc_public_ip_object': sddc_public_ip_object,
                            })
class SddcTemplate(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SddcTemplateStub)


    def get(self,
            org,
            sddc,
            ):
        """
        Get configuration template for an SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :rtype: :class:`com.vmware.vmc.model_client.SddcTemplate`
        :return: com.vmware.vmc.model.SddcTemplate
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
            SDDC is in a state that cannot be use for generating configuration
            template
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            })
class _ClustersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'cluster_config': type.ReferenceType('com.vmware.vmc.model_client', 'ClusterConfig'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/clusters',
            request_body_parameter='cluster_config',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'cluster': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/clusters/{cluster}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'cluster': 'cluster',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.clusters',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ConvertStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/convert',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.convert',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _EsxsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'esx_config': type.ReferenceType('com.vmware.vmc.model_client', 'EsxConfig'),
            'action': type.OptionalType(type.StringType()),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/esxs',
            request_body_parameter='esx_config',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'action': 'action',
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.esxs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _PublicipsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'spec': type.ReferenceType('com.vmware.vmc.model_client', 'SddcAllocatePublicIpSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/publicips',
            request_body_parameter='spec',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'id': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/publicips/{id}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'id': 'id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/publicips/{id}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'id': 'id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/publicips',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'id': type.StringType(),
            'action': type.StringType(),
            'sddc_public_ip_object': type.ReferenceType('com.vmware.vmc.model_client', 'SddcPublicIp'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/publicips/{id}',
            request_body_parameter='sddc_public_ip_object',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'id': 'id',
            },
            query_parameters={
                'action': 'action',
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'SddcPublicIp'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'SddcPublicIp')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.publicips',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SddcTemplateStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/sddc-template',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'SddcTemplate'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.sddc_template',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Clusters': Clusters,
        'Convert': Convert,
        'Esxs': Esxs,
        'Publicips': Publicips,
        'SddcTemplate': SddcTemplate,
        'dns': 'com.vmware.vmc.orgs.sddcs.dns_client.StubFactory',
        'mgw': 'com.vmware.vmc.orgs.sddcs.mgw_client.StubFactory',
        'networks': 'com.vmware.vmc.orgs.sddcs.networks_client.StubFactory',
    }

