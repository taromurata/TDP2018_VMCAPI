# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.ovf.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.ovf_client`` module provides services to capture and
deploy Open Virtualization Format (OVF) packages to and from the content
library. 

It provides the ability to deploy OVF packages from the content library with
support for advanced network topologies, network services, creating virtual
appliances and virtual machines in hosts, resource pools or clusters. It also
provides the ability to export virtual appliances and virtual machines from
hosts, resource pools or clusters as OVF packages to the content library.

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

class DiskProvisioningType(Enum):
    """
    The ``DiskProvisioningType`` class defines the virtual disk provisioning
    types that can be set for a disk on the target platform.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    thin = None
    """
    A thin provisioned virtual disk has space allocated and zeroed on demand as
    the space is used.

    """
    thick = None
    """
    A thick provisioned virtual disk has all space allocated at creation time
    and the space is zeroed on demand as the space is used.

    """
    eagerZeroedThick = None
    """
    An eager zeroed thick provisioned virtual disk has all space allocated and
    wiped clean of any previous contents on the physical media at creation
    time. 
    
    Disks specified as eager zeroed thick may take longer time to create than
    disks specified with the other disk provisioning types.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`DiskProvisioningType` instance.
        """
        Enum.__init__(string)

DiskProvisioningType._set_values([
    DiskProvisioningType('thin'),
    DiskProvisioningType('thick'),
    DiskProvisioningType('eagerZeroedThick'),
])
DiskProvisioningType._set_binding_type(type.EnumType(
    'com.vmware.vcenter.ovf.disk_provisioning_type',
    DiskProvisioningType))




class CertificateParams(VapiStruct):
    """
    The ``CertificateParams`` class contains information about the public key
    certificate used to sign the OVF package. This class will only be returned
    if the OVF package is signed. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 issuer=None,
                 subject=None,
                 is_valid=None,
                 is_self_signed=None,
                 x509=None,
                 type=None,
                ):
        """
        :type  issuer: :class:`str`
        :param issuer: Certificate issuer. For example: /C=US/ST=California/L=Palo
            Alto/O=VMware, Inc.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  subject: :class:`str`
        :param subject: Certificate subject. For example:
            /C=US/ST=Massachusetts/L=Hopkinton/O=EMC Corporation/OU=EMC
            Avamar/CN=EMC Corporation.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  is_valid: :class:`bool`
        :param is_valid: Is the certificate chain validated.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  is_self_signed: :class:`bool`
        :param is_self_signed: Is the certificate self-signed.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  x509: :class:`str`
        :param x509: The X509 representation of the certificate.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.issuer = issuer
        self.subject = subject
        self.is_valid = is_valid
        self.is_self_signed = is_self_signed
        self.x509 = x509
        self.type = type
        VapiStruct.__init__(self)

CertificateParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.certificate_params', {
        'issuer': type.OptionalType(type.StringType()),
        'subject': type.OptionalType(type.StringType()),
        'is_valid': type.OptionalType(type.BooleanType()),
        'is_self_signed': type.OptionalType(type.BooleanType()),
        'x509': type.OptionalType(type.StringType()),
        'type': type.OptionalType(type.StringType()),
    },
    CertificateParams,
    False,
    None))



class DeploymentOption(VapiStruct):
    """
    The ``DeploymentOption`` class contains the information about a deployment
    option as defined in the OVF specification. 
    
    This corresponds to the ovf:Configuration element of the
    ovf:DeploymentOptionSection in the specification. The
    ovf:DeploymentOptionSection specifies a discrete set of intended resource
    allocation configurations. This class represents one item from that set. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 key=None,
                 label=None,
                 description=None,
                 default_choice=None,
                ):
        """
        :type  key: :class:`str`
        :param key: The key of the deployment option, corresponding to the ovf:id
            attribute in the OVF descriptor.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  label: :class:`str`
        :param label: A localizable label for the deployment option.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  description: :class:`str`
        :param description: A localizable description for the deployment option.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  default_choice: :class:`bool`
        :param default_choice: A :class:`bool` flag indicates whether this deployment option is
            the default choice.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package. If None or false, it
            is not the default.
        """
        self.key = key
        self.label = label
        self.description = description
        self.default_choice = default_choice
        VapiStruct.__init__(self)

DeploymentOption._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.deployment_option', {
        'key': type.OptionalType(type.StringType()),
        'label': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'default_choice': type.OptionalType(type.BooleanType()),
    },
    DeploymentOption,
    False,
    None))



class DeploymentOptionParams(VapiStruct):
    """
    The ``DeploymentOptionParams`` class describes the possible deployment
    options as well as the choice provided by the user. 
    
     This information based on the ovf:DeploymentOptionSection. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 deployment_options=None,
                 selected_key=None,
                 type=None,
                ):
        """
        :type  deployment_options: :class:`list` of :class:`DeploymentOption`
        :param deployment_options: :class:`list` of deployment options. This attribute corresponds to
            the ovf:Configuration elements of the ovf:DeploymentOptionSection
            in the specification. It is a discrete set of intended resource
            allocation configurations from which one can be selected.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  selected_key: :class:`str`
        :param selected_key: The selected deployment option. Identifies the
            :class:`DeploymentOption` in the list in the ``deploymentOptions``
            attribute with a matching value in the :attr:`DeploymentOption.key`
            attribute.
            This attribute is optional in the input parameters when deploying
            an OVF package. If None the server will use the default deployment
            configuration, usually it's the first one in
            :attr:`DeploymentOptionParams.deployment_options` :class:`list`.
            This attribute is optional in the result when retrieving
            information about an OVF package. The value will be set only if it
            is specified with the optional ovf:default attribute.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.deployment_options = deployment_options
        self.selected_key = selected_key
        self.type = type
        VapiStruct.__init__(self)

DeploymentOptionParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.deployment_option_params', {
        'deployment_options': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DeploymentOption'))),
        'selected_key': type.OptionalType(type.StringType()),
        'type': type.OptionalType(type.StringType()),
    },
    DeploymentOptionParams,
    False,
    None))



class ExtraConfig(VapiStruct):
    """
    The ``ExtraConfig`` class contains the information about a vmw:ExtraConfig
    element which can be used to specify configuration settings that are
    transferred directly to the ``.vmx`` file. The behavior of the
    vmw:ExtraConfig element is similar to the ``extraConfig`` property of the
    ``VirtualMachineConfigSpec`` object in the VMware vSphere API. Thus, the
    same restrictions apply, such as you cannot set values that could otherwise
    be set with other properties in the ``VirtualMachineConfigSpec`` object.
    See the VMware vSphere API reference for details on this. 
    
    vmw:ExtraConfig elements may occur as direct child elements of a
    VirtualHardwareSection, or as child elements of individual virtual hardware
    items. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 key=None,
                 value=None,
                 virtual_system_id=None,
                ):
        """
        :type  key: :class:`str`
        :param key: The key of the ExtraConfig element.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        :type  value: :class:`str`
        :param value: The value of the ExtraConfig element.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        :type  virtual_system_id: :class:`str`
        :param virtual_system_id: The identifier of the virtual system containing the vmw:ExtraConfig
            element.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        """
        self.key = key
        self.value = value
        self.virtual_system_id = virtual_system_id
        VapiStruct.__init__(self)

ExtraConfig._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.extra_config', {
        'key': type.OptionalType(type.StringType()),
        'value': type.OptionalType(type.StringType()),
        'virtual_system_id': type.OptionalType(type.StringType()),
    },
    ExtraConfig,
    False,
    None))



class ExtraConfigParams(VapiStruct):
    """
    The ``ExtraConfigParams`` class contains the parameters with information
    about the vmw:ExtraConfig elements in an OVF package. 
    
    vmw:ExtraConfig elements can be used to specify configuration settings that
    are transferred directly to the ``.vmx`` file. 
    
    The behavior of the vmw:ExtraConfig element is similar to the
    ``extraConfig`` property of the ``VirtualMachineConfigSpec`` object in the
    VMware vSphere API. Thus, the same restrictions apply, such as you cannot
    set values that could otherwise be set with other properties in the
    ``VirtualMachineConfigSpec`` object. See the VMware vSphere API reference
    for details on this. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 extra_configs=None,
                 exclude_keys=None,
                 include_keys=None,
                 type=None,
                ):
        """
        :type  extra_configs: :class:`list` of :class:`ExtraConfig`
        :param extra_configs: :class:`list` of vmw:ExtraConfig elements in the OVF package.
            This attribute is optional in the input parameters when deploying
            an OVF package. If None there are no extra configuration elements
            to use for this OVF package deployment. This attribute will always
            be present in the result when retrieving information about an OVF
            package. It will be an empty :class:`list` if there are no extra
            configuration elements in the OVF package.
        :type  exclude_keys: :class:`list` of :class:`str`
        :param exclude_keys: Specifies which extra configuration items in the :class:`list` in
            the ``extraConfigs`` ``field`` should be ignored during deployment.
            
            If set, the given keys for extra configurations will be ignored
            during deployment. The key is defined in the
            :attr:`ExtraConfig.key` attribute.
            This attribute is optional in the input parameters when deploying
            an OVF package. It is an error to set both this and
            :attr:`ExtraConfigParams.include_keys`. This attribute is optional
            in the result when retrieving information about an OVF package. It
            is an error to set both this and
            :attr:`ExtraConfigParams.include_keys`.
        :type  include_keys: :class:`list` of :class:`str`
        :param include_keys: Specifies which extra configuration items in the :class:`list` in
            the ``extraConfigs`` ``field`` should be included during
            deployment. 
            
            If set, all but the given keys for extra configurations will be
            ignored during deployment. The key is defined in the
            :attr:`ExtraConfig.key` attribute.
            This attribute is optional in the input parameters when deploying
            an OVF package. It is an error to set both this and
            :attr:`ExtraConfigParams.exclude_keys`. This attribute is optional
            in the result when retrieving information about an OVF package. It
            is an error to set both this and
            :attr:`ExtraConfigParams.exclude_keys`.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.extra_configs = extra_configs
        self.exclude_keys = exclude_keys
        self.include_keys = include_keys
        self.type = type
        VapiStruct.__init__(self)

ExtraConfigParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.extra_config_params', {
        'extra_configs': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ExtraConfig'))),
        'exclude_keys': type.OptionalType(type.ListType(type.StringType())),
        'include_keys': type.OptionalType(type.ListType(type.StringType())),
        'type': type.OptionalType(type.StringType()),
    },
    ExtraConfigParams,
    False,
    None))



class IpAllocationParams(VapiStruct):
    """
    The ``IpAllocationParams`` class specifies how IP addresses are allocated
    to OVF properties. In particular, it informs the deployment platform
    whether the guest supports IPv4, IPv6, or both. It also specifies whether
    the IP addresses can be obtained through DHCP or through the properties
    provided in the OVF environment. 
    
    Ovf Property elements are exposed to the guest software through the OVF
    environment. Each Property element exposed in the OVF environment shall be
    constructed from the value of the ovf:key attribute. A Property element
    contains a key/value pair, it may optionally specify type qualifiers using
    the ovf:qualifiers attribute with multiple qualifiers separated by commas. 
    
    The settings in ``IpAllocationParams`` class are global to a deployment.
    Thus, if a virtual machine is part of a virtual appliance, then its
    settings are ignored and the settings for the virtual appliance is used. 
    
     This information is based on the vmw:IpAssignmentSection in OVF package. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 supported_allocation_scheme=None,
                 supported_ip_allocation_policy=None,
                 ip_allocation_policy=None,
                 supported_ip_protocol=None,
                 ip_protocol=None,
                 type=None,
                ):
        """
        :type  supported_allocation_scheme: :class:`list` of :class:`IpAllocationParams.IpAllocationScheme`
        :param supported_allocation_scheme: Specifies the IP allocation schemes supported by the guest
            software. This attribute defines the valid values for the IP
            allocation policy. This setting is often configured by the virtual
            appliance template author or OVF package author to reflect what the
            guest software supports, and the IP allocation policy is configured
            at deployment time. See
            :attr:`IpAllocationParams.ip_allocation_policy`.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  supported_ip_allocation_policy: :class:`list` of :class:`IpAllocationParams.IpAllocationPolicy`
        :param supported_ip_allocation_policy: Specifies the IP allocation policies supported. The set of valid
            options for the policy is based on the capabilities of the virtual
            appliance software, as specified by the
            :attr:`IpAllocationParams.supported_allocation_scheme` attribute.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  ip_allocation_policy: :class:`IpAllocationParams.IpAllocationPolicy`
        :param ip_allocation_policy: Specifies how IP allocation is done through an IP Pool. This is
            typically specified by the deployer.
            This attribute is optional in the input parameters when deploying
            an OVF package. If None there is no IP allocation policy. This
            attribute will always be present in the result when retrieving
            information about an OVF package.
        :type  supported_ip_protocol: :class:`list` of :class:`IpAllocationParams.IpProtocol`
        :param supported_ip_protocol: Specifies the IP protocols supported by the guest.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  ip_protocol: :class:`IpAllocationParams.IpProtocol`
        :param ip_protocol: Specifies the chosen IP protocol for this deployment. This must be
            one of the IP protocols supported by the guest software. See
            :attr:`IpAllocationParams.supported_ip_protocol`.
            This attribute is optional in the input parameters when deploying
            an OVF package. If None there is no IP protocol chosen. This
            attribute will always be present in the result when retrieving
            information about an OVF package.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.supported_allocation_scheme = supported_allocation_scheme
        self.supported_ip_allocation_policy = supported_ip_allocation_policy
        self.ip_allocation_policy = ip_allocation_policy
        self.supported_ip_protocol = supported_ip_protocol
        self.ip_protocol = ip_protocol
        self.type = type
        VapiStruct.__init__(self)

    class IpAllocationPolicy(Enum):
        """
        The ``IpAllocationParams.IpAllocationPolicy`` class defines the possible IP
        allocation policy for a deployment.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        DHCP = None
        """
        Specifies that DHCP will be used to allocate IP addresses.

        """
        TRANSIENT_IPPOOL = None
        """
        Specifies that IP addresses are allocated from an IP pool. The IP addresses
        are allocated when needed, typically at power-on, and deallocated during
        power-off. There is no guarantee that a property will receive same IP
        address when restarted.

        """
        STATIC_MANUAL = None
        """
        Specifies that IP addresses are configured manually upon deployment, and
        will be kept until reconfigured or the virtual appliance destroyed. This
        ensures that a property gets a consistent IP for its lifetime.

        """
        STATIC_IPPOOL = None
        """
        Specifies that IP addresses are allocated from the range managed by an IP
        pool. The IP addresses are allocated at first power-on, and remain
        allocated at power-off. This ensures that a virtual appliance gets a
        consistent IP for its life-time.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IpAllocationPolicy` instance.
            """
            Enum.__init__(string)

    IpAllocationPolicy._set_values([
        IpAllocationPolicy('DHCP'),
        IpAllocationPolicy('TRANSIENT_IPPOOL'),
        IpAllocationPolicy('STATIC_MANUAL'),
        IpAllocationPolicy('STATIC_IPPOOL'),
    ])
    IpAllocationPolicy._set_binding_type(type.EnumType(
        'com.vmware.vcenter.ovf.ip_allocation_params.ip_allocation_policy',
        IpAllocationPolicy))

    class IpAllocationScheme(Enum):
        """
        The ``IpAllocationParams.IpAllocationScheme`` class defines the possible IP
        allocation schemes that can be supported by the guest software.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        DHCP = None
        """
        It supports DHCP to acquire IP configuration.

        """
        OVF_ENVIRONMENT = None
        """
        It supports setting the IP configuration through the properties provided in
        the OVF environment.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IpAllocationScheme` instance.
            """
            Enum.__init__(string)

    IpAllocationScheme._set_values([
        IpAllocationScheme('DHCP'),
        IpAllocationScheme('OVF_ENVIRONMENT'),
    ])
    IpAllocationScheme._set_binding_type(type.EnumType(
        'com.vmware.vcenter.ovf.ip_allocation_params.ip_allocation_scheme',
        IpAllocationScheme))

    class IpProtocol(Enum):
        """
        The ``IpAllocationParams.IpProtocol`` class defines the IP protocols
        supported by the guest software.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        IPV4 = None
        """
        It supports the IPv4 protocol.

        """
        IPV6 = None
        """
        It supports the IPv6 protocol.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IpProtocol` instance.
            """
            Enum.__init__(string)

    IpProtocol._set_values([
        IpProtocol('IPV4'),
        IpProtocol('IPV6'),
    ])
    IpProtocol._set_binding_type(type.EnumType(
        'com.vmware.vcenter.ovf.ip_allocation_params.ip_protocol',
        IpProtocol))

IpAllocationParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.ip_allocation_params', {
        'supported_allocation_scheme': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'IpAllocationParams.IpAllocationScheme'))),
        'supported_ip_allocation_policy': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'IpAllocationParams.IpAllocationPolicy'))),
        'ip_allocation_policy': type.OptionalType(type.ReferenceType(__name__, 'IpAllocationParams.IpAllocationPolicy')),
        'supported_ip_protocol': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'IpAllocationParams.IpProtocol'))),
        'ip_protocol': type.OptionalType(type.ReferenceType(__name__, 'IpAllocationParams.IpProtocol')),
        'type': type.OptionalType(type.StringType()),
    },
    IpAllocationParams,
    False,
    None))



class OvfMessage(VapiStruct):
    """
    The ``OvfMessage`` class describes a base OVF handling error message
    related to accessing, validating, deploying, or exporting an OVF package. 
    
    These messages fall into different categories defined in
    :class:`OvfMessage.Category`:

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'category',
            {
                'VALIDATION' : [('issues', True)],
                'INPUT' : [('name', True), ('value', True), ('message', True)],
                'SERVER' : [('error', True)],
            }
        ),
    ]



    def __init__(self,
                 category=None,
                 issues=None,
                 name=None,
                 value=None,
                 message=None,
                 error=None,
                ):
        """
        :type  category: :class:`OvfMessage.Category`
        :param category: The message category.
        :type  issues: :class:`list` of :class:`ParseIssue`
        :param issues: :class:`list` of parse issues (see :class:`ParseIssue`).
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.VALIDATION`.
        :type  name: :class:`str`
        :param name: The name of input parameter.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  value: :class:`str`
        :param value: The value of input parameter.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param message: A localizable message.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  error: :class:`vmware.vapi.struct.VapiStruct`
        :param error: Represents a server
            :class:`com.vmware.vapi.std.errors_client.Error`.
            When clients pass a value of this class as a parameter, the
            attribute must contain all the attributes defined in
            :class:`com.vmware.vapi.std.errors_client.Error`. When methods
            return a value of this class as a return value, the attribute will
            contain all the attributes defined in
            :class:`com.vmware.vapi.std.errors_client.Error`.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.SERVER`.
        """
        self.category = category
        self.issues = issues
        self.name = name
        self.value = value
        self.message = message
        self.error = error
        VapiStruct.__init__(self)

    class Category(Enum):
        """
        The ``OvfMessage.Category`` class defines the categories of messages (see
        :class:`OvfMessage`).

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        VALIDATION = None
        """
        The OVF descriptor is invalid, for example, syntax errors or schema errors.

        """
        INPUT = None
        """
        The user provided input parameters are invalid.

        """
        SERVER = None
        """
        Server error.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Category` instance.
            """
            Enum.__init__(string)

    Category._set_values([
        Category('VALIDATION'),
        Category('INPUT'),
        Category('SERVER'),
    ])
    Category._set_binding_type(type.EnumType(
        'com.vmware.vcenter.ovf.ovf_message.category',
        Category))

OvfMessage._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.ovf_message', {
        'category': type.ReferenceType(__name__, 'OvfMessage.Category'),
        'issues': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ParseIssue'))),
        'name': type.OptionalType(type.StringType()),
        'value': type.OptionalType(type.StringType()),
        'message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'error': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error')])),
    },
    OvfMessage,
    False,
    None))



class ParseIssue(VapiStruct):
    """
    The ``ParseIssue`` class contains the information about the issue found
    when parsing an OVF package during deployment or exporting an OVF package
    including: 
    
    * Parsing and validation error on OVF descriptor (which is an XML
      document), manifest and certificate files.
    * OVF descriptor generating and device error.
    * Unexpected server error.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 category=None,
                 file=None,
                 line_number=None,
                 column_number=None,
                 message=None,
                ):
        """
        :type  category: :class:`ParseIssue.Category`
        :param category: The category of the parse issue.
        :type  file: :class:`str`
        :param file: The name of the file in which the parse issue was found.
        :type  line_number: :class:`long`
        :param line_number: The line number of the line in the file (see
            :attr:`ParseIssue.file`) where the parse issue was found (or -1 if
            not applicable).
        :type  column_number: :class:`long`
        :param column_number: The position in the line (see :attr:`ParseIssue.line_number`) (or
            -1 if not applicable).
        :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param message: A localizable message describing the parse issue.
        """
        self.category = category
        self.file = file
        self.line_number = line_number
        self.column_number = column_number
        self.message = message
        VapiStruct.__init__(self)

    class Category(Enum):
        """
        The ``ParseIssue.Category`` class defines the categories of issues that can
        be found when parsing files inside an OVF package (see :class:`ParseIssue`)
        including OVF descriptor (which is an XML document), manifest and
        certificate files, or exporting an OVF package.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        VALUE_ILLEGAL = None
        """
        Illegal value error. For example, the value is malformed, not a number, or
        outside of the given range, and so on.

        """
        ATTRIBUTE_REQUIRED = None
        """
        Required attribute error. It indicates that a required attribute is missing
        from an element in the OVF descriptor.

        """
        ATTRIBUTE_ILLEGAL = None
        """
        Illegal attribute error. It indicates that an illegal attribute is set for
        an element in the OVF descriptor. For example, empty disks do not use
        format, parentRef, and populatedSize attributes, if these attributes are
        present in an empty disk element then will get this pasrse issue.

        """
        ELEMENT_REQUIRED = None
        """
        Required element error. It indicates that a required element is missing
        from the OVF descriptor.

        """
        ELEMENT_ILLEGAL = None
        """
        Illegal element error. It indicates that an element is present in a
        location which is not allowed, or found multiple elements but only one is
        allowed at the location in the OVF descriptor.

        """
        ELEMENT_UNKNOWN = None
        """
        Unknown element error. It indicates that an element is unsupported when
        parsing an OVF descriptor.

        """
        SECTION_UNKNOWN = None
        """
        Section unknown error. It indicates that a section is unsupported when
        parsing an OVF descriptor.

        """
        SECTION_RESTRICTION = None
        """
        Section restriction error. It indicates that a section appears in place in
        the OVF descriptor where it is not allowed, a section appears fewer times
        than is required, or a section appears more times than is allowed.

        """
        PARSE_ERROR = None
        """
        OVF package parsing error, including: 
        
        * OVF descriptor parsing errors, for example, syntax errors or schema
          errors.
        * Manifest file parsing and verification errors.
        * Certificate file parsing and verification errors.

        """
        GENERATE_ERROR = None
        """
        OVF descriptor (which is an XML document) generating error, for example,
        well-formedness errors as well as unexpected processing conditions.

        """
        VALIDATION_ERROR = None
        """
        An issue with the manifest and signing.

        """
        EXPORT_ERROR = None
        """
        Issue during OVF export, for example, malformed deviceId, controller not
        found, or file backing for a device not found.

        """
        INTERNAL_ERROR = None
        """
        Server encountered an unexpected error which prevented it from fulfilling
        the request.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Category` instance.
            """
            Enum.__init__(string)

    Category._set_values([
        Category('VALUE_ILLEGAL'),
        Category('ATTRIBUTE_REQUIRED'),
        Category('ATTRIBUTE_ILLEGAL'),
        Category('ELEMENT_REQUIRED'),
        Category('ELEMENT_ILLEGAL'),
        Category('ELEMENT_UNKNOWN'),
        Category('SECTION_UNKNOWN'),
        Category('SECTION_RESTRICTION'),
        Category('PARSE_ERROR'),
        Category('GENERATE_ERROR'),
        Category('VALIDATION_ERROR'),
        Category('EXPORT_ERROR'),
        Category('INTERNAL_ERROR'),
    ])
    Category._set_binding_type(type.EnumType(
        'com.vmware.vcenter.ovf.parse_issue.category',
        Category))

ParseIssue._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.parse_issue', {
        'category': type.ReferenceType(__name__, 'ParseIssue.Category'),
        'file': type.StringType(),
        'line_number': type.IntegerType(),
        'column_number': type.IntegerType(),
        'message': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
    },
    ParseIssue,
    False,
    None))



class OvfError(VapiStruct):
    """
    The ``OvfError`` class describes an error related to accessing, validating,
    deploying, or exporting an OVF package.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'category',
            {
                'VALIDATION' : [('issues', True)],
                'INPUT' : [('name', True), ('value', True), ('message', True)],
                'SERVER' : [('error', True)],
            }
        ),
    ]



    def __init__(self,
                 category=None,
                 issues=None,
                 name=None,
                 value=None,
                 message=None,
                 error=None,
                ):
        """
        :type  category: :class:`OvfMessage.Category`
        :param category: The message category.
        :type  issues: :class:`list` of :class:`ParseIssue`
        :param issues: :class:`list` of parse issues (see :class:`ParseIssue`).
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.VALIDATION`.
        :type  name: :class:`str`
        :param name: The name of input parameter.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  value: :class:`str`
        :param value: The value of input parameter.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param message: A localizable message.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  error: :class:`vmware.vapi.struct.VapiStruct`
        :param error: Represents a server
            :class:`com.vmware.vapi.std.errors_client.Error`.
            When clients pass a value of this class as a parameter, the
            attribute must contain all the attributes defined in
            :class:`com.vmware.vapi.std.errors_client.Error`. When methods
            return a value of this class as a return value, the attribute will
            contain all the attributes defined in
            :class:`com.vmware.vapi.std.errors_client.Error`.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.SERVER`.
        """
        self.category = category
        self.issues = issues
        self.name = name
        self.value = value
        self.message = message
        self.error = error
        VapiStruct.__init__(self)

OvfError._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.ovf_error', {
        'category': type.ReferenceType(__name__, 'OvfMessage.Category'),
        'issues': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ParseIssue'))),
        'name': type.OptionalType(type.StringType()),
        'value': type.OptionalType(type.StringType()),
        'message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'error': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error')])),
    },
    OvfError,
    False,
    None))



class OvfWarning(VapiStruct):
    """
    The ``OvfWarning`` class describes a warning related to accessing,
    validating, deploying, or exporting an OVF package.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'category',
            {
                'VALIDATION' : [('issues', True)],
                'INPUT' : [('name', True), ('value', True), ('message', True)],
                'SERVER' : [('error', True)],
            }
        ),
    ]



    def __init__(self,
                 category=None,
                 issues=None,
                 name=None,
                 value=None,
                 message=None,
                 error=None,
                ):
        """
        :type  category: :class:`OvfMessage.Category`
        :param category: The message category.
        :type  issues: :class:`list` of :class:`ParseIssue`
        :param issues: :class:`list` of parse issues (see :class:`ParseIssue`).
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.VALIDATION`.
        :type  name: :class:`str`
        :param name: The name of input parameter.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  value: :class:`str`
        :param value: The value of input parameter.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param message: A localizable message.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.INPUT`.
        :type  error: :class:`vmware.vapi.struct.VapiStruct`
        :param error: Represents a server
            :class:`com.vmware.vapi.std.errors_client.Error`.
            When clients pass a value of this class as a parameter, the
            attribute must contain all the attributes defined in
            :class:`com.vmware.vapi.std.errors_client.Error`. When methods
            return a value of this class as a return value, the attribute will
            contain all the attributes defined in
            :class:`com.vmware.vapi.std.errors_client.Error`.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`OvfMessage.Category.SERVER`.
        """
        self.category = category
        self.issues = issues
        self.name = name
        self.value = value
        self.message = message
        self.error = error
        VapiStruct.__init__(self)

OvfWarning._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.ovf_warning', {
        'category': type.ReferenceType(__name__, 'OvfMessage.Category'),
        'issues': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ParseIssue'))),
        'name': type.OptionalType(type.StringType()),
        'value': type.OptionalType(type.StringType()),
        'message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'error': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error')])),
    },
    OvfWarning,
    False,
    None))



class OvfInfo(VapiStruct):
    """
    The ``OvfInfo`` class contains informational messages related to accessing,
    validating, deploying, or exporting an OVF package.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 messages=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: A :class:`list` of localizable messages (see
            :class:`com.vmware.vapi.std_client.LocalizableMessage`).
        """
        self.messages = messages
        VapiStruct.__init__(self)

OvfInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.ovf_info', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
    },
    OvfInfo,
    False,
    None))



class OvfParams(VapiStruct):
    """
    The ``OvfParams`` class defines the common attributes for all OVF
    deployment parameters. OVF parameters serve several purposes: 
    
    * Describe information about a given OVF package.
    * Describe default deployment configuration.
    * Describe possible deployment values based on the deployment environment.
    * Provide deployment-specific configuration.
    
    Each OVF parameters class specifies a particular configurable aspect of OVF
    deployment. An aspect has both a query-model and a deploy-model. The
    query-model is used when the OVF package is queried, and the deploy-model
    is used when deploying an OVF package. 
    
    Most OVF parameter classes provide both informational and deployment
    parameters. However, some are purely informational (for example, download
    size) and some are purely deployment parameters (for example, the flag to
    indicate whether registration as a vCenter extension is accepted). 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 type=None,
                ):
        """
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.type = type
        VapiStruct.__init__(self)

OvfParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.ovf_params', {
        'type': type.OptionalType(type.StringType()),
    },
    OvfParams,
    False,
    None))



class Property(VapiStruct):
    """
    The ``Property`` class contains the information about a property in an OVF
    package. 
    
    A property is uniquely identified by its [classid.]id[.instanceid]
    fully-qualified name (see :attr:`Property.class_id`, :attr:`Property.id`,
    and :attr:`Property.instance_id`). If multiple properties in an OVF package
    have the same fully-qualified name, then the property is excluded and
    cannot be set. We do warn about this during import. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 class_id=None,
                 id=None,
                 instance_id=None,
                 category=None,
                 ui_optional=None,
                 label=None,
                 description=None,
                 type=None,
                 value=None,
                ):
        """
        :type  class_id: :class:`str`
        :param class_id: The classId of this OVF property.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  id: :class:`str`
        :param id: The identifier of this OVF property.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        :type  instance_id: :class:`str`
        :param instance_id: The instanceId of this OVF property.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  category: :class:`str`
        :param category: If this is set to a non-empty string, this property starts a new
            category.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package. If None, the property
            is in the same category as the previous item, otherwise, it starts
            a new category.
        :type  ui_optional: :class:`bool`
        :param ui_optional: Whether a category is UI optional. This is only used if this
            property starts a new category (see :attr:`Property.category`). 
            
            The value is stored in an optional attribute vmw:uioptional to the
            ovf:Category element. The default value is false. If this value is
            true, the properties within this category are optional. The UI
            renders this as a group with a check box, and the group is grayed
            out until the check box is selected. When the check box is
            selected, the input values are read and used in deployment. If
            properties within the same category specify conflicting values the
            default is used. Only implemented in vSphere Web Client 5.1 and
            later as of Nov 2012.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package.
        :type  label: :class:`str`
        :param label: The display name of this OVF property.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  description: :class:`str`
        :param description: A description of this OVF property.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package.
        :type  type: :class:`str`
        :param type: The type of this OVF property. Refer to the configuration of a
            virtual appliance/virtual machine for the valid values.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  value: :class:`str`
        :param value: The OVF property value. This contains the default value from
            ovf:defaultValue if ovf:value is not present when read.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.class_id = class_id
        self.id = id
        self.instance_id = instance_id
        self.category = category
        self.ui_optional = ui_optional
        self.label = label
        self.description = description
        self.type = type
        self.value = value
        VapiStruct.__init__(self)

Property._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.property', {
        'class_id': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'instance_id': type.OptionalType(type.StringType()),
        'category': type.OptionalType(type.StringType()),
        'ui_optional': type.OptionalType(type.BooleanType()),
        'label': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'type': type.OptionalType(type.StringType()),
        'value': type.OptionalType(type.StringType()),
    },
    Property,
    False,
    None))



class PropertyParams(VapiStruct):
    """
    The ``PropertyParams`` class contains a :class:`list` of OVF properties
    that can be configured when the OVF package is deployed. 
    
     This is based on the ovf:ProductSection. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 properties=None,
                 type=None,
                ):
        """
        :type  properties: :class:`list` of :class:`Property`
        :param properties: :class:`list` of OVF properties.
            This attribute is optional in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.properties = properties
        self.type = type
        VapiStruct.__init__(self)

PropertyParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.property_params', {
        'properties': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Property'))),
        'type': type.OptionalType(type.StringType()),
    },
    PropertyParams,
    False,
    None))



class ScaleOutGroup(VapiStruct):
    """
    The ``ScaleOutGroup`` class contains information about a scale-out group. 
    
    It allows a virtual system collection to contain a set of children that are
    homogeneous with respect to a prototypical virtual system or virtual system
    collection. It shall cause the deployment function to replicate the
    prototype a number of times, thus allowing the number of instantiated
    virtual systems to be configured dynamically at deployment time. 
    
     This is based on the ovf2:ScaleOutSection. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 description=None,
                 instance_count=None,
                 minimum_instance_count=None,
                 maximum_instance_count=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The identifier of the scale-out group.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        :type  description: :class:`str`
        :param description: The description of the scale-out group.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  instance_count: :class:`long`
        :param instance_count: The scaling factor to use. It defines the number of replicas of the
            prototypical virtual system or virtual system collection.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        :type  minimum_instance_count: :class:`long`
        :param minimum_instance_count: The minimum scaling factor.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package. This will be 1 if
            there is no explicit limit.
        :type  maximum_instance_count: :class:`long`
        :param maximum_instance_count: The maximum scaling factor.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package. This will be None if
            there is no explicit limit.
        """
        self.id = id
        self.description = description
        self.instance_count = instance_count
        self.minimum_instance_count = minimum_instance_count
        self.maximum_instance_count = maximum_instance_count
        VapiStruct.__init__(self)

ScaleOutGroup._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.scale_out_group', {
        'id': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'instance_count': type.OptionalType(type.IntegerType()),
        'minimum_instance_count': type.OptionalType(type.IntegerType()),
        'maximum_instance_count': type.OptionalType(type.IntegerType()),
    },
    ScaleOutGroup,
    False,
    None))



class ScaleOutParams(VapiStruct):
    """
    The ``ScaleOutParams`` class contains information about the scale-out
    groups described in the OVF package. 
    
    When deploying an OVF package, a deployment specific instance count can be
    specified (see :attr:`ScaleOutGroup.instance_count`. 
    
     This is based on the ovf2:ScaleOutSection. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 groups=None,
                 type=None,
                ):
        """
        :type  groups: :class:`list` of :class:`ScaleOutGroup`
        :param groups: The :class:`list` of scale-out groups.
            This attribute is optional in the input parameters when deploying
            an OVF package. If None there are no scale-out groups. This
            attribute will always be present in the result when retrieving
            information about an OVF package.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.groups = groups
        self.type = type
        VapiStruct.__init__(self)

ScaleOutParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.scale_out_params', {
        'groups': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ScaleOutGroup'))),
        'type': type.OptionalType(type.StringType()),
    },
    ScaleOutParams,
    False,
    None))



class SizeParams(VapiStruct):
    """
    The ``SizeParams`` class contains estimates of the download and deployment
    sizes. 
    
    This information is based on the file references and the ovf:DiskSection in
    the OVF descriptor. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 approximate_download_size=None,
                 approximate_flat_deployment_size=None,
                 approximate_sparse_deployment_size=None,
                 variable_disk_size=None,
                 type=None,
                ):
        """
        :type  approximate_download_size: :class:`long`
        :param approximate_download_size: A best guess as to the total amount of data that must be
            transferred to download the OVF package. 
            
             This may be inaccurate due to disk compression etc.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package. It will be None if
            there is insufficient information to provide a proper estimate.
        :type  approximate_flat_deployment_size: :class:`long`
        :param approximate_flat_deployment_size: A best guess as to the total amount of space required to deploy the
            OVF package if using flat disks.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package. It will be None if
            there is insufficient information to provide a proper estimate.
        :type  approximate_sparse_deployment_size: :class:`long`
        :param approximate_sparse_deployment_size: A best guess as to the total amount of space required to deploy the
            OVF package using sparse disks.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package. It will be None if
            there is insufficient information to provide a proper estimate.
        :type  variable_disk_size: :class:`bool`
        :param variable_disk_size: Whether the OVF uses variable disk sizes. 
            
            For empty disks, rather than specifying a fixed virtual disk
            capacity, the capacity may be given using a reference to a
            ovf:Property element in a ovf:ProductSection element in OVF
            package.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute is optional in the result when
            retrieving information about an OVF package. If None or false, the
            OVF does not use variable disk sizes.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.approximate_download_size = approximate_download_size
        self.approximate_flat_deployment_size = approximate_flat_deployment_size
        self.approximate_sparse_deployment_size = approximate_sparse_deployment_size
        self.variable_disk_size = variable_disk_size
        self.type = type
        VapiStruct.__init__(self)

SizeParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.size_params', {
        'approximate_download_size': type.OptionalType(type.IntegerType()),
        'approximate_flat_deployment_size': type.OptionalType(type.IntegerType()),
        'approximate_sparse_deployment_size': type.OptionalType(type.IntegerType()),
        'variable_disk_size': type.OptionalType(type.BooleanType()),
        'type': type.OptionalType(type.StringType()),
    },
    SizeParams,
    False,
    None))



class UnknownSection(VapiStruct):
    """
    The ``UnknownSection`` class contains information about an unknown section
    in an OVF package.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 tag=None,
                 info=None,
                ):
        """
        :type  tag: :class:`str`
        :param tag: A namespace-qualified tag in the form ``{ns}tag``.
        :type  info: :class:`str`
        :param info: The description of the Info element.
        """
        self.tag = tag
        self.info = info
        VapiStruct.__init__(self)

UnknownSection._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.unknown_section', {
        'tag': type.StringType(),
        'info': type.StringType(),
    },
    UnknownSection,
    False,
    None))



class UnknownSectionParams(VapiStruct):
    """
    The ``UnknownSectionParams`` class contains a :class:`list` of unknown,
    non-required sections. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 unknown_sections=None,
                 type=None,
                ):
        """
        :type  unknown_sections: :class:`list` of :class:`UnknownSection`
        :param unknown_sections: :class:`list` of unknown, non-required sections.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.unknown_sections = unknown_sections
        self.type = type
        VapiStruct.__init__(self)

UnknownSectionParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.unknown_section_params', {
        'unknown_sections': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'UnknownSection'))),
        'type': type.OptionalType(type.StringType()),
    },
    UnknownSectionParams,
    False,
    None))



class VcenterExtensionParams(VapiStruct):
    """
    The ``VcenterExtensionParams`` class specifies that the OVF package should
    be registered as a vCenter extension. The virtual machine or virtual
    appliance will gain unrestricted access to the vCenter Server APIs. It must
    be connected to a network with connectivity to the vCenter server. 
    
     See :func:`LibraryItem.deploy` and :func:`LibraryItem.filter`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 required=None,
                 registration_accepted=None,
                 type=None,
                ):
        """
        :type  required: :class:`bool`
        :param required: Whether registration as a vCenter extension is required.
            This attribute is not used in the input parameters when deploying
            an OVF package. This attribute will always be present in the result
            when retrieving information about an OVF package.
        :type  registration_accepted: :class:`bool`
        :param registration_accepted: Whether registration as a vCenter extension is accepted. 
            
            If registration as a vCenter extension is required (see
            :attr:`VcenterExtensionParams.required`), this must be set to true
            during deployment. Defaults to false when returned from server.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        :type  type: :class:`str`
        :param type: Unique identifier describing the type of the OVF parameters. The
            value is the name of the OVF parameters class.
            This attribute must be provided in the input parameters when
            deploying an OVF package. This attribute will always be present in
            the result when retrieving information about an OVF package.
        """
        self.required = required
        self.registration_accepted = registration_accepted
        self.type = type
        VapiStruct.__init__(self)

VcenterExtensionParams._set_binding_type(type.StructType(
    'com.vmware.vcenter.ovf.vcenter_extension_params', {
        'required': type.OptionalType(type.BooleanType()),
        'registration_accepted': type.OptionalType(type.BooleanType()),
        'type': type.OptionalType(type.StringType()),
    },
    VcenterExtensionParams,
    False,
    None))



class ExportFlag(VapiInterface):
    """
    The ``ExportFlag`` class provides methods for retrieving information about
    the export flags supported by the server. Export flags can be specified in
    a :class:`LibraryItem.CreateSpec` to customize an OVF export.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ExportFlagStub)

    class Info(VapiStruct):
        """
        The ``ExportFlag.Info`` class describes an export flag supported by the
        server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     option=None,
                     description=None,
                    ):
            """
            :type  option: :class:`str`
            :param option: The name of the export flag that is supported by the server.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Localizable description of the export flag.
            """
            self.option = option
            self.description = description
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.export_flag.info', {
            'option': type.StringType(),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        },
        Info,
        False,
        None))



    def list(self):
        """
        Returns information about the supported export flags by the server. 
        
         The supported flags are: 
        
        PRESERVE_MAC
            Include MAC addresses for network adapters.
        EXTRA_CONFIG
            Include extra configuration in OVF export.
         
        
         Future server versions might support additional flags.


        :rtype: :class:`list` of :class:`ExportFlag.Info`
        :return: A :class:`list` of supported export flags.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('list', None)
class ImportFlag(VapiInterface):
    """
    The ``ImportFlag`` class provides methods for retrieving information about
    the import flags supported by the deployment platform. Import flags can be
    specified in a :class:`LibraryItem.ResourcePoolDeploymentSpec` to customize
    an OVF deployment.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ImportFlagStub)

    class Info(VapiStruct):
        """
        The ``ImportFlag.Info`` class describes an import flag supported by the
        deployment platform.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     option=None,
                     description=None,
                    ):
            """
            :type  option: :class:`str`
            :param option: The name of the import flag that is supported by the deployment
                platform.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Localizable description of the import flag.
            """
            self.option = option
            self.description = description
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.import_flag.info', {
            'option': type.StringType(),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        },
        Info,
        False,
        None))



    def list(self,
             rp,
             ):
        """
        Returns information about the import flags supported by the deployment
        platform. 
        
         The supported flags are: 
        
        LAX
            Lax mode parsing of the OVF descriptor.
         
        
         Future server versions might support additional flags.

        :type  rp: :class:`str`
        :param rp: The identifier of resource pool target for retrieving the import
            flag(s).
            The parameter must be an identifier for the resource type:
            ``ResourcePool``.
        :rtype: :class:`list` of :class:`ImportFlag.Info`
        :return: A :class:`list` of supported import flags.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             If the resource pool associated with ``rp`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``ResourcePool`` referenced by the parameter ``rp``
              requires ``System.Read``.
        """
        return self._invoke('list',
                            {
                            'rp': rp,
                            })
class LibraryItem(VapiInterface):
    """
    The ``LibraryItem`` class provides methods to deploy virtual machines and
    virtual appliances from library items containing Open Virtualization Format
    (OVF) packages in content library, as well as methods to create library
    items in content library from virtual machines and virtual appliances. 
    
     To deploy a virtual machine or a virtual appliance from a library item: 
    
    #. Create a :class:`LibraryItem.DeploymentTarget` to specify the target
       deployment type and target deployment designation.
    #. Create a :class:`LibraryItem.ResourcePoolDeploymentSpec` to specify the
       parameters for the target deployment.
    #. Use the ``deploy`` method with the created target and parameter
       specifications, along with the identifier of the specified source content
       library item. See :func:`LibraryItem.deploy`.
    
     
    
     
    
    To create a library item in content library from a virtual machine or
    virtual appliance: 
    
    #. Create a :class:`LibraryItem.DeployableIdentity` to specify the source
       virtual machine or virtual appliance to be used as the OVF template source.
    #. Create a :class:`LibraryItem.CreateTarget` to specify the target library
       and library item.
    #. Create a :class:`LibraryItem.CreateSpec` to specify the settings for the
       OVF package to be created.
    #. Use the ``create`` method with the created target and parameter
       specifications, along with the specified source entity. See
       :func:`LibraryItem.create`.
    
     
    """
    DEPLOYABLE = ["VirtualMachine", "VirtualApp"]
    """
    The types of resources that can be created by deploying an OVF package and can
    be captured to create a library item using the ``LibraryItem`` class.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LibraryItemStub)

    class DeployableIdentity(VapiStruct):
        """
        The ``LibraryItem.DeployableIdentity`` class describes the resource created
        by a deployment, or the source resource from which library item can be
        created, by specifying its resource type and resource identifier.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                     id=None,
                    ):
            """
            :type  type: :class:`str`
            :param type: Type of the deployable resource.
                When clients pass a value of this class as a parameter, the
                attribute must be one of ``VirtualMachine`` or ``VirtualApp``. When
                methods return a value of this class as a return value, the
                attribute will be one of ``VirtualMachine`` or ``VirtualApp``.
            :type  id: :class:`str`
            :param id: Identifier of the deployable resource.
                When clients pass a value of this class as a parameter, the
                attribute ``type`` must contain the actual resource type. When
                methods return a value of this class as a return value, the
                attribute ``type`` will contain the actual resource type.
            """
            self.type = type
            self.id = id
            VapiStruct.__init__(self)

    DeployableIdentity._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.deployable_identity', {
            'type': type.StringType(),
            'id': type.IdType(resource_types=[], resource_type_field_name="type"),
        },
        DeployableIdentity,
        False,
        None))


    class ResourcePoolDeploymentSpec(VapiStruct):
        """
        The ``LibraryItem.ResourcePoolDeploymentSpec`` class defines the deployment
        parameters that can be specified for the ``deploy`` method where the
        deployment target is a resource pool. See :func:`LibraryItem.deploy`.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'accept_all_EULA': 'accept_all_eula',
                                }

        def __init__(self,
                     name=None,
                     annotation=None,
                     accept_all_eula=None,
                     network_mappings=None,
                     storage_mappings=None,
                     storage_provisioning=None,
                     storage_profile_id=None,
                     locale=None,
                     flags=None,
                     additional_parameters=None,
                     default_datastore_id=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: Name assigned to the deployed target virtual machine or virtual
                appliance.
                If None, the server will use the name from the OVF package.
            :type  annotation: :class:`str` or ``None``
            :param annotation: Annotation assigned to the deployed target virtual machine or
                virtual appliance.
                If None, the server will use the annotation from the OVF package.
            :type  accept_all_eula: :class:`bool`
            :param accept_all_eula: Whether to accept all End User License Agreements. See
                :attr:`LibraryItem.OvfSummary.eulas`.
            :type  network_mappings: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
            :param network_mappings: Specification of the target network to use for sections of type
                ovf:NetworkSection in the OVF descriptor. The key in the
                :class:`dict` is the section identifier of the ovf:NetworkSection
                section in the OVF descriptor and the value is the target network
                to be used for deployment.
                When clients pass a value of this class as a parameter, the value
                in the attribute :class:`dict` must be an identifier for the
                resource type: ``Network``. When methods return a value of this
                class as a return value, the value in the attribute :class:`dict`
                will be an identifier for the resource type: ``Network``.
                If None, the server will choose a network mapping.
            :type  storage_mappings: (:class:`dict` of :class:`str` and :class:`LibraryItem.StorageGroupMapping`) or ``None``
            :param storage_mappings: Specification of the target storage to use for sections of type
                vmw:StorageGroupSection in the OVF descriptor. The key in the
                :class:`dict` is the section identifier of the
                ovf:StorageGroupSection section in the OVF descriptor and the value
                is the target storage specification to be used for deployment. See
                :class:`LibraryItem.StorageGroupMapping`.
                If None, the server will choose a storage mapping.
            :type  storage_provisioning: :class:`DiskProvisioningType` or ``None``
            :param storage_provisioning: Default storage provisioning type to use for all sections of type
                vmw:StorageSection in the OVF descriptor.
                If None, the server will choose the provisioning type.
            :type  storage_profile_id: :class:`str` or ``None``
            :param storage_profile_id: Default storage profile to use for all sections of type
                vmw:StorageSection in the OVF descriptor.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``StorageProfile``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``StorageProfile``.
                If None, the server will choose the default profile.
            :type  locale: :class:`str` or ``None``
            :param locale: The locale to use for parsing the OVF descriptor.
                If None, the server locale will be used.
            :type  flags: :class:`list` of :class:`str` or ``None``
            :param flags: Flags to be use for deployment. The supported flag values can be
                obtained using :func:`ImportFlag.list`.
                If None, no flags will be used.
            :type  additional_parameters: :class:`list` of :class:`vmware.vapi.struct.VapiStruct` or ``None``
            :param additional_parameters: Additional OVF parameters that may be needed for the deployment.
                Additional OVF parameters may be required by the OVF descriptor of
                the OVF package in the library item. Examples of OVF parameters
                that can be specified through this attribute include, but are not
                limited to: 
                
                * :class:`DeploymentOptionParams`
                * :class:`ExtraConfigParams`
                * :class:`IpAllocationParams`
                * :class:`PropertyParams`
                * :class:`ScaleOutParams`
                * :class:`VcenterExtensionParams`
                When clients pass a value of this class as a parameter, the
                attribute must contain all the attributes defined in
                :class:`OvfParams`. When methods return a value of this class as a
                return value, the attribute will contain all the attributes defined
                in :class:`OvfParams`.
                If None, the server will choose default settings for all parameters
                necessary for the ``deploy`` method. See
                :func:`LibraryItem.deploy`.
            :type  default_datastore_id: :class:`str` or ``None``
            :param default_datastore_id: Default datastore to use for all sections of type
                vmw:StorageSection in the OVF descriptor.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
                If None, the server will choose the default datastore.
            """
            self.name = name
            self.annotation = annotation
            self.accept_all_eula = accept_all_eula
            self.network_mappings = network_mappings
            self.storage_mappings = storage_mappings
            self.storage_provisioning = storage_provisioning
            self.storage_profile_id = storage_profile_id
            self.locale = locale
            self.flags = flags
            self.additional_parameters = additional_parameters
            self.default_datastore_id = default_datastore_id
            VapiStruct.__init__(self)

    ResourcePoolDeploymentSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.resource_pool_deployment_spec', {
            'name': type.OptionalType(type.StringType()),
            'annotation': type.OptionalType(type.StringType()),
            'accept_all_EULA': type.BooleanType(),
            'network_mappings': type.OptionalType(type.MapType(type.StringType(), type.IdType())),
            'storage_mappings': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'LibraryItem.StorageGroupMapping'))),
            'storage_provisioning': type.OptionalType(type.ReferenceType(__name__, 'DiskProvisioningType')),
            'storage_profile_id': type.OptionalType(type.IdType()),
            'locale': type.OptionalType(type.StringType()),
            'flags': type.OptionalType(type.ListType(type.StringType())),
            'additional_parameters': type.OptionalType(type.ListType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType(__name__, 'OvfParams')]))),
            'default_datastore_id': type.OptionalType(type.IdType()),
        },
        ResourcePoolDeploymentSpec,
        False,
        None))


    class StorageGroupMapping(VapiStruct):
        """
        The ``LibraryItem.StorageGroupMapping`` class defines the storage
        deployment target and storage provisioning type for a section of type
        vmw:StorageGroupSection in the OVF descriptor.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'DATASTORE' : [('datastore_id', True)],
                    'STORAGE_PROFILE' : [('storage_profile_id', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     datastore_id=None,
                     storage_profile_id=None,
                     provisioning=None,
                    ):
            """
            :type  type: :class:`LibraryItem.StorageGroupMapping.Type`
            :param type: Type of storage deployment target to use for the
                vmw:StorageGroupSection section. The specified value must be
                :attr:`LibraryItem.StorageGroupMapping.Type.DATASTORE` or
                :attr:`LibraryItem.StorageGroupMapping.Type.STORAGE_PROFILE`.
            :type  datastore_id: :class:`str`
            :param datastore_id: Target datastore to be used for the storage group.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`LibraryItem.StorageGroupMapping.Type.DATASTORE`.
            :type  storage_profile_id: :class:`str`
            :param storage_profile_id: Target storage profile to be used for the storage group.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``StorageProfile``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``StorageProfile``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`LibraryItem.StorageGroupMapping.Type.STORAGE_PROFILE`.
            :type  provisioning: :class:`DiskProvisioningType` or ``None``
            :param provisioning: Target provisioning type to use for the storage group.
                If None,
                :attr:`LibraryItem.ResourcePoolDeploymentSpec.storage_provisioning`
                will be used.
            """
            self.type = type
            self.datastore_id = datastore_id
            self.storage_profile_id = storage_profile_id
            self.provisioning = provisioning
            VapiStruct.__init__(self)

        class Type(Enum):
            """
            The ``LibraryItem.StorageGroupMapping.Type`` class defines the supported
            types of storage targets for sections of type vmw:StorageGroupSection in
            the OVF descriptor.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            DATASTORE = None
            """
            Storage deployment target is a datastore.

            """
            STORAGE_PROFILE = None
            """
            Storage deployment target is a storage profile.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Type` instance.
                """
                Enum.__init__(string)

        Type._set_values([
            Type('DATASTORE'),
            Type('STORAGE_PROFILE'),
        ])
        Type._set_binding_type(type.EnumType(
            'com.vmware.vcenter.ovf.library_item.storage_group_mapping.type',
            Type))

    StorageGroupMapping._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.storage_group_mapping', {
            'type': type.ReferenceType(__name__, 'LibraryItem.StorageGroupMapping.Type'),
            'datastore_id': type.OptionalType(type.IdType()),
            'storage_profile_id': type.OptionalType(type.IdType()),
            'provisioning': type.OptionalType(type.ReferenceType(__name__, 'DiskProvisioningType')),
        },
        StorageGroupMapping,
        False,
        None))


    class ResultInfo(VapiStruct):
        """
        The ``LibraryItem.ResultInfo`` class defines the information returned along
        with the result of a ``create`` or ``deploy`` method to describe errors,
        warnings, and informational messages produced by the server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     errors=None,
                     warnings=None,
                     information=None,
                    ):
            """
            :type  errors: :class:`list` of :class:`OvfError`
            :param errors: Errors reported by the ``create`` or ``deploy`` method. These
                errors would have prevented the ``create`` or ``deploy`` method
                from completing successfully.
            :type  warnings: :class:`list` of :class:`OvfWarning`
            :param warnings: Warnings reported by the ``create`` or ``deploy`` method. These
                warnings would not have prevented the ``create`` or ``deploy``
                method from completing successfully, but there might be issues that
                warrant attention.
            :type  information: :class:`list` of :class:`OvfInfo`
            :param information: Information messages reported by the ``create`` or ``deploy``
                method. For example, a non-required parameter was ignored.
            """
            self.errors = errors
            self.warnings = warnings
            self.information = information
            VapiStruct.__init__(self)

    ResultInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.result_info', {
            'errors': type.ListType(type.ReferenceType(__name__, 'OvfError')),
            'warnings': type.ListType(type.ReferenceType(__name__, 'OvfWarning')),
            'information': type.ListType(type.ReferenceType(__name__, 'OvfInfo')),
        },
        ResultInfo,
        False,
        None))


    class DeploymentResult(VapiStruct):
        """
        The ``LibraryItem.DeploymentResult`` class defines the result of the
        ``deploy`` method. See :func:`LibraryItem.deploy`.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     succeeded=None,
                     resource_id=None,
                     error=None,
                    ):
            """
            :type  succeeded: :class:`bool`
            :param succeeded: Whether the ``deploy`` method completed successfully.
            :type  resource_id: :class:`LibraryItem.DeployableIdentity` or ``None``
            :param resource_id: Identifier of the deployed resource entity.
                If None, the ``deploy`` method failed and
                :attr:`LibraryItem.DeploymentResult.error` will describe the
                error(s) that caused the failure.
            :type  error: :class:`LibraryItem.ResultInfo` or ``None``
            :param error: Errors, warnings, and informational messages produced by the
                ``deploy`` method.
                If None, no errors, warnings, or informational messages were
                reported by the ``deploy`` method.
            """
            self.succeeded = succeeded
            self.resource_id = resource_id
            self.error = error
            VapiStruct.__init__(self)

    DeploymentResult._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.deployment_result', {
            'succeeded': type.BooleanType(),
            'resource_id': type.OptionalType(type.ReferenceType(__name__, 'LibraryItem.DeployableIdentity')),
            'error': type.OptionalType(type.ReferenceType(__name__, 'LibraryItem.ResultInfo')),
        },
        DeploymentResult,
        False,
        None))


    class DeploymentTarget(VapiStruct):
        """
        The ``LibraryItem.DeploymentTarget`` class describes the location (target)
        where a virtual machine or virtual appliance should be deployed. It is used
        in the ``deploy`` and ``filter`` methods. See :func:`LibraryItem.deploy`
        and :func:`LibraryItem.filter`.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     resource_pool_id=None,
                     host_id=None,
                     folder_id=None,
                    ):
            """
            :type  resource_pool_id: :class:`str`
            :param resource_pool_id: Identifier of the resource pool to which the virtual machine or
                virtual appliance should be attached.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``ResourcePool``.
            :type  host_id: :class:`str` or ``None``
            :param host_id: Identifier of the target host on which the virtual machine or
                virtual appliance will run. The target host must be a member of the
                cluster that contains the resource pool identified by
                :attr:`LibraryItem.DeploymentTarget.resource_pool_id`.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
                If None, the server will automatically select a target host from
                the resource pool if
                :attr:`LibraryItem.DeploymentTarget.resource_pool_id` is a
                stand-alone host or a cluster with Distributed Resource Scheduling
                (DRS) enabled.
            :type  folder_id: :class:`str` or ``None``
            :param folder_id: Identifier of the vCenter folder that should contain the virtual
                machine or virtual appliance. The folder must be virtual machine
                folder.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
                If None, the server will choose the deployment folder.
            """
            self.resource_pool_id = resource_pool_id
            self.host_id = host_id
            self.folder_id = folder_id
            VapiStruct.__init__(self)

    DeploymentTarget._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.deployment_target', {
            'resource_pool_id': type.IdType(resource_types='ResourcePool'),
            'host_id': type.OptionalType(type.IdType()),
            'folder_id': type.OptionalType(type.IdType()),
        },
        DeploymentTarget,
        False,
        None))


    class OvfSummary(VapiStruct):
        """
        The ``LibraryItem.OvfSummary`` class defines the result of the ``filter``
        method. See :func:`LibraryItem.filter`. The attributes in the class
        describe parameterizable information in the OVF descriptor, with respect to
        a deployment target, for the ``deploy`` method. See
        :func:`LibraryItem.deploy`.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'EULAs': 'eulas',
                                }

        def __init__(self,
                     name=None,
                     annotation=None,
                     eulas=None,
                     networks=None,
                     storage_groups=None,
                     additional_params=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: Default name for the virtual machine or virtual appliance.
                If None, the OVF descriptor did not specify a name.
            :type  annotation: :class:`str` or ``None``
            :param annotation: Default annotation for the virtual machine or virtual appliance.
                If None, the OVF descriptor did not specify an annotation.
            :type  eulas: :class:`list` of :class:`str`
            :param eulas: End User License Agreements specified in the OVF descriptor. All
                end user license agreements must be accepted in order for the
                ``deploy`` method to succeed. See
                :attr:`LibraryItem.ResourcePoolDeploymentSpec.accept_all_eula`.
            :type  networks: :class:`list` of :class:`str` or ``None``
            :param networks: Section identifiers for sections of type ovf:NetworkSection in the
                OVF descriptor. These identifiers can be used as keys in
                :attr:`LibraryItem.ResourcePoolDeploymentSpec.network_mappings`.
                If None, the OVF descriptor did not specify any networks.
            :type  storage_groups: :class:`list` of :class:`str` or ``None``
            :param storage_groups: Section identifiers for sections of type vmw:StorageGroupSection in
                the OVF descriptor. These identifiers can be used as keys in
                :attr:`LibraryItem.ResourcePoolDeploymentSpec.storage_mappings`.
                If None, the OVF descriptor did not specify any storage groups.
            :type  additional_params: :class:`list` of :class:`vmware.vapi.struct.VapiStruct` or ``None``
            :param additional_params: Additional OVF parameters which can be specified for the deployment
                target. These OVF parameters can be inspected, optionally modified,
                and used as values in
                :attr:`LibraryItem.ResourcePoolDeploymentSpec.additional_parameters`
                for the ``deploy`` method.
                When clients pass a value of this class as a parameter, the
                attribute must contain all the attributes defined in
                :class:`OvfParams`. When methods return a value of this class as a
                return value, the attribute will contain all the attributes defined
                in :class:`OvfParams`.
                If None, the OVF descriptor does not require addtional parameters
                or does not have additional parameters suitable for the deployment
                target.
            """
            self.name = name
            self.annotation = annotation
            self.eulas = eulas
            self.networks = networks
            self.storage_groups = storage_groups
            self.additional_params = additional_params
            VapiStruct.__init__(self)

    OvfSummary._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.ovf_summary', {
            'name': type.OptionalType(type.StringType()),
            'annotation': type.OptionalType(type.StringType()),
            'EULAs': type.ListType(type.StringType()),
            'networks': type.OptionalType(type.ListType(type.StringType())),
            'storage_groups': type.OptionalType(type.ListType(type.StringType())),
            'additional_params': type.OptionalType(type.ListType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType(__name__, 'OvfParams')]))),
        },
        OvfSummary,
        False,
        None))


    class CreateTarget(VapiStruct):
        """
        The ``LibraryItem.CreateTarget`` class specifies the target library item
        when capturing a virtual machine or virtual appliance as an OVF package in
        a library item in a content library. The target can be an existing library
        item, which will be updated, creating a new version, or it can be a newly
        created library item in a specified library. See
        :func:`LibraryItem.create`.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     library_id=None,
                     library_item_id=None,
                    ):
            """
            :type  library_id: :class:`str` or ``None``
            :param library_id: Identifier of the library in which a new library item should be
                created. This attribute is not used if the ``libraryItemId``
                attribute is specified.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.Library``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.content.Library``.
                If None, the ``libraryItemId`` attribute must be specified.
            :type  library_item_id: :class:`str` or ``None``
            :param library_item_id: Identifier of the library item that should be should be updated.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.library.Item``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.content.library.Item``.
                If None, a new library item will be created. The ``libraryId``
                attribute must be specified if this attribute is None.
            """
            self.library_id = library_id
            self.library_item_id = library_item_id
            VapiStruct.__init__(self)

    CreateTarget._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.create_target', {
            'library_id': type.OptionalType(type.IdType()),
            'library_item_id': type.OptionalType(type.IdType()),
        },
        CreateTarget,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``LibraryItem.CreateSpec`` class defines the information used to create
        or update a library item containing an OVF package.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     description=None,
                     flags=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: Name to use in the OVF descriptor stored in the library item.
                If None, the server will use source's current name.
            :type  description: :class:`str` or ``None``
            :param description: Description to use in the OVF descriptor stored in the library
                item.
                If None, the server will use source's current annotation.
            :type  flags: :class:`list` of :class:`str` or ``None``
            :param flags: Flags to use for OVF package creation. The supported flags can be
                obtained using :func:`ExportFlag.list`.
                If None, no flags will be used.
            """
            self.name = name
            self.description = description
            self.flags = flags
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.create_spec', {
            'name': type.OptionalType(type.StringType()),
            'description': type.OptionalType(type.StringType()),
            'flags': type.OptionalType(type.ListType(type.StringType())),
        },
        CreateSpec,
        False,
        None))


    class CreateResult(VapiStruct):
        """
        The ``LibraryItem.CreateResult`` class defines the result of the ``create``
        method. See :func:`LibraryItem.create`.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     succeeded=None,
                     ovf_library_item_id=None,
                     error=None,
                    ):
            """
            :type  succeeded: :class:`bool`
            :param succeeded: Whether the ``create`` method completed successfully.
            :type  ovf_library_item_id: :class:`str` or ``None``
            :param ovf_library_item_id: Identifier of the created or updated library item.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.library.Item``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.content.library.Item``.
                If None, the ``create`` method failed and
                :attr:`LibraryItem.CreateResult.error` will describe the error(s)
                that caused the failure.
            :type  error: :class:`LibraryItem.ResultInfo` or ``None``
            :param error: Errors, warnings, and informational messages produced by the
                ``create`` method.
                If None, no errors, warnings, or informational messages were
                reported by the ``create`` method.
            """
            self.succeeded = succeeded
            self.ovf_library_item_id = ovf_library_item_id
            self.error = error
            VapiStruct.__init__(self)

    CreateResult._set_binding_type(type.StructType(
        'com.vmware.vcenter.ovf.library_item.create_result', {
            'succeeded': type.BooleanType(),
            'ovf_library_item_id': type.OptionalType(type.IdType()),
            'error': type.OptionalType(type.ReferenceType(__name__, 'LibraryItem.ResultInfo')),
        },
        CreateResult,
        False,
        None))



    def deploy(self,
               ovf_library_item_id,
               target,
               deployment_spec,
               client_token=None,
               ):
        """
        Deploys an OVF package stored in content library to a newly created
        virtual machine or virtual appliance. 
        
        This method deploys an OVF package which is stored in the library item
        specified by ``ovf_library_item_id``. It uses the deployment
        specification in ``deployment_spec`` to deploy the OVF package to the
        location specified by ``target``. 

        :type  client_token: :class:`str` or ``None``
        :param client_token: Client-generated token used to retry a request if the client fails
            to get a response from the server. If the original request
            succeeded, the result of that request will be returned, otherwise
            the operation will be retried.
            If None, the server will create a token.
        :type  ovf_library_item_id: :class:`str`
        :param ovf_library_item_id: Identifier of the content library item containing the OVF package
            to be deployed.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  target: :class:`LibraryItem.DeploymentTarget`
        :param target:  Specification of the deployment target.
        :type  deployment_spec: :class:`LibraryItem.ResourcePoolDeploymentSpec`
        :param deployment_spec: Specification of how the OVF package should be deployed to the
            target.
        :rtype: :class:`LibraryItem.DeploymentResult`
        :return: Information about the success or failure of the method, along with
            the details of the result or failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if ``target`` contains invalid arguments.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if ``deployment_spec`` contains invalid arguments or has attributes
            that are inconsistent with ``target``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library item specified by ``ovf_library_item_id`` does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if any resource specified by a attribute of the
            :class:`LibraryItem.DeploymentTarget` class, specified by
            ``target``, does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if there was an error accessing the OVF package stored in the
            library item specified by ``ovf_library_item_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have all of the privileges described as follows : 
            
            * Method execution requires VirtualMachine.Config.AddNewDisk if the
              OVF descriptor has a disk drive (type 17) section.
            * Method execution requires VirtualMachine.Config.AdvancedConfig if
              the OVF descriptor has an ExtraConfig section.
            * Method execution requires Extension.Register for specified
              resource group if the OVF descriptor has a vServiceDependency
              section.
            * Method execution requires Network.Assign for target network if
              specified.
            * Method execution requires Datastore.AllocateSpace for target
              datastore if specified.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``ovf_library_item_id`` requires ``System.Read``.
            * The resource ``HostSystem`` referenced by the attribute
              :attr:`LibraryItem.DeploymentTarget.host_id` requires
              ``System.Read``.
            * The resource ``Network`` referenced by the :class:`dict` value of
              attribute
              :attr:`LibraryItem.ResourcePoolDeploymentSpec.network_mappings`
              requires ``System.Read``.
            * The resource ``StorageProfile`` referenced by the attribute
              :attr:`LibraryItem.ResourcePoolDeploymentSpec.storage_profile_id`
              requires ``System.Read``.
            * The resource ``Datastore`` referenced by the attribute
              :attr:`LibraryItem.ResourcePoolDeploymentSpec.default_datastore_id`
              requires ``System.Read``.
            * The resource ``ResourcePool`` referenced by the attribute
              :attr:`LibraryItem.DeploymentTarget.resource_pool_id` requires
              ``VApp.Import``.
            * The resource ``Folder`` referenced by the attribute
              :attr:`LibraryItem.DeploymentTarget.folder_id` requires
              ``VApp.Import``.
        """
        return self._invoke('deploy',
                            {
                            'client_token': client_token,
                            'ovf_library_item_id': ovf_library_item_id,
                            'target': target,
                            'deployment_spec': deployment_spec,
                            })

    def filter(self,
               ovf_library_item_id,
               target,
               ):
        """
        Queries an OVF package stored in content library to retrieve
        information to use when deploying the package. See
        :func:`LibraryItem.deploy`. 
        
        This method retrieves information from the descriptor of the OVF
        package stored in the library item specified by
        ``ovf_library_item_id``. The information returned by the method can be
        used to populate the deployment specification (see
        :class:`LibraryItem.ResourcePoolDeploymentSpec` when deploying the OVF
        package to the deployment target specified by ``target``. 

        :type  ovf_library_item_id: :class:`str`
        :param ovf_library_item_id: Identifier of the content library item containing the OVF package
            to query.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  target: :class:`LibraryItem.DeploymentTarget`
        :param target:  Specification of the deployment target.
        :rtype: :class:`LibraryItem.OvfSummary`
        :return: Information that can be used to populate the deployment
            specification (see :class:`LibraryItem.ResourcePoolDeploymentSpec`)
            when deploying the OVF package to the deployment target specified
            by ``target``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if ``target`` contains invalid arguments.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library item specified by ``ovf_library_item_id`` does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if any resource specified by a attribute of the
            :class:`LibraryItem.DeploymentTarget` class, specified by
            ``target``, does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if there was an error accessing the OVF package at the specified
            ``ovf_library_item_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``ovf_library_item_id`` requires ``System.Read``.
            * The resource ``ResourcePool`` referenced by the attribute
              :attr:`LibraryItem.DeploymentTarget.resource_pool_id` requires
              ``System.Read``.
            * The resource ``HostSystem`` referenced by the attribute
              :attr:`LibraryItem.DeploymentTarget.host_id` requires
              ``System.Read``.
            * The resource ``Folder`` referenced by the attribute
              :attr:`LibraryItem.DeploymentTarget.folder_id` requires
              ``System.Read``.
        """
        return self._invoke('filter',
                            {
                            'ovf_library_item_id': ovf_library_item_id,
                            'target': target,
                            })

    def create(self,
               source,
               target,
               create_spec,
               client_token=None,
               ):
        """
        Creates a library item in content library from a virtual machine or
        virtual appliance. 
        
        This method creates a library item in content library whose content is
        an OVF package derived from a source virtual machine or virtual
        appliance, using the supplied create specification. The OVF package may
        be stored as in a newly created library item or in an in an existing
        library item. For an existing library item whose content is updated by
        this method, the original content is overwritten. 

        :type  client_token: :class:`str` or ``None``
        :param client_token: Client-generated token used to retry a request if the client fails
            to get a response from the server. If the original request
            succeeded, the result of that request will be returned, otherwise
            the operation will be retried.
            If None, the server will create a token.
        :type  source: :class:`LibraryItem.DeployableIdentity`
        :param source: Identifier of the virtual machine or virtual appliance to use as
            the source.
        :type  target: :class:`LibraryItem.CreateTarget`
        :param target:  Specification of the target content library and library item.
        :type  create_spec: :class:`LibraryItem.CreateSpec`
        :param create_spec: Information used to create the OVF package from the source virtual
            machine or virtual appliance.
        :rtype: :class:`LibraryItem.CreateResult`
        :return: Information about the success or failure of the method, along with
            the details of the result or failure.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if ``create_spec`` contains invalid arguments.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if ``source`` describes an unexpected resource type.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual appliance specified by ``source``
            does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library or library item specified by ``target`` does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the operation cannot be performed because of the specified
            virtual machine or virtual appliance's current state. For example,
            if the virtual machine configuration information is not available,
            or if the virtual appliance is running.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if there was an error accessing a file from the source virtual
            machine or virtual appliance.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
             if the specified virtual machine or virtual appliance is busy.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The attribute :attr:`LibraryItem.DeployableIdentity.id` requires
              ``VApp.Export``.
            * The resource ``com.vmware.content.Library`` referenced by the
              attribute :attr:`LibraryItem.CreateTarget.library_id` requires
              ``ContentLibrary.AddLibraryItem``.
            * The resource ``com.vmware.content.library.Item`` referenced by
              the attribute :attr:`LibraryItem.CreateTarget.library_item_id`
              requires ``System.Read``.
        """
        return self._invoke('create',
                            {
                            'client_token': client_token,
                            'source': source,
                            'target': target,
                            'create_spec': create_spec,
                            })
class _ExportFlagStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'ExportFlag.Info')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.ovf.export_flag',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ImportFlagStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'rp': type.IdType(resource_types='ResourcePool'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'ImportFlag.Info')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.ovf.import_flag',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _LibraryItemStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for deploy operation
        deploy_input_type = type.StructType('operation-input', {
            'client_token': type.OptionalType(type.StringType()),
            'ovf_library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
            'target': type.ReferenceType(__name__, 'LibraryItem.DeploymentTarget'),
            'deployment_spec': type.ReferenceType(__name__, 'LibraryItem.ResourcePoolDeploymentSpec'),
        })
        deploy_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        deploy_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        deploy_output_validator_list = [
        ]
        deploy_rest_metadata = None

        # properties for filter operation
        filter_input_type = type.StructType('operation-input', {
            'ovf_library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
            'target': type.ReferenceType(__name__, 'LibraryItem.DeploymentTarget'),
        })
        filter_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),

        }
        filter_input_value_validator_list = [
        ]
        filter_output_validator_list = [
            HasFieldsOfValidator()
        ]
        filter_rest_metadata = None

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'client_token': type.OptionalType(type.StringType()),
            'source': type.ReferenceType(__name__, 'LibraryItem.DeployableIdentity'),
            'target': type.ReferenceType(__name__, 'LibraryItem.CreateTarget'),
            'create_spec': type.ReferenceType(__name__, 'LibraryItem.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        operations = {
            'deploy': {
                'input_type': deploy_input_type,
                'output_type': type.ReferenceType(__name__, 'LibraryItem.DeploymentResult'),
                'errors': deploy_error_dict,
                'input_value_validator_list': deploy_input_value_validator_list,
                'output_validator_list': deploy_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'filter': {
                'input_type': filter_input_type,
                'output_type': type.ReferenceType(__name__, 'LibraryItem.OvfSummary'),
                'errors': filter_error_dict,
                'input_value_validator_list': filter_input_value_validator_list,
                'output_validator_list': filter_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType(__name__, 'LibraryItem.CreateResult'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'deploy': deploy_rest_metadata,
            'filter': filter_rest_metadata,
            'create': create_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.ovf.library_item',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ExportFlag': ExportFlag,
        'ImportFlag': ImportFlag,
        'LibraryItem': LibraryItem,
    }

