# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.model.
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

class OfferType(Enum):
    """
    

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    TERM = None
    """


    """
    ON_DEMAND = None
    """


    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`OfferType` instance.
        """
        Enum.__init__(string)

OfferType._set_values([
    OfferType('TERM'),
    OfferType('ON_DEMAND'),
])
OfferType._set_binding_type(type.EnumType(
    'com.vmware.vmc.model.offer_type',
    OfferType))




class AbstractEntity(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str` or ``None``
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        VapiStruct.__init__(self)

AbstractEntity._set_binding_type(type.StructType(
    'com.vmware.vmc.model.abstract_entity', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.OptionalType(type.StringType()),
        'user_name': type.StringType(),
        'id': type.StringType(),
    },
    AbstractEntity,
    False,
    None))



class AccountLinkConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'delay_account_link': 'delay_account_link',
                            }

    def __init__(self,
                 delay_account_link=None,
                ):
        """
        :type  delay_account_link: :class:`bool` or ``None``
        :param delay_account_link: Boolean flag identifying whether account linking should be delayed
            or not for the SDDC.
        """
        self.delay_account_link = delay_account_link
        VapiStruct.__init__(self)

AccountLinkConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.account_link_config', {
        'delay_account_link': type.OptionalType(type.BooleanType()),
    },
    AccountLinkConfig,
    False,
    None))



class AccountLinkSddcConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'customer_subnet_ids': 'customer_subnet_ids',
                            'connected_account_id': 'connected_account_id',
                            }

    def __init__(self,
                 customer_subnet_ids=None,
                 connected_account_id=None,
                ):
        """
        :type  customer_subnet_ids: :class:`list` of :class:`str` or ``None``
        :param customer_subnet_ids: 
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: The ID of the customer connected account to work with.
        """
        self.customer_subnet_ids = customer_subnet_ids
        self.connected_account_id = connected_account_id
        VapiStruct.__init__(self)

AccountLinkSddcConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.account_link_sddc_config', {
        'customer_subnet_ids': type.OptionalType(type.ListType(type.StringType())),
        'connected_account_id': type.OptionalType(type.StringType()),
    },
    AccountLinkSddcConfig,
    False,
    None))



class AddressFWSourceDestination(VapiStruct):
    """
    Source or Destination for firewall rule. Default is 'any'.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'exclude': 'exclude',
                            'ipAddress': 'ip_address',
                            'groupingObjectId': 'grouping_object_id',
                            'vnicGroupId': 'vnic_group_id',
                            }

    def __init__(self,
                 exclude=None,
                 ip_address=None,
                 grouping_object_id=None,
                 vnic_group_id=None,
                ):
        """
        :type  exclude: :class:`bool` or ``None``
        :param exclude: Exclude the specified source or destination.
        :type  ip_address: :class:`list` of :class:`str` or ``None``
        :param ip_address: List of string. Can specify single IP address, range of IP address,
            or in CIDR format. Can define multiple.
        :type  grouping_object_id: :class:`list` of :class:`str` or ``None``
        :param grouping_object_id: List of string. Id of cluster, datacenter, distributedPortGroup,
            legacyPortGroup, VirtualMachine, vApp, resourcePool, logicalSwitch,
            IPSet, securityGroup. Can define multiple.
        :type  vnic_group_id: :class:`list` of :class:`str` or ``None``
        :param vnic_group_id: List of string. Possible values are vnic-index-[1-9], vse, external
            or internal. Can define multiple.
        """
        self.exclude = exclude
        self.ip_address = ip_address
        self.grouping_object_id = grouping_object_id
        self.vnic_group_id = vnic_group_id
        VapiStruct.__init__(self)

AddressFWSourceDestination._set_binding_type(type.StructType(
    'com.vmware.vmc.model.address_FW_source_destination', {
        'exclude': type.OptionalType(type.BooleanType()),
        'ipAddress': type.OptionalType(type.ListType(type.StringType())),
        'groupingObjectId': type.OptionalType(type.ListType(type.StringType())),
        'vnicGroupId': type.OptionalType(type.ListType(type.StringType())),
    },
    AddressFWSourceDestination,
    False,
    None))



class Agent(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "Agent"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'addresses': 'addresses',
                            'healthy': 'healthy',
                            'custom_properties': 'custom_properties',
                            'last_health_status_change': 'last_health_status_change',
                            'internal_ip': 'internal_ip',
                            'reserved_ip': 'reserved_ip',
                            'network_netmask': 'network_netmask',
                            'network_gateway': 'network_gateway',
                            'provider': 'provider',
                            'agent_url': 'agent_url',
                            'network_cidr': 'network_cidr',
                            'id': 'id',
                            }

    def __init__(self,
                 addresses=None,
                 healthy=None,
                 custom_properties=None,
                 last_health_status_change=None,
                 internal_ip=None,
                 reserved_ip=None,
                 network_netmask=None,
                 network_gateway=None,
                 provider='Agent',
                 agent_url=None,
                 network_cidr=None,
                 id=None,
                ):
        """
        :type  addresses: :class:`list` of :class:`str` or ``None``
        :param addresses: 
        :type  healthy: :class:`bool` or ``None``
        :param healthy: 
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  last_health_status_change: :class:`long` or ``None``
        :param last_health_status_change: 
        :type  internal_ip: :class:`str` or ``None``
        :param internal_ip: 
        :type  reserved_ip: :class:`str` or ``None``
        :param reserved_ip: 
        :type  network_netmask: :class:`str` or ``None``
        :param network_netmask: 
        :type  network_gateway: :class:`str` or ``None``
        :param network_gateway: 
        :type  provider: :class:`str`
        :param provider: 
        :type  agent_url: :class:`str` or ``None``
        :param agent_url: 
        :type  network_cidr: :class:`str` or ``None``
        :param network_cidr: 
        :type  id: :class:`str` or ``None``
        :param id: 
        """
        self.addresses = addresses
        self.healthy = healthy
        self.custom_properties = custom_properties
        self.last_health_status_change = last_health_status_change
        self.internal_ip = internal_ip
        self.reserved_ip = reserved_ip
        self.network_netmask = network_netmask
        self.network_gateway = network_gateway
        self.provider = provider
        self.agent_url = agent_url
        self.network_cidr = network_cidr
        self.id = id
        VapiStruct.__init__(self)

Agent._set_binding_type(type.StructType(
    'com.vmware.vmc.model.agent', {
        'addresses': type.OptionalType(type.ListType(type.StringType())),
        'healthy': type.OptionalType(type.BooleanType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'last_health_status_change': type.OptionalType(type.IntegerType()),
        'internal_ip': type.OptionalType(type.StringType()),
        'reserved_ip': type.OptionalType(type.StringType()),
        'network_netmask': type.OptionalType(type.StringType()),
        'network_gateway': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'agent_url': type.OptionalType(type.StringType()),
        'network_cidr': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
    },
    Agent,
    False,
    None))



class AmiInfo(VapiStruct):
    """
    the AmiInfo used for deploying esx of the sddc

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'region': 'region',
                            'id': 'id',
                            'name': 'name',
                            }

    def __init__(self,
                 region=None,
                 id=None,
                 name=None,
                ):
        """
        :type  region: :class:`str` or ``None``
        :param region: the region of the esx ami
        :type  id: :class:`str` or ``None``
        :param id: the ami id for the esx
        :type  name: :class:`str` or ``None``
        :param name: the name of the esx ami
        """
        self.region = region
        self.id = id
        self.name = name
        VapiStruct.__init__(self)

AmiInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ami_info', {
        'region': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
    },
    AmiInfo,
    False,
    None))



class AppliancesSummary(VapiStruct):
    """
    NSX Edge appliance summary.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'dataStoreMoidOfActiveVse': 'data_store_moid_of_active_vse',
                            'enableFips': 'enable_fips',
                            'hostNameOfActiveVse': 'host_name_of_active_vse',
                            'vmBuildInfo': 'vm_build_info',
                            'deployAppliances': 'deploy_appliances',
                            'communicationChannel': 'communication_channel',
                            'vmNameOfActiveVse': 'vm_name_of_active_vse',
                            'numberOfDeployedVms': 'number_of_deployed_vms',
                            'resourcePoolMoidOfActiveVse': 'resource_pool_moid_of_active_vse',
                            'dataStoreNameOfActiveVse': 'data_store_name_of_active_vse',
                            'vmMoidOfActiveVse': 'vm_moid_of_active_vse',
                            'statusFromVseUpdatedOn': 'status_from_vse_updated_on',
                            'fqdn': 'fqdn',
                            'applianceSize': 'appliance_size',
                            'resourcePoolNameOfActiveVse': 'resource_pool_name_of_active_vse',
                            'activeVseHaIndex': 'active_vse_ha_index',
                            'vmVersion': 'vm_version',
                            'hostMoidOfActiveVse': 'host_moid_of_active_vse',
                            }

    def __init__(self,
                 data_store_moid_of_active_vse=None,
                 enable_fips=None,
                 host_name_of_active_vse=None,
                 vm_build_info=None,
                 deploy_appliances=None,
                 communication_channel=None,
                 vm_name_of_active_vse=None,
                 number_of_deployed_vms=None,
                 resource_pool_moid_of_active_vse=None,
                 data_store_name_of_active_vse=None,
                 vm_moid_of_active_vse=None,
                 status_from_vse_updated_on=None,
                 fqdn=None,
                 appliance_size=None,
                 resource_pool_name_of_active_vse=None,
                 active_vse_ha_index=None,
                 vm_version=None,
                 host_moid_of_active_vse=None,
                ):
        """
        :type  data_store_moid_of_active_vse: :class:`str` or ``None``
        :param data_store_moid_of_active_vse: vCenter MOID of the active NSX Edge appliance's data store.
        :type  enable_fips: :class:`bool` or ``None``
        :param enable_fips: Value is true if FIPS is enabled on NSX Edge appliance.
        :type  host_name_of_active_vse: :class:`str` or ``None``
        :param host_name_of_active_vse: Host name of the active NSX Edge appliance.
        :type  vm_build_info: :class:`str` or ``None``
        :param vm_build_info: NSX Edge appliance build version.
        :type  deploy_appliances: :class:`bool` or ``None``
        :param deploy_appliances: Value is true if NSX Edge appliances are to be deployed.
        :type  communication_channel: :class:`str` or ``None``
        :param communication_channel: Communication channel used to communicate with NSX Edge appliance.
        :type  vm_name_of_active_vse: :class:`str` or ``None``
        :param vm_name_of_active_vse: Name of the active NSX Edge appliance.
        :type  number_of_deployed_vms: :class:`long` or ``None``
        :param number_of_deployed_vms: Number of deployed appliances of the NSX Edge. format: int32
        :type  resource_pool_moid_of_active_vse: :class:`str` or ``None``
        :param resource_pool_moid_of_active_vse: vCenter MOID of the active NSX Edge appliance's resource
            pool/cluster. Can be resource pool ID, e.g. resgroup-15 or cluster
            ID, e.g. domain-c41.
        :type  data_store_name_of_active_vse: :class:`str` or ``None``
        :param data_store_name_of_active_vse: Datastore name of the active NSX Edge appliance.
        :type  vm_moid_of_active_vse: :class:`str` or ``None``
        :param vm_moid_of_active_vse: vCenter MOID of the active NSX Edge appliance.
        :type  status_from_vse_updated_on: :class:`long` or ``None``
        :param status_from_vse_updated_on: Time stamp value when healthcheck status was last updated for the
            NSX Edge appliance. format: int64
        :type  fqdn: :class:`str` or ``None``
        :param fqdn: FQDN of the NSX Edge.
        :type  appliance_size: :class:`str` or ``None``
        :param appliance_size: NSX Edge appliance size.
        :type  resource_pool_name_of_active_vse: :class:`str` or ``None``
        :param resource_pool_name_of_active_vse: Resource Pool/Cluster name of the active NSX Edge appliance.
        :type  active_vse_ha_index: :class:`long` or ``None``
        :param active_vse_ha_index: HA index of the active NSX Edge appliance. format: int32
        :type  vm_version: :class:`str` or ``None``
        :param vm_version: NSX Edge appliance version.
        :type  host_moid_of_active_vse: :class:`str` or ``None``
        :param host_moid_of_active_vse: vCenter MOID of the active NSX Edge appliance's host.
        """
        self.data_store_moid_of_active_vse = data_store_moid_of_active_vse
        self.enable_fips = enable_fips
        self.host_name_of_active_vse = host_name_of_active_vse
        self.vm_build_info = vm_build_info
        self.deploy_appliances = deploy_appliances
        self.communication_channel = communication_channel
        self.vm_name_of_active_vse = vm_name_of_active_vse
        self.number_of_deployed_vms = number_of_deployed_vms
        self.resource_pool_moid_of_active_vse = resource_pool_moid_of_active_vse
        self.data_store_name_of_active_vse = data_store_name_of_active_vse
        self.vm_moid_of_active_vse = vm_moid_of_active_vse
        self.status_from_vse_updated_on = status_from_vse_updated_on
        self.fqdn = fqdn
        self.appliance_size = appliance_size
        self.resource_pool_name_of_active_vse = resource_pool_name_of_active_vse
        self.active_vse_ha_index = active_vse_ha_index
        self.vm_version = vm_version
        self.host_moid_of_active_vse = host_moid_of_active_vse
        VapiStruct.__init__(self)

AppliancesSummary._set_binding_type(type.StructType(
    'com.vmware.vmc.model.appliances_summary', {
        'dataStoreMoidOfActiveVse': type.OptionalType(type.StringType()),
        'enableFips': type.OptionalType(type.BooleanType()),
        'hostNameOfActiveVse': type.OptionalType(type.StringType()),
        'vmBuildInfo': type.OptionalType(type.StringType()),
        'deployAppliances': type.OptionalType(type.BooleanType()),
        'communicationChannel': type.OptionalType(type.StringType()),
        'vmNameOfActiveVse': type.OptionalType(type.StringType()),
        'numberOfDeployedVms': type.OptionalType(type.IntegerType()),
        'resourcePoolMoidOfActiveVse': type.OptionalType(type.StringType()),
        'dataStoreNameOfActiveVse': type.OptionalType(type.StringType()),
        'vmMoidOfActiveVse': type.OptionalType(type.StringType()),
        'statusFromVseUpdatedOn': type.OptionalType(type.IntegerType()),
        'fqdn': type.OptionalType(type.StringType()),
        'applianceSize': type.OptionalType(type.StringType()),
        'resourcePoolNameOfActiveVse': type.OptionalType(type.StringType()),
        'activeVseHaIndex': type.OptionalType(type.IntegerType()),
        'vmVersion': type.OptionalType(type.StringType()),
        'hostMoidOfActiveVse': type.OptionalType(type.StringType()),
    },
    AppliancesSummary,
    False,
    None))



class Application(VapiStruct):
    """
    Application for firewall rule

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'applicationId': 'application_id',
                            'service': 'service',
                            }

    def __init__(self,
                 application_id=None,
                 service=None,
                ):
        """
        :type  application_id: :class:`list` of :class:`str` or ``None``
        :param application_id: List of string. Id of service or serviceGroup groupingObject. Can
            define multiple.
        :type  service: :class:`list` of :class:`Nsxfirewallservice` or ``None``
        :param service: List of protocol and ports. Can define multiple.
        """
        self.application_id = application_id
        self.service = service
        VapiStruct.__init__(self)

Application._set_binding_type(type.StructType(
    'com.vmware.vmc.model.application', {
        'applicationId': type.OptionalType(type.ListType(type.StringType())),
        'service': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Nsxfirewallservice'))),
    },
    Application,
    False,
    None))



class AwsAgent(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'instance_id': 'instance_id',
                            'key_pair': 'key_pair',
                            'addresses': 'addresses',
                            'healthy': 'healthy',
                            'custom_properties': 'custom_properties',
                            'last_health_status_change': 'last_health_status_change',
                            'internal_ip': 'internal_ip',
                            'reserved_ip': 'reserved_ip',
                            'network_netmask': 'network_netmask',
                            'network_gateway': 'network_gateway',
                            'provider': 'provider',
                            'agent_url': 'agent_url',
                            'network_cidr': 'network_cidr',
                            'id': 'id',
                            }

    def __init__(self,
                 instance_id=None,
                 key_pair=None,
                 addresses=None,
                 healthy=None,
                 custom_properties=None,
                 last_health_status_change=None,
                 internal_ip=None,
                 reserved_ip=None,
                 network_netmask=None,
                 network_gateway=None,
                 provider='AWS',
                 agent_url=None,
                 network_cidr=None,
                 id=None,
                ):
        """
        :type  instance_id: :class:`str` or ``None``
        :param instance_id: 
        :type  key_pair: :class:`AwsKeyPair` or ``None``
        :param key_pair: 
        :type  addresses: :class:`list` of :class:`str` or ``None``
        :param addresses: 
        :type  healthy: :class:`bool` or ``None``
        :param healthy: 
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  last_health_status_change: :class:`long` or ``None``
        :param last_health_status_change: 
        :type  internal_ip: :class:`str` or ``None``
        :param internal_ip: 
        :type  reserved_ip: :class:`str` or ``None``
        :param reserved_ip: 
        :type  network_netmask: :class:`str` or ``None``
        :param network_netmask: 
        :type  network_gateway: :class:`str` or ``None``
        :param network_gateway: 
        :type  provider: :class:`str`
        :param provider: 
        :type  agent_url: :class:`str` or ``None``
        :param agent_url: 
        :type  network_cidr: :class:`str` or ``None``
        :param network_cidr: 
        :type  id: :class:`str` or ``None``
        :param id: 
        """
        self.instance_id = instance_id
        self.key_pair = key_pair
        self.addresses = addresses
        self.healthy = healthy
        self.custom_properties = custom_properties
        self.last_health_status_change = last_health_status_change
        self.internal_ip = internal_ip
        self.reserved_ip = reserved_ip
        self.network_netmask = network_netmask
        self.network_gateway = network_gateway
        self.provider = provider
        self.agent_url = agent_url
        self.network_cidr = network_cidr
        self.id = id
        VapiStruct.__init__(self)

AwsAgent._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_agent', {
        'instance_id': type.OptionalType(type.StringType()),
        'key_pair': type.OptionalType(type.ReferenceType(__name__, 'AwsKeyPair')),
        'addresses': type.OptionalType(type.ListType(type.StringType())),
        'healthy': type.OptionalType(type.BooleanType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'last_health_status_change': type.OptionalType(type.IntegerType()),
        'internal_ip': type.OptionalType(type.StringType()),
        'reserved_ip': type.OptionalType(type.StringType()),
        'network_netmask': type.OptionalType(type.StringType()),
        'network_gateway': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'agent_url': type.OptionalType(type.StringType()),
        'network_cidr': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
    },
    AwsAgent,
    False,
    None))



class AwsCloudProvider(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'regions': 'regions',
                            'provider': 'provider',
                            }

    def __init__(self,
                 regions=None,
                 provider='AWS',
                ):
        """
        :type  regions: :class:`list` of :class:`str` or ``None``
        :param regions: 
        :type  provider: :class:`str`
        :param provider: Name of the Cloud Provider
        """
        self.regions = regions
        self.provider = provider
        VapiStruct.__init__(self)

AwsCloudProvider._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_cloud_provider', {
        'regions': type.OptionalType(type.ListType(type.StringType())),
        'provider': type.StringType(),
    },
    AwsCloudProvider,
    False,
    None))



class AwsCompatibleSubnets(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'customer_available_zones': 'customer_available_zones',
                            'vpc_map': 'vpc_map',
                            }

    def __init__(self,
                 customer_available_zones=None,
                 vpc_map=None,
                ):
        """
        :type  customer_available_zones: :class:`list` of :class:`str` or ``None``
        :param customer_available_zones: 
        :type  vpc_map: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param vpc_map: 
        """
        self.customer_available_zones = customer_available_zones
        self.vpc_map = vpc_map
        VapiStruct.__init__(self)

AwsCompatibleSubnets._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_compatible_subnets', {
        'customer_available_zones': type.OptionalType(type.ListType(type.StringType())),
        'vpc_map': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    AwsCompatibleSubnets,
    False,
    None))



class AwsCustomerConnectedAccount(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'policy_payer_arn': 'policy_payer_arn',
                            'account_number': 'account_number',
                            'policy_external_id': 'policy_external_id',
                            'region_to_az_to_shadow_mapping': 'region_to_az_to_shadow_mapping',
                            'org_id': 'org_id',
                            'cf_stack_name': 'cf_stack_name',
                            'policy_service_arn': 'policy_service_arn',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 policy_payer_arn=None,
                 account_number=None,
                 policy_external_id=None,
                 region_to_az_to_shadow_mapping=None,
                 org_id=None,
                 cf_stack_name=None,
                 policy_service_arn=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str` or ``None``
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  policy_payer_arn: :class:`str` or ``None``
        :param policy_payer_arn: 
        :type  account_number: :class:`str` or ``None``
        :param account_number: 
        :type  policy_external_id: :class:`str` or ``None``
        :param policy_external_id: 
        :type  region_to_az_to_shadow_mapping: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param region_to_az_to_shadow_mapping: Provides a map of regions to availability zones from the shadow
            account's perspective
        :type  org_id: :class:`str` or ``None``
        :param org_id: 
        :type  cf_stack_name: :class:`str` or ``None``
        :param cf_stack_name: 
        :type  policy_service_arn: :class:`str` or ``None``
        :param policy_service_arn: 
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.policy_payer_arn = policy_payer_arn
        self.account_number = account_number
        self.policy_external_id = policy_external_id
        self.region_to_az_to_shadow_mapping = region_to_az_to_shadow_mapping
        self.org_id = org_id
        self.cf_stack_name = cf_stack_name
        self.policy_service_arn = policy_service_arn
        VapiStruct.__init__(self)

AwsCustomerConnectedAccount._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_customer_connected_account', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.OptionalType(type.StringType()),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'policy_payer_arn': type.OptionalType(type.StringType()),
        'account_number': type.OptionalType(type.StringType()),
        'policy_external_id': type.OptionalType(type.StringType()),
        'region_to_az_to_shadow_mapping': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'org_id': type.OptionalType(type.StringType()),
        'cf_stack_name': type.OptionalType(type.StringType()),
        'policy_service_arn': type.OptionalType(type.StringType()),
    },
    AwsCustomerConnectedAccount,
    False,
    None))



class AwsEsxHost(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'internal_public_ip_pool': 'internal_public_ip_pool',
                            'name': 'name',
                            'availability_zone': 'availability_zone',
                            'esx_id': 'esx_id',
                            'hostname': 'hostname',
                            'provider': 'provider',
                            'mac_address': 'mac_address',
                            'custom_properties': 'custom_properties',
                            'esx_state': 'esx_state',
                            }

    def __init__(self,
                 internal_public_ip_pool=None,
                 name=None,
                 availability_zone=None,
                 esx_id=None,
                 hostname=None,
                 provider='AWS',
                 mac_address=None,
                 custom_properties=None,
                 esx_state=None,
                ):
        """
        :type  internal_public_ip_pool: :class:`list` of :class:`SddcPublicIp` or ``None``
        :param internal_public_ip_pool: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  availability_zone: :class:`str` or ``None``
        :param availability_zone: Availability zone where the host is provisioned.
        :type  esx_id: :class:`str` or ``None``
        :param esx_id: 
        :type  hostname: :class:`str` or ``None``
        :param hostname: 
        :type  provider: :class:`str`
        :param provider: 
        :type  mac_address: :class:`str` or ``None``
        :param mac_address: 
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  esx_state: :class:`str` or ``None``
        :param esx_state: Possible values are: 
            
            * :attr:`EsxHost.ESX_STATE_DEPLOYING`
            * :attr:`EsxHost.ESX_STATE_PROVISIONED`
            * :attr:`EsxHost.ESX_STATE_READY`
            * :attr:`EsxHost.ESX_STATE_DELETING`
            * :attr:`EsxHost.ESX_STATE_DELETED`
            * :attr:`EsxHost.ESX_STATE_FAILED`
        """
        self.internal_public_ip_pool = internal_public_ip_pool
        self.name = name
        self.availability_zone = availability_zone
        self.esx_id = esx_id
        self.hostname = hostname
        self.provider = provider
        self.mac_address = mac_address
        self.custom_properties = custom_properties
        self.esx_state = esx_state
        VapiStruct.__init__(self)

AwsEsxHost._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_esx_host', {
        'internal_public_ip_pool': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcPublicIp'))),
        'name': type.OptionalType(type.StringType()),
        'availability_zone': type.OptionalType(type.StringType()),
        'esx_id': type.OptionalType(type.StringType()),
        'hostname': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'mac_address': type.OptionalType(type.StringType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'esx_state': type.OptionalType(type.StringType()),
    },
    AwsEsxHost,
    False,
    None))



class AwsKeyPair(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'key_name': 'key_name',
                            'key_fingerprint': 'key_fingerprint',
                            'key_material': 'key_material',
                            }

    def __init__(self,
                 key_name=None,
                 key_fingerprint=None,
                 key_material=None,
                ):
        """
        :type  key_name: :class:`str` or ``None``
        :param key_name: 
        :type  key_fingerprint: :class:`str` or ``None``
        :param key_fingerprint: 
        :type  key_material: :class:`str` or ``None``
        :param key_material: 
        """
        self.key_name = key_name
        self.key_fingerprint = key_fingerprint
        self.key_material = key_material
        VapiStruct.__init__(self)

AwsKeyPair._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_key_pair', {
        'key_name': type.OptionalType(type.StringType()),
        'key_fingerprint': type.OptionalType(type.StringType()),
        'key_material': type.OptionalType(type.StringType()),
    },
    AwsKeyPair,
    False,
    None))



class AwsOrgConfiguration(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'provider': 'provider',
                            }

    def __init__(self,
                 provider='AWS',
                ):
        """
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`OrgConfiguration.PROVIDER_AWS`
            
             Discriminator for provider specific properties
        """
        self.provider = provider
        VapiStruct.__init__(self)

AwsOrgConfiguration._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_org_configuration', {
        'provider': type.StringType(),
    },
    AwsOrgConfiguration,
    False,
    None))



class AwsSddcConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'region': 'region',
                            'vpc_name': 'vpc_name',
                            'name': 'name',
                            'account_link_sddc_config': 'account_link_sddc_config',
                            'vpc_cidr': 'vpc_cidr',
                            'num_hosts': 'num_hosts',
                            'sddc_type': 'sddc_type',
                            'vxlan_subnet': 'vxlan_subnet',
                            'account_link_config': 'account_link_config',
                            'provider': 'provider',
                            'sso_domain': 'sso_domain',
                            'sddc_template_id': 'sddc_template_id',
                            'deployment_type': 'deployment_type',
                            }

    def __init__(self,
                 region=None,
                 vpc_name=None,
                 name=None,
                 account_link_sddc_config=None,
                 vpc_cidr=None,
                 num_hosts=None,
                 sddc_type=None,
                 vxlan_subnet=None,
                 account_link_config=None,
                 provider='AWS',
                 sso_domain=None,
                 sddc_template_id=None,
                 deployment_type=None,
                ):
        """
        :type  region: :class:`str`
        :param region: 
        :type  vpc_name: :class:`str` or ``None``
        :param vpc_name: 
        :type  name: :class:`str`
        :param name: 
        :type  account_link_sddc_config: :class:`list` of :class:`AccountLinkSddcConfig` or ``None``
        :param account_link_sddc_config: A list of the SDDC linking configurations to use.
        :type  vpc_cidr: :class:`str` or ``None``
        :param vpc_cidr: AWS VPC IP range. Only prefix of 16 or 20 is currently supported.
        :type  num_hosts: :class:`long`
        :param num_hosts: 
        :type  sddc_type: :class:`str` or ``None``
        :param sddc_type: Denotes the sddc type , if the value is null or empty, the type is
            considered as default.
        :type  vxlan_subnet: :class:`str` or ``None``
        :param vxlan_subnet: VXLAN IP subnet
        :type  account_link_config: :class:`AccountLinkConfig` or ``None``
        :param account_link_config: The account linking configuration, we will keep this one and remove
            accountLinkSddcConfig finally.
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`SddcConfig.PROVIDER_AWS`
            
            Determines what additional properties are available based on cloud
            provider.
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: The SSO domain name to use for vSphere users. If not specified,
            vmc.local will be used.
        :type  sddc_template_id: :class:`str` or ``None``
        :param sddc_template_id: If provided, configuration from the template will applied to the
            provisioned SDDC. format: UUID
        :type  deployment_type: :class:`str` or ``None``
        :param deployment_type: Possible values are: 
            
            * :attr:`SddcConfig.DEPLOYMENT_TYPE_SINGLEAZ`
            * :attr:`SddcConfig.DEPLOYMENT_TYPE_MULTIAZ`
            
            Denotes if request is for a SingleAZ or a MultiAZ SDDC. Default is
            SingleAZ.
        """
        self.region = region
        self.vpc_name = vpc_name
        self.name = name
        self.account_link_sddc_config = account_link_sddc_config
        self.vpc_cidr = vpc_cidr
        self.num_hosts = num_hosts
        self.sddc_type = sddc_type
        self.vxlan_subnet = vxlan_subnet
        self.account_link_config = account_link_config
        self.provider = provider
        self.sso_domain = sso_domain
        self.sddc_template_id = sddc_template_id
        self.deployment_type = deployment_type
        VapiStruct.__init__(self)

AwsSddcConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_sddc_config', {
        'region': type.StringType(),
        'vpc_name': type.OptionalType(type.StringType()),
        'name': type.StringType(),
        'account_link_sddc_config': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AccountLinkSddcConfig'))),
        'vpc_cidr': type.OptionalType(type.StringType()),
        'num_hosts': type.IntegerType(),
        'sddc_type': type.OptionalType(type.StringType()),
        'vxlan_subnet': type.OptionalType(type.StringType()),
        'account_link_config': type.OptionalType(type.ReferenceType(__name__, 'AccountLinkConfig')),
        'provider': type.StringType(),
        'sso_domain': type.OptionalType(type.StringType()),
        'sddc_template_id': type.OptionalType(type.StringType()),
        'deployment_type': type.OptionalType(type.StringType()),
    },
    AwsSddcConfig,
    False,
    None))



class AwsSddcConnection(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'cidr_block_subnet': 'cidr_block_subnet',
                            'connected_account_id': 'connected_account_id',
                            'eni_group': 'eni_group',
                            'subnet_id': 'subnet_id',
                            'org_id': 'org_id',
                            'sddc_id': 'sddc_id',
                            'cidr_block_vpc': 'cidr_block_vpc',
                            'subnet_availability_zone': 'subnet_availability_zone',
                            'vpc_id': 'vpc_id',
                            'is_cgw_present': 'is_cgw_present',
                            'customer_eni_infos': 'customer_eni_infos',
                            'default_route_table': 'default_route_table',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 cidr_block_subnet=None,
                 connected_account_id=None,
                 eni_group=None,
                 subnet_id=None,
                 org_id=None,
                 sddc_id=None,
                 cidr_block_vpc=None,
                 subnet_availability_zone=None,
                 vpc_id=None,
                 is_cgw_present=None,
                 customer_eni_infos=None,
                 default_route_table=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str` or ``None``
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  cidr_block_subnet: :class:`str` or ``None``
        :param cidr_block_subnet: 
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: 
        :type  eni_group: :class:`str` or ``None``
        :param eni_group: 
        :type  subnet_id: :class:`str` or ``None``
        :param subnet_id: 
        :type  org_id: :class:`str` or ``None``
        :param org_id: 
        :type  sddc_id: :class:`str` or ``None``
        :param sddc_id: 
        :type  cidr_block_vpc: :class:`str` or ``None``
        :param cidr_block_vpc: 
        :type  subnet_availability_zone: :class:`str` or ``None``
        :param subnet_availability_zone: 
        :type  vpc_id: :class:`str` or ``None``
        :param vpc_id: 
        :type  is_cgw_present: :class:`bool` or ``None``
        :param is_cgw_present: 
        :type  customer_eni_infos: :class:`list` of :class:`str` or ``None``
        :param customer_eni_infos: 
        :type  default_route_table: :class:`str` or ``None``
        :param default_route_table: 
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.cidr_block_subnet = cidr_block_subnet
        self.connected_account_id = connected_account_id
        self.eni_group = eni_group
        self.subnet_id = subnet_id
        self.org_id = org_id
        self.sddc_id = sddc_id
        self.cidr_block_vpc = cidr_block_vpc
        self.subnet_availability_zone = subnet_availability_zone
        self.vpc_id = vpc_id
        self.is_cgw_present = is_cgw_present
        self.customer_eni_infos = customer_eni_infos
        self.default_route_table = default_route_table
        VapiStruct.__init__(self)

AwsSddcConnection._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_sddc_connection', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.OptionalType(type.StringType()),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'cidr_block_subnet': type.OptionalType(type.StringType()),
        'connected_account_id': type.OptionalType(type.StringType()),
        'eni_group': type.OptionalType(type.StringType()),
        'subnet_id': type.OptionalType(type.StringType()),
        'org_id': type.OptionalType(type.StringType()),
        'sddc_id': type.OptionalType(type.StringType()),
        'cidr_block_vpc': type.OptionalType(type.StringType()),
        'subnet_availability_zone': type.OptionalType(type.StringType()),
        'vpc_id': type.OptionalType(type.StringType()),
        'is_cgw_present': type.OptionalType(type.BooleanType()),
        'customer_eni_infos': type.OptionalType(type.ListType(type.StringType())),
        'default_route_table': type.OptionalType(type.StringType()),
    },
    AwsSddcConnection,
    False,
    None))



class AwsSddcResourceConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'account_link_sddc_config': 'account_link_sddc_config',
                            'public_ip_pool': 'public_ip_pool',
                            'region': 'region',
                            'vpc_info': 'vpc_info',
                            'max_num_public_ip': 'max_num_public_ip',
                            'vpc_info_peered_agent': 'vpc_info_peered_agent',
                            'backup_restore_bucket': 'backup_restore_bucket',
                            'nsxt': 'nsxt',
                            'mgw_id': 'mgw_id',
                            'nsx_mgr_url': 'nsx_mgr_url',
                            'psc_management_ip': 'psc_management_ip',
                            'psc_url': 'psc_url',
                            'cgws': 'cgws',
                            'availability_zones': 'availability_zones',
                            'management_ds': 'management_ds',
                            'custom_properties': 'custom_properties',
                            'cloud_password': 'cloud_password',
                            'provider': 'provider',
                            'clusters': 'clusters',
                            'vc_management_ip': 'vc_management_ip',
                            'sddc_networks': 'sddc_networks',
                            'cloud_username': 'cloud_username',
                            'esx_hosts': 'esx_hosts',
                            'nsx_mgr_management_ip': 'nsx_mgr_management_ip',
                            'vc_instance_id': 'vc_instance_id',
                            'esx_cluster_id': 'esx_cluster_id',
                            'vc_public_ip': 'vc_public_ip',
                            'vc_url': 'vc_url',
                            'sddc_manifest': 'sddc_manifest',
                            'vxlan_subnet': 'vxlan_subnet',
                            'cloud_user_group': 'cloud_user_group',
                            'management_rp': 'management_rp',
                            'witness_availability_zone': 'witness_availability_zone',
                            'sso_domain': 'sso_domain',
                            'deployment_type': 'deployment_type',
                            'dns_with_management_vm_private_ip': 'dns_with_management_vm_private_ip',
                            }

    def __init__(self,
                 account_link_sddc_config=None,
                 public_ip_pool=None,
                 region=None,
                 vpc_info=None,
                 max_num_public_ip=None,
                 vpc_info_peered_agent=None,
                 backup_restore_bucket=None,
                 nsxt=None,
                 mgw_id=None,
                 nsx_mgr_url=None,
                 psc_management_ip=None,
                 psc_url=None,
                 cgws=None,
                 availability_zones=None,
                 management_ds=None,
                 custom_properties=None,
                 cloud_password=None,
                 provider='AWS',
                 clusters=None,
                 vc_management_ip=None,
                 sddc_networks=None,
                 cloud_username=None,
                 esx_hosts=None,
                 nsx_mgr_management_ip=None,
                 vc_instance_id=None,
                 esx_cluster_id=None,
                 vc_public_ip=None,
                 vc_url=None,
                 sddc_manifest=None,
                 vxlan_subnet=None,
                 cloud_user_group=None,
                 management_rp=None,
                 witness_availability_zone=None,
                 sso_domain=None,
                 deployment_type=None,
                 dns_with_management_vm_private_ip=None,
                ):
        """
        :type  account_link_sddc_config: :class:`list` of :class:`SddcLinkConfig` or ``None``
        :param account_link_sddc_config: 
        :type  public_ip_pool: :class:`list` of :class:`SddcPublicIp` or ``None``
        :param public_ip_pool: 
        :type  region: :class:`str` or ``None``
        :param region: 
        :type  vpc_info: :class:`VpcInfo` or ``None``
        :param vpc_info: 
        :type  max_num_public_ip: :class:`long` or ``None``
        :param max_num_public_ip: maximum number of public IP that user can allocate.
        :type  vpc_info_peered_agent: :class:`VpcInfo` or ``None``
        :param vpc_info_peered_agent: 
        :type  backup_restore_bucket: :class:`str` or ``None``
        :param backup_restore_bucket: 
        :type  nsxt: :class:`bool` or ``None``
        :param nsxt: if true, NSX-T UI is enabled.
        :type  mgw_id: :class:`str` or ``None``
        :param mgw_id: Management Gateway Id
        :type  nsx_mgr_url: :class:`str` or ``None``
        :param nsx_mgr_url: URL of the NSX Manager
        :type  psc_management_ip: :class:`str` or ``None``
        :param psc_management_ip: PSC internal management IP
        :type  psc_url: :class:`str` or ``None``
        :param psc_url: URL of the PSC server
        :type  cgws: :class:`list` of :class:`str` or ``None``
        :param cgws: 
        :type  availability_zones: :class:`list` of :class:`str` or ``None``
        :param availability_zones: Availability zones over which esx hosts are provisioned. MultiAZ
            SDDCs will have hosts provisioned over two availability zones while
            SingleAZ SDDCs will provision over one.
        :type  management_ds: :class:`str` or ``None``
        :param management_ds: The ManagedObjectReference of the management Datastore
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  cloud_password: :class:`str` or ``None``
        :param cloud_password: Password for vCenter SDDC administrator
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`SddcResourceConfig.PROVIDER_AWS`
            
             Discriminator for additional properties
        :type  clusters: :class:`list` of :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param clusters: List of clusters in the SDDC.
            When clients pass a value of this class as a parameter, the
            attribute must contain all the attributes defined in
            :class:`Cluster`. When methods return a value of this class as a
            return value, the attribute will contain all the attributes defined
            in :class:`Cluster`.
        :type  vc_management_ip: :class:`str` or ``None``
        :param vc_management_ip: vCenter internal management IP
        :type  sddc_networks: :class:`list` of :class:`str` or ``None``
        :param sddc_networks: 
        :type  cloud_username: :class:`str` or ``None``
        :param cloud_username: Username for vCenter SDDC administrator
        :type  esx_hosts: :class:`list` of :class:`AwsEsxHost` or ``None``
        :param esx_hosts: 
        :type  nsx_mgr_management_ip: :class:`str` or ``None``
        :param nsx_mgr_management_ip: NSX Manager internal management IP
        :type  vc_instance_id: :class:`str` or ``None``
        :param vc_instance_id: unique id of the vCenter server
        :type  esx_cluster_id: :class:`str` or ``None``
        :param esx_cluster_id: Cluster Id to add ESX workflow
        :type  vc_public_ip: :class:`str` or ``None``
        :param vc_public_ip: vCenter public IP
        :type  vc_url: :class:`str` or ``None``
        :param vc_url: URL of the vCenter server
        :type  sddc_manifest: :class:`SddcManifest` or ``None``
        :param sddc_manifest: 
        :type  vxlan_subnet: :class:`str` or ``None``
        :param vxlan_subnet: VXLAN IP subnet
        :type  cloud_user_group: :class:`str` or ``None``
        :param cloud_user_group: Group name for vCenter SDDC administrator
        :type  management_rp: :class:`str` or ``None``
        :param management_rp: 
        :type  witness_availability_zone: :class:`str` or ``None``
        :param witness_availability_zone: Availability zone where the witness node is provisioned for a
            MultiAZ SDDC. This is null for a SingleAZ SDDC.
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: The SSO domain name to use for vSphere users
        :type  deployment_type: :class:`str` or ``None``
        :param deployment_type: Possible values are: 
            
            * :attr:`SddcResourceConfig.DEPLOYMENT_TYPE_SINGLEAZ`
            * :attr:`SddcResourceConfig.DEPLOYMENT_TYPE_MULTIAZ`
            
             Denotes if this is a SingleAZ SDDC or a MultiAZ SDDC.
        :type  dns_with_management_vm_private_ip: :class:`bool` or ``None``
        :param dns_with_management_vm_private_ip: if true, use the private IP addresses to register DNS records for
            the management VMs
        """
        self.account_link_sddc_config = account_link_sddc_config
        self.public_ip_pool = public_ip_pool
        self.region = region
        self.vpc_info = vpc_info
        self.max_num_public_ip = max_num_public_ip
        self.vpc_info_peered_agent = vpc_info_peered_agent
        self.backup_restore_bucket = backup_restore_bucket
        self.nsxt = nsxt
        self.mgw_id = mgw_id
        self.nsx_mgr_url = nsx_mgr_url
        self.psc_management_ip = psc_management_ip
        self.psc_url = psc_url
        self.cgws = cgws
        self.availability_zones = availability_zones
        self.management_ds = management_ds
        self.custom_properties = custom_properties
        self.cloud_password = cloud_password
        self.provider = provider
        self.clusters = clusters
        self.vc_management_ip = vc_management_ip
        self.sddc_networks = sddc_networks
        self.cloud_username = cloud_username
        self.esx_hosts = esx_hosts
        self.nsx_mgr_management_ip = nsx_mgr_management_ip
        self.vc_instance_id = vc_instance_id
        self.esx_cluster_id = esx_cluster_id
        self.vc_public_ip = vc_public_ip
        self.vc_url = vc_url
        self.sddc_manifest = sddc_manifest
        self.vxlan_subnet = vxlan_subnet
        self.cloud_user_group = cloud_user_group
        self.management_rp = management_rp
        self.witness_availability_zone = witness_availability_zone
        self.sso_domain = sso_domain
        self.deployment_type = deployment_type
        self.dns_with_management_vm_private_ip = dns_with_management_vm_private_ip
        VapiStruct.__init__(self)

AwsSddcResourceConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_sddc_resource_config', {
        'account_link_sddc_config': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcLinkConfig'))),
        'public_ip_pool': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcPublicIp'))),
        'region': type.OptionalType(type.StringType()),
        'vpc_info': type.OptionalType(type.ReferenceType(__name__, 'VpcInfo')),
        'max_num_public_ip': type.OptionalType(type.IntegerType()),
        'vpc_info_peered_agent': type.OptionalType(type.ReferenceType(__name__, 'VpcInfo')),
        'backup_restore_bucket': type.OptionalType(type.StringType()),
        'nsxt': type.OptionalType(type.BooleanType()),
        'mgw_id': type.OptionalType(type.StringType()),
        'nsx_mgr_url': type.OptionalType(type.StringType()),
        'psc_management_ip': type.OptionalType(type.StringType()),
        'psc_url': type.OptionalType(type.StringType()),
        'cgws': type.OptionalType(type.ListType(type.StringType())),
        'availability_zones': type.OptionalType(type.ListType(type.StringType())),
        'management_ds': type.OptionalType(type.StringType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'cloud_password': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'clusters': type.OptionalType(type.ListType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType(__name__, 'Cluster')]))),
        'vc_management_ip': type.OptionalType(type.StringType()),
        'sddc_networks': type.OptionalType(type.ListType(type.StringType())),
        'cloud_username': type.OptionalType(type.StringType()),
        'esx_hosts': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AwsEsxHost'))),
        'nsx_mgr_management_ip': type.OptionalType(type.StringType()),
        'vc_instance_id': type.OptionalType(type.StringType()),
        'esx_cluster_id': type.OptionalType(type.StringType()),
        'vc_public_ip': type.OptionalType(type.StringType()),
        'vc_url': type.OptionalType(type.StringType()),
        'sddc_manifest': type.OptionalType(type.ReferenceType(__name__, 'SddcManifest')),
        'vxlan_subnet': type.OptionalType(type.StringType()),
        'cloud_user_group': type.OptionalType(type.StringType()),
        'management_rp': type.OptionalType(type.StringType()),
        'witness_availability_zone': type.OptionalType(type.StringType()),
        'sso_domain': type.OptionalType(type.StringType()),
        'deployment_type': type.OptionalType(type.StringType()),
        'dns_with_management_vm_private_ip': type.OptionalType(type.BooleanType()),
    },
    AwsSddcResourceConfig,
    False,
    None))



class AwsSubnet(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'connected_account_id': 'connected_account_id',
                            'region_name': 'region_name',
                            'availability_zone': 'availability_zone',
                            'subnet_id': 'subnet_id',
                            'subnet_cidr_block': 'subnet_cidr_block',
                            'is_compatible': 'is_compatible',
                            'vpc_id': 'vpc_id',
                            'vpc_cidr_block': 'vpc_cidr_block',
                            'name': 'name',
                            }

    def __init__(self,
                 connected_account_id=None,
                 region_name=None,
                 availability_zone=None,
                 subnet_id=None,
                 subnet_cidr_block=None,
                 is_compatible=None,
                 vpc_id=None,
                 vpc_cidr_block=None,
                 name=None,
                ):
        """
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: The connected account ID this subnet is accessible through. This is
            an internal ID formatted as a UUID specific to Skyscraper.
        :type  region_name: :class:`str` or ``None``
        :param region_name: The region this subnet is in, usually in the form of country code,
            general location, and a number (ex. us-west-2).
        :type  availability_zone: :class:`str` or ``None``
        :param availability_zone: The availability zone this subnet is in, which should be the region
            name plus one extra letter (ex. us-west-2a).
        :type  subnet_id: :class:`str` or ``None``
        :param subnet_id: The subnet ID in AWS, provided in the form 'subnet-######'.
        :type  subnet_cidr_block: :class:`str` or ``None``
        :param subnet_cidr_block: The CIDR block of the subnet, in the form of '#.#.#.#/#'.
        :type  is_compatible: :class:`bool` or ``None``
        :param is_compatible: Flag indicating whether this subnet is compatible. If true, this is
            a valid choice for the customer to deploy a SDDC in.
        :type  vpc_id: :class:`str` or ``None``
        :param vpc_id: The VPC ID the subnet resides in within AWS. Tends to be
            'vpc-#######'.
        :type  vpc_cidr_block: :class:`str` or ``None``
        :param vpc_cidr_block: The CIDR block of the VPC, in the form of '#.#.#.#/#'.
        :type  name: :class:`str` or ``None``
        :param name: Optional field (may not be provided by AWS), indicates the found
            name tag for the subnet.
        """
        self.connected_account_id = connected_account_id
        self.region_name = region_name
        self.availability_zone = availability_zone
        self.subnet_id = subnet_id
        self.subnet_cidr_block = subnet_cidr_block
        self.is_compatible = is_compatible
        self.vpc_id = vpc_id
        self.vpc_cidr_block = vpc_cidr_block
        self.name = name
        VapiStruct.__init__(self)

AwsSubnet._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_subnet', {
        'connected_account_id': type.OptionalType(type.StringType()),
        'region_name': type.OptionalType(type.StringType()),
        'availability_zone': type.OptionalType(type.StringType()),
        'subnet_id': type.OptionalType(type.StringType()),
        'subnet_cidr_block': type.OptionalType(type.StringType()),
        'is_compatible': type.OptionalType(type.BooleanType()),
        'vpc_id': type.OptionalType(type.StringType()),
        'vpc_cidr_block': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
    },
    AwsSubnet,
    False,
    None))



class CaCertificates(VapiStruct):
    """
    CA certificate list. Optional.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'caCertificate': 'ca_certificate',
                            }

    def __init__(self,
                 ca_certificate=None,
                ):
        """
        :type  ca_certificate: :class:`list` of :class:`str` or ``None``
        :param ca_certificate: 
        """
        self.ca_certificate = ca_certificate
        VapiStruct.__init__(self)

CaCertificates._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ca_certificates', {
        'caCertificate': type.OptionalType(type.ListType(type.StringType())),
    },
    CaCertificates,
    False,
    None))



class CbmStatistic(VapiStruct):
    """
    Statistics data for each vnic.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vnic': 'vnic',
                            'timestamp': 'timestamp',
                            'out': 'out',
                            'in': 'in_',
                            }

    def __init__(self,
                 vnic=None,
                 timestamp=None,
                 out=None,
                 in_=None,
                ):
        """
        :type  vnic: :class:`long` or ``None``
        :param vnic: Vnic index. format: int32
        :type  timestamp: :class:`long` or ``None``
        :param timestamp: Timestamp value. format: int64
        :type  out: :class:`float` or ``None``
        :param out: Tx rate (Kilobits per second - kbps) format: double
        :type  in_: :class:`float` or ``None``
        :param in_: Rx rate (Kilobits per second - kbps) format: double
        """
        self.vnic = vnic
        self.timestamp = timestamp
        self.out = out
        self.in_ = in_
        VapiStruct.__init__(self)

CbmStatistic._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cbm_statistic', {
        'vnic': type.OptionalType(type.IntegerType()),
        'timestamp': type.OptionalType(type.IntegerType()),
        'out': type.OptionalType(type.DoubleType()),
        'in': type.OptionalType(type.DoubleType()),
    },
    CbmStatistic,
    False,
    None))



class CbmStatistics(VapiStruct):
    """
    NSX Edge Interface Statistics.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'dataDto': 'data_dto',
                            'metaDto': 'meta_dto',
                            }

    def __init__(self,
                 data_dto=None,
                 meta_dto=None,
                ):
        """
        :type  data_dto: :class:`CbmStatsData` or ``None``
        :param data_dto: Statistics data.
        :type  meta_dto: :class:`MetaDashboardStats` or ``None``
        :param meta_dto: Start time, end time and interval details.
        """
        self.data_dto = data_dto
        self.meta_dto = meta_dto
        VapiStruct.__init__(self)

CbmStatistics._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cbm_statistics', {
        'dataDto': type.OptionalType(type.ReferenceType(__name__, 'CbmStatsData')),
        'metaDto': type.OptionalType(type.ReferenceType(__name__, 'MetaDashboardStats')),
    },
    CbmStatistics,
    False,
    None))



class CbmStatsData(VapiStruct):
    """
    Statistics data.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vnic_9': 'vnic9',
                            'vnic_8': 'vnic8',
                            'vnic_7': 'vnic7',
                            'vnic_6': 'vnic6',
                            'vnic_5': 'vnic5',
                            'vnic_4': 'vnic4',
                            'vnic_3': 'vnic3',
                            'vnic_2': 'vnic2',
                            'vnic_1': 'vnic1',
                            'vnic_0': 'vnic0',
                            }

    def __init__(self,
                 vnic9=None,
                 vnic8=None,
                 vnic7=None,
                 vnic6=None,
                 vnic5=None,
                 vnic4=None,
                 vnic3=None,
                 vnic2=None,
                 vnic1=None,
                 vnic0=None,
                ):
        """
        :type  vnic9: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic9: 
        :type  vnic8: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic8: 
        :type  vnic7: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic7: 
        :type  vnic6: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic6: 
        :type  vnic5: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic5: 
        :type  vnic4: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic4: 
        :type  vnic3: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic3: 
        :type  vnic2: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic2: 
        :type  vnic1: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic1: 
        :type  vnic0: :class:`list` of :class:`CbmStatistic` or ``None``
        :param vnic0: 
        """
        self.vnic9 = vnic9
        self.vnic8 = vnic8
        self.vnic7 = vnic7
        self.vnic6 = vnic6
        self.vnic5 = vnic5
        self.vnic4 = vnic4
        self.vnic3 = vnic3
        self.vnic2 = vnic2
        self.vnic1 = vnic1
        self.vnic0 = vnic0
        VapiStruct.__init__(self)

CbmStatsData._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cbm_stats_data', {
        'vnic_9': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_8': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_7': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_6': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_5': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_4': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_3': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_2': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_1': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
        'vnic_0': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'CbmStatistic'))),
    },
    CbmStatsData,
    False,
    None))



class CloudProvider(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "CloudProvider"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'provider': 'provider',
                            }

    def __init__(self,
                 provider='CloudProvider',
                ):
        """
        :type  provider: :class:`str`
        :param provider: Name of the Cloud Provider
        """
        self.provider = provider
        VapiStruct.__init__(self)

CloudProvider._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cloud_provider', {
        'provider': type.StringType(),
    },
    CloudProvider,
    False,
    None))



class Cluster(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "Cluster"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    CLUSTER_STATE_DEPLOYING = "DEPLOYING"
    """


    """
    CLUSTER_STATE_ADDING_HOSTS = "ADDING_HOSTS"
    """


    """
    CLUSTER_STATE_READY = "READY"
    """


    """
    CLUSTER_STATE_FAILED = "FAILED"
    """


    """



    _canonical_to_pep_names = {
                            'cluster_name': 'cluster_name',
                            'esx_host_list': 'esx_host_list',
                            'cluster_id': 'cluster_id',
                            'cluster_state': 'cluster_state',
                            }

    def __init__(self,
                 cluster_name=None,
                 esx_host_list=None,
                 cluster_id='Cluster',
                 cluster_state=None,
                ):
        """
        :type  cluster_name: :class:`str` or ``None``
        :param cluster_name: 
        :type  esx_host_list: :class:`list` of :class:`AwsEsxHost` or ``None``
        :param esx_host_list: 
        :type  cluster_id: :class:`str`
        :param cluster_id: 
        :type  cluster_state: :class:`str` or ``None``
        :param cluster_state: Possible values are: 
            
            * :attr:`Cluster.CLUSTER_STATE_DEPLOYING`
            * :attr:`Cluster.CLUSTER_STATE_ADDING_HOSTS`
            * :attr:`Cluster.CLUSTER_STATE_READY`
            * :attr:`Cluster.CLUSTER_STATE_FAILED`
        """
        self.cluster_name = cluster_name
        self.esx_host_list = esx_host_list
        self.cluster_id = cluster_id
        self.cluster_state = cluster_state
        VapiStruct.__init__(self)

Cluster._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cluster', {
        'cluster_name': type.OptionalType(type.StringType()),
        'esx_host_list': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AwsEsxHost'))),
        'cluster_id': type.StringType(),
        'cluster_state': type.OptionalType(type.StringType()),
    },
    Cluster,
    False,
    None))



class ClusterConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'num_hosts': 'num_hosts',
                            }

    def __init__(self,
                 num_hosts=None,
                ):
        """
        :type  num_hosts: :class:`long`
        :param num_hosts: 
        """
        self.num_hosts = num_hosts
        VapiStruct.__init__(self)

ClusterConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cluster_config', {
        'num_hosts': type.IntegerType(),
    },
    ClusterConfig,
    False,
    None))



class ComputeGatewayTemplate(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'public_ip': 'public_ip',
                            'primary_dns': 'primary_dns',
                            'secondary_dns': 'secondary_dns',
                            'firewall_rules': 'firewall_rules',
                            'vpns': 'vpns',
                            'logical_networks': 'logical_networks',
                            'nat_rules': 'nat_rules',
                            'l2_vpn': 'l2_vpn',
                            }

    def __init__(self,
                 public_ip=None,
                 primary_dns=None,
                 secondary_dns=None,
                 firewall_rules=None,
                 vpns=None,
                 logical_networks=None,
                 nat_rules=None,
                 l2_vpn=None,
                ):
        """
        :type  public_ip: :class:`SddcPublicIp` or ``None``
        :param public_ip: 
        :type  primary_dns: :class:`str` or ``None``
        :param primary_dns: 
        :type  secondary_dns: :class:`str` or ``None``
        :param secondary_dns: 
        :type  firewall_rules: :class:`list` of :class:`FirewallRule` or ``None``
        :param firewall_rules: 
        :type  vpns: :class:`list` of :class:`Vpn` or ``None``
        :param vpns: 
        :type  logical_networks: :class:`list` of :class:`LogicalNetwork` or ``None``
        :param logical_networks: 
        :type  nat_rules: :class:`list` of :class:`NatRule` or ``None``
        :param nat_rules: 
        :type  l2_vpn: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param l2_vpn: 
        """
        self.public_ip = public_ip
        self.primary_dns = primary_dns
        self.secondary_dns = secondary_dns
        self.firewall_rules = firewall_rules
        self.vpns = vpns
        self.logical_networks = logical_networks
        self.nat_rules = nat_rules
        self.l2_vpn = l2_vpn
        VapiStruct.__init__(self)

ComputeGatewayTemplate._set_binding_type(type.StructType(
    'com.vmware.vmc.model.compute_gateway_template', {
        'public_ip': type.OptionalType(type.ReferenceType(__name__, 'SddcPublicIp')),
        'primary_dns': type.OptionalType(type.StringType()),
        'secondary_dns': type.OptionalType(type.StringType()),
        'firewall_rules': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'FirewallRule'))),
        'vpns': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Vpn'))),
        'logical_networks': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'LogicalNetwork'))),
        'nat_rules': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'NatRule'))),
        'l2_vpn': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    ComputeGatewayTemplate,
    False,
    None))



class CrlCertificates(VapiStruct):
    """
    CRL certificate list. Optional.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'crlCertificate': 'crl_certificate',
                            }

    def __init__(self,
                 crl_certificate=None,
                ):
        """
        :type  crl_certificate: :class:`list` of :class:`str` or ``None``
        :param crl_certificate: 
        """
        self.crl_certificate = crl_certificate
        VapiStruct.__init__(self)

CrlCertificates._set_binding_type(type.StructType(
    'com.vmware.vmc.model.crl_certificates', {
        'crlCertificate': type.OptionalType(type.ListType(type.StringType())),
    },
    CrlCertificates,
    False,
    None))



class DashboardData(VapiStruct):
    """
    Dashboard Statistics data.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'firewall': 'firewall',
                            'sslvpn': 'sslvpn',
                            'interfaces': 'interfaces',
                            'loadBalancer': 'load_balancer',
                            'ipsec': 'ipsec',
                            }

    def __init__(self,
                 firewall=None,
                 sslvpn=None,
                 interfaces=None,
                 load_balancer=None,
                 ipsec=None,
                ):
        """
        :type  firewall: :class:`FirewallDashboardStats` or ``None``
        :param firewall: NSX Edge Firewall Statistics data.
        :type  sslvpn: :class:`SslvpnDashboardStats` or ``None``
        :param sslvpn: NSX Edge SSL VPN Statistics data.
        :type  interfaces: :class:`InterfacesDashboardStats` or ``None``
        :param interfaces: NSX Edge Interface Statistics data.
        :type  load_balancer: :class:`LoadBalancerDashboardStats` or ``None``
        :param load_balancer: NSX Edge Load Balancer Statistics data.
        :type  ipsec: :class:`IpsecDashboardStats` or ``None``
        :param ipsec: NSX Edge Ipsec Statistics data.
        """
        self.firewall = firewall
        self.sslvpn = sslvpn
        self.interfaces = interfaces
        self.load_balancer = load_balancer
        self.ipsec = ipsec
        VapiStruct.__init__(self)

DashboardData._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dashboard_data', {
        'firewall': type.OptionalType(type.ReferenceType(__name__, 'FirewallDashboardStats')),
        'sslvpn': type.OptionalType(type.ReferenceType(__name__, 'SslvpnDashboardStats')),
        'interfaces': type.OptionalType(type.ReferenceType(__name__, 'InterfacesDashboardStats')),
        'loadBalancer': type.OptionalType(type.ReferenceType(__name__, 'LoadBalancerDashboardStats')),
        'ipsec': type.OptionalType(type.ReferenceType(__name__, 'IpsecDashboardStats')),
    },
    DashboardData,
    False,
    None))



class DashboardStat(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timestamp': 'timestamp',
                            'value': 'value',
                            }

    def __init__(self,
                 timestamp=None,
                 value=None,
                ):
        """
        :type  timestamp: :class:`long` or ``None``
        :param timestamp: 
        :type  value: :class:`float` or ``None``
        :param value: 
        """
        self.timestamp = timestamp
        self.value = value
        VapiStruct.__init__(self)

DashboardStat._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dashboard_stat', {
        'timestamp': type.OptionalType(type.IntegerType()),
        'value': type.OptionalType(type.DoubleType()),
    },
    DashboardStat,
    False,
    None))



class DashboardStatistics(VapiStruct):
    """
    Dashboard Statistics data.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'dataDto': 'data_dto',
                            'metaDto': 'meta_dto',
                            }

    def __init__(self,
                 data_dto=None,
                 meta_dto=None,
                ):
        """
        :type  data_dto: :class:`DashboardData` or ``None``
        :param data_dto: Dashboard Statistics data.
        :type  meta_dto: :class:`MetaDashboardStats` or ``None``
        :param meta_dto: Start time, end time and interval details.
        """
        self.data_dto = data_dto
        self.meta_dto = meta_dto
        VapiStruct.__init__(self)

DashboardStatistics._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dashboard_statistics', {
        'dataDto': type.OptionalType(type.ReferenceType(__name__, 'DashboardData')),
        'metaDto': type.OptionalType(type.ReferenceType(__name__, 'MetaDashboardStats')),
    },
    DashboardStatistics,
    False,
    None))



class DataPageEdgeSummary(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'pagingInfo': 'paging_info',
                            'data': 'data',
                            }

    def __init__(self,
                 paging_info=None,
                 data=None,
                ):
        """
        :type  paging_info: :class:`PagingInfo` or ``None``
        :param paging_info: 
        :type  data: :class:`list` of :class:`EdgeSummary` or ``None``
        :param data: 
        """
        self.paging_info = paging_info
        self.data = data
        VapiStruct.__init__(self)

DataPageEdgeSummary._set_binding_type(type.StructType(
    'com.vmware.vmc.model.data_page_edge_summary', {
        'pagingInfo': type.OptionalType(type.ReferenceType(__name__, 'PagingInfo')),
        'data': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'EdgeSummary'))),
    },
    DataPageEdgeSummary,
    False,
    None))



class DataPageSddcNetwork(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'pagingInfo': 'paging_info',
                            'data': 'data',
                            }

    def __init__(self,
                 paging_info=None,
                 data=None,
                ):
        """
        :type  paging_info: :class:`PagingInfo` or ``None``
        :param paging_info: 
        :type  data: :class:`list` of :class:`SddcNetwork` or ``None``
        :param data: 
        """
        self.paging_info = paging_info
        self.data = data
        VapiStruct.__init__(self)

DataPageSddcNetwork._set_binding_type(type.StructType(
    'com.vmware.vmc.model.data_page_sddc_network', {
        'pagingInfo': type.OptionalType(type.ReferenceType(__name__, 'PagingInfo')),
        'data': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcNetwork'))),
    },
    DataPageSddcNetwork,
    False,
    None))



class DataPermissions(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'savePermission': 'save_permission',
                            'publishPermission': 'publish_permission',
                            }

    def __init__(self,
                 save_permission=None,
                 publish_permission=None,
                ):
        """
        :type  save_permission: :class:`bool` or ``None``
        :param save_permission: 
        :type  publish_permission: :class:`bool` or ``None``
        :param publish_permission: 
        """
        self.save_permission = save_permission
        self.publish_permission = publish_permission
        VapiStruct.__init__(self)

DataPermissions._set_binding_type(type.StructType(
    'com.vmware.vmc.model.data_permissions', {
        'savePermission': type.OptionalType(type.BooleanType()),
        'publishPermission': type.OptionalType(type.BooleanType()),
    },
    DataPermissions,
    False,
    None))



class DhcpLeaseInfo(VapiStruct):
    """
    DHCP lease information.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'hostLeaseInfoDtos': 'host_lease_info_dtos',
                            }

    def __init__(self,
                 host_lease_info_dtos=None,
                ):
        """
        :type  host_lease_info_dtos: :class:`list` of :class:`HostLeaseInfo` or ``None``
        :param host_lease_info_dtos: List of DHCP leases.
        """
        self.host_lease_info_dtos = host_lease_info_dtos
        VapiStruct.__init__(self)

DhcpLeaseInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dhcp_lease_info', {
        'hostLeaseInfoDtos': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'HostLeaseInfo'))),
    },
    DhcpLeaseInfo,
    False,
    None))



class DhcpLeases(VapiStruct):
    """
    DHCP leases information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timeStamp': 'time_stamp',
                            'hostLeaseInfosDto': 'host_lease_infos_dto',
                            }

    def __init__(self,
                 time_stamp=None,
                 host_lease_infos_dto=None,
                ):
        """
        :type  time_stamp: :class:`long` or ``None``
        :param time_stamp: The timestamp of the DHCP lease. format: int64
        :type  host_lease_infos_dto: :class:`DhcpLeaseInfo` or ``None``
        :param host_lease_infos_dto: DHCP lease information.
        """
        self.time_stamp = time_stamp
        self.host_lease_infos_dto = host_lease_infos_dto
        VapiStruct.__init__(self)

DhcpLeases._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dhcp_leases', {
        'timeStamp': type.OptionalType(type.IntegerType()),
        'hostLeaseInfosDto': type.OptionalType(type.ReferenceType(__name__, 'DhcpLeaseInfo')),
    },
    DhcpLeases,
    False,
    None))



class DnsConfig(VapiStruct):
    """
    DNS configuration

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'featureType': 'feature_type',
                            'logging': 'logging',
                            'enabled': 'enabled',
                            'dnsViews': 'dns_views',
                            'listeners': 'listeners',
                            'version': 'version',
                            'template': 'template',
                            'cacheSize': 'cache_size',
                            'dnsServers': 'dns_servers',
                            }

    def __init__(self,
                 feature_type=None,
                 logging=None,
                 enabled=None,
                 dns_views=None,
                 listeners=None,
                 version=None,
                 template=None,
                 cache_size=None,
                 dns_servers=None,
                ):
        """
        :type  feature_type: :class:`str` or ``None``
        :param feature_type: 
        :type  logging: :class:`Logging` or ``None``
        :param logging: DNS logging setting.
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Value is true if feature is enabled. Default value is true.
            Optional.
        :type  dns_views: :class:`DnsViews` or ``None``
        :param dns_views: List of DNS views.
        :type  listeners: :class:`DnsListeners` or ``None``
        :param listeners: List of DNS listeners.
        :type  version: :class:`long` or ``None``
        :param version: Version number tracking each configuration change. To avoid
            problems with overwriting changes, always retrieve and modify the
            latest configuration to include the current version number in your
            request. If you provide a version number which is not current, the
            request is rejected. If you omit the version number, the request is
            accepted but may overwrite any current changes if your change is
            not in sync with the latest change. format: int64
        :type  template: :class:`str` or ``None``
        :param template: 
        :type  cache_size: :class:`long` or ``None``
        :param cache_size: The cache size of the DNS service. format: int64
        :type  dns_servers: :class:`IpAddresses` or ``None``
        :param dns_servers: 
        """
        self.feature_type = feature_type
        self.logging = logging
        self.enabled = enabled
        self.dns_views = dns_views
        self.listeners = listeners
        self.version = version
        self.template = template
        self.cache_size = cache_size
        self.dns_servers = dns_servers
        VapiStruct.__init__(self)

DnsConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dns_config', {
        'featureType': type.OptionalType(type.StringType()),
        'logging': type.OptionalType(type.ReferenceType(__name__, 'Logging')),
        'enabled': type.OptionalType(type.BooleanType()),
        'dnsViews': type.OptionalType(type.ReferenceType(__name__, 'DnsViews')),
        'listeners': type.OptionalType(type.ReferenceType(__name__, 'DnsListeners')),
        'version': type.OptionalType(type.IntegerType()),
        'template': type.OptionalType(type.StringType()),
        'cacheSize': type.OptionalType(type.IntegerType()),
        'dnsServers': type.OptionalType(type.ReferenceType(__name__, 'IpAddresses')),
    },
    DnsConfig,
    False,
    None))



class DnsForwarders(VapiStruct):
    """
    DNS forwarders.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ipAddress': 'ip_address',
                            }

    def __init__(self,
                 ip_address=None,
                ):
        """
        :type  ip_address: :class:`list` of :class:`str` or ``None``
        :param ip_address: IP addresses of the DNS servers.
        """
        self.ip_address = ip_address
        VapiStruct.__init__(self)

DnsForwarders._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dns_forwarders', {
        'ipAddress': type.OptionalType(type.ListType(type.StringType())),
    },
    DnsForwarders,
    False,
    None))



class DnsListeners(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ipAddress': 'ip_address',
                            'vnic': 'vnic',
                            'type': 'type',
                            }

    def __init__(self,
                 ip_address=None,
                 vnic=None,
                 type=None,
                ):
        """
        :type  ip_address: :class:`list` of :class:`str` or ``None``
        :param ip_address: List of IP addresses.
        :type  vnic: :class:`list` of :class:`str` or ``None``
        :param vnic: Vnic for DNS listener.
        :type  type: :class:`str` or ``None``
        :param type: 
        """
        self.ip_address = ip_address
        self.vnic = vnic
        self.type = type
        VapiStruct.__init__(self)

DnsListeners._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dns_listeners', {
        'ipAddress': type.OptionalType(type.ListType(type.StringType())),
        'vnic': type.OptionalType(type.ListType(type.StringType())),
        'type': type.OptionalType(type.StringType()),
    },
    DnsListeners,
    False,
    None))



class DnsResponseStats(VapiStruct):
    """
    DNS response statistics.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'total': 'total',
                            'formErr': 'form_err',
                            'nxDomain': 'nx_domain',
                            'success': 'success',
                            'serverFail': 'server_fail',
                            'nxrrset': 'nxrrset',
                            'others': 'others',
                            }

    def __init__(self,
                 total=None,
                 form_err=None,
                 nx_domain=None,
                 success=None,
                 server_fail=None,
                 nxrrset=None,
                 others=None,
                ):
        """
        :type  total: :class:`long` or ``None``
        :param total: 
        :type  form_err: :class:`long` or ``None``
        :param form_err: 
        :type  nx_domain: :class:`long` or ``None``
        :param nx_domain: 
        :type  success: :class:`long` or ``None``
        :param success: 
        :type  server_fail: :class:`long` or ``None``
        :param server_fail: 
        :type  nxrrset: :class:`long` or ``None``
        :param nxrrset: 
        :type  others: :class:`long` or ``None``
        :param others: 
        """
        self.total = total
        self.form_err = form_err
        self.nx_domain = nx_domain
        self.success = success
        self.server_fail = server_fail
        self.nxrrset = nxrrset
        self.others = others
        VapiStruct.__init__(self)

DnsResponseStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dns_response_stats', {
        'total': type.OptionalType(type.IntegerType()),
        'formErr': type.OptionalType(type.IntegerType()),
        'nxDomain': type.OptionalType(type.IntegerType()),
        'success': type.OptionalType(type.IntegerType()),
        'serverFail': type.OptionalType(type.IntegerType()),
        'nxrrset': type.OptionalType(type.IntegerType()),
        'others': type.OptionalType(type.IntegerType()),
    },
    DnsResponseStats,
    False,
    None))



class DnsStatusAndStats(VapiStruct):
    """
    DNS statistics.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timeStamp': 'time_stamp',
                            'requests': 'requests',
                            'responses': 'responses',
                            'cachedDBRRSet': 'cached_dbrr_set',
                            }

    def __init__(self,
                 time_stamp=None,
                 requests=None,
                 responses=None,
                 cached_dbrr_set=None,
                ):
        """
        :type  time_stamp: :class:`long` or ``None``
        :param time_stamp: 
        :type  requests: :class:`Requests` or ``None``
        :param requests: 
        :type  responses: :class:`DnsResponseStats` or ``None``
        :param responses: 
        :type  cached_dbrr_set: :class:`long` or ``None``
        :param cached_dbrr_set: 
        """
        self.time_stamp = time_stamp
        self.requests = requests
        self.responses = responses
        self.cached_dbrr_set = cached_dbrr_set
        VapiStruct.__init__(self)

DnsStatusAndStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dns_status_and_stats', {
        'timeStamp': type.OptionalType(type.IntegerType()),
        'requests': type.OptionalType(type.ReferenceType(__name__, 'Requests')),
        'responses': type.OptionalType(type.ReferenceType(__name__, 'DnsResponseStats')),
        'cachedDBRRSet': type.OptionalType(type.IntegerType()),
    },
    DnsStatusAndStats,
    False,
    None))



class DnsView(VapiStruct):
    """
    DNS View

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'name': 'name',
                            'viewMatch': 'view_match',
                            'recursion': 'recursion',
                            'viewId': 'view_id',
                            'forwarders': 'forwarders',
                            'enabled': 'enabled',
                            }

    def __init__(self,
                 name=None,
                 view_match=None,
                 recursion=None,
                 view_id=None,
                 forwarders=None,
                 enabled=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the DNS view.
        :type  view_match: :class:`DnsViewMatch` or ``None``
        :param view_match: Rules that match the DNS query to this view. The rule can be
            ipAddress, or ipSet. Defaults to ipAddress 'any' and 'any' vnic.
        :type  recursion: :class:`bool` or ``None``
        :param recursion: Recursion enabled on DNS view.
        :type  view_id: :class:`str` or ``None``
        :param view_id: Identifier for the DNS view.
        :type  forwarders: :class:`DnsForwarders` or ``None``
        :param forwarders: DNS forwarders.
        :type  enabled: :class:`bool` or ``None``
        :param enabled: DNS view is enabled.
        """
        self.name = name
        self.view_match = view_match
        self.recursion = recursion
        self.view_id = view_id
        self.forwarders = forwarders
        self.enabled = enabled
        VapiStruct.__init__(self)

DnsView._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dns_view', {
        'name': type.StringType(),
        'viewMatch': type.OptionalType(type.ReferenceType(__name__, 'DnsViewMatch')),
        'recursion': type.OptionalType(type.BooleanType()),
        'viewId': type.OptionalType(type.StringType()),
        'forwarders': type.OptionalType(type.ReferenceType(__name__, 'DnsForwarders')),
        'enabled': type.OptionalType(type.BooleanType()),
    },
    DnsView,
    False,
    None))



class DnsViewMatch(VapiStruct):
    """
    Dns view match

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vnic': 'vnic',
                            'ipSet': 'ip_set',
                            'ipAddress': 'ip_address',
                            }

    def __init__(self,
                 vnic=None,
                 ip_set=None,
                 ip_address=None,
                ):
        """
        :type  vnic: :class:`list` of :class:`str` or ``None``
        :param vnic: 
        :type  ip_set: :class:`list` of :class:`str` or ``None``
        :param ip_set: 
        :type  ip_address: :class:`list` of :class:`str` or ``None``
        :param ip_address: 
        """
        self.vnic = vnic
        self.ip_set = ip_set
        self.ip_address = ip_address
        VapiStruct.__init__(self)

DnsViewMatch._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dns_view_match', {
        'vnic': type.OptionalType(type.ListType(type.StringType())),
        'ipSet': type.OptionalType(type.ListType(type.StringType())),
        'ipAddress': type.OptionalType(type.ListType(type.StringType())),
    },
    DnsViewMatch,
    False,
    None))



class DnsViews(VapiStruct):
    """
    DNS views.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'dnsView': 'dns_view',
                            }

    def __init__(self,
                 dns_view=None,
                ):
        """
        :type  dns_view: :class:`list` of :class:`DnsView` or ``None``
        :param dns_view: List of DNS views.
        """
        self.dns_view = dns_view
        VapiStruct.__init__(self)

DnsViews._set_binding_type(type.StructType(
    'com.vmware.vmc.model.dns_views', {
        'dnsView': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DnsView'))),
    },
    DnsViews,
    False,
    None))



class EdgeJob(VapiStruct):
    """
    Job status information for the configuration change carried out on NSX
    Edge.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'status': 'status',
                            'edgeId': 'edge_id',
                            'module': 'module',
                            'jobId': 'job_id',
                            'errorCode': 'error_code',
                            'result': 'result',
                            'startTime': 'start_time',
                            'message': 'message',
                            'endTime': 'end_time',
                            }

    def __init__(self,
                 status=None,
                 edge_id=None,
                 module=None,
                 job_id=None,
                 error_code=None,
                 result=None,
                 start_time=None,
                 message=None,
                 end_time=None,
                ):
        """
        :type  status: :class:`str` or ``None``
        :param status: Job status.
        :type  edge_id: :class:`str` or ``None``
        :param edge_id: NSX Edge ID.
        :type  module: :class:`str` or ``None``
        :param module: Module information.
        :type  job_id: :class:`str` or ``None``
        :param job_id: Job ID.
        :type  error_code: :class:`str` or ``None``
        :param error_code: Error code identifying the failure of the configuration change.
        :type  result: :class:`list` of :class:`Result` or ``None``
        :param result: Job result information.
        :type  start_time: :class:`datetime.datetime` or ``None``
        :param start_time: Job start time. format: date-time
        :type  message: :class:`str` or ``None``
        :param message: Job message.
        :type  end_time: :class:`datetime.datetime` or ``None``
        :param end_time: Job end time. format: date-time
        """
        self.status = status
        self.edge_id = edge_id
        self.module = module
        self.job_id = job_id
        self.error_code = error_code
        self.result = result
        self.start_time = start_time
        self.message = message
        self.end_time = end_time
        VapiStruct.__init__(self)

EdgeJob._set_binding_type(type.StructType(
    'com.vmware.vmc.model.edge_job', {
        'status': type.OptionalType(type.StringType()),
        'edgeId': type.OptionalType(type.StringType()),
        'module': type.OptionalType(type.StringType()),
        'jobId': type.OptionalType(type.StringType()),
        'errorCode': type.OptionalType(type.StringType()),
        'result': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Result'))),
        'startTime': type.OptionalType(type.DateTimeType()),
        'message': type.OptionalType(type.StringType()),
        'endTime': type.OptionalType(type.DateTimeType()),
    },
    EdgeJob,
    False,
    None))



class EdgeStatus(VapiStruct):
    """
    NSX Edge Appliance status.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'preRulesExists': 'pre_rules_exists',
                            'featureStatuses': 'feature_statuses',
                            'timestamp': 'timestamp',
                            'publishStatus': 'publish_status',
                            'lastPublishedPreRulesGenerationNumber': 'last_published_pre_rules_generation_number',
                            'version': 'version',
                            'edgeVmStatus': 'edge_vm_status',
                            'activeVseHaIndex': 'active_vse_ha_index',
                            'systemStatus': 'system_status',
                            'haVnicInUse': 'ha_vnic_in_use',
                            'edgeStatus': 'edge_status',
                            }

    def __init__(self,
                 pre_rules_exists=None,
                 feature_statuses=None,
                 timestamp=None,
                 publish_status=None,
                 last_published_pre_rules_generation_number=None,
                 version=None,
                 edge_vm_status=None,
                 active_vse_ha_index=None,
                 system_status=None,
                 ha_vnic_in_use=None,
                 edge_status=None,
                ):
        """
        :type  pre_rules_exists: :class:`bool` or ``None``
        :param pre_rules_exists: Value is true if pre rules publish is enabled.
        :type  feature_statuses: :class:`list` of :class:`FeatureStatus` or ``None``
        :param feature_statuses: Individual feature status.
        :type  timestamp: :class:`long` or ``None``
        :param timestamp: Timestamp value at which the NSX Edge healthcheck was done. format:
            int64
        :type  publish_status: :class:`str` or ``None``
        :param publish_status: Status of the latest configuration change for the NSX Edge. Values
            are APPLIED or PERSISTED (not published to NSX Edge Appliance yet).
        :type  last_published_pre_rules_generation_number: :class:`long` or ``None``
        :param last_published_pre_rules_generation_number: Value of the last published pre rules generation number. format:
            int64
        :type  version: :class:`long` or ``None``
        :param version: Version number of the current configuration. format: int64
        :type  edge_vm_status: :class:`list` of :class:`EdgeVmStatus` or ``None``
        :param edge_vm_status: Detailed status of each of the deployed NSX Edge appliances.
        :type  active_vse_ha_index: :class:`long` or ``None``
        :param active_vse_ha_index: Index of the active NSX Edge appliance. Values are 0 and 1. format:
            int32
        :type  system_status: :class:`str` or ``None``
        :param system_status: System status of the active NSX Edge appliance.
        :type  ha_vnic_in_use: :class:`long` or ``None``
        :param ha_vnic_in_use: Index of the vnic consumed for NSX Edge HA. format: int32
        :type  edge_status: :class:`str` or ``None``
        :param edge_status: NSX Edge appliance health status identified by GREY (unknown
            status), GREEN (health checks are successful), YELLOW (intermittent
            health check failure), RED (none of the appliances are in serving
            state). If health check fails for 5 consecutive times for all
            appliance (2 for HA else 1) then status will turn from YELLOW to
            RED.
        """
        self.pre_rules_exists = pre_rules_exists
        self.feature_statuses = feature_statuses
        self.timestamp = timestamp
        self.publish_status = publish_status
        self.last_published_pre_rules_generation_number = last_published_pre_rules_generation_number
        self.version = version
        self.edge_vm_status = edge_vm_status
        self.active_vse_ha_index = active_vse_ha_index
        self.system_status = system_status
        self.ha_vnic_in_use = ha_vnic_in_use
        self.edge_status = edge_status
        VapiStruct.__init__(self)

EdgeStatus._set_binding_type(type.StructType(
    'com.vmware.vmc.model.edge_status', {
        'preRulesExists': type.OptionalType(type.BooleanType()),
        'featureStatuses': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'FeatureStatus'))),
        'timestamp': type.OptionalType(type.IntegerType()),
        'publishStatus': type.OptionalType(type.StringType()),
        'lastPublishedPreRulesGenerationNumber': type.OptionalType(type.IntegerType()),
        'version': type.OptionalType(type.IntegerType()),
        'edgeVmStatus': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'EdgeVmStatus'))),
        'activeVseHaIndex': type.OptionalType(type.IntegerType()),
        'systemStatus': type.OptionalType(type.StringType()),
        'haVnicInUse': type.OptionalType(type.IntegerType()),
        'edgeStatus': type.OptionalType(type.StringType()),
    },
    EdgeStatus,
    False,
    None))



class EdgeSummary(VapiStruct):
    """
    NSX Edge summary. Read only.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'featureCapabilities': 'feature_capabilities',
                            'edgeType': 'edge_type',
                            'logicalRouterScopes': 'logical_router_scopes',
                            'recentJobInfo': 'recent_job_info',
                            'hypervisorAssist': 'hypervisor_assist',
                            'edgeAssistId': 'edge_assist_id',
                            'edgeStatus': 'edge_status',
                            'edgeAssistInstanceName': 'edge_assist_instance_name',
                            'objectId': 'object_id',
                            'nodeId': 'node_id',
                            'id': 'id',
                            'datacenterName': 'datacenter_name',
                            'state': 'state',
                            'clientHandle': 'client_handle',
                            'scope': 'scope',
                            'type': 'type',
                            'revision': 'revision',
                            'vsmUuid': 'vsm_uuid',
                            'description': 'description',
                            'extendedAttributes': 'extended_attributes',
                            'localEgressEnabled': 'local_egress_enabled',
                            'universalRevision': 'universal_revision',
                            'allowedActions': 'allowed_actions',
                            'objectTypeName': 'object_type_name',
                            'isUpgradeAvailable': 'is_upgrade_available',
                            'isUniversal': 'is_universal',
                            'name': 'name',
                            'lrouterUuid': 'lrouter_uuid',
                            'appliancesSummary': 'appliances_summary',
                            'apiVersion': 'api_version',
                            'tenantId': 'tenant_id',
                            'datacenterMoid': 'datacenter_moid',
                            'numberOfConnectedVnics': 'number_of_connected_vnics',
                            }

    def __init__(self,
                 feature_capabilities=None,
                 edge_type=None,
                 logical_router_scopes=None,
                 recent_job_info=None,
                 hypervisor_assist=None,
                 edge_assist_id=None,
                 edge_status=None,
                 edge_assist_instance_name=None,
                 object_id=None,
                 node_id=None,
                 id=None,
                 datacenter_name=None,
                 state=None,
                 client_handle=None,
                 scope=None,
                 type=None,
                 revision=None,
                 vsm_uuid=None,
                 description=None,
                 extended_attributes=None,
                 local_egress_enabled=None,
                 universal_revision=None,
                 allowed_actions=None,
                 object_type_name=None,
                 is_upgrade_available=None,
                 is_universal=None,
                 name=None,
                 lrouter_uuid=None,
                 appliances_summary=None,
                 api_version=None,
                 tenant_id=None,
                 datacenter_moid=None,
                 number_of_connected_vnics=None,
                ):
        """
        :type  feature_capabilities: :class:`FeatureCapabilities` or ``None``
        :param feature_capabilities: List of Features and their capability details based on Edge
            appliance form factor.
        :type  edge_type: :class:`str` or ``None``
        :param edge_type: NSX Edge type, whether 'gatewayServices' or 'distributedRouter'.
        :type  logical_router_scopes: :class:`LogicalRouterScopes` or ``None``
        :param logical_router_scopes: Backing type scope (DistributedVirtualSwitch - VLAN, TransportZone
            -VXLAN) and its ID for the Distributed Logical Router.
        :type  recent_job_info: :class:`EdgeJob` or ``None``
        :param recent_job_info: Job information for the most recent configuration change carried
            out on the NSX Edge.
        :type  hypervisor_assist: :class:`bool` or ``None``
        :param hypervisor_assist: 
        :type  edge_assist_id: :class:`long` or ``None``
        :param edge_assist_id: ID generated by NSX Manager for Distributed Logical Router only.
            format: int64
        :type  edge_status: :class:`str` or ``None``
        :param edge_status: NSX Edge appliance health status identified by GREY (unknown
            status), GREEN (health checks are successful), YELLOW (intermittent
            health check failure), RED (none of the appliances are in serving
            state). If health check fails for 5 consecutive times for all
            appliance (2 for HA else 1) then status will turn from YELLOW to
            RED.
        :type  edge_assist_instance_name: :class:`str` or ``None``
        :param edge_assist_instance_name: Name derived by NSX Manager only for Distributed Logical Router.
        :type  object_id: :class:`str` or ``None``
        :param object_id: 
        :type  node_id: :class:`str` or ``None``
        :param node_id: 
        :type  id: :class:`str` or ``None``
        :param id: NSX Edge ID.
        :type  datacenter_name: :class:`str` or ``None``
        :param datacenter_name: Datacenter name where the NSX Edge is deployed.
        :type  state: :class:`str` or ``None``
        :param state: Deployment state of the NSX Edge appliance. Values are 'deployed'
            when VMs have been deployed, 'undeployed' when no VMs are deployed
            and 'active' when Edge type is Distributed Logical Router and has
            no appliance deployed but is serving data path.
        :type  client_handle: :class:`str` or ``None``
        :param client_handle: 
        :type  scope: :class:`ScopeInfo` or ``None``
        :param scope: 
        :type  type: :class:`ObjectType` or ``None``
        :param type: 
        :type  revision: :class:`long` or ``None``
        :param revision: 
        :type  vsm_uuid: :class:`str` or ``None``
        :param vsm_uuid: 
        :type  description: :class:`str` or ``None``
        :param description: 
        :type  extended_attributes: :class:`list` of :class:`ExtendedAttribute` or ``None``
        :param extended_attributes: 
        :type  local_egress_enabled: :class:`bool` or ``None``
        :param local_egress_enabled: Value is true if local egress is enabled for UDLR traffic.
            Applicable only for Universal Distributed Logical Router.
        :type  universal_revision: :class:`long` or ``None``
        :param universal_revision: 
        :type  allowed_actions: :class:`list` of :class:`str` or ``None``
        :param allowed_actions: 
        :type  object_type_name: :class:`str` or ``None``
        :param object_type_name: 
        :type  is_upgrade_available: :class:`bool` or ``None``
        :param is_upgrade_available: Value is true if NSX Edge upgrade is available.
        :type  is_universal: :class:`bool` or ``None``
        :param is_universal: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  lrouter_uuid: :class:`str` or ``None``
        :param lrouter_uuid: Distributed Logical Router UUID provided by the NSX Controller.
        :type  appliances_summary: :class:`AppliancesSummary` or ``None``
        :param appliances_summary: NSX Edge appliance summary.
        :type  api_version: :class:`str` or ``None``
        :param api_version: REST API version applicable for the NSX Edge.
        :type  tenant_id: :class:`str` or ``None``
        :param tenant_id: Tenant ID for the NSX Edge.
        :type  datacenter_moid: :class:`str` or ``None``
        :param datacenter_moid: vCenter MOID of the datacenter where the NSX Edge is deployed.
        :type  number_of_connected_vnics: :class:`long` or ``None``
        :param number_of_connected_vnics: Number of connected vnics that are configured on the NSX Edge.
            format: int32
        """
        self.feature_capabilities = feature_capabilities
        self.edge_type = edge_type
        self.logical_router_scopes = logical_router_scopes
        self.recent_job_info = recent_job_info
        self.hypervisor_assist = hypervisor_assist
        self.edge_assist_id = edge_assist_id
        self.edge_status = edge_status
        self.edge_assist_instance_name = edge_assist_instance_name
        self.object_id = object_id
        self.node_id = node_id
        self.id = id
        self.datacenter_name = datacenter_name
        self.state = state
        self.client_handle = client_handle
        self.scope = scope
        self.type = type
        self.revision = revision
        self.vsm_uuid = vsm_uuid
        self.description = description
        self.extended_attributes = extended_attributes
        self.local_egress_enabled = local_egress_enabled
        self.universal_revision = universal_revision
        self.allowed_actions = allowed_actions
        self.object_type_name = object_type_name
        self.is_upgrade_available = is_upgrade_available
        self.is_universal = is_universal
        self.name = name
        self.lrouter_uuid = lrouter_uuid
        self.appliances_summary = appliances_summary
        self.api_version = api_version
        self.tenant_id = tenant_id
        self.datacenter_moid = datacenter_moid
        self.number_of_connected_vnics = number_of_connected_vnics
        VapiStruct.__init__(self)

EdgeSummary._set_binding_type(type.StructType(
    'com.vmware.vmc.model.edge_summary', {
        'featureCapabilities': type.OptionalType(type.ReferenceType(__name__, 'FeatureCapabilities')),
        'edgeType': type.OptionalType(type.StringType()),
        'logicalRouterScopes': type.OptionalType(type.ReferenceType(__name__, 'LogicalRouterScopes')),
        'recentJobInfo': type.OptionalType(type.ReferenceType(__name__, 'EdgeJob')),
        'hypervisorAssist': type.OptionalType(type.BooleanType()),
        'edgeAssistId': type.OptionalType(type.IntegerType()),
        'edgeStatus': type.OptionalType(type.StringType()),
        'edgeAssistInstanceName': type.OptionalType(type.StringType()),
        'objectId': type.OptionalType(type.StringType()),
        'nodeId': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'datacenterName': type.OptionalType(type.StringType()),
        'state': type.OptionalType(type.StringType()),
        'clientHandle': type.OptionalType(type.StringType()),
        'scope': type.OptionalType(type.ReferenceType(__name__, 'ScopeInfo')),
        'type': type.OptionalType(type.ReferenceType(__name__, 'ObjectType')),
        'revision': type.OptionalType(type.IntegerType()),
        'vsmUuid': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'extendedAttributes': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ExtendedAttribute'))),
        'localEgressEnabled': type.OptionalType(type.BooleanType()),
        'universalRevision': type.OptionalType(type.IntegerType()),
        'allowedActions': type.OptionalType(type.ListType(type.StringType())),
        'objectTypeName': type.OptionalType(type.StringType()),
        'isUpgradeAvailable': type.OptionalType(type.BooleanType()),
        'isUniversal': type.OptionalType(type.BooleanType()),
        'name': type.OptionalType(type.StringType()),
        'lrouterUuid': type.OptionalType(type.StringType()),
        'appliancesSummary': type.OptionalType(type.ReferenceType(__name__, 'AppliancesSummary')),
        'apiVersion': type.OptionalType(type.StringType()),
        'tenantId': type.OptionalType(type.StringType()),
        'datacenterMoid': type.OptionalType(type.StringType()),
        'numberOfConnectedVnics': type.OptionalType(type.IntegerType()),
    },
    EdgeSummary,
    False,
    None))



class EdgeVmStatus(VapiStruct):
    """
    Status of each of the deployed NSX Edge appliances.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'index': 'index',
                            'haState': 'ha_state',
                            'name': 'name',
                            'id': 'id',
                            'edgeVMStatus': 'edge_vm_status',
                            'preRulesGenerationNumber': 'pre_rules_generation_number',
                            }

    def __init__(self,
                 index=None,
                 ha_state=None,
                 name=None,
                 id=None,
                 edge_vm_status=None,
                 pre_rules_generation_number=None,
                ):
        """
        :type  index: :class:`long` or ``None``
        :param index: High Availability index of the appliance. Values are 0 and 1.
            format: int32
        :type  ha_state: :class:`str` or ``None``
        :param ha_state: High Availability state of the appliance. Values are active and
            standby.
        :type  name: :class:`str` or ``None``
        :param name: Name of the NSX Edge appliance.
        :type  id: :class:`str` or ``None``
        :param id: vCenter MOID of the NSX Edge appliance.
        :type  edge_vm_status: :class:`str` or ``None``
        :param edge_vm_status: NSX Edge appliance health status identified by GREY (unknown
            status), GREEN (health checks are successful), YELLOW (intermittent
            health check failure), RED (appliance not in serving state).
        :type  pre_rules_generation_number: :class:`long` or ``None``
        :param pre_rules_generation_number: Value of the last published pre rules generation number. format:
            int64
        """
        self.index = index
        self.ha_state = ha_state
        self.name = name
        self.id = id
        self.edge_vm_status = edge_vm_status
        self.pre_rules_generation_number = pre_rules_generation_number
        VapiStruct.__init__(self)

EdgeVmStatus._set_binding_type(type.StructType(
    'com.vmware.vmc.model.edge_vm_status', {
        'index': type.OptionalType(type.IntegerType()),
        'haState': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'edgeVMStatus': type.OptionalType(type.StringType()),
        'preRulesGenerationNumber': type.OptionalType(type.IntegerType()),
    },
    EdgeVmStatus,
    False,
    None))



class EdgeVnicAddressGroup(VapiStruct):
    """
    Address group configuration of the NSX Edge vnic. An interface can have one
    primary and multiple secondary IP addresses.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'subnetPrefixLength': 'subnet_prefix_length',
                            'secondaryAddresses': 'secondary_addresses',
                            'primaryAddress': 'primary_address',
                            'subnetMask': 'subnet_mask',
                            }

    def __init__(self,
                 subnet_prefix_length=None,
                 secondary_addresses=None,
                 primary_address=None,
                 subnet_mask=None,
                ):
        """
        :type  subnet_prefix_length: :class:`str` or ``None``
        :param subnet_prefix_length: Subnet prefix length of the primary IP address.
        :type  secondary_addresses: :class:`SecondaryAddresses` or ``None``
        :param secondary_addresses: Secondary IP addresses of the NSX Edge vnic address group.
            Optional.
        :type  primary_address: :class:`str` or ``None``
        :param primary_address: Primary IP address of the vnic interface. Required.
        :type  subnet_mask: :class:`str` or ``None``
        :param subnet_mask: 
        """
        self.subnet_prefix_length = subnet_prefix_length
        self.secondary_addresses = secondary_addresses
        self.primary_address = primary_address
        self.subnet_mask = subnet_mask
        VapiStruct.__init__(self)

EdgeVnicAddressGroup._set_binding_type(type.StructType(
    'com.vmware.vmc.model.edge_vnic_address_group', {
        'subnetPrefixLength': type.OptionalType(type.StringType()),
        'secondaryAddresses': type.OptionalType(type.ReferenceType(__name__, 'SecondaryAddresses')),
        'primaryAddress': type.OptionalType(type.StringType()),
        'subnetMask': type.OptionalType(type.StringType()),
    },
    EdgeVnicAddressGroup,
    False,
    None))



class EdgeVnicAddressGroups(VapiStruct):
    """
    NSX Edge vnic address group configuration details.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'addressGroups': 'address_groups',
                            }

    def __init__(self,
                 address_groups=None,
                ):
        """
        :type  address_groups: :class:`list` of :class:`EdgeVnicAddressGroup` or ``None``
        :param address_groups: Address group configuration of the NSX Edge vnic. Vnic can be
            configured to have more than one address group/subnets.
        """
        self.address_groups = address_groups
        VapiStruct.__init__(self)

EdgeVnicAddressGroups._set_binding_type(type.StructType(
    'com.vmware.vmc.model.edge_vnic_address_groups', {
        'addressGroups': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'EdgeVnicAddressGroup'))),
    },
    EdgeVnicAddressGroups,
    False,
    None))



class ErrorResponse(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'status': 'status',
                            'path': 'path',
                            'retryable': 'retryable',
                            'error_code': 'error_code',
                            'error_messages': 'error_messages',
                            }

    def __init__(self,
                 status=None,
                 path=None,
                 retryable=None,
                 error_code=None,
                 error_messages=None,
                ):
        """
        :type  status: :class:`long`
        :param status: HTTP status code
        :type  path: :class:`str`
        :param path: Originating request URI
        :type  retryable: :class:`bool`
        :param retryable: If true, client should retry operation
        :type  error_code: :class:`str`
        :param error_code: unique error code
        :type  error_messages: :class:`list` of :class:`str`
        :param error_messages: localized error messages
        """
        self.status = status
        self.path = path
        self.retryable = retryable
        self.error_code = error_code
        self.error_messages = error_messages
        VapiStruct.__init__(self)

ErrorResponse._set_binding_type(type.StructType(
    'com.vmware.vmc.model.error_response', {
        'status': type.IntegerType(),
        'path': type.StringType(),
        'retryable': type.BooleanType(),
        'error_code': type.StringType(),
        'error_messages': type.ListType(type.StringType()),
    },
    ErrorResponse,
    False,
    None))



class EsxConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'num_hosts': 'num_hosts',
                            'availability_zone': 'availability_zone',
                            }

    def __init__(self,
                 num_hosts=None,
                 availability_zone=None,
                ):
        """
        :type  num_hosts: :class:`long`
        :param num_hosts: 
        :type  availability_zone: :class:`str` or ``None``
        :param availability_zone: Availability zone where the hosts should be provisioned. (Can be
            specified only for privileged host operations).
        """
        self.num_hosts = num_hosts
        self.availability_zone = availability_zone
        VapiStruct.__init__(self)

EsxConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.esx_config', {
        'num_hosts': type.IntegerType(),
        'availability_zone': type.OptionalType(type.StringType()),
    },
    EsxConfig,
    False,
    None))



class EsxHost(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "EsxHost"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    ESX_STATE_DEPLOYING = "DEPLOYING"
    """


    """
    ESX_STATE_PROVISIONED = "PROVISIONED"
    """


    """
    ESX_STATE_READY = "READY"
    """


    """
    ESX_STATE_DELETING = "DELETING"
    """


    """
    ESX_STATE_DELETED = "DELETED"
    """


    """
    ESX_STATE_FAILED = "FAILED"
    """


    """



    _canonical_to_pep_names = {
                            'name': 'name',
                            'availability_zone': 'availability_zone',
                            'esx_id': 'esx_id',
                            'hostname': 'hostname',
                            'provider': 'provider',
                            'mac_address': 'mac_address',
                            'custom_properties': 'custom_properties',
                            'esx_state': 'esx_state',
                            }

    def __init__(self,
                 name=None,
                 availability_zone=None,
                 esx_id=None,
                 hostname=None,
                 provider='EsxHost',
                 mac_address=None,
                 custom_properties=None,
                 esx_state=None,
                ):
        """
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  availability_zone: :class:`str` or ``None``
        :param availability_zone: Availability zone where the host is provisioned.
        :type  esx_id: :class:`str` or ``None``
        :param esx_id: 
        :type  hostname: :class:`str` or ``None``
        :param hostname: 
        :type  provider: :class:`str`
        :param provider: 
        :type  mac_address: :class:`str` or ``None``
        :param mac_address: 
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  esx_state: :class:`str` or ``None``
        :param esx_state: Possible values are: 
            
            * :attr:`EsxHost.ESX_STATE_DEPLOYING`
            * :attr:`EsxHost.ESX_STATE_PROVISIONED`
            * :attr:`EsxHost.ESX_STATE_READY`
            * :attr:`EsxHost.ESX_STATE_DELETING`
            * :attr:`EsxHost.ESX_STATE_DELETED`
            * :attr:`EsxHost.ESX_STATE_FAILED`
        """
        self.name = name
        self.availability_zone = availability_zone
        self.esx_id = esx_id
        self.hostname = hostname
        self.provider = provider
        self.mac_address = mac_address
        self.custom_properties = custom_properties
        self.esx_state = esx_state
        VapiStruct.__init__(self)

EsxHost._set_binding_type(type.StructType(
    'com.vmware.vmc.model.esx_host', {
        'name': type.OptionalType(type.StringType()),
        'availability_zone': type.OptionalType(type.StringType()),
        'esx_id': type.OptionalType(type.StringType()),
        'hostname': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'mac_address': type.OptionalType(type.StringType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'esx_state': type.OptionalType(type.StringType()),
    },
    EsxHost,
    False,
    None))



class ExtendedAttribute(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'name': 'name',
                            'value': 'value',
                            }

    def __init__(self,
                 name=None,
                 value=None,
                ):
        """
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  value: :class:`str` or ``None``
        :param value: 
        """
        self.name = name
        self.value = value
        VapiStruct.__init__(self)

ExtendedAttribute._set_binding_type(type.StructType(
    'com.vmware.vmc.model.extended_attribute', {
        'name': type.OptionalType(type.StringType()),
        'value': type.OptionalType(type.StringType()),
    },
    ExtendedAttribute,
    False,
    None))



class FeatureCapabilities(VapiStruct):
    """
    List of features and their capability details based on NSX Edge appliance
    form factor.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timestamp': 'timestamp',
                            'featureCapabilities': 'feature_capabilities',
                            }

    def __init__(self,
                 timestamp=None,
                 feature_capabilities=None,
                ):
        """
        :type  timestamp: :class:`long` or ``None``
        :param timestamp: Time stamp value at which the feature capabilities were retrieved.
            format: int64
        :type  feature_capabilities: :class:`list` of :class:`FeatureCapability` or ``None``
        :param feature_capabilities: List of feature capability information.
        """
        self.timestamp = timestamp
        self.feature_capabilities = feature_capabilities
        VapiStruct.__init__(self)

FeatureCapabilities._set_binding_type(type.StructType(
    'com.vmware.vmc.model.feature_capabilities', {
        'timestamp': type.OptionalType(type.IntegerType()),
        'featureCapabilities': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'FeatureCapability'))),
    },
    FeatureCapabilities,
    False,
    None))



class FeatureCapability(VapiStruct):
    """
    Feature capability information.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'configurationLimits': 'configuration_limits',
                            'isSupported': 'is_supported',
                            'service': 'service',
                            'permission': 'permission',
                            }

    def __init__(self,
                 configuration_limits=None,
                 is_supported=None,
                 service=None,
                 permission=None,
                ):
        """
        :type  configuration_limits: :class:`list` of :class:`KeyValueAttributes` or ``None``
        :param configuration_limits: List of key value pairs describing the feature configuration
            limits.
        :type  is_supported: :class:`bool` or ``None``
        :param is_supported: Value is true if feature is supported on NSX Edge.
        :type  service: :class:`str` or ``None``
        :param service: Name of the feature or service.
        :type  permission: :class:`LicenceAclPermissions` or ``None``
        :param permission: Licence and access control information for the feature.
        """
        self.configuration_limits = configuration_limits
        self.is_supported = is_supported
        self.service = service
        self.permission = permission
        VapiStruct.__init__(self)

FeatureCapability._set_binding_type(type.StructType(
    'com.vmware.vmc.model.feature_capability', {
        'configurationLimits': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'KeyValueAttributes'))),
        'isSupported': type.OptionalType(type.BooleanType()),
        'service': type.OptionalType(type.StringType()),
        'permission': type.OptionalType(type.ReferenceType(__name__, 'LicenceAclPermissions')),
    },
    FeatureCapability,
    False,
    None))



class FeatureStatus(VapiStruct):
    """
    Individual feature status.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'status': 'status',
                            'configured': 'configured',
                            'serverStatus': 'server_status',
                            'publishStatus': 'publish_status',
                            'service': 'service',
                            }

    def __init__(self,
                 status=None,
                 configured=None,
                 server_status=None,
                 publish_status=None,
                 service=None,
                ):
        """
        :type  status: :class:`str` or ``None``
        :param status: Status of the feature or service.
        :type  configured: :class:`bool` or ``None``
        :param configured: Value is true if feature is configured.
        :type  server_status: :class:`str` or ``None``
        :param server_status: Server status of the feature or service. Values are up and down.
        :type  publish_status: :class:`str` or ``None``
        :param publish_status: Publish status of the feature, whether APPLIED or PERSISTED.
        :type  service: :class:`str` or ``None``
        :param service: Name of the feature or service.
        """
        self.status = status
        self.configured = configured
        self.server_status = server_status
        self.publish_status = publish_status
        self.service = service
        VapiStruct.__init__(self)

FeatureStatus._set_binding_type(type.StructType(
    'com.vmware.vmc.model.feature_status', {
        'status': type.OptionalType(type.StringType()),
        'configured': type.OptionalType(type.BooleanType()),
        'serverStatus': type.OptionalType(type.StringType()),
        'publishStatus': type.OptionalType(type.StringType()),
        'service': type.OptionalType(type.StringType()),
    },
    FeatureStatus,
    False,
    None))



class FirewallConfig(VapiStruct):
    """
    Firewall Configuration

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'firewallRules': 'firewall_rules',
                            'featureType': 'feature_type',
                            'version': 'version',
                            'template': 'template',
                            'globalConfig': 'global_config',
                            'enabled': 'enabled',
                            'defaultPolicy': 'default_policy',
                            }

    def __init__(self,
                 firewall_rules=None,
                 feature_type=None,
                 version=None,
                 template=None,
                 global_config=None,
                 enabled=None,
                 default_policy=None,
                ):
        """
        :type  firewall_rules: :class:`FirewallRules` or ``None``
        :param firewall_rules: Ordered list of firewall rules.
        :type  feature_type: :class:`str` or ``None``
        :param feature_type: 
        :type  version: :class:`long` or ``None``
        :param version: Version number tracking each configuration change. To avoid
            problems with overwriting changes, always retrieve and modify the
            latest configuration to include the current version number in your
            request. If you provide a version number which is not current, the
            request is rejected. If you omit the version number, the request is
            accepted but may overwrite any current changes if your change is
            not in sync with the latest change. format: int64
        :type  template: :class:`str` or ``None``
        :param template: 
        :type  global_config: :class:`FirewallGlobalConfig` or ``None``
        :param global_config: Global configuration applicable to all rules.
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Value is true if feature is enabled. Default value is true.
            Optional.
        :type  default_policy: :class:`FirewallDefaultPolicy` or ``None``
        :param default_policy: Default Policy.
        """
        self.firewall_rules = firewall_rules
        self.feature_type = feature_type
        self.version = version
        self.template = template
        self.global_config = global_config
        self.enabled = enabled
        self.default_policy = default_policy
        VapiStruct.__init__(self)

FirewallConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_config', {
        'firewallRules': type.OptionalType(type.ReferenceType(__name__, 'FirewallRules')),
        'featureType': type.OptionalType(type.StringType()),
        'version': type.OptionalType(type.IntegerType()),
        'template': type.OptionalType(type.StringType()),
        'globalConfig': type.OptionalType(type.ReferenceType(__name__, 'FirewallGlobalConfig')),
        'enabled': type.OptionalType(type.BooleanType()),
        'defaultPolicy': type.OptionalType(type.ReferenceType(__name__, 'FirewallDefaultPolicy')),
    },
    FirewallConfig,
    False,
    None))



class FirewallDashboardStats(VapiStruct):
    """
    Dashboard Statistics data for Firewall.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'connections': 'connections',
                            }

    def __init__(self,
                 connections=None,
                ):
        """
        :type  connections: :class:`list` of :class:`DashboardStat` or ``None``
        :param connections: Number of NSX Edge firewall connections and rules.
        """
        self.connections = connections
        VapiStruct.__init__(self)

FirewallDashboardStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_dashboard_stats', {
        'connections': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
    },
    FirewallDashboardStats,
    False,
    None))



class FirewallDefaultPolicy(VapiStruct):
    """
    Firewall default policy. Default is deny.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'action': 'action',
                            'loggingEnabled': 'logging_enabled',
                            }

    def __init__(self,
                 action=None,
                 logging_enabled=None,
                ):
        """
        :type  action: :class:`str` or ``None``
        :param action: Action. Default is deny. Supported values accept, deny
        :type  logging_enabled: :class:`bool` or ``None``
        :param logging_enabled: Enable logging for the rule.
        """
        self.action = action
        self.logging_enabled = logging_enabled
        VapiStruct.__init__(self)

FirewallDefaultPolicy._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_default_policy', {
        'action': type.OptionalType(type.StringType()),
        'loggingEnabled': type.OptionalType(type.BooleanType()),
    },
    FirewallDefaultPolicy,
    False,
    None))



class FirewallGlobalConfig(VapiStruct):
    """
    Global configuration applicable to all rules.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'tcpAllowOutOfWindowPackets': 'tcp_allow_out_of_window_packets',
                            'udpTimeout': 'udp_timeout',
                            'ipGenericTimeout': 'ip_generic_timeout',
                            'tcpPickOngoingConnections': 'tcp_pick_ongoing_connections',
                            'tcpTimeoutOpen': 'tcp_timeout_open',
                            'tcpTimeoutClose': 'tcp_timeout_close',
                            'icmp6Timeout': 'icmp6_timeout',
                            'dropIcmpReplays': 'drop_icmp_replays',
                            'logIcmpErrors': 'log_icmp_errors',
                            'tcpSendResetForClosedVsePorts': 'tcp_send_reset_for_closed_vse_ports',
                            'dropInvalidTraffic': 'drop_invalid_traffic',
                            'enableSynFloodProtection': 'enable_syn_flood_protection',
                            'icmpTimeout': 'icmp_timeout',
                            'tcpTimeoutEstablished': 'tcp_timeout_established',
                            'logInvalidTraffic': 'log_invalid_traffic',
                            }

    def __init__(self,
                 tcp_allow_out_of_window_packets=None,
                 udp_timeout=None,
                 ip_generic_timeout=None,
                 tcp_pick_ongoing_connections=None,
                 tcp_timeout_open=None,
                 tcp_timeout_close=None,
                 icmp6_timeout=None,
                 drop_icmp_replays=None,
                 log_icmp_errors=None,
                 tcp_send_reset_for_closed_vse_ports=None,
                 drop_invalid_traffic=None,
                 enable_syn_flood_protection=None,
                 icmp_timeout=None,
                 tcp_timeout_established=None,
                 log_invalid_traffic=None,
                ):
        """
        :type  tcp_allow_out_of_window_packets: :class:`bool` or ``None``
        :param tcp_allow_out_of_window_packets: Allow TCP out of window packets.
        :type  udp_timeout: :class:`long` or ``None``
        :param udp_timeout: UDP timeout close. format: int32
        :type  ip_generic_timeout: :class:`long` or ``None``
        :param ip_generic_timeout: IP generic timeout. format: int32
        :type  tcp_pick_ongoing_connections: :class:`bool` or ``None``
        :param tcp_pick_ongoing_connections: Pick TCP ongoing connections.
        :type  tcp_timeout_open: :class:`long` or ``None``
        :param tcp_timeout_open: TCP timeout open. format: int32
        :type  tcp_timeout_close: :class:`long` or ``None``
        :param tcp_timeout_close: TCP timeout close. format: int32
        :type  icmp6_timeout: :class:`long` or ``None``
        :param icmp6_timeout: ICMP6 timeout. format: int32
        :type  drop_icmp_replays: :class:`bool` or ``None``
        :param drop_icmp_replays: Drop icmp replays.
        :type  log_icmp_errors: :class:`bool` or ``None``
        :param log_icmp_errors: Log icmp errors.
        :type  tcp_send_reset_for_closed_vse_ports: :class:`bool` or ``None``
        :param tcp_send_reset_for_closed_vse_ports: Send TCP reset for closed NSX Edge ports.
        :type  drop_invalid_traffic: :class:`bool` or ``None``
        :param drop_invalid_traffic: Drop invalid traffic.
        :type  enable_syn_flood_protection: :class:`bool` or ``None``
        :param enable_syn_flood_protection: Protect against SYN flood attacks by detecting bogus TCP
            connections and terminating them without consuming firewall state
            tracking resources. Default : false
        :type  icmp_timeout: :class:`long` or ``None``
        :param icmp_timeout: ICMP timeout. format: int32
        :type  tcp_timeout_established: :class:`long` or ``None``
        :param tcp_timeout_established: TCP timeout established. format: int32
        :type  log_invalid_traffic: :class:`bool` or ``None``
        :param log_invalid_traffic: Log invalid traffic.
        """
        self.tcp_allow_out_of_window_packets = tcp_allow_out_of_window_packets
        self.udp_timeout = udp_timeout
        self.ip_generic_timeout = ip_generic_timeout
        self.tcp_pick_ongoing_connections = tcp_pick_ongoing_connections
        self.tcp_timeout_open = tcp_timeout_open
        self.tcp_timeout_close = tcp_timeout_close
        self.icmp6_timeout = icmp6_timeout
        self.drop_icmp_replays = drop_icmp_replays
        self.log_icmp_errors = log_icmp_errors
        self.tcp_send_reset_for_closed_vse_ports = tcp_send_reset_for_closed_vse_ports
        self.drop_invalid_traffic = drop_invalid_traffic
        self.enable_syn_flood_protection = enable_syn_flood_protection
        self.icmp_timeout = icmp_timeout
        self.tcp_timeout_established = tcp_timeout_established
        self.log_invalid_traffic = log_invalid_traffic
        VapiStruct.__init__(self)

FirewallGlobalConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_global_config', {
        'tcpAllowOutOfWindowPackets': type.OptionalType(type.BooleanType()),
        'udpTimeout': type.OptionalType(type.IntegerType()),
        'ipGenericTimeout': type.OptionalType(type.IntegerType()),
        'tcpPickOngoingConnections': type.OptionalType(type.BooleanType()),
        'tcpTimeoutOpen': type.OptionalType(type.IntegerType()),
        'tcpTimeoutClose': type.OptionalType(type.IntegerType()),
        'icmp6Timeout': type.OptionalType(type.IntegerType()),
        'dropIcmpReplays': type.OptionalType(type.BooleanType()),
        'logIcmpErrors': type.OptionalType(type.BooleanType()),
        'tcpSendResetForClosedVsePorts': type.OptionalType(type.BooleanType()),
        'dropInvalidTraffic': type.OptionalType(type.BooleanType()),
        'enableSynFloodProtection': type.OptionalType(type.BooleanType()),
        'icmpTimeout': type.OptionalType(type.IntegerType()),
        'tcpTimeoutEstablished': type.OptionalType(type.IntegerType()),
        'logInvalidTraffic': type.OptionalType(type.BooleanType()),
    },
    FirewallGlobalConfig,
    False,
    None))



class FirewallRule(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    RULE_TYPE_USER = "USER"
    """


    """
    RULE_TYPE_DEFAULT = "DEFAULT"
    """


    """
    ACTION_ALLOW = "ALLOW"
    """


    """
    ACTION_DENY = "DENY"
    """


    """



    _canonical_to_pep_names = {
                            'rule_type': 'rule_type',
                            'application_ids': 'application_ids',
                            'name': 'name',
                            'rule_interface': 'rule_interface',
                            'destination': 'destination',
                            'id': 'id',
                            'destination_scope': 'destination_scope',
                            'source': 'source',
                            'source_scope': 'source_scope',
                            'services': 'services',
                            'action': 'action',
                            'revision': 'revision',
                            }

    def __init__(self,
                 rule_type=None,
                 application_ids=None,
                 name=None,
                 rule_interface=None,
                 destination=None,
                 id=None,
                 destination_scope=None,
                 source=None,
                 source_scope=None,
                 services=None,
                 action=None,
                 revision=None,
                ):
        """
        :type  rule_type: :class:`str` or ``None``
        :param rule_type: Possible values are: 
            
            * :attr:`FirewallRule.RULE_TYPE_USER`
            * :attr:`FirewallRule.RULE_TYPE_DEFAULT`
        :type  application_ids: :class:`list` of :class:`str` or ``None``
        :param application_ids: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  rule_interface: :class:`str` or ``None``
        :param rule_interface: Deprecated, left for backwards compatibility. Remove once UI stops
            using it.
        :type  destination: :class:`str` or ``None``
        :param destination: Optional. Possible formats are IP, IP1-IPn, CIDR or comma separated
            list of those entries. If not specified, defaults to 'any'.
        :type  id: :class:`str` or ``None``
        :param id: 
        :type  destination_scope: :class:`FirewallRuleScope` or ``None``
        :param destination_scope: 
        :type  source: :class:`str` or ``None``
        :param source: Optional. Possible formats are IP, IP1-IPn, CIDR or comma separated
            list of those entries. If not specified, defaults to 'any'.
        :type  source_scope: :class:`FirewallRuleScope` or ``None``
        :param source_scope: 
        :type  services: :class:`list` of :class:`FirewallService` or ``None``
        :param services: list of protocols and ports for this firewall rule
        :type  action: :class:`str` or ``None``
        :param action: Possible values are: 
            
            * :attr:`FirewallRule.ACTION_ALLOW`
            * :attr:`FirewallRule.ACTION_DENY`
        :type  revision: :class:`long` or ``None``
        :param revision: current revision of the list of firewall rules, used to protect
            against concurrent modification (first writer wins) format: int32
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.rule_type = rule_type
        self.application_ids = application_ids
        self.name = name
        self.rule_interface = rule_interface
        self.destination = destination
        self.id = id
        self.destination_scope = destination_scope
        self.source = source
        self.source_scope = source_scope
        self.services = services
        self.action = action
        self.revision = revision
        VapiStruct.__init__(self)

FirewallRule._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_rule', {
        'rule_type': type.OptionalType(type.StringType()),
        'application_ids': type.OptionalType(type.ListType(type.StringType())),
        'name': type.OptionalType(type.StringType()),
        'rule_interface': type.OptionalType(type.StringType()),
        'destination': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'destination_scope': type.OptionalType(type.ReferenceType(__name__, 'FirewallRuleScope')),
        'source': type.OptionalType(type.StringType()),
        'source_scope': type.OptionalType(type.ReferenceType(__name__, 'FirewallRuleScope')),
        'services': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'FirewallService'))),
        'action': type.OptionalType(type.StringType()),
        'revision': type.OptionalType(type.IntegerType()),
    },
    FirewallRule,
    False,
    None))



class FirewallRuleScope(VapiStruct):
    """
    Optional for FirewallRule. If not specified, defaults to 'any'.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    VNIC_GROUP_IDS_VSE = "vse"
    """


    """
    VNIC_GROUP_IDS_INTERNAL = "internal"
    """


    """
    VNIC_GROUP_IDS_EXTERNAL = "external"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_0 = "vnic-index-0"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_1 = "vnic-index-1"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_2 = "vnic-index-2"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_3 = "vnic-index-3"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_4 = "vnic-index-4"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_5 = "vnic-index-5"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_6 = "vnic-index-6"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_7 = "vnic-index-7"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_8 = "vnic-index-8"
    """


    """
    VNIC_GROUP_IDS_VNIC_INDEX_9 = "vnic-index-9"
    """


    """



    _canonical_to_pep_names = {
                            'grouping_object_ids': 'grouping_object_ids',
                            'vnic_group_ids': 'vnic_group_ids',
                            }

    def __init__(self,
                 grouping_object_ids=None,
                 vnic_group_ids=None,
                ):
        """
        :type  grouping_object_ids: :class:`list` of :class:`str` or ``None``
        :param grouping_object_ids: 
        :type  vnic_group_ids: :class:`list` of :class:`str` or ``None``
        :param vnic_group_ids: Possible values are: 
            
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VSE`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_INTERNAL`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_EXTERNAL`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_0`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_1`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_2`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_3`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_4`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_5`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_6`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_7`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_8`
            * :attr:`FirewallRuleScope.VNIC_GROUP_IDS_VNIC_INDEX_9`
        """
        self.grouping_object_ids = grouping_object_ids
        self.vnic_group_ids = vnic_group_ids
        VapiStruct.__init__(self)

FirewallRuleScope._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_rule_scope', {
        'grouping_object_ids': type.OptionalType(type.ListType(type.StringType())),
        'vnic_group_ids': type.OptionalType(type.ListType(type.StringType())),
    },
    FirewallRuleScope,
    False,
    None))



class FirewallRuleStats(VapiStruct):
    """
    Statistics for firewall rule

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timestamp': 'timestamp',
                            'connectionCount': 'connection_count',
                            'byteCount': 'byte_count',
                            'packetCount': 'packet_count',
                            }

    def __init__(self,
                 timestamp=None,
                 connection_count=None,
                 byte_count=None,
                 packet_count=None,
                ):
        """
        :type  timestamp: :class:`long` or ``None``
        :param timestamp: Timestamp of statistics collection. format: int64
        :type  connection_count: :class:`long` or ``None``
        :param connection_count: Connection count. format: int64
        :type  byte_count: :class:`long` or ``None``
        :param byte_count: Byte count. format: int64
        :type  packet_count: :class:`long` or ``None``
        :param packet_count: Packet count. format: int64
        """
        self.timestamp = timestamp
        self.connection_count = connection_count
        self.byte_count = byte_count
        self.packet_count = packet_count
        VapiStruct.__init__(self)

FirewallRuleStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_rule_stats', {
        'timestamp': type.OptionalType(type.IntegerType()),
        'connectionCount': type.OptionalType(type.IntegerType()),
        'byteCount': type.OptionalType(type.IntegerType()),
        'packetCount': type.OptionalType(type.IntegerType()),
    },
    FirewallRuleStats,
    False,
    None))



class FirewallRules(VapiStruct):
    """
    Ordered list of firewall rules.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'firewallRules': 'firewall_rules',
                            }

    def __init__(self,
                 firewall_rules=None,
                ):
        """
        :type  firewall_rules: :class:`list` of :class:`Nsxfirewallrule` or ``None``
        :param firewall_rules: Ordered list of firewall rules.
        """
        self.firewall_rules = firewall_rules
        VapiStruct.__init__(self)

FirewallRules._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_rules', {
        'firewallRules': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Nsxfirewallrule'))),
    },
    FirewallRules,
    False,
    None))



class FirewallService(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'protocol': 'protocol',
                            'ports': 'ports',
                            }

    def __init__(self,
                 protocol=None,
                 ports=None,
                ):
        """
        :type  protocol: :class:`str` or ``None``
        :param protocol: protocol name, such as 'tcp', 'udp' etc.
        :type  ports: :class:`list` of :class:`str` or ``None``
        :param ports: a list of port numbers and port ranges, such as {80, 91-95, 99}. If
            not specified, defaults to 'any'.
        """
        self.protocol = protocol
        self.ports = ports
        VapiStruct.__init__(self)

FirewallService._set_binding_type(type.StructType(
    'com.vmware.vmc.model.firewall_service', {
        'protocol': type.OptionalType(type.StringType()),
        'ports': type.OptionalType(type.ListType(type.StringType())),
    },
    FirewallService,
    False,
    None))



class GatewayTemplate(VapiStruct):
    """
    Describes common properties for MGW and CGW configuration templates

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'public_ip': 'public_ip',
                            'primary_dns': 'primary_dns',
                            'secondary_dns': 'secondary_dns',
                            'firewall_rules': 'firewall_rules',
                            'vpns': 'vpns',
                            }

    def __init__(self,
                 public_ip=None,
                 primary_dns=None,
                 secondary_dns=None,
                 firewall_rules=None,
                 vpns=None,
                ):
        """
        :type  public_ip: :class:`SddcPublicIp` or ``None``
        :param public_ip: 
        :type  primary_dns: :class:`str` or ``None``
        :param primary_dns: 
        :type  secondary_dns: :class:`str` or ``None``
        :param secondary_dns: 
        :type  firewall_rules: :class:`list` of :class:`FirewallRule` or ``None``
        :param firewall_rules: 
        :type  vpns: :class:`list` of :class:`Vpn` or ``None``
        :param vpns: 
        """
        self.public_ip = public_ip
        self.primary_dns = primary_dns
        self.secondary_dns = secondary_dns
        self.firewall_rules = firewall_rules
        self.vpns = vpns
        VapiStruct.__init__(self)

GatewayTemplate._set_binding_type(type.StructType(
    'com.vmware.vmc.model.gateway_template', {
        'public_ip': type.OptionalType(type.ReferenceType(__name__, 'SddcPublicIp')),
        'primary_dns': type.OptionalType(type.StringType()),
        'secondary_dns': type.OptionalType(type.StringType()),
        'firewall_rules': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'FirewallRule'))),
        'vpns': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Vpn'))),
    },
    GatewayTemplate,
    False,
    None))



class GlcmBundle(VapiStruct):
    """
    the GlcmBundle used for deploying the sddc

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            's3Bucket': 's3_bucket',
                            'id': 'id',
                            }

    def __init__(self,
                 s3_bucket=None,
                 id=None,
                ):
        """
        :type  s3_bucket: :class:`str` or ``None``
        :param s3_bucket: the glcmbundle's s3 bucket
        :type  id: :class:`str` or ``None``
        :param id: the glcmbundle's id
        """
        self.s3_bucket = s3_bucket
        self.id = id
        VapiStruct.__init__(self)

GlcmBundle._set_binding_type(type.StructType(
    'com.vmware.vmc.model.glcm_bundle', {
        's3Bucket': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
    },
    GlcmBundle,
    False,
    None))



class HostLeaseInfo(VapiStruct):
    """
    DHCP lease information.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'macAddress': 'mac_address',
                            'ends': 'ends',
                            'abandoned': 'abandoned',
                            'cltt': 'cltt',
                            'clientHostname': 'client_hostname',
                            'starts': 'starts',
                            'bindingState': 'binding_state',
                            'hardwareType': 'hardware_type',
                            'tsfp': 'tsfp',
                            'uid': 'uid',
                            'nextBindingState': 'next_binding_state',
                            'ipAddress': 'ip_address',
                            'tstp': 'tstp',
                            }

    def __init__(self,
                 mac_address=None,
                 ends=None,
                 abandoned=None,
                 cltt=None,
                 client_hostname=None,
                 starts=None,
                 binding_state=None,
                 hardware_type=None,
                 tsfp=None,
                 uid=None,
                 next_binding_state=None,
                 ip_address=None,
                 tstp=None,
                ):
        """
        :type  mac_address: :class:`str` or ``None``
        :param mac_address: MAC address of the client.
        :type  ends: :class:`str` or ``None``
        :param ends: End time of the lease.
        :type  abandoned: :class:`str` or ``None``
        :param abandoned: Time stamp of when IP address was marked as abandoned.
        :type  cltt: :class:`str` or ``None``
        :param cltt: Client Last Transaction Time of the lease info.
        :type  client_hostname: :class:`str` or ``None``
        :param client_hostname: Name of the client.
        :type  starts: :class:`str` or ``None``
        :param starts: Start time of the lease.
        :type  binding_state: :class:`str` or ``None``
        :param binding_state: Lease's binding state.
        :type  hardware_type: :class:`str` or ``None``
        :param hardware_type: The hardware type on which the lease will be used.
        :type  tsfp: :class:`str` or ``None``
        :param tsfp: Time Sent From Partner of the lease info.
        :type  uid: :class:`str` or ``None``
        :param uid: Uid to identify the DHCP lease.
        :type  next_binding_state: :class:`str` or ``None``
        :param next_binding_state: Indicates what state the lease will move to when the current state
            expires.
        :type  ip_address: :class:`str` or ``None``
        :param ip_address: IP address of the client.
        :type  tstp: :class:`str` or ``None``
        :param tstp: Time Sent To Partner of the lease info.
        """
        self.mac_address = mac_address
        self.ends = ends
        self.abandoned = abandoned
        self.cltt = cltt
        self.client_hostname = client_hostname
        self.starts = starts
        self.binding_state = binding_state
        self.hardware_type = hardware_type
        self.tsfp = tsfp
        self.uid = uid
        self.next_binding_state = next_binding_state
        self.ip_address = ip_address
        self.tstp = tstp
        VapiStruct.__init__(self)

HostLeaseInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.host_lease_info', {
        'macAddress': type.OptionalType(type.StringType()),
        'ends': type.OptionalType(type.StringType()),
        'abandoned': type.OptionalType(type.StringType()),
        'cltt': type.OptionalType(type.StringType()),
        'clientHostname': type.OptionalType(type.StringType()),
        'starts': type.OptionalType(type.StringType()),
        'bindingState': type.OptionalType(type.StringType()),
        'hardwareType': type.OptionalType(type.StringType()),
        'tsfp': type.OptionalType(type.StringType()),
        'uid': type.OptionalType(type.StringType()),
        'nextBindingState': type.OptionalType(type.StringType()),
        'ipAddress': type.OptionalType(type.StringType()),
        'tstp': type.OptionalType(type.StringType()),
    },
    HostLeaseInfo,
    False,
    None))



class InteractionPermissions(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'managePermission': 'manage_permission',
                            'viewPermission': 'view_permission',
                            }

    def __init__(self,
                 manage_permission=None,
                 view_permission=None,
                ):
        """
        :type  manage_permission: :class:`bool` or ``None``
        :param manage_permission: 
        :type  view_permission: :class:`bool` or ``None``
        :param view_permission: 
        """
        self.manage_permission = manage_permission
        self.view_permission = view_permission
        VapiStruct.__init__(self)

InteractionPermissions._set_binding_type(type.StructType(
    'com.vmware.vmc.model.interaction_permissions', {
        'managePermission': type.OptionalType(type.BooleanType()),
        'viewPermission': type.OptionalType(type.BooleanType()),
    },
    InteractionPermissions,
    False,
    None))



class InterfacesDashboardStats(VapiStruct):
    """
    Dashboard Statistics data for Interfaces.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vnic_7_in_pkt': 'vnic7_in_pkt',
                            'vnic_0_in_byte': 'vnic0_in_byte',
                            'vnic_8_out_pkt': 'vnic8_out_pkt',
                            'vnic_5_in_byte': 'vnic5_in_byte',
                            'vnic_2_in_pkt': 'vnic2_in_pkt',
                            'vnic_3_in_pkt': 'vnic3_in_pkt',
                            'vnic_6_out_byte': 'vnic6_out_byte',
                            'vnic_3_in_byte': 'vnic3_in_byte',
                            'vnic_8_in_pkt': 'vnic8_in_pkt',
                            'vnic_1_in_byte': 'vnic1_in_byte',
                            'vnic_1_out_pkt': 'vnic1_out_pkt',
                            'vnic_5_out_byte': 'vnic5_out_byte',
                            'vnic_0_out_pkt': 'vnic0_out_pkt',
                            'vnic_0_out_byte': 'vnic0_out_byte',
                            'vnic_6_out_pkt': 'vnic6_out_pkt',
                            'vnic_3_out_byte': 'vnic3_out_byte',
                            'vnic_7_in_byte': 'vnic7_in_byte',
                            'vnic_1_out_byte': 'vnic1_out_byte',
                            'vnic_9_out_pkt': 'vnic9_out_pkt',
                            'vnic_9_in_pkt': 'vnic9_in_pkt',
                            'vnic_4_in_byte': 'vnic4_in_byte',
                            'vnic_5_out_pkt': 'vnic5_out_pkt',
                            'vnic_2_out_pkt': 'vnic2_out_pkt',
                            'vnic_2_in_byte': 'vnic2_in_byte',
                            'vnic_5_in_pkt': 'vnic5_in_pkt',
                            'vnic_7_out_pkt': 'vnic7_out_pkt',
                            'vnic_3_out_pkt': 'vnic3_out_pkt',
                            'vnic_4_out_pkt': 'vnic4_out_pkt',
                            'vnic_4_out_byte': 'vnic4_out_byte',
                            'vnic_1_in_pkt': 'vnic1_in_pkt',
                            'vnic_2_out_byte': 'vnic2_out_byte',
                            'vnic_6_in_byte': 'vnic6_in_byte',
                            'vnic_0_in_pkt': 'vnic0_in_pkt',
                            'vnic_9_in_byte': 'vnic9_in_byte',
                            'vnic_7_out_byte': 'vnic7_out_byte',
                            'vnic_4_in_pkt': 'vnic4_in_pkt',
                            'vnic_9_out_byte': 'vnic9_out_byte',
                            'vnic_8_out_byte': 'vnic8_out_byte',
                            'vnic_8_in_byte': 'vnic8_in_byte',
                            'vnic_6_in_pkt': 'vnic6_in_pkt',
                            }

    def __init__(self,
                 vnic7_in_pkt=None,
                 vnic0_in_byte=None,
                 vnic8_out_pkt=None,
                 vnic5_in_byte=None,
                 vnic2_in_pkt=None,
                 vnic3_in_pkt=None,
                 vnic6_out_byte=None,
                 vnic3_in_byte=None,
                 vnic8_in_pkt=None,
                 vnic1_in_byte=None,
                 vnic1_out_pkt=None,
                 vnic5_out_byte=None,
                 vnic0_out_pkt=None,
                 vnic0_out_byte=None,
                 vnic6_out_pkt=None,
                 vnic3_out_byte=None,
                 vnic7_in_byte=None,
                 vnic1_out_byte=None,
                 vnic9_out_pkt=None,
                 vnic9_in_pkt=None,
                 vnic4_in_byte=None,
                 vnic5_out_pkt=None,
                 vnic2_out_pkt=None,
                 vnic2_in_byte=None,
                 vnic5_in_pkt=None,
                 vnic7_out_pkt=None,
                 vnic3_out_pkt=None,
                 vnic4_out_pkt=None,
                 vnic4_out_byte=None,
                 vnic1_in_pkt=None,
                 vnic2_out_byte=None,
                 vnic6_in_byte=None,
                 vnic0_in_pkt=None,
                 vnic9_in_byte=None,
                 vnic7_out_byte=None,
                 vnic4_in_pkt=None,
                 vnic9_out_byte=None,
                 vnic8_out_byte=None,
                 vnic8_in_byte=None,
                 vnic6_in_pkt=None,
                ):
        """
        :type  vnic7_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic7_in_pkt: 
        :type  vnic0_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic0_in_byte: 
        :type  vnic8_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic8_out_pkt: 
        :type  vnic5_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic5_in_byte: 
        :type  vnic2_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic2_in_pkt: 
        :type  vnic3_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic3_in_pkt: 
        :type  vnic6_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic6_out_byte: 
        :type  vnic3_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic3_in_byte: 
        :type  vnic8_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic8_in_pkt: 
        :type  vnic1_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic1_in_byte: 
        :type  vnic1_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic1_out_pkt: 
        :type  vnic5_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic5_out_byte: 
        :type  vnic0_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic0_out_pkt: 
        :type  vnic0_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic0_out_byte: 
        :type  vnic6_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic6_out_pkt: 
        :type  vnic3_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic3_out_byte: 
        :type  vnic7_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic7_in_byte: 
        :type  vnic1_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic1_out_byte: 
        :type  vnic9_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic9_out_pkt: 
        :type  vnic9_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic9_in_pkt: 
        :type  vnic4_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic4_in_byte: 
        :type  vnic5_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic5_out_pkt: 
        :type  vnic2_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic2_out_pkt: 
        :type  vnic2_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic2_in_byte: 
        :type  vnic5_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic5_in_pkt: 
        :type  vnic7_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic7_out_pkt: 
        :type  vnic3_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic3_out_pkt: 
        :type  vnic4_out_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic4_out_pkt: 
        :type  vnic4_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic4_out_byte: 
        :type  vnic1_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic1_in_pkt: 
        :type  vnic2_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic2_out_byte: 
        :type  vnic6_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic6_in_byte: 
        :type  vnic0_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic0_in_pkt: 
        :type  vnic9_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic9_in_byte: 
        :type  vnic7_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic7_out_byte: 
        :type  vnic4_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic4_in_pkt: 
        :type  vnic9_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic9_out_byte: 
        :type  vnic8_out_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic8_out_byte: 
        :type  vnic8_in_byte: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic8_in_byte: 
        :type  vnic6_in_pkt: :class:`list` of :class:`DashboardStat` or ``None``
        :param vnic6_in_pkt: 
        """
        self.vnic7_in_pkt = vnic7_in_pkt
        self.vnic0_in_byte = vnic0_in_byte
        self.vnic8_out_pkt = vnic8_out_pkt
        self.vnic5_in_byte = vnic5_in_byte
        self.vnic2_in_pkt = vnic2_in_pkt
        self.vnic3_in_pkt = vnic3_in_pkt
        self.vnic6_out_byte = vnic6_out_byte
        self.vnic3_in_byte = vnic3_in_byte
        self.vnic8_in_pkt = vnic8_in_pkt
        self.vnic1_in_byte = vnic1_in_byte
        self.vnic1_out_pkt = vnic1_out_pkt
        self.vnic5_out_byte = vnic5_out_byte
        self.vnic0_out_pkt = vnic0_out_pkt
        self.vnic0_out_byte = vnic0_out_byte
        self.vnic6_out_pkt = vnic6_out_pkt
        self.vnic3_out_byte = vnic3_out_byte
        self.vnic7_in_byte = vnic7_in_byte
        self.vnic1_out_byte = vnic1_out_byte
        self.vnic9_out_pkt = vnic9_out_pkt
        self.vnic9_in_pkt = vnic9_in_pkt
        self.vnic4_in_byte = vnic4_in_byte
        self.vnic5_out_pkt = vnic5_out_pkt
        self.vnic2_out_pkt = vnic2_out_pkt
        self.vnic2_in_byte = vnic2_in_byte
        self.vnic5_in_pkt = vnic5_in_pkt
        self.vnic7_out_pkt = vnic7_out_pkt
        self.vnic3_out_pkt = vnic3_out_pkt
        self.vnic4_out_pkt = vnic4_out_pkt
        self.vnic4_out_byte = vnic4_out_byte
        self.vnic1_in_pkt = vnic1_in_pkt
        self.vnic2_out_byte = vnic2_out_byte
        self.vnic6_in_byte = vnic6_in_byte
        self.vnic0_in_pkt = vnic0_in_pkt
        self.vnic9_in_byte = vnic9_in_byte
        self.vnic7_out_byte = vnic7_out_byte
        self.vnic4_in_pkt = vnic4_in_pkt
        self.vnic9_out_byte = vnic9_out_byte
        self.vnic8_out_byte = vnic8_out_byte
        self.vnic8_in_byte = vnic8_in_byte
        self.vnic6_in_pkt = vnic6_in_pkt
        VapiStruct.__init__(self)

InterfacesDashboardStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.interfaces_dashboard_stats', {
        'vnic_7_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_0_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_8_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_5_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_2_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_3_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_6_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_3_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_8_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_1_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_1_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_5_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_0_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_0_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_6_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_3_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_7_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_1_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_9_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_9_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_4_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_5_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_2_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_2_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_5_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_7_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_3_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_4_out_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_4_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_1_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_2_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_6_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_0_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_9_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_7_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_4_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_9_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_8_out_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_8_in_byte': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'vnic_6_in_pkt': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
    },
    InterfacesDashboardStats,
    False,
    None))



class IpAddresses(VapiStruct):
    """
    IP address

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ipAddress': 'ip_address',
                            }

    def __init__(self,
                 ip_address=None,
                ):
        """
        :type  ip_address: :class:`list` of :class:`str` or ``None``
        :param ip_address: List of IP addresses.
        """
        self.ip_address = ip_address
        VapiStruct.__init__(self)

IpAddresses._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ip_addresses', {
        'ipAddress': type.OptionalType(type.ListType(type.StringType())),
    },
    IpAddresses,
    False,
    None))



class Ipsec(VapiStruct):
    """
    NSX Edge IPsec configuration details.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'featureType': 'feature_type',
                            'logging': 'logging',
                            'global': 'global_',
                            'enabled': 'enabled',
                            'sites': 'sites',
                            'disableEvent': 'disable_event',
                            'version': 'version',
                            'template': 'template',
                            }

    def __init__(self,
                 feature_type=None,
                 logging=None,
                 global_=None,
                 enabled=None,
                 sites=None,
                 disable_event=None,
                 version=None,
                 template=None,
                ):
        """
        :type  feature_type: :class:`str` or ``None``
        :param feature_type: 
        :type  logging: :class:`Logging` or ``None``
        :param logging: Configure logging for the feature on NSX Edge appliance. Logging is
            disabled by default. Optional.
        :type  global_: :class:`IpsecGlobalConfig` or ``None``
        :param global_: IPsec Global configuration details.
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Value is true if feature is enabled. Default value is true.
            Optional.
        :type  sites: :class:`IpsecSites` or ``None``
        :param sites: IPsec Site configuration details.
        :type  disable_event: :class:`bool` or ``None``
        :param disable_event: Enable/disable event generation on NSX Edge appliance for IPsec.
        :type  version: :class:`long` or ``None``
        :param version: Version number tracking each configuration change. To avoid
            problems with overwriting changes, always retrieve and modify the
            latest configuration to include the current version number in your
            request. If you provide a version number which is not current, the
            request is rejected. If you omit the version number, the request is
            accepted but may overwrite any current changes if your change is
            not in sync with the latest change. format: int64
        :type  template: :class:`str` or ``None``
        :param template: 
        """
        self.feature_type = feature_type
        self.logging = logging
        self.global_ = global_
        self.enabled = enabled
        self.sites = sites
        self.disable_event = disable_event
        self.version = version
        self.template = template
        VapiStruct.__init__(self)

Ipsec._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec', {
        'featureType': type.OptionalType(type.StringType()),
        'logging': type.OptionalType(type.ReferenceType(__name__, 'Logging')),
        'global': type.OptionalType(type.ReferenceType(__name__, 'IpsecGlobalConfig')),
        'enabled': type.OptionalType(type.BooleanType()),
        'sites': type.OptionalType(type.ReferenceType(__name__, 'IpsecSites')),
        'disableEvent': type.OptionalType(type.BooleanType()),
        'version': type.OptionalType(type.IntegerType()),
        'template': type.OptionalType(type.StringType()),
    },
    Ipsec,
    False,
    None))



class IpsecDashboardStats(VapiStruct):
    """
    Dashboard Statistics data for Ipsec.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ipsecBytesOut': 'ipsec_bytes_out',
                            'ipsecBytesIn': 'ipsec_bytes_in',
                            'ipsecTunnels': 'ipsec_tunnels',
                            }

    def __init__(self,
                 ipsec_bytes_out=None,
                 ipsec_bytes_in=None,
                 ipsec_tunnels=None,
                ):
        """
        :type  ipsec_bytes_out: :class:`list` of :class:`DashboardStat` or ``None``
        :param ipsec_bytes_out: Tx transmitted bytes.
        :type  ipsec_bytes_in: :class:`list` of :class:`DashboardStat` or ``None``
        :param ipsec_bytes_in: Rx received bytes.
        :type  ipsec_tunnels: :class:`list` of :class:`DashboardStat` or ``None``
        :param ipsec_tunnels: Number of Ipsec tunnels.
        """
        self.ipsec_bytes_out = ipsec_bytes_out
        self.ipsec_bytes_in = ipsec_bytes_in
        self.ipsec_tunnels = ipsec_tunnels
        VapiStruct.__init__(self)

IpsecDashboardStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec_dashboard_stats', {
        'ipsecBytesOut': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'ipsecBytesIn': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'ipsecTunnels': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
    },
    IpsecDashboardStats,
    False,
    None))



class IpsecGlobalConfig(VapiStruct):
    """
    IPsec Global configuration details.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'psk': 'psk',
                            'caCertificates': 'ca_certificates',
                            'serviceCertificate': 'service_certificate',
                            'crlCertificates': 'crl_certificates',
                            'extension': 'extension',
                            }

    def __init__(self,
                 psk=None,
                 ca_certificates=None,
                 service_certificate=None,
                 crl_certificates=None,
                 extension=None,
                ):
        """
        :type  psk: :class:`str` or ``None``
        :param psk: IPsec Global Pre Shared Key. Maximum characters is 128. Required
            when peerIp is configured as 'any' in NSX Edge IPsec Site
            configuration.
        :type  ca_certificates: :class:`CaCertificates` or ``None``
        :param ca_certificates: CA certificate list. Optional.
        :type  service_certificate: :class:`str` or ``None``
        :param service_certificate: Certificate name or identifier. Required when x.509 is selected as
            the authentication mode.
        :type  crl_certificates: :class:`CrlCertificates` or ``None``
        :param crl_certificates: CRL certificate list. Optional.
        :type  extension: :class:`str` or ``None``
        :param extension: 
        """
        self.psk = psk
        self.ca_certificates = ca_certificates
        self.service_certificate = service_certificate
        self.crl_certificates = crl_certificates
        self.extension = extension
        VapiStruct.__init__(self)

IpsecGlobalConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec_global_config', {
        'psk': type.OptionalType(type.StringType()),
        'caCertificates': type.OptionalType(type.ReferenceType(__name__, 'CaCertificates')),
        'serviceCertificate': type.OptionalType(type.StringType()),
        'crlCertificates': type.OptionalType(type.ReferenceType(__name__, 'CrlCertificates')),
        'extension': type.OptionalType(type.StringType()),
    },
    IpsecGlobalConfig,
    False,
    None))



class IpsecSite(VapiStruct):
    """
    NSX Edge IPsec Site configuration details.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'psk': 'psk',
                            'localId': 'local_id',
                            'enablePfs': 'enable_pfs',
                            'authenticationMode': 'authentication_mode',
                            'peerSubnets': 'peer_subnets',
                            'dhGroup': 'dh_group',
                            'siteId': 'site_id',
                            'description': 'description',
                            'peerIp': 'peer_ip',
                            'name': 'name',
                            'certificate': 'certificate',
                            'localIp': 'local_ip',
                            'encryptionAlgorithm': 'encryption_algorithm',
                            'enabled': 'enabled',
                            'mtu': 'mtu',
                            'extension': 'extension',
                            'peerId': 'peer_id',
                            'localSubnets': 'local_subnets',
                            }

    def __init__(self,
                 psk=None,
                 local_id=None,
                 enable_pfs=None,
                 authentication_mode=None,
                 peer_subnets=None,
                 dh_group=None,
                 site_id=None,
                 description=None,
                 peer_ip=None,
                 name=None,
                 certificate=None,
                 local_ip=None,
                 encryption_algorithm=None,
                 enabled=None,
                 mtu=None,
                 extension=None,
                 peer_id=None,
                 local_subnets=None,
                ):
        """
        :type  psk: :class:`str` or ``None``
        :param psk: Pre Shared Key for the IPsec Site. Required if Site peerIp is not
            'any'. Global PSK is used when Authentication mode is PSK and Site
            peerIp is 'any'.
        :type  local_id: :class:`str` or ``None``
        :param local_id: Local ID of the IPsec Site. Defaults to the local IP.
        :type  enable_pfs: :class:`bool` or ``None``
        :param enable_pfs: Enable/disable Perfect Forward Secrecy. Default is true.
        :type  authentication_mode: :class:`str` or ``None``
        :param authentication_mode: Authentication mode for the IPsec Site. Valid values are psk and
            x.509, with psk as default.
        :type  peer_subnets: :class:`Subnets` or ``None``
        :param peer_subnets: Peer subnets for which IPsec VPN is configured.
        :type  dh_group: :class:`str` or ``None``
        :param dh_group: Diffie-Hellman algorithm group. Defaults to DH14 for FIPS enabled
            NSX Edge. DH2 and DH5 are not supported when FIPS is enabled on NSX
            Edge. Valid values are DH2, DH5, DH14, DH15, DH16.
        :type  site_id: :class:`str` or ``None``
        :param site_id: ID of the IPsec Site configuration provided by NSX Manager.
        :type  description: :class:`str` or ``None``
        :param description: Description of the IPsec Site.
        :type  peer_ip: :class:`str` or ``None``
        :param peer_ip: IP (IPv4) address or FQDN of the Peer. Can also be specified as
            'any'. Required.
        :type  name: :class:`str` or ``None``
        :param name: Name of the IPsec Site.
        :type  certificate: :class:`str` or ``None``
        :param certificate: 
        :type  local_ip: :class:`str` or ``None``
        :param local_ip: Local IP of the IPsec Site. Should be one of the IP addresses
            configured on the uplink interfaces of the NSX Edge. Required.
        :type  encryption_algorithm: :class:`str` or ``None``
        :param encryption_algorithm: IPsec encryption algorithm with default as aes256. Valid values are
            'aes', 'aes256', '3des', 'aes-gcm'.
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Enable/disable IPsec Site.
        :type  mtu: :class:`long` or ``None``
        :param mtu: MTU for the IPsec site. Defaults to the mtu of the NSX Edge vnic
            specified by the localIp. Optional. format: int32
        :type  extension: :class:`str` or ``None``
        :param extension: 
        :type  peer_id: :class:`str` or ``None``
        :param peer_id: Peer ID. Should be unique for all IPsec Site's configured for an
            NSX Edge.
        :type  local_subnets: :class:`Subnets` or ``None``
        :param local_subnets: Local subnets for which IPsec VPN is configured.
        """
        self.psk = psk
        self.local_id = local_id
        self.enable_pfs = enable_pfs
        self.authentication_mode = authentication_mode
        self.peer_subnets = peer_subnets
        self.dh_group = dh_group
        self.site_id = site_id
        self.description = description
        self.peer_ip = peer_ip
        self.name = name
        self.certificate = certificate
        self.local_ip = local_ip
        self.encryption_algorithm = encryption_algorithm
        self.enabled = enabled
        self.mtu = mtu
        self.extension = extension
        self.peer_id = peer_id
        self.local_subnets = local_subnets
        VapiStruct.__init__(self)

IpsecSite._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec_site', {
        'psk': type.OptionalType(type.StringType()),
        'localId': type.OptionalType(type.StringType()),
        'enablePfs': type.OptionalType(type.BooleanType()),
        'authenticationMode': type.OptionalType(type.StringType()),
        'peerSubnets': type.OptionalType(type.ReferenceType(__name__, 'Subnets')),
        'dhGroup': type.OptionalType(type.StringType()),
        'siteId': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'peerIp': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'certificate': type.OptionalType(type.StringType()),
        'localIp': type.OptionalType(type.StringType()),
        'encryptionAlgorithm': type.OptionalType(type.StringType()),
        'enabled': type.OptionalType(type.BooleanType()),
        'mtu': type.OptionalType(type.IntegerType()),
        'extension': type.OptionalType(type.StringType()),
        'peerId': type.OptionalType(type.StringType()),
        'localSubnets': type.OptionalType(type.ReferenceType(__name__, 'Subnets')),
    },
    IpsecSite,
    False,
    None))



class IpsecSiteIKEStatus(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'channelStatus': 'channel_status',
                            'channelState': 'channel_state',
                            'peerIpAddress': 'peer_ip_address',
                            'localIpAddress': 'local_ip_address',
                            'peerSubnets': 'peer_subnets',
                            'peerId': 'peer_id',
                            'lastInformationalMessage': 'last_informational_message',
                            'localSubnets': 'local_subnets',
                            }

    def __init__(self,
                 channel_status=None,
                 channel_state=None,
                 peer_ip_address=None,
                 local_ip_address=None,
                 peer_subnets=None,
                 peer_id=None,
                 last_informational_message=None,
                 local_subnets=None,
                ):
        """
        :type  channel_status: :class:`str` or ``None``
        :param channel_status: 
        :type  channel_state: :class:`str` or ``None``
        :param channel_state: 
        :type  peer_ip_address: :class:`str` or ``None``
        :param peer_ip_address: 
        :type  local_ip_address: :class:`str` or ``None``
        :param local_ip_address: 
        :type  peer_subnets: :class:`list` of :class:`str` or ``None``
        :param peer_subnets: 
        :type  peer_id: :class:`str` or ``None``
        :param peer_id: 
        :type  last_informational_message: :class:`str` or ``None``
        :param last_informational_message: 
        :type  local_subnets: :class:`list` of :class:`str` or ``None``
        :param local_subnets: 
        """
        self.channel_status = channel_status
        self.channel_state = channel_state
        self.peer_ip_address = peer_ip_address
        self.local_ip_address = local_ip_address
        self.peer_subnets = peer_subnets
        self.peer_id = peer_id
        self.last_informational_message = last_informational_message
        self.local_subnets = local_subnets
        VapiStruct.__init__(self)

IpsecSiteIKEStatus._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec_site_IKE_status', {
        'channelStatus': type.OptionalType(type.StringType()),
        'channelState': type.OptionalType(type.StringType()),
        'peerIpAddress': type.OptionalType(type.StringType()),
        'localIpAddress': type.OptionalType(type.StringType()),
        'peerSubnets': type.OptionalType(type.ListType(type.StringType())),
        'peerId': type.OptionalType(type.StringType()),
        'lastInformationalMessage': type.OptionalType(type.StringType()),
        'localSubnets': type.OptionalType(type.ListType(type.StringType())),
    },
    IpsecSiteIKEStatus,
    False,
    None))



class IpsecSiteStats(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'rxBytesOnSite': 'rx_bytes_on_site',
                            'tunnelStats': 'tunnel_stats',
                            'ikeStatus': 'ike_status',
                            'siteStatus': 'site_status',
                            'txBytesFromSite': 'tx_bytes_from_site',
                            }

    def __init__(self,
                 rx_bytes_on_site=None,
                 tunnel_stats=None,
                 ike_status=None,
                 site_status=None,
                 tx_bytes_from_site=None,
                ):
        """
        :type  rx_bytes_on_site: :class:`long` or ``None``
        :param rx_bytes_on_site: 
        :type  tunnel_stats: :class:`list` of :class:`IpsecTunnelStats` or ``None``
        :param tunnel_stats: 
        :type  ike_status: :class:`IpsecSiteIKEStatus` or ``None``
        :param ike_status: 
        :type  site_status: :class:`str` or ``None``
        :param site_status: 
        :type  tx_bytes_from_site: :class:`long` or ``None``
        :param tx_bytes_from_site: 
        """
        self.rx_bytes_on_site = rx_bytes_on_site
        self.tunnel_stats = tunnel_stats
        self.ike_status = ike_status
        self.site_status = site_status
        self.tx_bytes_from_site = tx_bytes_from_site
        VapiStruct.__init__(self)

IpsecSiteStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec_site_stats', {
        'rxBytesOnSite': type.OptionalType(type.IntegerType()),
        'tunnelStats': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'IpsecTunnelStats'))),
        'ikeStatus': type.OptionalType(type.ReferenceType(__name__, 'IpsecSiteIKEStatus')),
        'siteStatus': type.OptionalType(type.StringType()),
        'txBytesFromSite': type.OptionalType(type.IntegerType()),
    },
    IpsecSiteStats,
    False,
    None))



class IpsecSites(VapiStruct):
    """
    List of IPsec sites for NSX Edge.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'sites': 'sites',
                            }

    def __init__(self,
                 sites=None,
                ):
        """
        :type  sites: :class:`list` of :class:`IpsecSite` or ``None``
        :param sites: 
        """
        self.sites = sites
        VapiStruct.__init__(self)

IpsecSites._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec_sites', {
        'sites': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'IpsecSite'))),
    },
    IpsecSites,
    False,
    None))



class IpsecStatusAndStats(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timeStamp': 'time_stamp',
                            'serverStatus': 'server_status',
                            'siteStatistics': 'site_statistics',
                            }

    def __init__(self,
                 time_stamp=None,
                 server_status=None,
                 site_statistics=None,
                ):
        """
        :type  time_stamp: :class:`long` or ``None``
        :param time_stamp: 
        :type  server_status: :class:`str` or ``None``
        :param server_status: 
        :type  site_statistics: :class:`list` of :class:`IpsecSiteStats` or ``None``
        :param site_statistics: 
        """
        self.time_stamp = time_stamp
        self.server_status = server_status
        self.site_statistics = site_statistics
        VapiStruct.__init__(self)

IpsecStatusAndStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec_status_and_stats', {
        'timeStamp': type.OptionalType(type.IntegerType()),
        'serverStatus': type.OptionalType(type.StringType()),
        'siteStatistics': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'IpsecSiteStats'))),
    },
    IpsecStatusAndStats,
    False,
    None))



class IpsecTunnelStats(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'tunnelStatus': 'tunnel_status',
                            'peerSPI': 'peer_spi',
                            'rxBytesOnLocalSubnet': 'rx_bytes_on_local_subnet',
                            'establishedDate': 'established_date',
                            'peerSubnet': 'peer_subnet',
                            'authenticationAlgorithm': 'authentication_algorithm',
                            'tunnelState': 'tunnel_state',
                            'txBytesFromLocalSubnet': 'tx_bytes_from_local_subnet',
                            'lastInformationalMessage': 'last_informational_message',
                            'localSPI': 'local_spi',
                            'encryptionAlgorithm': 'encryption_algorithm',
                            'localSubnet': 'local_subnet',
                            }

    def __init__(self,
                 tunnel_status=None,
                 peer_spi=None,
                 rx_bytes_on_local_subnet=None,
                 established_date=None,
                 peer_subnet=None,
                 authentication_algorithm=None,
                 tunnel_state=None,
                 tx_bytes_from_local_subnet=None,
                 last_informational_message=None,
                 local_spi=None,
                 encryption_algorithm=None,
                 local_subnet=None,
                ):
        """
        :type  tunnel_status: :class:`str` or ``None``
        :param tunnel_status: 
        :type  peer_spi: :class:`str` or ``None``
        :param peer_spi: 
        :type  rx_bytes_on_local_subnet: :class:`long` or ``None``
        :param rx_bytes_on_local_subnet: 
        :type  established_date: :class:`str` or ``None``
        :param established_date: 
        :type  peer_subnet: :class:`str` or ``None``
        :param peer_subnet: 
        :type  authentication_algorithm: :class:`str` or ``None``
        :param authentication_algorithm: 
        :type  tunnel_state: :class:`str` or ``None``
        :param tunnel_state: 
        :type  tx_bytes_from_local_subnet: :class:`long` or ``None``
        :param tx_bytes_from_local_subnet: 
        :type  last_informational_message: :class:`str` or ``None``
        :param last_informational_message: 
        :type  local_spi: :class:`str` or ``None``
        :param local_spi: 
        :type  encryption_algorithm: :class:`str` or ``None``
        :param encryption_algorithm: 
        :type  local_subnet: :class:`str` or ``None``
        :param local_subnet: 
        """
        self.tunnel_status = tunnel_status
        self.peer_spi = peer_spi
        self.rx_bytes_on_local_subnet = rx_bytes_on_local_subnet
        self.established_date = established_date
        self.peer_subnet = peer_subnet
        self.authentication_algorithm = authentication_algorithm
        self.tunnel_state = tunnel_state
        self.tx_bytes_from_local_subnet = tx_bytes_from_local_subnet
        self.last_informational_message = last_informational_message
        self.local_spi = local_spi
        self.encryption_algorithm = encryption_algorithm
        self.local_subnet = local_subnet
        VapiStruct.__init__(self)

IpsecTunnelStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ipsec_tunnel_stats', {
        'tunnelStatus': type.OptionalType(type.StringType()),
        'peerSPI': type.OptionalType(type.StringType()),
        'rxBytesOnLocalSubnet': type.OptionalType(type.IntegerType()),
        'establishedDate': type.OptionalType(type.StringType()),
        'peerSubnet': type.OptionalType(type.StringType()),
        'authenticationAlgorithm': type.OptionalType(type.StringType()),
        'tunnelState': type.OptionalType(type.StringType()),
        'txBytesFromLocalSubnet': type.OptionalType(type.IntegerType()),
        'lastInformationalMessage': type.OptionalType(type.StringType()),
        'localSPI': type.OptionalType(type.StringType()),
        'encryptionAlgorithm': type.OptionalType(type.StringType()),
        'localSubnet': type.OptionalType(type.StringType()),
    },
    IpsecTunnelStats,
    False,
    None))



class KeyValueAttributes(VapiStruct):
    """
    Key value pair describing the feature configuration limit.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'value': 'value',
                            'key': 'key',
                            }

    def __init__(self,
                 value=None,
                 key=None,
                ):
        """
        :type  value: :class:`str` or ``None``
        :param value: Value corresponding to the key of the configuration limit
            parameter.
        :type  key: :class:`str` or ``None``
        :param key: Key name of the configuration limit parameter.
        """
        self.value = value
        self.key = key
        VapiStruct.__init__(self)

KeyValueAttributes._set_binding_type(type.StructType(
    'com.vmware.vmc.model.key_value_attributes', {
        'value': type.OptionalType(type.StringType()),
        'key': type.OptionalType(type.StringType()),
    },
    KeyValueAttributes,
    False,
    None))



class L2Extension(VapiStruct):
    """
    Layer 2 extension.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'tunnelId': 'tunnel_id',
                            }

    def __init__(self,
                 tunnel_id=None,
                ):
        """
        :type  tunnel_id: :class:`long`
        :param tunnel_id: Identifier for layer 2 extension tunnel. Valid range: 1-4093.
            format: int32
        """
        self.tunnel_id = tunnel_id
        VapiStruct.__init__(self)

L2Extension._set_binding_type(type.StructType(
    'com.vmware.vmc.model.l2_extension', {
        'tunnelId': type.IntegerType(),
    },
    L2Extension,
    False,
    None))



class L2Vpn(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'enabled': 'enabled',
                            'sites': 'sites',
                            'listener_ip': 'listener_ip',
                            }

    def __init__(self,
                 enabled=None,
                 sites=None,
                 listener_ip=None,
                ):
        """
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Enable (true) or disable (false) L2 VPN.
        :type  sites: :class:`list` of :class:`Site` or ``None``
        :param sites: Array of L2 vpn site config.
        :type  listener_ip: :class:`str` or ``None``
        :param listener_ip: Public uplink ip address. IP of external interface on which L2VPN
            service listens to.
        """
        self.enabled = enabled
        self.sites = sites
        self.listener_ip = listener_ip
        VapiStruct.__init__(self)

L2Vpn._set_binding_type(type.StructType(
    'com.vmware.vmc.model.l2_vpn', {
        'enabled': type.OptionalType(type.BooleanType()),
        'sites': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Site'))),
        'listener_ip': type.OptionalType(type.StringType()),
    },
    L2Vpn,
    False,
    None))



class L2vpnStats(VapiStruct):
    """
    L2 VPN status and statistics of a single L2 VPN site.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'tunnelStatus': 'tunnel_status',
                            'establishedDate': 'established_date',
                            'name': 'name',
                            'droppedRxPackets': 'dropped_rx_packets',
                            'encryptionAlgorithm': 'encryption_algorithm',
                            'failureMessage': 'failure_message',
                            'txBytesFromLocalSubnet': 'tx_bytes_from_local_subnet',
                            'rxBytesOnLocalSubnet': 'rx_bytes_on_local_subnet',
                            'droppedTxPackets': 'dropped_tx_packets',
                            'lastUpdatedTime': 'last_updated_time',
                            }

    def __init__(self,
                 tunnel_status=None,
                 established_date=None,
                 name=None,
                 dropped_rx_packets=None,
                 encryption_algorithm=None,
                 failure_message=None,
                 tx_bytes_from_local_subnet=None,
                 rx_bytes_on_local_subnet=None,
                 dropped_tx_packets=None,
                 last_updated_time=None,
                ):
        """
        :type  tunnel_status: :class:`str` or ``None``
        :param tunnel_status: Status of the tunnel (UP/DOWN).
        :type  established_date: :class:`long` or ``None``
        :param established_date: Tunnel established date. format: int64
        :type  name: :class:`str` or ``None``
        :param name: User defined name of the site.
        :type  dropped_rx_packets: :class:`long` or ``None``
        :param dropped_rx_packets: Number of received packets dropped.
        :type  encryption_algorithm: :class:`str` or ``None``
        :param encryption_algorithm: Cipher used in encryption.
        :type  failure_message: :class:`str` or ``None``
        :param failure_message: Reason for the tunnel down.
        :type  tx_bytes_from_local_subnet: :class:`long` or ``None``
        :param tx_bytes_from_local_subnet: Number of bytes transferred from local subnet.
        :type  rx_bytes_on_local_subnet: :class:`long` or ``None``
        :param rx_bytes_on_local_subnet: Number of bytes received on the local subnet.
        :type  dropped_tx_packets: :class:`long` or ``None``
        :param dropped_tx_packets: Number of transferred packets dropped.
        :type  last_updated_time: :class:`long` or ``None``
        :param last_updated_time: Time stamp of the statistics collection. format: int64
        """
        self.tunnel_status = tunnel_status
        self.established_date = established_date
        self.name = name
        self.dropped_rx_packets = dropped_rx_packets
        self.encryption_algorithm = encryption_algorithm
        self.failure_message = failure_message
        self.tx_bytes_from_local_subnet = tx_bytes_from_local_subnet
        self.rx_bytes_on_local_subnet = rx_bytes_on_local_subnet
        self.dropped_tx_packets = dropped_tx_packets
        self.last_updated_time = last_updated_time
        VapiStruct.__init__(self)

L2vpnStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.l2vpn_stats', {
        'tunnelStatus': type.OptionalType(type.StringType()),
        'establishedDate': type.OptionalType(type.IntegerType()),
        'name': type.OptionalType(type.StringType()),
        'droppedRxPackets': type.OptionalType(type.IntegerType()),
        'encryptionAlgorithm': type.OptionalType(type.StringType()),
        'failureMessage': type.OptionalType(type.StringType()),
        'txBytesFromLocalSubnet': type.OptionalType(type.IntegerType()),
        'rxBytesOnLocalSubnet': type.OptionalType(type.IntegerType()),
        'droppedTxPackets': type.OptionalType(type.IntegerType()),
        'lastUpdatedTime': type.OptionalType(type.IntegerType()),
    },
    L2vpnStats,
    False,
    None))



class L2vpnStatusAndStats(VapiStruct):
    """
    L2 VPN status and statistics.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timeStamp': 'time_stamp',
                            'serverStatus': 'server_status',
                            'siteStats': 'site_stats',
                            }

    def __init__(self,
                 time_stamp=None,
                 server_status=None,
                 site_stats=None,
                ):
        """
        :type  time_stamp: :class:`long` or ``None``
        :param time_stamp: Time stamp of statistics collection. format: int64
        :type  server_status: :class:`str` or ``None``
        :param server_status: 
        :type  site_stats: :class:`list` of :class:`L2vpnStats` or ``None``
        :param site_stats: List of statistics for each Site.
        """
        self.time_stamp = time_stamp
        self.server_status = server_status
        self.site_stats = site_stats
        VapiStruct.__init__(self)

L2vpnStatusAndStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.l2vpn_status_and_stats', {
        'timeStamp': type.OptionalType(type.IntegerType()),
        'serverStatus': type.OptionalType(type.StringType()),
        'siteStats': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'L2vpnStats'))),
    },
    L2vpnStatusAndStats,
    False,
    None))



class LicenceAclPermissions(VapiStruct):
    """
    Licence and access control information for the feature.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'dataPermission': 'data_permission',
                            'isLicensed': 'is_licensed',
                            'accessPermission': 'access_permission',
                            }

    def __init__(self,
                 data_permission=None,
                 is_licensed=None,
                 access_permission=None,
                ):
        """
        :type  data_permission: :class:`DataPermissions` or ``None``
        :param data_permission: Data access control information for the feature.
        :type  is_licensed: :class:`bool` or ``None``
        :param is_licensed: Value is true if feature is licenced.
        :type  access_permission: :class:`InteractionPermissions` or ``None``
        :param access_permission: Access control information for the feature.
        """
        self.data_permission = data_permission
        self.is_licensed = is_licensed
        self.access_permission = access_permission
        VapiStruct.__init__(self)

LicenceAclPermissions._set_binding_type(type.StructType(
    'com.vmware.vmc.model.licence_acl_permissions', {
        'dataPermission': type.OptionalType(type.ReferenceType(__name__, 'DataPermissions')),
        'isLicensed': type.OptionalType(type.BooleanType()),
        'accessPermission': type.OptionalType(type.ReferenceType(__name__, 'InteractionPermissions')),
    },
    LicenceAclPermissions,
    False,
    None))



class LoadBalancerDashboardStats(VapiStruct):
    """
    Dashboard Statistics data for Load Balancer.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'lbBpsIn': 'lb_bps_in',
                            'lbHttpReqs': 'lb_http_reqs',
                            'lbBpsOut': 'lb_bps_out',
                            'lbSessions': 'lb_sessions',
                            }

    def __init__(self,
                 lb_bps_in=None,
                 lb_http_reqs=None,
                 lb_bps_out=None,
                 lb_sessions=None,
                ):
        """
        :type  lb_bps_in: :class:`list` of :class:`DashboardStat` or ``None``
        :param lb_bps_in: Number of bytes in.
        :type  lb_http_reqs: :class:`list` of :class:`DashboardStat` or ``None``
        :param lb_http_reqs: Number of HTTP requests received by Load Balancer.
        :type  lb_bps_out: :class:`list` of :class:`DashboardStat` or ``None``
        :param lb_bps_out: Number of bytes out.
        :type  lb_sessions: :class:`list` of :class:`DashboardStat` or ``None``
        :param lb_sessions: Number of Load Balancer sessions.
        """
        self.lb_bps_in = lb_bps_in
        self.lb_http_reqs = lb_http_reqs
        self.lb_bps_out = lb_bps_out
        self.lb_sessions = lb_sessions
        VapiStruct.__init__(self)

LoadBalancerDashboardStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.load_balancer_dashboard_stats', {
        'lbBpsIn': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'lbHttpReqs': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'lbBpsOut': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'lbSessions': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
    },
    LoadBalancerDashboardStats,
    False,
    None))



class Logging(VapiStruct):
    """
    logging.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'logLevel': 'log_level',
                            'enable': 'enable',
                            }

    def __init__(self,
                 log_level=None,
                 enable=None,
                ):
        """
        :type  log_level: :class:`str` or ``None``
        :param log_level: Log level. Valid values: emergency, alert, critical, error,
            warning, notice, info, debug.
        :type  enable: :class:`bool` or ``None``
        :param enable: Logging enabled.
        """
        self.log_level = log_level
        self.enable = enable
        VapiStruct.__init__(self)

Logging._set_binding_type(type.StructType(
    'com.vmware.vmc.model.logging', {
        'logLevel': type.OptionalType(type.StringType()),
        'enable': type.OptionalType(type.BooleanType()),
    },
    Logging,
    False,
    None))



class LogicalNetwork(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    NETWORK_TYPE_HOSTED = "HOSTED"
    """


    """
    NETWORK_TYPE_ROUTED = "ROUTED"
    """


    """
    NETWORK_TYPE_EXTENDED = "EXTENDED"
    """


    """



    _canonical_to_pep_names = {
                            'subnet_cidr': 'subnet_cidr',
                            'name': 'name',
                            'gatewayIp': 'gateway_ip',
                            'dhcp_enabled': 'dhcp_enabled',
                            'dhcp_ip_range': 'dhcp_ip_range',
                            'tunnel_id': 'tunnel_id',
                            'id': 'id',
                            'network_type': 'network_type',
                            }

    def __init__(self,
                 subnet_cidr=None,
                 name=None,
                 gateway_ip=None,
                 dhcp_enabled=None,
                 dhcp_ip_range=None,
                 tunnel_id=None,
                 id=None,
                 network_type=None,
                ):
        """
        :type  subnet_cidr: :class:`str` or ``None``
        :param subnet_cidr: the subnet cidr
        :type  name: :class:`str` or ``None``
        :param name: name of the network
        :type  gateway_ip: :class:`str` or ``None``
        :param gateway_ip: gateway ip of the logical network
        :type  dhcp_enabled: :class:`str` or ``None``
        :param dhcp_enabled: if 'true' - enabled; if 'false' - disabled
        :type  dhcp_ip_range: :class:`str` or ``None``
        :param dhcp_ip_range: ip range within the subnet mask, range delimiter is '-' (example
            10.118.10.130-10.118.10.140)
        :type  tunnel_id: :class:`long` or ``None``
        :param tunnel_id: tunnel id of extended network format: int32
        :type  id: :class:`str` or ``None``
        :param id: 
        :type  network_type: :class:`str` or ``None``
        :param network_type: Possible values are: 
            
            * :attr:`LogicalNetwork.NETWORK_TYPE_HOSTED`
            * :attr:`LogicalNetwork.NETWORK_TYPE_ROUTED`
            * :attr:`LogicalNetwork.NETWORK_TYPE_EXTENDED`
        """
        self.subnet_cidr = subnet_cidr
        self.name = name
        self.gateway_ip = gateway_ip
        self.dhcp_enabled = dhcp_enabled
        self.dhcp_ip_range = dhcp_ip_range
        self.tunnel_id = tunnel_id
        self.id = id
        self.network_type = network_type
        VapiStruct.__init__(self)

LogicalNetwork._set_binding_type(type.StructType(
    'com.vmware.vmc.model.logical_network', {
        'subnet_cidr': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'gatewayIp': type.OptionalType(type.StringType()),
        'dhcp_enabled': type.OptionalType(type.StringType()),
        'dhcp_ip_range': type.OptionalType(type.StringType()),
        'tunnel_id': type.OptionalType(type.IntegerType()),
        'id': type.OptionalType(type.StringType()),
        'network_type': type.OptionalType(type.StringType()),
    },
    LogicalNetwork,
    False,
    None))



class LogicalRouterScope(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'type': 'type',
                            'id': 'id',
                            }

    def __init__(self,
                 type=None,
                 id=None,
                ):
        """
        :type  type: :class:`str` or ``None``
        :param type: 
        :type  id: :class:`str` or ``None``
        :param id: 
        """
        self.type = type
        self.id = id
        VapiStruct.__init__(self)

LogicalRouterScope._set_binding_type(type.StructType(
    'com.vmware.vmc.model.logical_router_scope', {
        'type': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
    },
    LogicalRouterScope,
    False,
    None))



class LogicalRouterScopes(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'logicalRouterScope': 'logical_router_scope',
                            }

    def __init__(self,
                 logical_router_scope=None,
                ):
        """
        :type  logical_router_scope: :class:`list` of :class:`LogicalRouterScope` or ``None``
        :param logical_router_scope: 
        """
        self.logical_router_scope = logical_router_scope
        VapiStruct.__init__(self)

LogicalRouterScopes._set_binding_type(type.StructType(
    'com.vmware.vmc.model.logical_router_scopes', {
        'logicalRouterScope': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'LogicalRouterScope'))),
    },
    LogicalRouterScopes,
    False,
    None))



class MacAddress(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'edgeVmHaIndex': 'edge_vm_ha_index',
                            'value': 'value',
                            }

    def __init__(self,
                 edge_vm_ha_index=None,
                 value=None,
                ):
        """
        :type  edge_vm_ha_index: :class:`long` or ``None``
        :param edge_vm_ha_index: 
        :type  value: :class:`str` or ``None``
        :param value: 
        """
        self.edge_vm_ha_index = edge_vm_ha_index
        self.value = value
        VapiStruct.__init__(self)

MacAddress._set_binding_type(type.StructType(
    'com.vmware.vmc.model.mac_address', {
        'edgeVmHaIndex': type.OptionalType(type.IntegerType()),
        'value': type.OptionalType(type.StringType()),
    },
    MacAddress,
    False,
    None))



class ManagementGatewayTemplate(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'public_ip': 'public_ip',
                            'primary_dns': 'primary_dns',
                            'secondary_dns': 'secondary_dns',
                            'firewall_rules': 'firewall_rules',
                            'vpns': 'vpns',
                            'subnet_cidr': 'subnet_cidr',
                            }

    def __init__(self,
                 public_ip=None,
                 primary_dns=None,
                 secondary_dns=None,
                 firewall_rules=None,
                 vpns=None,
                 subnet_cidr=None,
                ):
        """
        :type  public_ip: :class:`SddcPublicIp` or ``None``
        :param public_ip: 
        :type  primary_dns: :class:`str` or ``None``
        :param primary_dns: 
        :type  secondary_dns: :class:`str` or ``None``
        :param secondary_dns: 
        :type  firewall_rules: :class:`list` of :class:`FirewallRule` or ``None``
        :param firewall_rules: 
        :type  vpns: :class:`list` of :class:`Vpn` or ``None``
        :param vpns: 
        :type  subnet_cidr: :class:`str` or ``None``
        :param subnet_cidr: mgw network subnet cidr
        """
        self.public_ip = public_ip
        self.primary_dns = primary_dns
        self.secondary_dns = secondary_dns
        self.firewall_rules = firewall_rules
        self.vpns = vpns
        self.subnet_cidr = subnet_cidr
        VapiStruct.__init__(self)

ManagementGatewayTemplate._set_binding_type(type.StructType(
    'com.vmware.vmc.model.management_gateway_template', {
        'public_ip': type.OptionalType(type.ReferenceType(__name__, 'SddcPublicIp')),
        'primary_dns': type.OptionalType(type.StringType()),
        'secondary_dns': type.OptionalType(type.StringType()),
        'firewall_rules': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'FirewallRule'))),
        'vpns': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Vpn'))),
        'subnet_cidr': type.OptionalType(type.StringType()),
    },
    ManagementGatewayTemplate,
    False,
    None))



class MapZonesRequest(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'connected_account_id': 'connected_account_id',
                            'org_id': 'org_id',
                            'petronas_regions_to_map': 'petronas_regions_to_map',
                            }

    def __init__(self,
                 connected_account_id=None,
                 org_id=None,
                 petronas_regions_to_map=None,
                ):
        """
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: The connected account ID to remap. This is a standard UUID.
        :type  org_id: :class:`str` or ``None``
        :param org_id: The org ID to remap in. This is a standard UUID.
        :type  petronas_regions_to_map: :class:`list` of :class:`str` or ``None``
        :param petronas_regions_to_map: A list of Petronas regions to map.
        """
        self.connected_account_id = connected_account_id
        self.org_id = org_id
        self.petronas_regions_to_map = petronas_regions_to_map
        VapiStruct.__init__(self)

MapZonesRequest._set_binding_type(type.StructType(
    'com.vmware.vmc.model.map_zones_request', {
        'connected_account_id': type.OptionalType(type.StringType()),
        'org_id': type.OptionalType(type.StringType()),
        'petronas_regions_to_map': type.OptionalType(type.ListType(type.StringType())),
    },
    MapZonesRequest,
    False,
    None))



class MetaDashboardStats(VapiStruct):
    """
    Start time, end time and interval details.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vnics': 'vnics',
                            'endTime': 'end_time',
                            'startTime': 'start_time',
                            'interval': 'interval',
                            }

    def __init__(self,
                 vnics=None,
                 end_time=None,
                 start_time=None,
                 interval=None,
                ):
        """
        :type  vnics: :class:`list` of :class:`Vnic` or ``None``
        :param vnics: Statistics data is collected for these vNICs.
        :type  end_time: :class:`long` or ``None``
        :param end_time: End time in seconds. format: int64
        :type  start_time: :class:`long` or ``None``
        :param start_time: Start time in seconds. format: int64
        :type  interval: :class:`long` or ``None``
        :param interval: Time interval in seconds. format: int32
        """
        self.vnics = vnics
        self.end_time = end_time
        self.start_time = start_time
        self.interval = interval
        VapiStruct.__init__(self)

MetaDashboardStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.meta_dashboard_stats', {
        'vnics': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Vnic'))),
        'endTime': type.OptionalType(type.IntegerType()),
        'startTime': type.OptionalType(type.IntegerType()),
        'interval': type.OptionalType(type.IntegerType()),
    },
    MetaDashboardStats,
    False,
    None))



class Metadata(VapiStruct):
    """
    metadata of the sddc manifest

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timestamp': 'timestamp',
                            'cycle_id': 'cycle_id',
                            }

    def __init__(self,
                 timestamp=None,
                 cycle_id=None,
                ):
        """
        :type  timestamp: :class:`str` or ``None``
        :param timestamp: the timestamp for the bundle
        :type  cycle_id: :class:`str` or ``None``
        :param cycle_id: the cycle id
        """
        self.timestamp = timestamp
        self.cycle_id = cycle_id
        VapiStruct.__init__(self)

Metadata._set_binding_type(type.StructType(
    'com.vmware.vmc.model.metadata', {
        'timestamp': type.OptionalType(type.StringType()),
        'cycle_id': type.OptionalType(type.StringType()),
    },
    Metadata,
    False,
    None))



class Nat(VapiStruct):
    """
    NAT configuration

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'rules': 'rules',
                            'featureType': 'feature_type',
                            'version': 'version',
                            'enabled': 'enabled',
                            'template': 'template',
                            }

    def __init__(self,
                 rules=None,
                 feature_type=None,
                 version=None,
                 enabled=None,
                 template=None,
                ):
        """
        :type  rules: :class:`NatRules` or ``None``
        :param rules: Ordered list of NAT rules.
        :type  feature_type: :class:`str` or ``None``
        :param feature_type: 
        :type  version: :class:`long` or ``None``
        :param version: Version number tracking each configuration change. To avoid
            problems with overwriting changes, always retrieve and modify the
            latest configuration to include the current version number in your
            request. If you provide a version number which is not current, the
            request is rejected. If you omit the version number, the request is
            accepted but may overwrite any current changes if your change is
            not in sync with the latest change. format: int64
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Value is true if feature is enabled. Default value is true.
            Optional.
        :type  template: :class:`str` or ``None``
        :param template: 
        """
        self.rules = rules
        self.feature_type = feature_type
        self.version = version
        self.enabled = enabled
        self.template = template
        VapiStruct.__init__(self)

Nat._set_binding_type(type.StructType(
    'com.vmware.vmc.model.nat', {
        'rules': type.OptionalType(type.ReferenceType(__name__, 'NatRules')),
        'featureType': type.OptionalType(type.StringType()),
        'version': type.OptionalType(type.IntegerType()),
        'enabled': type.OptionalType(type.BooleanType()),
        'template': type.OptionalType(type.StringType()),
    },
    Nat,
    False,
    None))



class NatRule(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    ACTION_DNAT = "dnat"
    """


    """
    ACTION_SNAT = "snat"
    """


    """



    _canonical_to_pep_names = {
                            'rule_type': 'rule_type',
                            'protocol': 'protocol',
                            'name': 'name',
                            'internal_ports': 'internal_ports',
                            'public_ports': 'public_ports',
                            'public_ip': 'public_ip',
                            'internal_ip': 'internal_ip',
                            'action': 'action',
                            'id': 'id',
                            'revision': 'revision',
                            }

    def __init__(self,
                 rule_type=None,
                 protocol=None,
                 name=None,
                 internal_ports=None,
                 public_ports=None,
                 public_ip=None,
                 internal_ip=None,
                 action=None,
                 id=None,
                 revision=None,
                ):
        """
        :type  rule_type: :class:`str` or ``None``
        :param rule_type: 
        :type  protocol: :class:`str` or ``None``
        :param protocol: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  internal_ports: :class:`str` or ``None``
        :param internal_ports: 
        :type  public_ports: :class:`str` or ``None``
        :param public_ports: 
        :type  public_ip: :class:`str` or ``None``
        :param public_ip: 
        :type  internal_ip: :class:`str` or ``None``
        :param internal_ip: 
        :type  action: :class:`str` or ``None``
        :param action: Possible values are: 
            
            * :attr:`NatRule.ACTION_DNAT`
            * :attr:`NatRule.ACTION_SNAT`
        :type  id: :class:`str` or ``None``
        :param id: 
        :type  revision: :class:`long` or ``None``
        :param revision: current revision of the list of nat rules, used to protect against
            concurrent modification (first writer wins) format: int32
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.rule_type = rule_type
        self.protocol = protocol
        self.name = name
        self.internal_ports = internal_ports
        self.public_ports = public_ports
        self.public_ip = public_ip
        self.internal_ip = internal_ip
        self.action = action
        self.id = id
        self.revision = revision
        VapiStruct.__init__(self)

NatRule._set_binding_type(type.StructType(
    'com.vmware.vmc.model.nat_rule', {
        'rule_type': type.OptionalType(type.StringType()),
        'protocol': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'internal_ports': type.OptionalType(type.StringType()),
        'public_ports': type.OptionalType(type.StringType()),
        'public_ip': type.OptionalType(type.StringType()),
        'internal_ip': type.OptionalType(type.StringType()),
        'action': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'revision': type.OptionalType(type.IntegerType()),
    },
    NatRule,
    False,
    None))



class NatRules(VapiStruct):
    """
    Ordered list of NAT rules.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'natRulesDtos': 'nat_rules_dtos',
                            }

    def __init__(self,
                 nat_rules_dtos=None,
                ):
        """
        :type  nat_rules_dtos: :class:`list` of :class:`Nsxnatrule` or ``None``
        :param nat_rules_dtos: Ordered list of NAT rules.
        """
        self.nat_rules_dtos = nat_rules_dtos
        VapiStruct.__init__(self)

NatRules._set_binding_type(type.StructType(
    'com.vmware.vmc.model.nat_rules', {
        'natRulesDtos': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Nsxnatrule'))),
    },
    NatRules,
    False,
    None))



class NetworkingTemplate(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'management_gateway_templates': 'management_gateway_templates',
                            'compute_gateway_templates': 'compute_gateway_templates',
                            }

    def __init__(self,
                 management_gateway_templates=None,
                 compute_gateway_templates=None,
                ):
        """
        :type  management_gateway_templates: :class:`list` of :class:`ManagementGatewayTemplate` or ``None``
        :param management_gateway_templates: 
        :type  compute_gateway_templates: :class:`list` of :class:`ComputeGatewayTemplate` or ``None``
        :param compute_gateway_templates: 
        """
        self.management_gateway_templates = management_gateway_templates
        self.compute_gateway_templates = compute_gateway_templates
        VapiStruct.__init__(self)

NetworkingTemplate._set_binding_type(type.StructType(
    'com.vmware.vmc.model.networking_template', {
        'management_gateway_templates': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ManagementGatewayTemplate'))),
        'compute_gateway_templates': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ComputeGatewayTemplate'))),
    },
    NetworkingTemplate,
    False,
    None))



class Nsxfirewallrule(VapiStruct):
    """
    Firewall Rule

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ruleType': 'rule_type',
                            'description': 'description',
                            'ruleId': 'rule_id',
                            'matchTranslated': 'match_translated',
                            'invalidApplication': 'invalid_application',
                            'direction': 'direction',
                            'statistics': 'statistics',
                            'name': 'name',
                            'invalidSource': 'invalid_source',
                            'loggingEnabled': 'logging_enabled',
                            'destination': 'destination',
                            'enabled': 'enabled',
                            'application': 'application',
                            'source': 'source',
                            'action': 'action',
                            'invalidDestination': 'invalid_destination',
                            'ruleTag': 'rule_tag',
                            }

    def __init__(self,
                 rule_type=None,
                 description=None,
                 rule_id=None,
                 match_translated=None,
                 invalid_application=None,
                 direction=None,
                 statistics=None,
                 name=None,
                 invalid_source=None,
                 logging_enabled=None,
                 destination=None,
                 enabled=None,
                 application=None,
                 source=None,
                 action=None,
                 invalid_destination=None,
                 rule_tag=None,
                ):
        """
        :type  rule_type: :class:`str` or ``None``
        :param rule_type: Identifies the type of the rule. internal_high or user.
        :type  description: :class:`str` or ``None``
        :param description: Description for the rule
        :type  rule_id: :class:`long` or ``None``
        :param rule_id: Identifier for the rule. format: int64
        :type  match_translated: :class:`bool` or ``None``
        :param match_translated: Defines the order of NAT and Firewall pipeline. When false,
            firewall happens before NAT. Default : false
        :type  invalid_application: :class:`bool` or ``None``
        :param invalid_application: 
        :type  direction: :class:`str` or ``None``
        :param direction: Direction. Possible values in or out. Default is 'any'.
        :type  statistics: :class:`FirewallRuleStats` or ``None``
        :param statistics: Statistics for the rule
        :type  name: :class:`str` or ``None``
        :param name: Name for the rule.
        :type  invalid_source: :class:`bool` or ``None``
        :param invalid_source: 
        :type  logging_enabled: :class:`bool` or ``None``
        :param logging_enabled: Enable logging for the rule.
        :type  destination: :class:`AddressFWSourceDestination` or ``None``
        :param destination: List of destinations. Default is any.
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Enable rule.
        :type  application: :class:`Application` or ``None``
        :param application: List of applications. Default is any.
        :type  source: :class:`AddressFWSourceDestination` or ``None``
        :param source: List of sources. Default is any.
        :type  action: :class:`str` or ``None``
        :param action: Action. Values : accept, deny
        :type  invalid_destination: :class:`bool` or ``None``
        :param invalid_destination: 
        :type  rule_tag: :class:`long` or ``None``
        :param rule_tag: Rule tag. Used to specify user-defined ruleId. If not specified NSX
            Manager will generate ruleId. format: int64
        """
        self.rule_type = rule_type
        self.description = description
        self.rule_id = rule_id
        self.match_translated = match_translated
        self.invalid_application = invalid_application
        self.direction = direction
        self.statistics = statistics
        self.name = name
        self.invalid_source = invalid_source
        self.logging_enabled = logging_enabled
        self.destination = destination
        self.enabled = enabled
        self.application = application
        self.source = source
        self.action = action
        self.invalid_destination = invalid_destination
        self.rule_tag = rule_tag
        VapiStruct.__init__(self)

Nsxfirewallrule._set_binding_type(type.StructType(
    'com.vmware.vmc.model.nsxfirewallrule', {
        'ruleType': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'ruleId': type.OptionalType(type.IntegerType()),
        'matchTranslated': type.OptionalType(type.BooleanType()),
        'invalidApplication': type.OptionalType(type.BooleanType()),
        'direction': type.OptionalType(type.StringType()),
        'statistics': type.OptionalType(type.ReferenceType(__name__, 'FirewallRuleStats')),
        'name': type.OptionalType(type.StringType()),
        'invalidSource': type.OptionalType(type.BooleanType()),
        'loggingEnabled': type.OptionalType(type.BooleanType()),
        'destination': type.OptionalType(type.ReferenceType(__name__, 'AddressFWSourceDestination')),
        'enabled': type.OptionalType(type.BooleanType()),
        'application': type.OptionalType(type.ReferenceType(__name__, 'Application')),
        'source': type.OptionalType(type.ReferenceType(__name__, 'AddressFWSourceDestination')),
        'action': type.OptionalType(type.StringType()),
        'invalidDestination': type.OptionalType(type.BooleanType()),
        'ruleTag': type.OptionalType(type.IntegerType()),
    },
    Nsxfirewallrule,
    False,
    None))



class Nsxfirewallservice(VapiStruct):
    """
    Application (service) for firewall rule.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'sourcePort': 'source_port',
                            'protocol': 'protocol',
                            'port': 'port',
                            'icmpType': 'icmp_type',
                            }

    def __init__(self,
                 source_port=None,
                 protocol=None,
                 port=None,
                 icmp_type=None,
                ):
        """
        :type  source_port: :class:`list` of :class:`str` or ``None``
        :param source_port: List of source ports.
        :type  protocol: :class:`str` or ``None``
        :param protocol: Protocol.
        :type  port: :class:`list` of :class:`str` or ``None``
        :param port: List of destination ports.
        :type  icmp_type: :class:`str` or ``None``
        :param icmp_type: IcmpType. Only supported when protocol is icmp. Default is 'any'.
        """
        self.source_port = source_port
        self.protocol = protocol
        self.port = port
        self.icmp_type = icmp_type
        VapiStruct.__init__(self)

Nsxfirewallservice._set_binding_type(type.StructType(
    'com.vmware.vmc.model.nsxfirewallservice', {
        'sourcePort': type.OptionalType(type.ListType(type.StringType())),
        'protocol': type.OptionalType(type.StringType()),
        'port': type.OptionalType(type.ListType(type.StringType())),
        'icmpType': type.OptionalType(type.StringType()),
    },
    Nsxfirewallservice,
    False,
    None))



class Nsxl2vpn(VapiStruct):
    """
    L2 VPN server configuration.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'listenerIps': 'listener_ips',
                            'enabled': 'enabled',
                            'sites': 'sites',
                            }

    def __init__(self,
                 listener_ips=None,
                 enabled=None,
                 sites=None,
                ):
        """
        :type  listener_ips: :class:`list` of :class:`str`
        :param listener_ips: Listener IP addresses.
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Enabled state of L2 VPN service.
        :type  sites: :class:`Sites`
        :param sites: List of L2 VPN sites.
        """
        self.listener_ips = listener_ips
        self.enabled = enabled
        self.sites = sites
        VapiStruct.__init__(self)

Nsxl2vpn._set_binding_type(type.StructType(
    'com.vmware.vmc.model.nsxl2vpn', {
        'listenerIps': type.ListType(type.StringType()),
        'enabled': type.OptionalType(type.BooleanType()),
        'sites': type.ReferenceType(__name__, 'Sites'),
    },
    Nsxl2vpn,
    False,
    None))



class Nsxnatrule(VapiStruct):
    """
    NAT rule

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vnic': 'vnic',
                            'ruleType': 'rule_type',
                            'protocol': 'protocol',
                            'description': 'description',
                            'ruleId': 'rule_id',
                            'snatMatchDestinationPort': 'snat_match_destination_port',
                            'originalAddress': 'original_address',
                            'dnatMatchSourceAddress': 'dnat_match_source_address',
                            'dnatMatchSourcePort': 'dnat_match_source_port',
                            'snatMatchDestinationAddress': 'snat_match_destination_address',
                            'originalPort': 'original_port',
                            'loggingEnabled': 'logging_enabled',
                            'translatedAddress': 'translated_address',
                            'enabled': 'enabled',
                            'icmpType': 'icmp_type',
                            'translatedPort': 'translated_port',
                            'action': 'action',
                            'ruleTag': 'rule_tag',
                            }

    def __init__(self,
                 vnic=None,
                 rule_type=None,
                 protocol=None,
                 description=None,
                 rule_id=None,
                 snat_match_destination_port=None,
                 original_address=None,
                 dnat_match_source_address=None,
                 dnat_match_source_port=None,
                 snat_match_destination_address=None,
                 original_port=None,
                 logging_enabled=None,
                 translated_address=None,
                 enabled=None,
                 icmp_type=None,
                 translated_port=None,
                 action=None,
                 rule_tag=None,
                ):
        """
        :type  vnic: :class:`str` or ``None``
        :param vnic: Interface on which the NAT rule is applied.
        :type  rule_type: :class:`str` or ``None``
        :param rule_type: Identifies the type of the rule. internal_high or user.
        :type  protocol: :class:`str` or ``None``
        :param protocol: Protocol. Default is 'any'
        :type  description: :class:`str` or ``None``
        :param description: Description for the rule.
        :type  rule_id: :class:`long` or ``None``
        :param rule_id: Identifier for the rule. format: int64
        :type  snat_match_destination_port: :class:`str` or ``None``
        :param snat_match_destination_port: Apply SNAT rule only if traffic has this destination port. Default
            is 'any'.
        :type  original_address: :class:`str` or ``None``
        :param original_address: Original address or address range. This is the original source
            address for SNAT rules and the original destination address for
            DNAT rules.
        :type  dnat_match_source_address: :class:`str` or ``None``
        :param dnat_match_source_address: Apply DNAT rule only if traffic has this source address. Default is
            'any'.
        :type  dnat_match_source_port: :class:`str` or ``None``
        :param dnat_match_source_port: Apply DNAT rule only if traffic has this source port. Default is
            'any'.
        :type  snat_match_destination_address: :class:`str` or ``None``
        :param snat_match_destination_address: Apply SNAT rule only if traffic has this destination address.
            Default is 'any'.
        :type  original_port: :class:`str` or ``None``
        :param original_port: Original port. This is the original source port for SNAT rules, and
            the original destination port for DNAT rules.
        :type  logging_enabled: :class:`bool` or ``None``
        :param logging_enabled: Enable logging for the rule.
        :type  translated_address: :class:`str` or ``None``
        :param translated_address: Translated address or address range.
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Enable rule.
        :type  icmp_type: :class:`str` or ``None``
        :param icmp_type: ICMP type. Only supported when protocol is icmp. Default is 'any'.
        :type  translated_port: :class:`str` or ``None``
        :param translated_port: Translated port. Supported in DNAT rules only.
        :type  action: :class:`str` or ``None``
        :param action: Action for the rule. SNAT or DNAT.
        :type  rule_tag: :class:`long` or ``None``
        :param rule_tag: Rule tag. Used to specify user-defined ruleId. If not specified NSX
            Manager will generate ruleId. format: int64
        """
        self.vnic = vnic
        self.rule_type = rule_type
        self.protocol = protocol
        self.description = description
        self.rule_id = rule_id
        self.snat_match_destination_port = snat_match_destination_port
        self.original_address = original_address
        self.dnat_match_source_address = dnat_match_source_address
        self.dnat_match_source_port = dnat_match_source_port
        self.snat_match_destination_address = snat_match_destination_address
        self.original_port = original_port
        self.logging_enabled = logging_enabled
        self.translated_address = translated_address
        self.enabled = enabled
        self.icmp_type = icmp_type
        self.translated_port = translated_port
        self.action = action
        self.rule_tag = rule_tag
        VapiStruct.__init__(self)

Nsxnatrule._set_binding_type(type.StructType(
    'com.vmware.vmc.model.nsxnatrule', {
        'vnic': type.OptionalType(type.StringType()),
        'ruleType': type.OptionalType(type.StringType()),
        'protocol': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'ruleId': type.OptionalType(type.IntegerType()),
        'snatMatchDestinationPort': type.OptionalType(type.StringType()),
        'originalAddress': type.OptionalType(type.StringType()),
        'dnatMatchSourceAddress': type.OptionalType(type.StringType()),
        'dnatMatchSourcePort': type.OptionalType(type.StringType()),
        'snatMatchDestinationAddress': type.OptionalType(type.StringType()),
        'originalPort': type.OptionalType(type.StringType()),
        'loggingEnabled': type.OptionalType(type.BooleanType()),
        'translatedAddress': type.OptionalType(type.StringType()),
        'enabled': type.OptionalType(type.BooleanType()),
        'icmpType': type.OptionalType(type.StringType()),
        'translatedPort': type.OptionalType(type.StringType()),
        'action': type.OptionalType(type.StringType()),
        'ruleTag': type.OptionalType(type.IntegerType()),
    },
    Nsxnatrule,
    False,
    None))



class Nsxsite(VapiStruct):
    """
    L2 VPN site.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'secureTraffic': 'secure_traffic',
                            'siteId': 'site_id',
                            'name': 'name',
                            'password': 'password',
                            'userId': 'user_id',
                            'description': 'description',
                            }

    def __init__(self,
                 secure_traffic=None,
                 site_id=None,
                 name=None,
                 password=None,
                 user_id=None,
                 description=None,
                ):
        """
        :type  secure_traffic: :class:`bool` or ``None``
        :param secure_traffic: Secure L2VPN traffic.
        :type  site_id: :class:`str` or ``None``
        :param site_id: Identifier for L2 VPN site.
        :type  name: :class:`str` or ``None``
        :param name: Name of L2 VPN site. Length: 1-255 characters.
        :type  password: :class:`str` or ``None``
        :param password: Password for L2 VPN user. Passwords must contain the following:
            12-63 characters, a mix of upper case letters, lower case letters,
            numbers, and at least one special character. Password must not
            contain the username as a substring. Do not repeat a character 3 or
            more times.
        :type  user_id: :class:`str` or ``None``
        :param user_id: L2 VPN user ID. Valid user names: 1-63 characters, letters and
            numbers only. No white space or special characters.
        :type  description: :class:`str` or ``None``
        :param description: Description of L2 VPN site.
        """
        self.secure_traffic = secure_traffic
        self.site_id = site_id
        self.name = name
        self.password = password
        self.user_id = user_id
        self.description = description
        VapiStruct.__init__(self)

Nsxsite._set_binding_type(type.StructType(
    'com.vmware.vmc.model.nsxsite', {
        'secureTraffic': type.OptionalType(type.BooleanType()),
        'siteId': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'password': type.OptionalType(type.StringType()),
        'userId': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
    },
    Nsxsite,
    False,
    None))



class ObjectType(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'name': 'name',
                            }

    def __init__(self,
                 name=None,
                ):
        """
        :type  name: :class:`str` or ``None``
        :param name: 
        """
        self.name = name
        VapiStruct.__init__(self)

ObjectType._set_binding_type(type.StructType(
    'com.vmware.vmc.model.object_type', {
        'name': type.OptionalType(type.StringType()),
    },
    ObjectType,
    False,
    None))



class OfferInstancesHolder(VapiStruct):
    """
    Holder for the offer instances.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'on_demand': 'on_demand',
                            'offers': 'offers',
                            }

    def __init__(self,
                 on_demand=None,
                 offers=None,
                ):
        """
        :type  on_demand: :class:`OnDemandOfferInstance`
        :param on_demand: 
        :type  offers: :class:`list` of :class:`TermOfferInstance`
        :param offers: 
        """
        self.on_demand = on_demand
        self.offers = offers
        VapiStruct.__init__(self)

OfferInstancesHolder._set_binding_type(type.StructType(
    'com.vmware.vmc.model.offer_instances_holder', {
        'on_demand': type.ReferenceType(__name__, 'OnDemandOfferInstance'),
        'offers': type.ListType(type.ReferenceType(__name__, 'TermOfferInstance')),
    },
    OfferInstancesHolder,
    False,
    None))



class OnDemandOfferInstance(VapiStruct):
    """
    Holder for the on-demand offer instance.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'product_type': 'product_type',
                            'name': 'name',
                            'currency': 'currency',
                            'region': 'region',
                            'unit_price': 'unit_price',
                            'monthly_cost': 'monthly_cost',
                            'version': 'version',
                            'description': 'description',
                            }

    def __init__(self,
                 product_type=None,
                 name=None,
                 currency=None,
                 region=None,
                 unit_price=None,
                 monthly_cost=None,
                 version=None,
                 description=None,
                ):
        """
        :type  product_type: :class:`str`
        :param product_type: 
        :type  name: :class:`str`
        :param name: 
        :type  currency: :class:`str`
        :param currency: 
        :type  region: :class:`str`
        :param region: 
        :type  unit_price: :class:`str`
        :param unit_price: 
        :type  monthly_cost: :class:`str`
        :param monthly_cost: 
        :type  version: :class:`str`
        :param version: 
        :type  description: :class:`str`
        :param description: 
        """
        self.product_type = product_type
        self.name = name
        self.currency = currency
        self.region = region
        self.unit_price = unit_price
        self.monthly_cost = monthly_cost
        self.version = version
        self.description = description
        VapiStruct.__init__(self)

OnDemandOfferInstance._set_binding_type(type.StructType(
    'com.vmware.vmc.model.on_demand_offer_instance', {
        'product_type': type.StringType(),
        'name': type.StringType(),
        'currency': type.StringType(),
        'region': type.StringType(),
        'unit_price': type.StringType(),
        'monthly_cost': type.StringType(),
        'version': type.StringType(),
        'description': type.StringType(),
    },
    OnDemandOfferInstance,
    False,
    None))



class OrgConfiguration(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "OrgConfiguration"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    PROVIDER_AWS = "AWS"
    """


    """



    _canonical_to_pep_names = {
                            'provider': 'provider',
                            }

    def __init__(self,
                 provider='OrgConfiguration',
                ):
        """
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`OrgConfiguration.PROVIDER_AWS`
            
             Discriminator for provider specific properties
        """
        self.provider = provider
        VapiStruct.__init__(self)

OrgConfiguration._set_binding_type(type.StructType(
    'com.vmware.vmc.model.org_configuration', {
        'provider': type.StringType(),
    },
    OrgConfiguration,
    False,
    None))



class OrgProperties(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'values': 'values',
                            }

    def __init__(self,
                 values=None,
                ):
        """
        :type  values: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param values: A map of string properties to values.
        """
        self.values = values
        VapiStruct.__init__(self)

OrgProperties._set_binding_type(type.StructType(
    'com.vmware.vmc.model.org_properties', {
        'values': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
    },
    OrgProperties,
    False,
    None))



class Organization(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    SLA_CUSTOMER = "CUSTOMER"
    """


    """
    SLA_THIRD_PARTY_PARTNER = "THIRD_PARTY_PARTNER"
    """


    """
    SLA_SECOND_PARTY_PARTNER = "SECOND_PARTY_PARTNER"
    """


    """
    SLA_INTERNAL_CUSTOMER = "INTERNAL_CUSTOMER"
    """


    """
    SLA_VMC_INTERNAL = "VMC_INTERNAL"
    """


    """
    PROJECT_STATE_CREATED = "CREATED"
    """


    """
    PROJECT_STATE_DELETED = "DELETED"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'org_type': 'org_type',
                            'display_name': 'display_name',
                            'name': 'name',
                            'sla': 'sla',
                            'project_state': 'project_state',
                            'properties': 'properties',
                            'cloud_configurations': 'cloud_configurations',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 org_type=None,
                 display_name=None,
                 name=None,
                 sla=None,
                 project_state=None,
                 properties=None,
                 cloud_configurations=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str` or ``None``
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  org_type: :class:`str` or ``None``
        :param org_type: ORG_TYPE to be associated with the org
        :type  display_name: :class:`str` or ``None``
        :param display_name: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  sla: :class:`str` or ``None``
        :param sla: Possible values are: 
            
            * :attr:`Organization.SLA_CUSTOMER`
            * :attr:`Organization.SLA_THIRD_PARTY_PARTNER`
            * :attr:`Organization.SLA_SECOND_PARTY_PARTNER`
            * :attr:`Organization.SLA_INTERNAL_CUSTOMER`
            * :attr:`Organization.SLA_VMC_INTERNAL`
            
             SLA to be associated with the org
        :type  project_state: :class:`str` or ``None``
        :param project_state: Possible values are: 
            
            * :attr:`Organization.PROJECT_STATE_CREATED`
            * :attr:`Organization.PROJECT_STATE_DELETED`
        :type  properties: :class:`OrgProperties` or ``None``
        :param properties: 
        :type  cloud_configurations: (:class:`dict` of :class:`str` and :class:`AwsOrgConfiguration`) or ``None``
        :param cloud_configurations: A Map of provider to OrgConfiguration Model.
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.org_type = org_type
        self.display_name = display_name
        self.name = name
        self.sla = sla
        self.project_state = project_state
        self.properties = properties
        self.cloud_configurations = cloud_configurations
        VapiStruct.__init__(self)

Organization._set_binding_type(type.StructType(
    'com.vmware.vmc.model.organization', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.OptionalType(type.StringType()),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'org_type': type.OptionalType(type.StringType()),
        'display_name': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'sla': type.OptionalType(type.StringType()),
        'project_state': type.OptionalType(type.StringType()),
        'properties': type.OptionalType(type.ReferenceType(__name__, 'OrgProperties')),
        'cloud_configurations': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'AwsOrgConfiguration'))),
    },
    Organization,
    False,
    None))



class PagedEdgeList(VapiStruct):
    """
    NSX Edges listed by pages.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'edgePage': 'edge_page',
                            }

    def __init__(self,
                 edge_page=None,
                ):
        """
        :type  edge_page: :class:`DataPageEdgeSummary` or ``None``
        :param edge_page: Page details with matched records.
        """
        self.edge_page = edge_page
        VapiStruct.__init__(self)

PagedEdgeList._set_binding_type(type.StructType(
    'com.vmware.vmc.model.paged_edge_list', {
        'edgePage': type.OptionalType(type.ReferenceType(__name__, 'DataPageEdgeSummary')),
    },
    PagedEdgeList,
    False,
    None))



class PagingInfo(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'sortOrderAscending': 'sort_order_ascending',
                            'totalCount': 'total_count',
                            'startIndex': 'start_index',
                            'sortBy': 'sort_by',
                            'pageSize': 'page_size',
                            }

    def __init__(self,
                 sort_order_ascending=None,
                 total_count=None,
                 start_index=None,
                 sort_by=None,
                 page_size=None,
                ):
        """
        :type  sort_order_ascending: :class:`bool` or ``None``
        :param sort_order_ascending: 
        :type  total_count: :class:`long` or ``None``
        :param total_count: 
        :type  start_index: :class:`long` or ``None``
        :param start_index: 
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: 
        :type  page_size: :class:`long` or ``None``
        :param page_size: 
        """
        self.sort_order_ascending = sort_order_ascending
        self.total_count = total_count
        self.start_index = start_index
        self.sort_by = sort_by
        self.page_size = page_size
        VapiStruct.__init__(self)

PagingInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.paging_info', {
        'sortOrderAscending': type.OptionalType(type.BooleanType()),
        'totalCount': type.OptionalType(type.IntegerType()),
        'startIndex': type.OptionalType(type.IntegerType()),
        'sortBy': type.OptionalType(type.StringType()),
        'pageSize': type.OptionalType(type.IntegerType()),
    },
    PagingInfo,
    False,
    None))



class PopAmiInfo(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    TYPE_CENTOS = "CENTOS"
    """


    """
    TYPE_POP = "POP"
    """


    """



    _canonical_to_pep_names = {
                            'region': 'region',
                            'id': 'id',
                            'name': 'name',
                            'type': 'type',
                            }

    def __init__(self,
                 region=None,
                 id=None,
                 name=None,
                 type=None,
                ):
        """
        :type  region: :class:`str` or ``None``
        :param region: the region of the esx ami
        :type  id: :class:`str` or ``None``
        :param id: the ami id for the esx
        :type  name: :class:`str` or ``None``
        :param name: the name of the esx ami
        :type  type: :class:`str` or ``None``
        :param type: Possible values are: 
            
            * :attr:`PopAmiInfo.TYPE_CENTOS`
            * :attr:`PopAmiInfo.TYPE_POP`
            
             PoP AMI type. CENTOS: a Centos AMI; POP: a PoP AMI.
        """
        self.region = region
        self.id = id
        self.name = name
        self.type = type
        VapiStruct.__init__(self)

PopAmiInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.pop_ami_info', {
        'region': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'type': type.OptionalType(type.StringType()),
    },
    PopAmiInfo,
    False,
    None))



class PopInfo(VapiStruct):
    """
    Present a SDDC PoP information.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ami_infos': 'ami_infos',
                            'created_at': 'created_at',
                            'id': 'id',
                            'service_infos': 'service_infos',
                            }

    def __init__(self,
                 ami_infos=None,
                 created_at=None,
                 id=None,
                 service_infos=None,
                ):
        """
        :type  ami_infos: :class:`dict` of :class:`str` and :class:`PopAmiInfo`
        :param ami_infos: A map of [region name of PoP / PoP-AMI]:[PopAmiInfo].
        :type  created_at: :class:`datetime.datetime` or ``None``
        :param created_at: The PopInfo (or PoP AMI) created time. Using ISO 8601 date-time
            pattern. format: date-time
        :type  id: :class:`str` or ``None``
        :param id: UUID of the PopInfo format: UUID
        :type  service_infos: (:class:`dict` of :class:`str` and :class:`PopServiceInfo`) or ``None``
        :param service_infos: A map of [service type]:[PopServiceInfo]
        """
        self.ami_infos = ami_infos
        self.created_at = created_at
        self.id = id
        self.service_infos = service_infos
        VapiStruct.__init__(self)

PopInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.pop_info', {
        'ami_infos': type.MapType(type.StringType(), type.ReferenceType(__name__, 'PopAmiInfo')),
        'created_at': type.OptionalType(type.DateTimeType()),
        'id': type.OptionalType(type.StringType()),
        'service_infos': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'PopServiceInfo'))),
    },
    PopInfo,
    False,
    None))



class PopServiceInfo(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    SERVICE_OS = "OS"
    """


    """
    SERVICE_AGENT = "AGENT"
    """


    """
    SERVICE_GLCM = "GLCM"
    """


    """
    SERVICE_S3_ADAPTER = "S3_ADAPTER"
    """


    """
    SERVICE_JRE = "JRE"
    """


    """
    SERVICE_DOCKER = "DOCKER"
    """


    """
    SERVICE_AIDE = "AIDE"
    """


    """
    SERVICE_RTS = "RTS"
    """


    """
    SERVICE_FM_MANAGEMENT = "FM_MANAGEMENT"
    """


    """
    SERVICE_FM_LOG_COLLECTOR = "FM_LOG_COLLECTOR"
    """


    """
    SERVICE_FM_METRICS_COLLECTOR = "FM_METRICS_COLLECTOR"
    """


    """
    SERVICE_BRE = "BRE"
    """


    """
    SERVICE_BRF = "BRF"
    """


    """
    SERVICE_REVERSE_PROXY = "REVERSE_PROXY"
    """


    """
    SERVICE_FORWARD_PROXY = "FORWARD_PROXY"
    """


    """
    SERVICE_DNS = "DNS"
    """


    """
    SERVICE_NTP = "NTP"
    """


    """
    SERVICE_LOGZ_LOG_COLLECTOR = "LOGZ_LOG_COLLECTOR"
    """


    """



    _canonical_to_pep_names = {
                            'cln': 'cln',
                            'version': 'version',
                            'build': 'build',
                            'service': 'service',
                            }

    def __init__(self,
                 cln=None,
                 version=None,
                 build=None,
                 service=None,
                ):
        """
        :type  cln: :class:`str` or ``None``
        :param cln: The service change set number.
        :type  version: :class:`str` or ``None``
        :param version: The service API version.
        :type  build: :class:`str` or ``None``
        :param build: The service build number.
        :type  service: :class:`str`
        :param service: Possible values are: 
            
            * :attr:`PopServiceInfo.SERVICE_OS`
            * :attr:`PopServiceInfo.SERVICE_AGENT`
            * :attr:`PopServiceInfo.SERVICE_GLCM`
            * :attr:`PopServiceInfo.SERVICE_S3_ADAPTER`
            * :attr:`PopServiceInfo.SERVICE_JRE`
            * :attr:`PopServiceInfo.SERVICE_DOCKER`
            * :attr:`PopServiceInfo.SERVICE_AIDE`
            * :attr:`PopServiceInfo.SERVICE_RTS`
            * :attr:`PopServiceInfo.SERVICE_FM_MANAGEMENT`
            * :attr:`PopServiceInfo.SERVICE_FM_LOG_COLLECTOR`
            * :attr:`PopServiceInfo.SERVICE_FM_METRICS_COLLECTOR`
            * :attr:`PopServiceInfo.SERVICE_BRE`
            * :attr:`PopServiceInfo.SERVICE_BRF`
            * :attr:`PopServiceInfo.SERVICE_REVERSE_PROXY`
            * :attr:`PopServiceInfo.SERVICE_FORWARD_PROXY`
            * :attr:`PopServiceInfo.SERVICE_DNS`
            * :attr:`PopServiceInfo.SERVICE_NTP`
            * :attr:`PopServiceInfo.SERVICE_LOGZ_LOG_COLLECTOR`
            
             An enum of PoP related services (including os platform and JRE).
        """
        self.cln = cln
        self.version = version
        self.build = build
        self.service = service
        VapiStruct.__init__(self)

PopServiceInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.pop_service_info', {
        'cln': type.OptionalType(type.StringType()),
        'version': type.OptionalType(type.StringType()),
        'build': type.OptionalType(type.StringType()),
        'service': type.StringType(),
    },
    PopServiceInfo,
    False,
    None))



class Requests(VapiStruct):
    """
    DNS request statistics.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'total': 'total',
                            'queries': 'queries',
                            }

    def __init__(self,
                 total=None,
                 queries=None,
                ):
        """
        :type  total: :class:`long` or ``None``
        :param total: 
        :type  queries: :class:`long` or ``None``
        :param queries: 
        """
        self.total = total
        self.queries = queries
        VapiStruct.__init__(self)

Requests._set_binding_type(type.StructType(
    'com.vmware.vmc.model.requests', {
        'total': type.OptionalType(type.IntegerType()),
        'queries': type.OptionalType(type.IntegerType()),
    },
    Requests,
    False,
    None))



class Result(VapiStruct):
    """
    Job result information for the configuration change carried out on NSX
    Edge.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'value': 'value',
                            'key': 'key',
                            }

    def __init__(self,
                 value=None,
                 key=None,
                ):
        """
        :type  value: :class:`str` or ``None``
        :param value: Job Result value associated with key ID.
        :type  key: :class:`str` or ``None``
        :param key: Job Result key ID.
        """
        self.value = value
        self.key = key
        VapiStruct.__init__(self)

Result._set_binding_type(type.StructType(
    'com.vmware.vmc.model.result', {
        'value': type.OptionalType(type.StringType()),
        'key': type.OptionalType(type.StringType()),
    },
    Result,
    False,
    None))



class ScopeInfo(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'objectTypeName': 'object_type_name',
                            'id': 'id',
                            'name': 'name',
                            }

    def __init__(self,
                 object_type_name=None,
                 id=None,
                 name=None,
                ):
        """
        :type  object_type_name: :class:`str` or ``None``
        :param object_type_name: 
        :type  id: :class:`str` or ``None``
        :param id: 
        :type  name: :class:`str` or ``None``
        :param name: 
        """
        self.object_type_name = object_type_name
        self.id = id
        self.name = name
        VapiStruct.__init__(self)

ScopeInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.scope_info', {
        'objectTypeName': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
    },
    ScopeInfo,
    False,
    None))



class Sddc(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    SDDC_STATE_DEPLOYING = "DEPLOYING"
    """


    """
    SDDC_STATE_READY = "READY"
    """


    """
    SDDC_STATE_DELETING = "DELETING"
    """


    """
    SDDC_STATE_DELETION_FAILED = "DELETION_FAILED"
    """


    """
    SDDC_STATE_DELETED = "DELETED"
    """


    """
    SDDC_STATE_FAILED = "FAILED"
    """


    """
    PROVIDER_AWS = "AWS"
    """


    """
    ACCOUNT_LINK_STATE_DELAYED = "DELAYED"
    """


    """
    ACCOUNT_LINK_STATE_LINKED = "LINKED"
    """


    """
    ACCOUNT_LINK_STATE_UNLINKED = "UNLINKED"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'name': 'name',
                            'sddc_state': 'sddc_state',
                            'expiration_date': 'expiration_date',
                            'org_id': 'org_id',
                            'sddc_type': 'sddc_type',
                            'provider': 'provider',
                            'account_link_state': 'account_link_state',
                            'resource_config': 'resource_config',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 name=None,
                 sddc_state=None,
                 expiration_date=None,
                 org_id=None,
                 sddc_type=None,
                 provider=None,
                 account_link_state=None,
                 resource_config=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str` or ``None``
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  name: :class:`str` or ``None``
        :param name: name for SDDC
        :type  sddc_state: :class:`str` or ``None``
        :param sddc_state: Possible values are: 
            
            * :attr:`Sddc.SDDC_STATE_DEPLOYING`
            * :attr:`Sddc.SDDC_STATE_READY`
            * :attr:`Sddc.SDDC_STATE_DELETING`
            * :attr:`Sddc.SDDC_STATE_DELETION_FAILED`
            * :attr:`Sddc.SDDC_STATE_DELETED`
            * :attr:`Sddc.SDDC_STATE_FAILED`
        :type  expiration_date: :class:`datetime.datetime` or ``None``
        :param expiration_date: Expiration date of a sddc in UTC (will be set if its applicable)
            format: date-time
        :type  org_id: :class:`str` or ``None``
        :param org_id: 
        :type  sddc_type: :class:`str` or ``None``
        :param sddc_type: Type of the sddc
        :type  provider: :class:`str` or ``None``
        :param provider: Possible values are: 
            
            * :attr:`Sddc.PROVIDER_AWS`
        :type  account_link_state: :class:`str` or ``None``
        :param account_link_state: Possible values are: 
            
            * :attr:`Sddc.ACCOUNT_LINK_STATE_DELAYED`
            * :attr:`Sddc.ACCOUNT_LINK_STATE_LINKED`
            * :attr:`Sddc.ACCOUNT_LINK_STATE_UNLINKED`
            
             Account linking state of the sddc
        :type  resource_config: :class:`AwsSddcResourceConfig` or ``None``
        :param resource_config: 
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.name = name
        self.sddc_state = sddc_state
        self.expiration_date = expiration_date
        self.org_id = org_id
        self.sddc_type = sddc_type
        self.provider = provider
        self.account_link_state = account_link_state
        self.resource_config = resource_config
        VapiStruct.__init__(self)

Sddc._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.OptionalType(type.StringType()),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'name': type.OptionalType(type.StringType()),
        'sddc_state': type.OptionalType(type.StringType()),
        'expiration_date': type.OptionalType(type.DateTimeType()),
        'org_id': type.OptionalType(type.StringType()),
        'sddc_type': type.OptionalType(type.StringType()),
        'provider': type.OptionalType(type.StringType()),
        'account_link_state': type.OptionalType(type.StringType()),
        'resource_config': type.OptionalType(type.ReferenceType(__name__, 'AwsSddcResourceConfig')),
    },
    Sddc,
    False,
    None))



class SddcAllocatePublicIpSpec(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'count': 'count',
                            'private_ips': 'private_ips',
                            'names': 'names',
                            }

    def __init__(self,
                 count=None,
                 private_ips=None,
                 names=None,
                ):
        """
        :type  count: :class:`long`
        :param count: 
        :type  private_ips: :class:`list` of :class:`str` or ``None``
        :param private_ips: List of workload VM private IPs to be assigned the public IP just
            allocated.
        :type  names: :class:`list` of :class:`str` or ``None``
        :param names: List of names for the workload VM public IP assignment.
        """
        self.count = count
        self.private_ips = private_ips
        self.names = names
        VapiStruct.__init__(self)

SddcAllocatePublicIpSpec._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_allocate_public_ip_spec', {
        'count': type.IntegerType(),
        'private_ips': type.OptionalType(type.ListType(type.StringType())),
        'names': type.OptionalType(type.ListType(type.StringType())),
    },
    SddcAllocatePublicIpSpec,
    False,
    None))



class SddcConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "SddcConfig"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    PROVIDER_AWS = "AWS"
    """


    """
    DEPLOYMENT_TYPE_SINGLEAZ = "SingleAZ"
    """


    """
    DEPLOYMENT_TYPE_MULTIAZ = "MultiAZ"
    """


    """



    _canonical_to_pep_names = {
                            'name': 'name',
                            'account_link_sddc_config': 'account_link_sddc_config',
                            'vpc_cidr': 'vpc_cidr',
                            'num_hosts': 'num_hosts',
                            'sddc_type': 'sddc_type',
                            'vxlan_subnet': 'vxlan_subnet',
                            'account_link_config': 'account_link_config',
                            'provider': 'provider',
                            'sso_domain': 'sso_domain',
                            'sddc_template_id': 'sddc_template_id',
                            'deployment_type': 'deployment_type',
                            }

    def __init__(self,
                 name=None,
                 account_link_sddc_config=None,
                 vpc_cidr=None,
                 num_hosts=None,
                 sddc_type=None,
                 vxlan_subnet=None,
                 account_link_config=None,
                 provider='SddcConfig',
                 sso_domain=None,
                 sddc_template_id=None,
                 deployment_type=None,
                ):
        """
        :type  name: :class:`str`
        :param name: 
        :type  account_link_sddc_config: :class:`list` of :class:`AccountLinkSddcConfig` or ``None``
        :param account_link_sddc_config: A list of the SDDC linking configurations to use.
        :type  vpc_cidr: :class:`str` or ``None``
        :param vpc_cidr: AWS VPC IP range. Only prefix of 16 or 20 is currently supported.
        :type  num_hosts: :class:`long`
        :param num_hosts: 
        :type  sddc_type: :class:`str` or ``None``
        :param sddc_type: Denotes the sddc type , if the value is null or empty, the type is
            considered as default.
        :type  vxlan_subnet: :class:`str` or ``None``
        :param vxlan_subnet: VXLAN IP subnet
        :type  account_link_config: :class:`AccountLinkConfig` or ``None``
        :param account_link_config: The account linking configuration, we will keep this one and remove
            accountLinkSddcConfig finally.
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`SddcConfig.PROVIDER_AWS`
            
            Determines what additional properties are available based on cloud
            provider.
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: The SSO domain name to use for vSphere users. If not specified,
            vmc.local will be used.
        :type  sddc_template_id: :class:`str` or ``None``
        :param sddc_template_id: If provided, configuration from the template will applied to the
            provisioned SDDC. format: UUID
        :type  deployment_type: :class:`str` or ``None``
        :param deployment_type: Possible values are: 
            
            * :attr:`SddcConfig.DEPLOYMENT_TYPE_SINGLEAZ`
            * :attr:`SddcConfig.DEPLOYMENT_TYPE_MULTIAZ`
            
            Denotes if request is for a SingleAZ or a MultiAZ SDDC. Default is
            SingleAZ.
        """
        self.name = name
        self.account_link_sddc_config = account_link_sddc_config
        self.vpc_cidr = vpc_cidr
        self.num_hosts = num_hosts
        self.sddc_type = sddc_type
        self.vxlan_subnet = vxlan_subnet
        self.account_link_config = account_link_config
        self.provider = provider
        self.sso_domain = sso_domain
        self.sddc_template_id = sddc_template_id
        self.deployment_type = deployment_type
        VapiStruct.__init__(self)

SddcConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_config', {
        'name': type.StringType(),
        'account_link_sddc_config': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AccountLinkSddcConfig'))),
        'vpc_cidr': type.OptionalType(type.StringType()),
        'num_hosts': type.IntegerType(),
        'sddc_type': type.OptionalType(type.StringType()),
        'vxlan_subnet': type.OptionalType(type.StringType()),
        'account_link_config': type.OptionalType(type.ReferenceType(__name__, 'AccountLinkConfig')),
        'provider': type.StringType(),
        'sso_domain': type.OptionalType(type.StringType()),
        'sddc_template_id': type.OptionalType(type.StringType()),
        'deployment_type': type.OptionalType(type.StringType()),
    },
    SddcConfig,
    False,
    None))



class SddcLinkConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'customer_subnet_ids': 'customer_subnet_ids',
                            'connected_account_id': 'connected_account_id',
                            }

    def __init__(self,
                 customer_subnet_ids=None,
                 connected_account_id=None,
                ):
        """
        :type  customer_subnet_ids: :class:`list` of :class:`str` or ``None``
        :param customer_subnet_ids: 
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: Determines which connected customer account to link to
        """
        self.customer_subnet_ids = customer_subnet_ids
        self.connected_account_id = connected_account_id
        VapiStruct.__init__(self)

SddcLinkConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_link_config', {
        'customer_subnet_ids': type.OptionalType(type.ListType(type.StringType())),
        'connected_account_id': type.OptionalType(type.StringType()),
    },
    SddcLinkConfig,
    False,
    None))



class SddcManifest(VapiStruct):
    """
    Describes software components of the installed SDDC

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vmc_version': 'vmc_version',
                            'glcm_bundle': 'glcm_bundle',
                            'pop_info': 'pop_info',
                            'vmc_internal_version': 'vmc_internal_version',
                            'esx_ami': 'esx_ami',
                            'esx_nsxt_ami': 'esx_nsxt_ami',
                            'metadata': 'metadata',
                            }

    def __init__(self,
                 vmc_version=None,
                 glcm_bundle=None,
                 pop_info=None,
                 vmc_internal_version=None,
                 esx_ami=None,
                 esx_nsxt_ami=None,
                 metadata=None,
                ):
        """
        :type  vmc_version: :class:`str` or ``None``
        :param vmc_version: the vmcVersion of the sddc for display
        :type  glcm_bundle: :class:`GlcmBundle` or ``None``
        :param glcm_bundle: 
        :type  pop_info: :class:`PopInfo` or ``None``
        :param pop_info: 
        :type  vmc_internal_version: :class:`str` or ``None``
        :param vmc_internal_version: the vmcInternalVersion of the sddc for internal use
        :type  esx_ami: :class:`AmiInfo` or ``None``
        :param esx_ami: 
        :type  esx_nsxt_ami: :class:`AmiInfo` or ``None``
        :param esx_nsxt_ami: 
        :type  metadata: :class:`Metadata` or ``None``
        :param metadata: 
        """
        self.vmc_version = vmc_version
        self.glcm_bundle = glcm_bundle
        self.pop_info = pop_info
        self.vmc_internal_version = vmc_internal_version
        self.esx_ami = esx_ami
        self.esx_nsxt_ami = esx_nsxt_ami
        self.metadata = metadata
        VapiStruct.__init__(self)

SddcManifest._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_manifest', {
        'vmc_version': type.OptionalType(type.StringType()),
        'glcm_bundle': type.OptionalType(type.ReferenceType(__name__, 'GlcmBundle')),
        'pop_info': type.OptionalType(type.ReferenceType(__name__, 'PopInfo')),
        'vmc_internal_version': type.OptionalType(type.StringType()),
        'esx_ami': type.OptionalType(type.ReferenceType(__name__, 'AmiInfo')),
        'esx_nsxt_ami': type.OptionalType(type.ReferenceType(__name__, 'AmiInfo')),
        'metadata': type.OptionalType(type.ReferenceType(__name__, 'Metadata')),
    },
    SddcManifest,
    False,
    None))



class SddcNetwork(VapiStruct):
    """
    Logical network.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'subnets': 'subnets',
                            'cgwName': 'cgw_name',
                            'name': 'name',
                            'l2Extension': 'l2_extension',
                            'cgwId': 'cgw_id',
                            'dhcpConfigs': 'dhcp_configs',
                            'id': 'id',
                            }

    def __init__(self,
                 subnets=None,
                 cgw_name=None,
                 name=None,
                 l2_extension=None,
                 cgw_id=None,
                 dhcp_configs=None,
                 id=None,
                ):
        """
        :type  subnets: :class:`SddcNetworkAddressGroups` or ``None``
        :param subnets: Network address groups for routed logical networks.
        :type  cgw_name: :class:`str` or ``None``
        :param cgw_name: Name of the compute gateway to which the logical network is
            attached.
        :type  name: :class:`str`
        :param name: Name of logical network. Length needs to be between 1-35
            characters.
        :type  l2_extension: :class:`L2Extension` or ``None``
        :param l2_extension: Layer 2 extension for extended logical networks.
        :type  cgw_id: :class:`str`
        :param cgw_id: ID of the compute gateway edge to which the logical network is
            attached.
        :type  dhcp_configs: :class:`SddcNetworkDhcpConfig` or ``None``
        :param dhcp_configs: DHCP configuration for routed logical networks.
        :type  id: :class:`str` or ``None``
        :param id: ID of logical network.
        """
        self.subnets = subnets
        self.cgw_name = cgw_name
        self.name = name
        self.l2_extension = l2_extension
        self.cgw_id = cgw_id
        self.dhcp_configs = dhcp_configs
        self.id = id
        VapiStruct.__init__(self)

SddcNetwork._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_network', {
        'subnets': type.OptionalType(type.ReferenceType(__name__, 'SddcNetworkAddressGroups')),
        'cgwName': type.OptionalType(type.StringType()),
        'name': type.StringType(),
        'l2Extension': type.OptionalType(type.ReferenceType(__name__, 'L2Extension')),
        'cgwId': type.StringType(),
        'dhcpConfigs': type.OptionalType(type.ReferenceType(__name__, 'SddcNetworkDhcpConfig')),
        'id': type.OptionalType(type.StringType()),
    },
    SddcNetwork,
    False,
    None))



class SddcNetworkAddressGroup(VapiStruct):
    """
    Logical Network address group.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'prefixLength': 'prefix_length',
                            'primaryAddress': 'primary_address',
                            }

    def __init__(self,
                 prefix_length=None,
                 primary_address=None,
                ):
        """
        :type  prefix_length: :class:`str` or ``None``
        :param prefix_length: Prefix length of logical network.
        :type  primary_address: :class:`str` or ``None``
        :param primary_address: Primary address for logical network.
        """
        self.prefix_length = prefix_length
        self.primary_address = primary_address
        VapiStruct.__init__(self)

SddcNetworkAddressGroup._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_network_address_group', {
        'prefixLength': type.OptionalType(type.StringType()),
        'primaryAddress': type.OptionalType(type.StringType()),
    },
    SddcNetworkAddressGroup,
    False,
    None))



class SddcNetworkAddressGroups(VapiStruct):
    """
    Logical network address groups.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'addressGroups': 'address_groups',
                            }

    def __init__(self,
                 address_groups=None,
                ):
        """
        :type  address_groups: :class:`list` of :class:`SddcNetworkAddressGroup` or ``None``
        :param address_groups: List of logical network address groups.
        """
        self.address_groups = address_groups
        VapiStruct.__init__(self)

SddcNetworkAddressGroups._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_network_address_groups', {
        'addressGroups': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcNetworkAddressGroup'))),
    },
    SddcNetworkAddressGroups,
    False,
    None))



class SddcNetworkDhcpConfig(VapiStruct):
    """
    DHCP configuration for the logical network.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ipPools': 'ip_pools',
                            }

    def __init__(self,
                 ip_pools=None,
                ):
        """
        :type  ip_pools: :class:`list` of :class:`SddcNetworkDhcpIpPool` or ``None``
        :param ip_pools: List of IP pools in DHCP configuration.
        """
        self.ip_pools = ip_pools
        VapiStruct.__init__(self)

SddcNetworkDhcpConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_network_dhcp_config', {
        'ipPools': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcNetworkDhcpIpPool'))),
    },
    SddcNetworkDhcpConfig,
    False,
    None))



class SddcNetworkDhcpIpPool(VapiStruct):
    """
    DHCP IP pool for logical network.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ipRange': 'ip_range',
                            'domainName': 'domain_name',
                            }

    def __init__(self,
                 ip_range=None,
                 domain_name=None,
                ):
        """
        :type  ip_range: :class:`str` or ``None``
        :param ip_range: IP range for DHCP IP pool.
        :type  domain_name: :class:`str` or ``None``
        :param domain_name: DNS domain name.
        """
        self.ip_range = ip_range
        self.domain_name = domain_name
        VapiStruct.__init__(self)

SddcNetworkDhcpIpPool._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_network_dhcp_ip_pool', {
        'ipRange': type.OptionalType(type.StringType()),
        'domainName': type.OptionalType(type.StringType()),
    },
    SddcNetworkDhcpIpPool,
    False,
    None))



class SddcPublicIp(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'public_ip': 'public_ip',
                            'name': 'name',
                            'allocation_id': 'allocation_id',
                            'dnat_rule_id': 'dnat_rule_id',
                            'associated_private_ip': 'associated_private_ip',
                            'snat_rule_id': 'snat_rule_id',
                            }

    def __init__(self,
                 public_ip=None,
                 name=None,
                 allocation_id=None,
                 dnat_rule_id=None,
                 associated_private_ip=None,
                 snat_rule_id=None,
                ):
        """
        :type  public_ip: :class:`str`
        :param public_ip: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  allocation_id: :class:`str` or ``None``
        :param allocation_id: 
        :type  dnat_rule_id: :class:`str` or ``None``
        :param dnat_rule_id: 
        :type  associated_private_ip: :class:`str` or ``None``
        :param associated_private_ip: 
        :type  snat_rule_id: :class:`str` or ``None``
        :param snat_rule_id: 
        """
        self.public_ip = public_ip
        self.name = name
        self.allocation_id = allocation_id
        self.dnat_rule_id = dnat_rule_id
        self.associated_private_ip = associated_private_ip
        self.snat_rule_id = snat_rule_id
        VapiStruct.__init__(self)

SddcPublicIp._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_public_ip', {
        'public_ip': type.StringType(),
        'name': type.OptionalType(type.StringType()),
        'allocation_id': type.OptionalType(type.StringType()),
        'dnat_rule_id': type.OptionalType(type.StringType()),
        'associated_private_ip': type.OptionalType(type.StringType()),
        'snat_rule_id': type.OptionalType(type.StringType()),
    },
    SddcPublicIp,
    False,
    None))



class SddcResourceConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "SddcResourceConfig"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    PROVIDER_AWS = "AWS"
    """


    """
    DEPLOYMENT_TYPE_SINGLEAZ = "SingleAZ"
    """


    """
    DEPLOYMENT_TYPE_MULTIAZ = "MultiAZ"
    """


    """



    _canonical_to_pep_names = {
                            'nsxt': 'nsxt',
                            'mgw_id': 'mgw_id',
                            'nsx_mgr_url': 'nsx_mgr_url',
                            'psc_management_ip': 'psc_management_ip',
                            'psc_url': 'psc_url',
                            'cgws': 'cgws',
                            'availability_zones': 'availability_zones',
                            'management_ds': 'management_ds',
                            'custom_properties': 'custom_properties',
                            'cloud_password': 'cloud_password',
                            'provider': 'provider',
                            'clusters': 'clusters',
                            'vc_management_ip': 'vc_management_ip',
                            'sddc_networks': 'sddc_networks',
                            'cloud_username': 'cloud_username',
                            'esx_hosts': 'esx_hosts',
                            'nsx_mgr_management_ip': 'nsx_mgr_management_ip',
                            'vc_instance_id': 'vc_instance_id',
                            'esx_cluster_id': 'esx_cluster_id',
                            'vc_public_ip': 'vc_public_ip',
                            'vc_url': 'vc_url',
                            'sddc_manifest': 'sddc_manifest',
                            'vxlan_subnet': 'vxlan_subnet',
                            'cloud_user_group': 'cloud_user_group',
                            'management_rp': 'management_rp',
                            'witness_availability_zone': 'witness_availability_zone',
                            'sso_domain': 'sso_domain',
                            'deployment_type': 'deployment_type',
                            'dns_with_management_vm_private_ip': 'dns_with_management_vm_private_ip',
                            }

    def __init__(self,
                 nsxt=None,
                 mgw_id=None,
                 nsx_mgr_url=None,
                 psc_management_ip=None,
                 psc_url=None,
                 cgws=None,
                 availability_zones=None,
                 management_ds=None,
                 custom_properties=None,
                 cloud_password=None,
                 provider='SddcResourceConfig',
                 clusters=None,
                 vc_management_ip=None,
                 sddc_networks=None,
                 cloud_username=None,
                 esx_hosts=None,
                 nsx_mgr_management_ip=None,
                 vc_instance_id=None,
                 esx_cluster_id=None,
                 vc_public_ip=None,
                 vc_url=None,
                 sddc_manifest=None,
                 vxlan_subnet=None,
                 cloud_user_group=None,
                 management_rp=None,
                 witness_availability_zone=None,
                 sso_domain=None,
                 deployment_type=None,
                 dns_with_management_vm_private_ip=None,
                ):
        """
        :type  nsxt: :class:`bool` or ``None``
        :param nsxt: if true, NSX-T UI is enabled.
        :type  mgw_id: :class:`str` or ``None``
        :param mgw_id: Management Gateway Id
        :type  nsx_mgr_url: :class:`str` or ``None``
        :param nsx_mgr_url: URL of the NSX Manager
        :type  psc_management_ip: :class:`str` or ``None``
        :param psc_management_ip: PSC internal management IP
        :type  psc_url: :class:`str` or ``None``
        :param psc_url: URL of the PSC server
        :type  cgws: :class:`list` of :class:`str` or ``None``
        :param cgws: 
        :type  availability_zones: :class:`list` of :class:`str` or ``None``
        :param availability_zones: Availability zones over which esx hosts are provisioned. MultiAZ
            SDDCs will have hosts provisioned over two availability zones while
            SingleAZ SDDCs will provision over one.
        :type  management_ds: :class:`str` or ``None``
        :param management_ds: The ManagedObjectReference of the management Datastore
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  cloud_password: :class:`str` or ``None``
        :param cloud_password: Password for vCenter SDDC administrator
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`SddcResourceConfig.PROVIDER_AWS`
            
             Discriminator for additional properties
        :type  clusters: :class:`list` of :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param clusters: List of clusters in the SDDC.
            When clients pass a value of this class as a parameter, the
            attribute must contain all the attributes defined in
            :class:`Cluster`. When methods return a value of this class as a
            return value, the attribute will contain all the attributes defined
            in :class:`Cluster`.
        :type  vc_management_ip: :class:`str` or ``None``
        :param vc_management_ip: vCenter internal management IP
        :type  sddc_networks: :class:`list` of :class:`str` or ``None``
        :param sddc_networks: 
        :type  cloud_username: :class:`str` or ``None``
        :param cloud_username: Username for vCenter SDDC administrator
        :type  esx_hosts: :class:`list` of :class:`AwsEsxHost` or ``None``
        :param esx_hosts: 
        :type  nsx_mgr_management_ip: :class:`str` or ``None``
        :param nsx_mgr_management_ip: NSX Manager internal management IP
        :type  vc_instance_id: :class:`str` or ``None``
        :param vc_instance_id: unique id of the vCenter server
        :type  esx_cluster_id: :class:`str` or ``None``
        :param esx_cluster_id: Cluster Id to add ESX workflow
        :type  vc_public_ip: :class:`str` or ``None``
        :param vc_public_ip: vCenter public IP
        :type  vc_url: :class:`str` or ``None``
        :param vc_url: URL of the vCenter server
        :type  sddc_manifest: :class:`SddcManifest` or ``None``
        :param sddc_manifest: 
        :type  vxlan_subnet: :class:`str` or ``None``
        :param vxlan_subnet: VXLAN IP subnet
        :type  cloud_user_group: :class:`str` or ``None``
        :param cloud_user_group: Group name for vCenter SDDC administrator
        :type  management_rp: :class:`str` or ``None``
        :param management_rp: 
        :type  witness_availability_zone: :class:`str` or ``None``
        :param witness_availability_zone: Availability zone where the witness node is provisioned for a
            MultiAZ SDDC. This is null for a SingleAZ SDDC.
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: The SSO domain name to use for vSphere users
        :type  deployment_type: :class:`str` or ``None``
        :param deployment_type: Possible values are: 
            
            * :attr:`SddcResourceConfig.DEPLOYMENT_TYPE_SINGLEAZ`
            * :attr:`SddcResourceConfig.DEPLOYMENT_TYPE_MULTIAZ`
            
             Denotes if this is a SingleAZ SDDC or a MultiAZ SDDC.
        :type  dns_with_management_vm_private_ip: :class:`bool` or ``None``
        :param dns_with_management_vm_private_ip: if true, use the private IP addresses to register DNS records for
            the management VMs
        """
        self.nsxt = nsxt
        self.mgw_id = mgw_id
        self.nsx_mgr_url = nsx_mgr_url
        self.psc_management_ip = psc_management_ip
        self.psc_url = psc_url
        self.cgws = cgws
        self.availability_zones = availability_zones
        self.management_ds = management_ds
        self.custom_properties = custom_properties
        self.cloud_password = cloud_password
        self.provider = provider
        self.clusters = clusters
        self.vc_management_ip = vc_management_ip
        self.sddc_networks = sddc_networks
        self.cloud_username = cloud_username
        self.esx_hosts = esx_hosts
        self.nsx_mgr_management_ip = nsx_mgr_management_ip
        self.vc_instance_id = vc_instance_id
        self.esx_cluster_id = esx_cluster_id
        self.vc_public_ip = vc_public_ip
        self.vc_url = vc_url
        self.sddc_manifest = sddc_manifest
        self.vxlan_subnet = vxlan_subnet
        self.cloud_user_group = cloud_user_group
        self.management_rp = management_rp
        self.witness_availability_zone = witness_availability_zone
        self.sso_domain = sso_domain
        self.deployment_type = deployment_type
        self.dns_with_management_vm_private_ip = dns_with_management_vm_private_ip
        VapiStruct.__init__(self)

SddcResourceConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_resource_config', {
        'nsxt': type.OptionalType(type.BooleanType()),
        'mgw_id': type.OptionalType(type.StringType()),
        'nsx_mgr_url': type.OptionalType(type.StringType()),
        'psc_management_ip': type.OptionalType(type.StringType()),
        'psc_url': type.OptionalType(type.StringType()),
        'cgws': type.OptionalType(type.ListType(type.StringType())),
        'availability_zones': type.OptionalType(type.ListType(type.StringType())),
        'management_ds': type.OptionalType(type.StringType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'cloud_password': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'clusters': type.OptionalType(type.ListType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType(__name__, 'Cluster')]))),
        'vc_management_ip': type.OptionalType(type.StringType()),
        'sddc_networks': type.OptionalType(type.ListType(type.StringType())),
        'cloud_username': type.OptionalType(type.StringType()),
        'esx_hosts': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AwsEsxHost'))),
        'nsx_mgr_management_ip': type.OptionalType(type.StringType()),
        'vc_instance_id': type.OptionalType(type.StringType()),
        'esx_cluster_id': type.OptionalType(type.StringType()),
        'vc_public_ip': type.OptionalType(type.StringType()),
        'vc_url': type.OptionalType(type.StringType()),
        'sddc_manifest': type.OptionalType(type.ReferenceType(__name__, 'SddcManifest')),
        'vxlan_subnet': type.OptionalType(type.StringType()),
        'cloud_user_group': type.OptionalType(type.StringType()),
        'management_rp': type.OptionalType(type.StringType()),
        'witness_availability_zone': type.OptionalType(type.StringType()),
        'sso_domain': type.OptionalType(type.StringType()),
        'deployment_type': type.OptionalType(type.StringType()),
        'dns_with_management_vm_private_ip': type.OptionalType(type.BooleanType()),
    },
    SddcResourceConfig,
    False,
    None))



class SddcTemplate(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATE_AVAILABLE = "AVAILABLE"
    """


    """
    STATE_INUSE = "INUSE"
    """


    """
    STATE_APPLIED = "APPLIED"
    """


    """
    STATE_DELETING = "DELETING"
    """


    """
    STATE_DELETED = "DELETED"
    """


    """
    STATE_FAILED = "FAILED"
    """


    """
    PROVIDER_AWS = "AWS"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'name': 'name',
                            'tenant_id': 'tenant_id',
                            'source_sddc_id': 'source_sddc_id',
                            'state': 'state',
                            'num_hosts': 'num_hosts',
                            'public_ips': 'public_ips',
                            'vpc_cidr': 'vpc_cidr',
                            'provider': 'provider',
                            'vc_public_ip': 'vc_public_ip',
                            'sso_domain': 'sso_domain',
                            'networking_template': 'networking_template',
                            'region': 'region',
                            'vc_url': 'vc_url',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 name=None,
                 tenant_id=None,
                 source_sddc_id=None,
                 state=None,
                 num_hosts=None,
                 public_ips=None,
                 vpc_cidr=None,
                 provider=None,
                 vc_public_ip=None,
                 sso_domain=None,
                 networking_template=None,
                 region=None,
                 vc_url=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str` or ``None``
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  name: :class:`str` or ``None``
        :param name: name for SDDC configuration template
        :type  tenant_id: :class:`str` or ``None``
        :param tenant_id: 
        :type  source_sddc_id: :class:`str` or ``None``
        :param source_sddc_id: 
        :type  state: :class:`str` or ``None``
        :param state: Possible values are: 
            
            * :attr:`SddcTemplate.STATE_AVAILABLE`
            * :attr:`SddcTemplate.STATE_INUSE`
            * :attr:`SddcTemplate.STATE_APPLIED`
            * :attr:`SddcTemplate.STATE_DELETING`
            * :attr:`SddcTemplate.STATE_DELETED`
            * :attr:`SddcTemplate.STATE_FAILED`
        :type  num_hosts: :class:`long` or ``None``
        :param num_hosts: 
        :type  public_ips: :class:`list` of :class:`SddcPublicIp` or ``None``
        :param public_ips: 
        :type  vpc_cidr: :class:`str` or ``None``
        :param vpc_cidr: 
        :type  provider: :class:`str` or ``None``
        :param provider: Possible values are: 
            
            * :attr:`SddcTemplate.PROVIDER_AWS`
        :type  vc_public_ip: :class:`SddcPublicIp` or ``None``
        :param vc_public_ip: 
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: 
        :type  networking_template: :class:`NetworkingTemplate` or ``None``
        :param networking_template: 
        :type  region: :class:`str` or ``None``
        :param region: 
        :type  vc_url: :class:`str` or ``None``
        :param vc_url: 
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.name = name
        self.tenant_id = tenant_id
        self.source_sddc_id = source_sddc_id
        self.state = state
        self.num_hosts = num_hosts
        self.public_ips = public_ips
        self.vpc_cidr = vpc_cidr
        self.provider = provider
        self.vc_public_ip = vc_public_ip
        self.sso_domain = sso_domain
        self.networking_template = networking_template
        self.region = region
        self.vc_url = vc_url
        VapiStruct.__init__(self)

SddcTemplate._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_template', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.OptionalType(type.StringType()),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'name': type.OptionalType(type.StringType()),
        'tenant_id': type.OptionalType(type.StringType()),
        'source_sddc_id': type.OptionalType(type.StringType()),
        'state': type.OptionalType(type.StringType()),
        'num_hosts': type.OptionalType(type.IntegerType()),
        'public_ips': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcPublicIp'))),
        'vpc_cidr': type.OptionalType(type.StringType()),
        'provider': type.OptionalType(type.StringType()),
        'vc_public_ip': type.OptionalType(type.ReferenceType(__name__, 'SddcPublicIp')),
        'sso_domain': type.OptionalType(type.StringType()),
        'networking_template': type.OptionalType(type.ReferenceType(__name__, 'NetworkingTemplate')),
        'region': type.OptionalType(type.StringType()),
        'vc_url': type.OptionalType(type.StringType()),
    },
    SddcTemplate,
    False,
    None))



class SecondaryAddresses(VapiStruct):
    """
    Secondary IP addresses of the NSX Edge vnic address group. These are used
    for NAT, LB, VPN etc. Optional.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'type': 'type',
                            'ipAddress': 'ip_address',
                            }

    def __init__(self,
                 type=None,
                 ip_address=None,
                ):
        """
        :type  type: :class:`str` or ``None``
        :param type: 
        :type  ip_address: :class:`list` of :class:`str` or ``None``
        :param ip_address: List of IP addresses.
        """
        self.type = type
        self.ip_address = ip_address
        VapiStruct.__init__(self)

SecondaryAddresses._set_binding_type(type.StructType(
    'com.vmware.vmc.model.secondary_addresses', {
        'type': type.OptionalType(type.StringType()),
        'ipAddress': type.OptionalType(type.ListType(type.StringType())),
    },
    SecondaryAddresses,
    False,
    None))



class ServiceError(VapiStruct):
    """
    Detailed service errors associated with a task.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'original_service': 'original_service',
                            'params': 'params',
                            'default_message': 'default_message',
                            'original_service_error_code': 'original_service_error_code',
                            'error_code': 'error_code',
                            'localized_message': 'localized_message',
                            }

    def __init__(self,
                 original_service=None,
                 params=None,
                 default_message=None,
                 original_service_error_code=None,
                 error_code=None,
                 localized_message=None,
                ):
        """
        :type  original_service: :class:`str`
        :param original_service: The original service name of the error.
        :type  params: :class:`list` of :class:`str` or ``None``
        :param params: The parameters of the service error.
        :type  default_message: :class:`str` or ``None``
        :param default_message: Error message in English.
        :type  original_service_error_code: :class:`str`
        :param original_service_error_code: The original error code of the service.
        :type  error_code: :class:`str`
        :param error_code: Localizable error code.
        :type  localized_message: :class:`str` or ``None``
        :param localized_message: The localized message.
        """
        self.original_service = original_service
        self.params = params
        self.default_message = default_message
        self.original_service_error_code = original_service_error_code
        self.error_code = error_code
        self.localized_message = localized_message
        VapiStruct.__init__(self)

ServiceError._set_binding_type(type.StructType(
    'com.vmware.vmc.model.service_error', {
        'original_service': type.StringType(),
        'params': type.OptionalType(type.ListType(type.StringType())),
        'default_message': type.OptionalType(type.StringType()),
        'original_service_error_code': type.StringType(),
        'error_code': type.StringType(),
        'localized_message': type.OptionalType(type.StringType()),
    },
    ServiceError,
    False,
    None))



class Site(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    TUNNEL_STATUS_CONNECTED = "CONNECTED"
    """


    """
    TUNNEL_STATUS_DISCONNECTED = "DISCONNECTED"
    """


    """
    TUNNEL_STATUS_UNKNOWN = "UNKNOWN"
    """


    """



    _canonical_to_pep_names = {
                            'password': 'password',
                            'user_id': 'user_id',
                            'name': 'name',
                            'rx_bytes_on_local_subnet': 'rx_bytes_on_local_subnet',
                            'secure_traffic': 'secure_traffic',
                            'established_date': 'established_date',
                            'failure_message': 'failure_message',
                            'dropped_tx_packets': 'dropped_tx_packets',
                            'dropped_rx_packets': 'dropped_rx_packets',
                            'tunnel_status': 'tunnel_status',
                            'tx_bytes_from_local_subnet': 'tx_bytes_from_local_subnet',
                            }

    def __init__(self,
                 password=None,
                 user_id=None,
                 name=None,
                 rx_bytes_on_local_subnet=None,
                 secure_traffic=None,
                 established_date=None,
                 failure_message=None,
                 dropped_tx_packets=None,
                 dropped_rx_packets=None,
                 tunnel_status=None,
                 tx_bytes_from_local_subnet=None,
                ):
        """
        :type  password: :class:`str` or ``None``
        :param password: Site password.
        :type  user_id: :class:`str` or ``None``
        :param user_id: Site user id.
        :type  name: :class:`str` or ``None``
        :param name: Unique name for the site getting configured.
        :type  rx_bytes_on_local_subnet: :class:`long` or ``None``
        :param rx_bytes_on_local_subnet: Bytes received on local network. format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  secure_traffic: :class:`bool` or ``None``
        :param secure_traffic: Enable/disable encription.
        :type  established_date: :class:`str` or ``None``
        :param established_date: Date tunnel was established.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  failure_message: :class:`str` or ``None``
        :param failure_message: failure message.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  dropped_tx_packets: :class:`str` or ``None``
        :param dropped_tx_packets: Number of transmitted packets dropped.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  dropped_rx_packets: :class:`str` or ``None``
        :param dropped_rx_packets: Number of received packets dropped.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  tunnel_status: :class:`str` or ``None``
        :param tunnel_status: Possible values are: 
            
            * :attr:`Site.TUNNEL_STATUS_CONNECTED`
            * :attr:`Site.TUNNEL_STATUS_DISCONNECTED`
            * :attr:`Site.TUNNEL_STATUS_UNKNOWN`
            
             Site tunnel status.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  tx_bytes_from_local_subnet: :class:`long` or ``None``
        :param tx_bytes_from_local_subnet: Bytes transmitted from local subnet. format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.password = password
        self.user_id = user_id
        self.name = name
        self.rx_bytes_on_local_subnet = rx_bytes_on_local_subnet
        self.secure_traffic = secure_traffic
        self.established_date = established_date
        self.failure_message = failure_message
        self.dropped_tx_packets = dropped_tx_packets
        self.dropped_rx_packets = dropped_rx_packets
        self.tunnel_status = tunnel_status
        self.tx_bytes_from_local_subnet = tx_bytes_from_local_subnet
        VapiStruct.__init__(self)

Site._set_binding_type(type.StructType(
    'com.vmware.vmc.model.site', {
        'password': type.OptionalType(type.StringType()),
        'user_id': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'rx_bytes_on_local_subnet': type.OptionalType(type.IntegerType()),
        'secure_traffic': type.OptionalType(type.BooleanType()),
        'established_date': type.OptionalType(type.StringType()),
        'failure_message': type.OptionalType(type.StringType()),
        'dropped_tx_packets': type.OptionalType(type.StringType()),
        'dropped_rx_packets': type.OptionalType(type.StringType()),
        'tunnel_status': type.OptionalType(type.StringType()),
        'tx_bytes_from_local_subnet': type.OptionalType(type.IntegerType()),
    },
    Site,
    False,
    None))



class Sites(VapiStruct):
    """
    L2 VPN sites.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'sites': 'sites',
                            }

    def __init__(self,
                 sites=None,
                ):
        """
        :type  sites: :class:`list` of :class:`Nsxsite` or ``None``
        :param sites: 
        """
        self.sites = sites
        VapiStruct.__init__(self)

Sites._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sites', {
        'sites': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Nsxsite'))),
    },
    Sites,
    False,
    None))



class SslvpnDashboardStats(VapiStruct):
    """
    Dashboard Statistics data for SSL VPN.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'activeClients': 'active_clients',
                            'sslvpnBytesIn': 'sslvpn_bytes_in',
                            'authFailures': 'auth_failures',
                            'sessionsCreated': 'sessions_created',
                            'sslvpnBytesOut': 'sslvpn_bytes_out',
                            }

    def __init__(self,
                 active_clients=None,
                 sslvpn_bytes_in=None,
                 auth_failures=None,
                 sessions_created=None,
                 sslvpn_bytes_out=None,
                ):
        """
        :type  active_clients: :class:`list` of :class:`DashboardStat` or ``None``
        :param active_clients: Number of active clients.
        :type  sslvpn_bytes_in: :class:`list` of :class:`DashboardStat` or ``None``
        :param sslvpn_bytes_in: Rx bytes received for SSL VPN.
        :type  auth_failures: :class:`list` of :class:`DashboardStat` or ``None``
        :param auth_failures: Number of authentication failures.
        :type  sessions_created: :class:`list` of :class:`DashboardStat` or ``None``
        :param sessions_created: Number of SSL VPN sessions created.
        :type  sslvpn_bytes_out: :class:`list` of :class:`DashboardStat` or ``None``
        :param sslvpn_bytes_out: Tx bytes transmitted for SSL VPN.
        """
        self.active_clients = active_clients
        self.sslvpn_bytes_in = sslvpn_bytes_in
        self.auth_failures = auth_failures
        self.sessions_created = sessions_created
        self.sslvpn_bytes_out = sslvpn_bytes_out
        VapiStruct.__init__(self)

SslvpnDashboardStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sslvpn_dashboard_stats', {
        'activeClients': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'sslvpnBytesIn': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'authFailures': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'sessionsCreated': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
        'sslvpnBytesOut': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DashboardStat'))),
    },
    SslvpnDashboardStats,
    False,
    None))



class SubInterface(VapiStruct):
    """
    NSX Edge sub interface configuration details. Sub interfaces are created on
    a trunk interface.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'index': 'index',
                            'tunnelId': 'tunnel_id',
                            'name': 'name',
                            'addressGroups': 'address_groups',
                            'vlanId': 'vlan_id',
                            'label': 'label',
                            'logicalSwitchName': 'logical_switch_name',
                            'isConnected': 'is_connected',
                            'mtu': 'mtu',
                            'logicalSwitchId': 'logical_switch_id',
                            'enableSendRedirects': 'enable_send_redirects',
                            }

    def __init__(self,
                 index=None,
                 tunnel_id=None,
                 name=None,
                 address_groups=None,
                 vlan_id=None,
                 label=None,
                 logical_switch_name=None,
                 is_connected=None,
                 mtu=None,
                 logical_switch_id=None,
                 enable_send_redirects=None,
                ):
        """
        :type  index: :class:`long` or ``None``
        :param index: Index of the sub interface assigned by NSX Manager. Min value is 10
            and max value is 4103. format: int32
        :type  tunnel_id: :class:`long`
        :param tunnel_id: Valid values for tunnel ID are min 1 to max 4093. Required. format:
            int32
        :type  name: :class:`str` or ``None``
        :param name: Name of the sub interface. Required.
        :type  address_groups: :class:`EdgeVnicAddressGroups` or ``None``
        :param address_groups: Address group configuration of the sub interface.
        :type  vlan_id: :class:`long` or ``None``
        :param vlan_id: VLAN ID of the virtual LAN used by this sub interface. VLAN IDs can
            range from 0 to 4094. format: int32
        :type  label: :class:`str` or ``None``
        :param label: Sub interface label of format vNic_{index} provided by NSX Manager.
            Read only.
        :type  logical_switch_name: :class:`str` or ``None``
        :param logical_switch_name: Name of the logical switch connected to this sub interface.
        :type  is_connected: :class:`bool` or ``None``
        :param is_connected: Value is true if the sub interface is connected to a logical
            switch, standard portgroup or distributed portgroup.
        :type  mtu: :class:`long` or ``None``
        :param mtu: MTU value of the sub interface. This value would be the least mtu
            for all the trunk interfaces of the NSX Edge. Default is 1500.
            format: int32
        :type  logical_switch_id: :class:`str` or ``None``
        :param logical_switch_id: ID of the logical switch connected to this sub interface.
        :type  enable_send_redirects: :class:`bool` or ``None``
        :param enable_send_redirects: Value is true if send redirects is enabled. Enable ICMP redirect to
            convey routing information to hosts.
        """
        self.index = index
        self.tunnel_id = tunnel_id
        self.name = name
        self.address_groups = address_groups
        self.vlan_id = vlan_id
        self.label = label
        self.logical_switch_name = logical_switch_name
        self.is_connected = is_connected
        self.mtu = mtu
        self.logical_switch_id = logical_switch_id
        self.enable_send_redirects = enable_send_redirects
        VapiStruct.__init__(self)

SubInterface._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sub_interface', {
        'index': type.OptionalType(type.IntegerType()),
        'tunnelId': type.IntegerType(),
        'name': type.OptionalType(type.StringType()),
        'addressGroups': type.OptionalType(type.ReferenceType(__name__, 'EdgeVnicAddressGroups')),
        'vlanId': type.OptionalType(type.IntegerType()),
        'label': type.OptionalType(type.StringType()),
        'logicalSwitchName': type.OptionalType(type.StringType()),
        'isConnected': type.OptionalType(type.BooleanType()),
        'mtu': type.OptionalType(type.IntegerType()),
        'logicalSwitchId': type.OptionalType(type.StringType()),
        'enableSendRedirects': type.OptionalType(type.BooleanType()),
    },
    SubInterface,
    False,
    None))



class SubInterfaces(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'subInterfaces': 'sub_interfaces',
                            }

    def __init__(self,
                 sub_interfaces=None,
                ):
        """
        :type  sub_interfaces: :class:`list` of :class:`SubInterface` or ``None``
        :param sub_interfaces: List of sub interfaces.
        """
        self.sub_interfaces = sub_interfaces
        VapiStruct.__init__(self)

SubInterfaces._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sub_interfaces', {
        'subInterfaces': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SubInterface'))),
    },
    SubInterfaces,
    False,
    None))



class Subnets(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'subnets': 'subnets',
                            }

    def __init__(self,
                 subnets=None,
                ):
        """
        :type  subnets: :class:`list` of :class:`str` or ``None``
        :param subnets: List of subnets for which IPsec VPN is configured. Subnets should
            be network address specified in CIDR format and can accept
            '0.0.0.0/0' (any)
        """
        self.subnets = subnets
        VapiStruct.__init__(self)

Subnets._set_binding_type(type.StructType(
    'com.vmware.vmc.model.subnets', {
        'subnets': type.OptionalType(type.ListType(type.StringType())),
    },
    Subnets,
    False,
    None))



class SubscriptionDetails(VapiStruct):
    """
    details of a subscription

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATUS_CREATED = "CREATED"
    """


    """
    STATUS_ACTIVATED = "ACTIVATED"
    """


    """
    STATUS_FAILED = "FAILED"
    """


    """
    STATUS_CANCELLED = "CANCELLED"
    """


    """
    STATUS_EXPIRED = "EXPIRED"
    """


    """
    STATUS_PENDING_PROVISIONING = "PENDING_PROVISIONING"
    """


    """



    _canonical_to_pep_names = {
                            'status': 'status',
                            'anniversary_billing_date': 'anniversary_billing_date',
                            'end_date': 'end_date',
                            'auto_renewed_allowed': 'auto_renewed_allowed',
                            'description': 'description',
                            'commitment_term': 'commitment_term',
                            'csp_subscription_id': 'csp_subscription_id',
                            'billing_subscription_id': 'billing_subscription_id',
                            'commitment_term_uom': 'commitment_term_uom',
                            'offer_version': 'offer_version',
                            'region': 'region',
                            'offer_name': 'offer_name',
                            'offer_type': 'offer_type',
                            'start_date': 'start_date',
                            'quantity': 'quantity',
                            }

    def __init__(self,
                 status=None,
                 anniversary_billing_date=None,
                 end_date=None,
                 auto_renewed_allowed=None,
                 description=None,
                 commitment_term=None,
                 csp_subscription_id=None,
                 billing_subscription_id=None,
                 commitment_term_uom=None,
                 offer_version=None,
                 region=None,
                 offer_name=None,
                 offer_type=None,
                 start_date=None,
                 quantity=None,
                ):
        """
        :type  status: :class:`str` or ``None``
        :param status: Possible values are: 
            
            * :attr:`SubscriptionDetails.STATUS_CREATED`
            * :attr:`SubscriptionDetails.STATUS_ACTIVATED`
            * :attr:`SubscriptionDetails.STATUS_FAILED`
            * :attr:`SubscriptionDetails.STATUS_CANCELLED`
            * :attr:`SubscriptionDetails.STATUS_EXPIRED`
            * :attr:`SubscriptionDetails.STATUS_PENDING_PROVISIONING`
        :type  anniversary_billing_date: :class:`str` or ``None``
        :param anniversary_billing_date: 
        :type  end_date: :class:`str` or ``None``
        :param end_date: 
        :type  auto_renewed_allowed: :class:`str` or ``None``
        :param auto_renewed_allowed: 
        :type  description: :class:`str` or ``None``
        :param description: 
        :type  commitment_term: :class:`str` or ``None``
        :param commitment_term: 
        :type  csp_subscription_id: :class:`str` or ``None``
        :param csp_subscription_id: 
        :type  billing_subscription_id: :class:`str` or ``None``
        :param billing_subscription_id: 
        :type  commitment_term_uom: :class:`str` or ``None``
        :param commitment_term_uom: unit of measurment for commitment term
        :type  offer_version: :class:`str` or ``None``
        :param offer_version: 
        :type  region: :class:`str` or ``None``
        :param region: 
        :type  offer_name: :class:`str` or ``None``
        :param offer_name: 
        :type  offer_type: :class:`OfferType` or ``None``
        :param offer_type: 
        :type  start_date: :class:`str` or ``None``
        :param start_date: 
        :type  quantity: :class:`str` or ``None``
        :param quantity: 
        """
        self.status = status
        self.anniversary_billing_date = anniversary_billing_date
        self.end_date = end_date
        self.auto_renewed_allowed = auto_renewed_allowed
        self.description = description
        self.commitment_term = commitment_term
        self.csp_subscription_id = csp_subscription_id
        self.billing_subscription_id = billing_subscription_id
        self.commitment_term_uom = commitment_term_uom
        self.offer_version = offer_version
        self.region = region
        self.offer_name = offer_name
        self.offer_type = offer_type
        self.start_date = start_date
        self.quantity = quantity
        VapiStruct.__init__(self)

SubscriptionDetails._set_binding_type(type.StructType(
    'com.vmware.vmc.model.subscription_details', {
        'status': type.OptionalType(type.StringType()),
        'anniversary_billing_date': type.OptionalType(type.StringType()),
        'end_date': type.OptionalType(type.StringType()),
        'auto_renewed_allowed': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'commitment_term': type.OptionalType(type.StringType()),
        'csp_subscription_id': type.OptionalType(type.StringType()),
        'billing_subscription_id': type.OptionalType(type.StringType()),
        'commitment_term_uom': type.OptionalType(type.StringType()),
        'offer_version': type.OptionalType(type.StringType()),
        'region': type.OptionalType(type.StringType()),
        'offer_name': type.OptionalType(type.StringType()),
        'offer_type': type.OptionalType(type.ReferenceType(__name__, 'OfferType')),
        'start_date': type.OptionalType(type.StringType()),
        'quantity': type.OptionalType(type.StringType()),
    },
    SubscriptionDetails,
    False,
    None))



class SubscriptionRequest(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'offer_version': 'offer_version',
                            'product_type': 'product_type',
                            'region': 'region',
                            'commitment_term': 'commitment_term',
                            'offer_name': 'offer_name',
                            'quantity': 'quantity',
                            }

    def __init__(self,
                 offer_version=None,
                 product_type=None,
                 region=None,
                 commitment_term=None,
                 offer_name=None,
                 quantity=None,
                ):
        """
        :type  offer_version: :class:`str`
        :param offer_version: 
        :type  product_type: :class:`str`
        :param product_type: 
        :type  region: :class:`str`
        :param region: 
        :type  commitment_term: :class:`str`
        :param commitment_term: 
        :type  offer_name: :class:`str`
        :param offer_name: 
        :type  quantity: :class:`long`
        :param quantity: 
        """
        self.offer_version = offer_version
        self.product_type = product_type
        self.region = region
        self.commitment_term = commitment_term
        self.offer_name = offer_name
        self.quantity = quantity
        VapiStruct.__init__(self)

SubscriptionRequest._set_binding_type(type.StructType(
    'com.vmware.vmc.model.subscription_request', {
        'offer_version': type.StringType(),
        'product_type': type.StringType(),
        'region': type.StringType(),
        'commitment_term': type.StringType(),
        'offer_name': type.StringType(),
        'quantity': type.IntegerType(),
    },
    SubscriptionRequest,
    False,
    None))



class Task(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATUS_STARTED = "STARTED"
    """


    """
    STATUS_CANCELING = "CANCELING"
    """


    """
    STATUS_FINISHED = "FINISHED"
    """


    """
    STATUS_FAILED = "FAILED"
    """


    """
    STATUS_CANCELED = "CANCELED"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'status': 'status',
                            'resource_id': 'resource_id',
                            'start_time': 'start_time',
                            'service_errors': 'service_errors',
                            'sub_status': 'sub_status',
                            'task_type': 'task_type',
                            'task_progress_phases': 'task_progress_phases',
                            'error_message': 'error_message',
                            'org_id': 'org_id',
                            'progress_percent': 'progress_percent',
                            'estimated_remaining_minutes': 'estimated_remaining_minutes',
                            'params': 'params',
                            'end_time': 'end_time',
                            'phase_in_progress': 'phase_in_progress',
                            'task_version': 'task_version',
                            'resource_type': 'resource_type',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 status=None,
                 resource_id=None,
                 start_time=None,
                 service_errors=None,
                 sub_status=None,
                 task_type=None,
                 task_progress_phases=None,
                 error_message=None,
                 org_id=None,
                 progress_percent=None,
                 estimated_remaining_minutes=None,
                 params=None,
                 end_time=None,
                 phase_in_progress=None,
                 task_version=None,
                 resource_type=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str` or ``None``
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  status: :class:`str` or ``None``
        :param status: Possible values are: 
            
            * :attr:`Task.STATUS_STARTED`
            * :attr:`Task.STATUS_CANCELING`
            * :attr:`Task.STATUS_FINISHED`
            * :attr:`Task.STATUS_FAILED`
            * :attr:`Task.STATUS_CANCELED`
        :type  resource_id: :class:`str` or ``None``
        :param resource_id: UUID of resources task is acting upon
        :type  start_time: :class:`datetime.datetime` or ``None``
        :param start_time: 
        :type  service_errors: :class:`list` of :class:`ServiceError` or ``None``
        :param service_errors: Service errors returned from SDDC services.
        :type  sub_status: :class:`str` or ``None``
        :param sub_status: 
        :type  task_type: :class:`str` or ``None``
        :param task_type: 
        :type  task_progress_phases: :class:`list` of :class:`TaskProgressPhase` or ``None``
        :param task_progress_phases: Task progress phases involved in current task execution
        :type  error_message: :class:`str` or ``None``
        :param error_message: 
        :type  org_id: :class:`str` or ``None``
        :param org_id: 
        :type  progress_percent: :class:`long` or ``None``
        :param progress_percent: Estimated progress percentage the task executed format: int32
        :type  estimated_remaining_minutes: :class:`long` or ``None``
        :param estimated_remaining_minutes: Estimated remaining time in minute of the task execution, < 0 means
            no estimation for the task. format: int32
        :type  params: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param params: 
        :type  end_time: :class:`datetime.datetime` or ``None``
        :param end_time: 
        :type  phase_in_progress: :class:`str` or ``None``
        :param phase_in_progress: The current in progress phase ID in the task execution, if none in
            progress, empty string returned.
        :type  task_version: :class:`str` or ``None``
        :param task_version: 
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: Type of resource being acted upon
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.status = status
        self.resource_id = resource_id
        self.start_time = start_time
        self.service_errors = service_errors
        self.sub_status = sub_status
        self.task_type = task_type
        self.task_progress_phases = task_progress_phases
        self.error_message = error_message
        self.org_id = org_id
        self.progress_percent = progress_percent
        self.estimated_remaining_minutes = estimated_remaining_minutes
        self.params = params
        self.end_time = end_time
        self.phase_in_progress = phase_in_progress
        self.task_version = task_version
        self.resource_type = resource_type
        VapiStruct.__init__(self)

Task._set_binding_type(type.StructType(
    'com.vmware.vmc.model.task', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.OptionalType(type.StringType()),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'status': type.OptionalType(type.StringType()),
        'resource_id': type.OptionalType(type.StringType()),
        'start_time': type.OptionalType(type.DateTimeType()),
        'service_errors': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ServiceError'))),
        'sub_status': type.OptionalType(type.StringType()),
        'task_type': type.OptionalType(type.StringType()),
        'task_progress_phases': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'TaskProgressPhase'))),
        'error_message': type.OptionalType(type.StringType()),
        'org_id': type.OptionalType(type.StringType()),
        'progress_percent': type.OptionalType(type.IntegerType()),
        'estimated_remaining_minutes': type.OptionalType(type.IntegerType()),
        'params': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'end_time': type.OptionalType(type.DateTimeType()),
        'phase_in_progress': type.OptionalType(type.StringType()),
        'task_version': type.OptionalType(type.StringType()),
        'resource_type': type.OptionalType(type.StringType()),
    },
    Task,
    False,
    None))



class TaskProgressPhase(VapiStruct):
    """
    A task progress can be (but does NOT have to be) divided to more meaningful
    progress phases.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'id': 'id',
                            'name': 'name',
                            'progress_percent': 'progress_percent',
                            }

    def __init__(self,
                 id=None,
                 name=None,
                 progress_percent=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The identifier of the task progress phase
        :type  name: :class:`str`
        :param name: The display name of the task progress phase
        :type  progress_percent: :class:`long`
        :param progress_percent: The percentage of the phase that has completed format: int32
        """
        self.id = id
        self.name = name
        self.progress_percent = progress_percent
        VapiStruct.__init__(self)

TaskProgressPhase._set_binding_type(type.StructType(
    'com.vmware.vmc.model.task_progress_phase', {
        'id': type.StringType(),
        'name': type.StringType(),
        'progress_percent': type.IntegerType(),
    },
    TaskProgressPhase,
    False,
    None))



class TermOfferInstance(VapiStruct):
    """
    Holder for the term offer instances.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'product_type': 'product_type',
                            'name': 'name',
                            'region': 'region',
                            'commitment_term': 'commitment_term',
                            'unit_price': 'unit_price',
                            'currency': 'currency',
                            'version': 'version',
                            'description': 'description',
                            }

    def __init__(self,
                 product_type=None,
                 name=None,
                 region=None,
                 commitment_term=None,
                 unit_price=None,
                 currency=None,
                 version=None,
                 description=None,
                ):
        """
        :type  product_type: :class:`str`
        :param product_type: 
        :type  name: :class:`str`
        :param name: 
        :type  region: :class:`str`
        :param region: 
        :type  commitment_term: :class:`long`
        :param commitment_term: 
        :type  unit_price: :class:`str`
        :param unit_price: 
        :type  currency: :class:`str`
        :param currency: 
        :type  version: :class:`str`
        :param version: 
        :type  description: :class:`str`
        :param description: 
        """
        self.product_type = product_type
        self.name = name
        self.region = region
        self.commitment_term = commitment_term
        self.unit_price = unit_price
        self.currency = currency
        self.version = version
        self.description = description
        VapiStruct.__init__(self)

TermOfferInstance._set_binding_type(type.StructType(
    'com.vmware.vmc.model.term_offer_instance', {
        'product_type': type.StringType(),
        'name': type.StringType(),
        'region': type.StringType(),
        'commitment_term': type.IntegerType(),
        'unit_price': type.StringType(),
        'currency': type.StringType(),
        'version': type.StringType(),
        'description': type.StringType(),
    },
    TermOfferInstance,
    False,
    None))



class TrafficShapingPolicy(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'burstSize': 'burst_size',
                            'averageBandwidth': 'average_bandwidth',
                            'peakBandwidth': 'peak_bandwidth',
                            'enabled': 'enabled',
                            'inherited': 'inherited',
                            }

    def __init__(self,
                 burst_size=None,
                 average_bandwidth=None,
                 peak_bandwidth=None,
                 enabled=None,
                 inherited=None,
                ):
        """
        :type  burst_size: :class:`long` or ``None``
        :param burst_size: 
        :type  average_bandwidth: :class:`long` or ``None``
        :param average_bandwidth: 
        :type  peak_bandwidth: :class:`long` or ``None``
        :param peak_bandwidth: 
        :type  enabled: :class:`bool` or ``None``
        :param enabled: 
        :type  inherited: :class:`bool` or ``None``
        :param inherited: 
        """
        self.burst_size = burst_size
        self.average_bandwidth = average_bandwidth
        self.peak_bandwidth = peak_bandwidth
        self.enabled = enabled
        self.inherited = inherited
        VapiStruct.__init__(self)

TrafficShapingPolicy._set_binding_type(type.StructType(
    'com.vmware.vmc.model.traffic_shaping_policy', {
        'burstSize': type.OptionalType(type.IntegerType()),
        'averageBandwidth': type.OptionalType(type.IntegerType()),
        'peakBandwidth': type.OptionalType(type.IntegerType()),
        'enabled': type.OptionalType(type.BooleanType()),
        'inherited': type.OptionalType(type.BooleanType()),
    },
    TrafficShapingPolicy,
    False,
    None))



class Vnic(VapiStruct):
    """
    NSX Edge vnic configuration details.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'subInterfaces': 'sub_interfaces',
                            'addressGroups': 'address_groups',
                            'isConnected': 'is_connected',
                            'enableSendRedirects': 'enable_send_redirects',
                            'inShapingPolicy': 'in_shaping_policy',
                            'label': 'label',
                            'enableProxyArp': 'enable_proxy_arp',
                            'index': 'index',
                            'name': 'name',
                            'mtu': 'mtu',
                            'fenceParameters': 'fence_parameters',
                            'macAddresses': 'mac_addresses',
                            'outShapingPolicy': 'out_shaping_policy',
                            'portgroupName': 'portgroup_name',
                            'enableBridgeMode': 'enable_bridge_mode',
                            'type': 'type',
                            'portgroupId': 'portgroup_id',
                            }

    def __init__(self,
                 sub_interfaces=None,
                 address_groups=None,
                 is_connected=None,
                 enable_send_redirects=None,
                 in_shaping_policy=None,
                 label=None,
                 enable_proxy_arp=None,
                 index=None,
                 name=None,
                 mtu=None,
                 fence_parameters=None,
                 mac_addresses=None,
                 out_shaping_policy=None,
                 portgroup_name=None,
                 enable_bridge_mode=None,
                 type=None,
                 portgroup_id=None,
                ):
        """
        :type  sub_interfaces: :class:`SubInterfaces` or ``None``
        :param sub_interfaces: List of sub interfaces. Sub interfaces can be created only on a
            trunk interface.
        :type  address_groups: :class:`EdgeVnicAddressGroups` or ``None``
        :param address_groups: Address group configuration of the interface.
        :type  is_connected: :class:`bool` or ``None``
        :param is_connected: Value is true if the vnic is connected to a logical switch,
            standard portgroup or distributed portgroup.
        :type  enable_send_redirects: :class:`bool` or ``None``
        :param enable_send_redirects: Value is true if send redirects is enabled. Enable ICMP redirect to
            convey routing information to hosts.
        :type  in_shaping_policy: :class:`TrafficShapingPolicy` or ``None``
        :param in_shaping_policy: 
        :type  label: :class:`str` or ``None``
        :param label: Interface label of format vNic_{vnicIndex} provided by NSX Manager.
            Read only.
        :type  enable_proxy_arp: :class:`bool` or ``None``
        :param enable_proxy_arp: Value is true if proxy arp is enabled. Enable proxy ARP if you want
            to allow the NSX Edge of type 'gatewayServices' to answer ARP
            requests intended for other machines.
        :type  index: :class:`long`
        :param index: Index of the vnic. Min value is 0 and max value is 9. format: int32
        :type  name: :class:`str` or ``None``
        :param name: Name of the interface. Optional.
        :type  mtu: :class:`long` or ``None``
        :param mtu: MTU of the interface, with default as 1500. Min is 68, Max is 9000.
            Optional. format: int32
        :type  fence_parameters: :class:`list` of :class:`KeyValueAttributes` or ``None``
        :param fence_parameters: 
        :type  mac_addresses: :class:`list` of :class:`MacAddress` or ``None``
        :param mac_addresses: Distinct MAC addresses configured for the vnic. Optional.
        :type  out_shaping_policy: :class:`TrafficShapingPolicy` or ``None``
        :param out_shaping_policy: 
        :type  portgroup_name: :class:`str` or ``None``
        :param portgroup_name: Name of the port group or logical switch.
        :type  enable_bridge_mode: :class:`bool` or ``None``
        :param enable_bridge_mode: Value is true if bridge mode is enabled.
        :type  type: :class:`str` or ``None``
        :param type: Type of the vnic. Values are uplink, internal, trunk. At least one
            internal interface must be configured for NSX Edge HA to work.
        :type  portgroup_id: :class:`str` or ``None``
        :param portgroup_id: Value are port group ID (standard portgroup or distributed
            portgroup) or virtual wire ID (logical switch). Logical switch
            cannot be used for a TRUNK vnic. Portgroup cannot be shared among
            vnics/LIFs. Required when isConnected is specified as true. Example
            'network-17' (standard portgroup), 'dvportgroup-34' (distributed
            portgroup) or 'virtualwire-2' (logical switch).
        """
        self.sub_interfaces = sub_interfaces
        self.address_groups = address_groups
        self.is_connected = is_connected
        self.enable_send_redirects = enable_send_redirects
        self.in_shaping_policy = in_shaping_policy
        self.label = label
        self.enable_proxy_arp = enable_proxy_arp
        self.index = index
        self.name = name
        self.mtu = mtu
        self.fence_parameters = fence_parameters
        self.mac_addresses = mac_addresses
        self.out_shaping_policy = out_shaping_policy
        self.portgroup_name = portgroup_name
        self.enable_bridge_mode = enable_bridge_mode
        self.type = type
        self.portgroup_id = portgroup_id
        VapiStruct.__init__(self)

Vnic._set_binding_type(type.StructType(
    'com.vmware.vmc.model.vnic', {
        'subInterfaces': type.OptionalType(type.ReferenceType(__name__, 'SubInterfaces')),
        'addressGroups': type.OptionalType(type.ReferenceType(__name__, 'EdgeVnicAddressGroups')),
        'isConnected': type.OptionalType(type.BooleanType()),
        'enableSendRedirects': type.OptionalType(type.BooleanType()),
        'inShapingPolicy': type.OptionalType(type.ReferenceType(__name__, 'TrafficShapingPolicy')),
        'label': type.OptionalType(type.StringType()),
        'enableProxyArp': type.OptionalType(type.BooleanType()),
        'index': type.IntegerType(),
        'name': type.OptionalType(type.StringType()),
        'mtu': type.OptionalType(type.IntegerType()),
        'fenceParameters': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'KeyValueAttributes'))),
        'macAddresses': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'MacAddress'))),
        'outShapingPolicy': type.OptionalType(type.ReferenceType(__name__, 'TrafficShapingPolicy')),
        'portgroupName': type.OptionalType(type.StringType()),
        'enableBridgeMode': type.OptionalType(type.BooleanType()),
        'type': type.OptionalType(type.StringType()),
        'portgroupId': type.OptionalType(type.StringType()),
    },
    Vnic,
    False,
    None))



class Vnics(VapiStruct):
    """
    Ordered list of NSX Edge vnics. Until one connected vnic is configured,
    none of the configured features will serve the network.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vnics': 'vnics',
                            }

    def __init__(self,
                 vnics=None,
                ):
        """
        :type  vnics: :class:`list` of :class:`Vnic` or ``None``
        :param vnics: Ordered list of NSX Edge vnics.
        """
        self.vnics = vnics
        VapiStruct.__init__(self)

Vnics._set_binding_type(type.StructType(
    'com.vmware.vmc.model.vnics', {
        'vnics': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Vnic'))),
    },
    Vnics,
    False,
    None))



class VpcInfo(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vpc_cidr': 'vpc_cidr',
                            'vm_security_group_id': 'vm_security_group_id',
                            'route_table_id': 'route_table_id',
                            'edge_subnet_id': 'edge_subnet_id',
                            'id': 'id',
                            'api_association_id': 'api_association_id',
                            'private_subnet_id': 'private_subnet_id',
                            'api_subnet_id': 'api_subnet_id',
                            'esx_security_group_id': 'esx_security_group_id',
                            'subnet_id': 'subnet_id',
                            'internet_gateway_id': 'internet_gateway_id',
                            'security_group_id': 'security_group_id',
                            'association_id': 'association_id',
                            'vgw_route_table_id': 'vgw_route_table_id',
                            'edge_association_id': 'edge_association_id',
                            'vif_ids': 'vif_ids',
                            'peering_connection_id': 'peering_connection_id',
                            }

    def __init__(self,
                 vpc_cidr=None,
                 vm_security_group_id=None,
                 route_table_id=None,
                 edge_subnet_id=None,
                 id=None,
                 api_association_id=None,
                 private_subnet_id=None,
                 api_subnet_id=None,
                 esx_security_group_id=None,
                 subnet_id=None,
                 internet_gateway_id=None,
                 security_group_id=None,
                 association_id=None,
                 vgw_route_table_id=None,
                 edge_association_id=None,
                 vif_ids=None,
                 peering_connection_id=None,
                ):
        """
        :type  vpc_cidr: :class:`str` or ``None``
        :param vpc_cidr: 
        :type  vm_security_group_id: :class:`str` or ``None``
        :param vm_security_group_id: 
        :type  route_table_id: :class:`str` or ``None``
        :param route_table_id: 
        :type  edge_subnet_id: :class:`str` or ``None``
        :param edge_subnet_id: Id of the NSX edge associated with this VPC
        :type  id: :class:`str` or ``None``
        :param id: 
        :type  api_association_id: :class:`str` or ``None``
        :param api_association_id: Id of the association between subnet and route-table
        :type  private_subnet_id: :class:`str` or ``None``
        :param private_subnet_id: 
        :type  api_subnet_id: :class:`str` or ``None``
        :param api_subnet_id: Id associated with this VPC
        :type  esx_security_group_id: :class:`str` or ``None``
        :param esx_security_group_id: 
        :type  subnet_id: :class:`str` or ``None``
        :param subnet_id: 
        :type  internet_gateway_id: :class:`str` or ``None``
        :param internet_gateway_id: 
        :type  security_group_id: :class:`str` or ``None``
        :param security_group_id: 
        :type  association_id: :class:`str` or ``None``
        :param association_id: 
        :type  vgw_route_table_id: :class:`str` or ``None``
        :param vgw_route_table_id: Route table which contains the route to VGW
        :type  edge_association_id: :class:`str` or ``None``
        :param edge_association_id: Id of the association between edge subnet and route-table
        :type  vif_ids: :class:`list` of :class:`str` or ``None``
        :param vif_ids: 
        :type  peering_connection_id: :class:`str` or ``None``
        :param peering_connection_id: 
        """
        self.vpc_cidr = vpc_cidr
        self.vm_security_group_id = vm_security_group_id
        self.route_table_id = route_table_id
        self.edge_subnet_id = edge_subnet_id
        self.id = id
        self.api_association_id = api_association_id
        self.private_subnet_id = private_subnet_id
        self.api_subnet_id = api_subnet_id
        self.esx_security_group_id = esx_security_group_id
        self.subnet_id = subnet_id
        self.internet_gateway_id = internet_gateway_id
        self.security_group_id = security_group_id
        self.association_id = association_id
        self.vgw_route_table_id = vgw_route_table_id
        self.edge_association_id = edge_association_id
        self.vif_ids = vif_ids
        self.peering_connection_id = peering_connection_id
        VapiStruct.__init__(self)

VpcInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.vpc_info', {
        'vpc_cidr': type.OptionalType(type.StringType()),
        'vm_security_group_id': type.OptionalType(type.StringType()),
        'route_table_id': type.OptionalType(type.StringType()),
        'edge_subnet_id': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'api_association_id': type.OptionalType(type.StringType()),
        'private_subnet_id': type.OptionalType(type.StringType()),
        'api_subnet_id': type.OptionalType(type.StringType()),
        'esx_security_group_id': type.OptionalType(type.StringType()),
        'subnet_id': type.OptionalType(type.StringType()),
        'internet_gateway_id': type.OptionalType(type.StringType()),
        'security_group_id': type.OptionalType(type.StringType()),
        'association_id': type.OptionalType(type.StringType()),
        'vgw_route_table_id': type.OptionalType(type.StringType()),
        'edge_association_id': type.OptionalType(type.StringType()),
        'vif_ids': type.OptionalType(type.ListType(type.StringType())),
        'peering_connection_id': type.OptionalType(type.StringType()),
    },
    VpcInfo,
    False,
    None))



class Vpn(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    ENCRYPTION_AES = "AES"
    """


    """
    ENCRYPTION_AES256 = "AES256"
    """


    """
    ENCRYPTION_AES_GCM = "AES_GCM"
    """


    """
    ENCRYPTION_TRIPLE_DES = "TRIPLE_DES"
    """


    """
    ENCRYPTION_UNKNOWN = "UNKNOWN"
    """


    """
    STATE_CONNECTED = "CONNECTED"
    """


    """
    STATE_DISCONNECTED = "DISCONNECTED"
    """


    """
    STATE_PARTIALLY_CONNECTED = "PARTIALLY_CONNECTED"
    """


    """
    STATE_UNKNOWN = "UNKNOWN"
    """


    """
    DH_GROUP_DH2 = "DH2"
    """


    """
    DH_GROUP_DH5 = "DH5"
    """


    """
    DH_GROUP_DH14 = "DH14"
    """


    """
    DH_GROUP_DH15 = "DH15"
    """


    """
    DH_GROUP_DH16 = "DH16"
    """


    """
    DH_GROUP_UNKNOWN = "UNKNOWN"
    """


    """
    AUTHENTICATION_PSK = "PSK"
    """


    """
    AUTHENTICATION_UNKNOWN = "UNKNOWN"
    """


    """



    _canonical_to_pep_names = {
                            'version': 'version',
                            'on_prem_gateway_ip': 'on_prem_gateway_ip',
                            'on_prem_network_cidr': 'on_prem_network_cidr',
                            'pfs_enabled': 'pfs_enabled',
                            'id': 'id',
                            'channel_status': 'channel_status',
                            'on_prem_nat_ip': 'on_prem_nat_ip',
                            'name': 'name',
                            'internal_network_ids': 'internal_network_ids',
                            'tunnel_statuses': 'tunnel_statuses',
                            'encryption': 'encryption',
                            'enabled': 'enabled',
                            'state': 'state',
                            'dh_group': 'dh_group',
                            'authentication': 'authentication',
                            'pre_shared_key': 'pre_shared_key',
                            }

    def __init__(self,
                 version=None,
                 on_prem_gateway_ip=None,
                 on_prem_network_cidr=None,
                 pfs_enabled=None,
                 id=None,
                 channel_status=None,
                 on_prem_nat_ip=None,
                 name=None,
                 internal_network_ids=None,
                 tunnel_statuses=None,
                 encryption=None,
                 enabled=None,
                 state=None,
                 dh_group=None,
                 authentication=None,
                 pre_shared_key=None,
                ):
        """
        :type  version: :class:`str` or ``None``
        :param version: 
        :type  on_prem_gateway_ip: :class:`str` or ``None``
        :param on_prem_gateway_ip: 
        :type  on_prem_network_cidr: :class:`str` or ``None``
        :param on_prem_network_cidr: 
        :type  pfs_enabled: :class:`bool` or ``None``
        :param pfs_enabled: 
        :type  id: :class:`str` or ``None``
        :param id: 
        :type  channel_status: :class:`VpnChannelStatus` or ``None``
        :param channel_status: 
        :type  on_prem_nat_ip: :class:`str` or ``None``
        :param on_prem_nat_ip: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  internal_network_ids: :class:`list` of :class:`str` or ``None``
        :param internal_network_ids: 
        :type  tunnel_statuses: :class:`list` of :class:`VpnTunnelStatus` or ``None``
        :param tunnel_statuses: 
        :type  encryption: :class:`str` or ``None``
        :param encryption: Possible values are: 
            
            * :attr:`Vpn.ENCRYPTION_AES`
            * :attr:`Vpn.ENCRYPTION_AES256`
            * :attr:`Vpn.ENCRYPTION_AES_GCM`
            * :attr:`Vpn.ENCRYPTION_TRIPLE_DES`
            * :attr:`Vpn.ENCRYPTION_UNKNOWN`
        :type  enabled: :class:`bool` or ``None``
        :param enabled: 
        :type  state: :class:`str` or ``None``
        :param state: Possible values are: 
            
            * :attr:`Vpn.STATE_CONNECTED`
            * :attr:`Vpn.STATE_DISCONNECTED`
            * :attr:`Vpn.STATE_PARTIALLY_CONNECTED`
            * :attr:`Vpn.STATE_UNKNOWN`
        :type  dh_group: :class:`str` or ``None``
        :param dh_group: Possible values are: 
            
            * :attr:`Vpn.DH_GROUP_DH2`
            * :attr:`Vpn.DH_GROUP_DH5`
            * :attr:`Vpn.DH_GROUP_DH14`
            * :attr:`Vpn.DH_GROUP_DH15`
            * :attr:`Vpn.DH_GROUP_DH16`
            * :attr:`Vpn.DH_GROUP_UNKNOWN`
        :type  authentication: :class:`str` or ``None``
        :param authentication: Possible values are: 
            
            * :attr:`Vpn.AUTHENTICATION_PSK`
            * :attr:`Vpn.AUTHENTICATION_UNKNOWN`
        :type  pre_shared_key: :class:`str` or ``None``
        :param pre_shared_key: 
        """
        self.version = version
        self.on_prem_gateway_ip = on_prem_gateway_ip
        self.on_prem_network_cidr = on_prem_network_cidr
        self.pfs_enabled = pfs_enabled
        self.id = id
        self.channel_status = channel_status
        self.on_prem_nat_ip = on_prem_nat_ip
        self.name = name
        self.internal_network_ids = internal_network_ids
        self.tunnel_statuses = tunnel_statuses
        self.encryption = encryption
        self.enabled = enabled
        self.state = state
        self.dh_group = dh_group
        self.authentication = authentication
        self.pre_shared_key = pre_shared_key
        VapiStruct.__init__(self)

Vpn._set_binding_type(type.StructType(
    'com.vmware.vmc.model.vpn', {
        'version': type.OptionalType(type.StringType()),
        'on_prem_gateway_ip': type.OptionalType(type.StringType()),
        'on_prem_network_cidr': type.OptionalType(type.StringType()),
        'pfs_enabled': type.OptionalType(type.BooleanType()),
        'id': type.OptionalType(type.StringType()),
        'channel_status': type.OptionalType(type.ReferenceType(__name__, 'VpnChannelStatus')),
        'on_prem_nat_ip': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'internal_network_ids': type.OptionalType(type.ListType(type.StringType())),
        'tunnel_statuses': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VpnTunnelStatus'))),
        'encryption': type.OptionalType(type.StringType()),
        'enabled': type.OptionalType(type.BooleanType()),
        'state': type.OptionalType(type.StringType()),
        'dh_group': type.OptionalType(type.StringType()),
        'authentication': type.OptionalType(type.StringType()),
        'pre_shared_key': type.OptionalType(type.StringType()),
    },
    Vpn,
    False,
    None))



class VpnChannelStatus(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    CHANNEL_STATUS_CONNECTED = "CONNECTED"
    """


    """
    CHANNEL_STATUS_DISCONNECTED = "DISCONNECTED"
    """


    """
    CHANNEL_STATUS_UNKNOWN = "UNKNOWN"
    """


    """



    _canonical_to_pep_names = {
                            'channel_status': 'channel_status',
                            'channel_state': 'channel_state',
                            'last_info_message': 'last_info_message',
                            'failure_message': 'failure_message',
                            }

    def __init__(self,
                 channel_status=None,
                 channel_state=None,
                 last_info_message=None,
                 failure_message=None,
                ):
        """
        :type  channel_status: :class:`str` or ``None``
        :param channel_status: Possible values are: 
            
            * :attr:`VpnChannelStatus.CHANNEL_STATUS_CONNECTED`
            * :attr:`VpnChannelStatus.CHANNEL_STATUS_DISCONNECTED`
            * :attr:`VpnChannelStatus.CHANNEL_STATUS_UNKNOWN`
        :type  channel_state: :class:`str` or ``None``
        :param channel_state: 
        :type  last_info_message: :class:`str` or ``None``
        :param last_info_message: 
        :type  failure_message: :class:`str` or ``None``
        :param failure_message: 
        """
        self.channel_status = channel_status
        self.channel_state = channel_state
        self.last_info_message = last_info_message
        self.failure_message = failure_message
        VapiStruct.__init__(self)

VpnChannelStatus._set_binding_type(type.StructType(
    'com.vmware.vmc.model.vpn_channel_status', {
        'channel_status': type.OptionalType(type.StringType()),
        'channel_state': type.OptionalType(type.StringType()),
        'last_info_message': type.OptionalType(type.StringType()),
        'failure_message': type.OptionalType(type.StringType()),
    },
    VpnChannelStatus,
    False,
    None))



class VpnTunnelStatus(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    TUNNEL_STATUS_CONNECTED = "CONNECTED"
    """


    """
    TUNNEL_STATUS_DISCONNECTED = "DISCONNECTED"
    """


    """
    TUNNEL_STATUS_UNKNOWN = "UNKNOWN"
    """


    """



    _canonical_to_pep_names = {
                            'on_prem_subnet': 'on_prem_subnet',
                            'traffic_stats': 'traffic_stats',
                            'last_info_message': 'last_info_message',
                            'local_subnet': 'local_subnet',
                            'tunnel_state': 'tunnel_state',
                            'failure_message': 'failure_message',
                            'tunnel_status': 'tunnel_status',
                            }

    def __init__(self,
                 on_prem_subnet=None,
                 traffic_stats=None,
                 last_info_message=None,
                 local_subnet=None,
                 tunnel_state=None,
                 failure_message=None,
                 tunnel_status=None,
                ):
        """
        :type  on_prem_subnet: :class:`str` or ``None``
        :param on_prem_subnet: 
        :type  traffic_stats: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param traffic_stats: 
        :type  last_info_message: :class:`str` or ``None``
        :param last_info_message: 
        :type  local_subnet: :class:`str` or ``None``
        :param local_subnet: 
        :type  tunnel_state: :class:`str` or ``None``
        :param tunnel_state: 
        :type  failure_message: :class:`str` or ``None``
        :param failure_message: 
        :type  tunnel_status: :class:`str` or ``None``
        :param tunnel_status: Possible values are: 
            
            * :attr:`VpnTunnelStatus.TUNNEL_STATUS_CONNECTED`
            * :attr:`VpnTunnelStatus.TUNNEL_STATUS_DISCONNECTED`
            * :attr:`VpnTunnelStatus.TUNNEL_STATUS_UNKNOWN`
        """
        self.on_prem_subnet = on_prem_subnet
        self.traffic_stats = traffic_stats
        self.last_info_message = last_info_message
        self.local_subnet = local_subnet
        self.tunnel_state = tunnel_state
        self.failure_message = failure_message
        self.tunnel_status = tunnel_status
        VapiStruct.__init__(self)

VpnTunnelStatus._set_binding_type(type.StructType(
    'com.vmware.vmc.model.vpn_tunnel_status', {
        'on_prem_subnet': type.OptionalType(type.StringType()),
        'traffic_stats': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'last_info_message': type.OptionalType(type.StringType()),
        'local_subnet': type.OptionalType(type.StringType()),
        'tunnel_state': type.OptionalType(type.StringType()),
        'failure_message': type.OptionalType(type.StringType()),
        'tunnel_status': type.OptionalType(type.StringType()),
    },
    VpnTunnelStatus,
    False,
    None))



class VpnTunnelTrafficStats(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'packets_out': 'packets_out',
                            'packet_received_errors': 'packet_received_errors',
                            'rx_bytes_on_local_subnet': 'rx_bytes_on_local_subnet',
                            'replay_errors': 'replay_errors',
                            'sequence_number_over_flow_errors': 'sequence_number_over_flow_errors',
                            'encryption_failures': 'encryption_failures',
                            'integrity_errors': 'integrity_errors',
                            'packet_sent_errors': 'packet_sent_errors',
                            'decryption_failures': 'decryption_failures',
                            'packets_in': 'packets_in',
                            'tx_bytes_from_local_subnet': 'tx_bytes_from_local_subnet',
                            }

    def __init__(self,
                 packets_out=None,
                 packet_received_errors=None,
                 rx_bytes_on_local_subnet=None,
                 replay_errors=None,
                 sequence_number_over_flow_errors=None,
                 encryption_failures=None,
                 integrity_errors=None,
                 packet_sent_errors=None,
                 decryption_failures=None,
                 packets_in=None,
                 tx_bytes_from_local_subnet=None,
                ):
        """
        :type  packets_out: :class:`str` or ``None``
        :param packets_out: 
        :type  packet_received_errors: :class:`str` or ``None``
        :param packet_received_errors: 
        :type  rx_bytes_on_local_subnet: :class:`str` or ``None``
        :param rx_bytes_on_local_subnet: 
        :type  replay_errors: :class:`str` or ``None``
        :param replay_errors: 
        :type  sequence_number_over_flow_errors: :class:`str` or ``None``
        :param sequence_number_over_flow_errors: 
        :type  encryption_failures: :class:`str` or ``None``
        :param encryption_failures: 
        :type  integrity_errors: :class:`str` or ``None``
        :param integrity_errors: 
        :type  packet_sent_errors: :class:`str` or ``None``
        :param packet_sent_errors: 
        :type  decryption_failures: :class:`str` or ``None``
        :param decryption_failures: 
        :type  packets_in: :class:`str` or ``None``
        :param packets_in: 
        :type  tx_bytes_from_local_subnet: :class:`str` or ``None``
        :param tx_bytes_from_local_subnet: 
        """
        self.packets_out = packets_out
        self.packet_received_errors = packet_received_errors
        self.rx_bytes_on_local_subnet = rx_bytes_on_local_subnet
        self.replay_errors = replay_errors
        self.sequence_number_over_flow_errors = sequence_number_over_flow_errors
        self.encryption_failures = encryption_failures
        self.integrity_errors = integrity_errors
        self.packet_sent_errors = packet_sent_errors
        self.decryption_failures = decryption_failures
        self.packets_in = packets_in
        self.tx_bytes_from_local_subnet = tx_bytes_from_local_subnet
        VapiStruct.__init__(self)

VpnTunnelTrafficStats._set_binding_type(type.StructType(
    'com.vmware.vmc.model.vpn_tunnel_traffic_stats', {
        'packets_out': type.OptionalType(type.StringType()),
        'packet_received_errors': type.OptionalType(type.StringType()),
        'rx_bytes_on_local_subnet': type.OptionalType(type.StringType()),
        'replay_errors': type.OptionalType(type.StringType()),
        'sequence_number_over_flow_errors': type.OptionalType(type.StringType()),
        'encryption_failures': type.OptionalType(type.StringType()),
        'integrity_errors': type.OptionalType(type.StringType()),
        'packet_sent_errors': type.OptionalType(type.StringType()),
        'decryption_failures': type.OptionalType(type.StringType()),
        'packets_in': type.OptionalType(type.StringType()),
        'tx_bytes_from_local_subnet': type.OptionalType(type.StringType()),
    },
    VpnTunnelTrafficStats,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

