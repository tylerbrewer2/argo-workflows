"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/v3.5.2/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from argo_workflows.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from argo_workflows.exceptions import ApiAttributeError


def lazy_import():
    from argo_workflows.model.io_argoproj_events_v1alpha1_argo_workflow_trigger import IoArgoprojEventsV1alpha1ArgoWorkflowTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_aws_lambda_trigger import IoArgoprojEventsV1alpha1AWSLambdaTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_azure_event_hubs_trigger import IoArgoprojEventsV1alpha1AzureEventHubsTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_conditions_reset_criteria import IoArgoprojEventsV1alpha1ConditionsResetCriteria
    from argo_workflows.model.io_argoproj_events_v1alpha1_custom_trigger import IoArgoprojEventsV1alpha1CustomTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_http_trigger import IoArgoprojEventsV1alpha1HTTPTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_kafka_trigger import IoArgoprojEventsV1alpha1KafkaTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_log_trigger import IoArgoprojEventsV1alpha1LogTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_nats_trigger import IoArgoprojEventsV1alpha1NATSTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_open_whisk_trigger import IoArgoprojEventsV1alpha1OpenWhiskTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_pulsar_trigger import IoArgoprojEventsV1alpha1PulsarTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_slack_trigger import IoArgoprojEventsV1alpha1SlackTrigger
    from argo_workflows.model.io_argoproj_events_v1alpha1_standard_k8_s_trigger import IoArgoprojEventsV1alpha1StandardK8STrigger
    globals()['IoArgoprojEventsV1alpha1AWSLambdaTrigger'] = IoArgoprojEventsV1alpha1AWSLambdaTrigger
    globals()['IoArgoprojEventsV1alpha1ArgoWorkflowTrigger'] = IoArgoprojEventsV1alpha1ArgoWorkflowTrigger
    globals()['IoArgoprojEventsV1alpha1AzureEventHubsTrigger'] = IoArgoprojEventsV1alpha1AzureEventHubsTrigger
    globals()['IoArgoprojEventsV1alpha1ConditionsResetCriteria'] = IoArgoprojEventsV1alpha1ConditionsResetCriteria
    globals()['IoArgoprojEventsV1alpha1CustomTrigger'] = IoArgoprojEventsV1alpha1CustomTrigger
    globals()['IoArgoprojEventsV1alpha1HTTPTrigger'] = IoArgoprojEventsV1alpha1HTTPTrigger
    globals()['IoArgoprojEventsV1alpha1KafkaTrigger'] = IoArgoprojEventsV1alpha1KafkaTrigger
    globals()['IoArgoprojEventsV1alpha1LogTrigger'] = IoArgoprojEventsV1alpha1LogTrigger
    globals()['IoArgoprojEventsV1alpha1NATSTrigger'] = IoArgoprojEventsV1alpha1NATSTrigger
    globals()['IoArgoprojEventsV1alpha1OpenWhiskTrigger'] = IoArgoprojEventsV1alpha1OpenWhiskTrigger
    globals()['IoArgoprojEventsV1alpha1PulsarTrigger'] = IoArgoprojEventsV1alpha1PulsarTrigger
    globals()['IoArgoprojEventsV1alpha1SlackTrigger'] = IoArgoprojEventsV1alpha1SlackTrigger
    globals()['IoArgoprojEventsV1alpha1StandardK8STrigger'] = IoArgoprojEventsV1alpha1StandardK8STrigger


class IoArgoprojEventsV1alpha1TriggerTemplate(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'argo_workflow': (IoArgoprojEventsV1alpha1ArgoWorkflowTrigger,),  # noqa: E501
            'aws_lambda': (IoArgoprojEventsV1alpha1AWSLambdaTrigger,),  # noqa: E501
            'azure_event_hubs': (IoArgoprojEventsV1alpha1AzureEventHubsTrigger,),  # noqa: E501
            'conditions': (str,),  # noqa: E501
            'conditions_reset': ([IoArgoprojEventsV1alpha1ConditionsResetCriteria],),  # noqa: E501
            'custom': (IoArgoprojEventsV1alpha1CustomTrigger,),  # noqa: E501
            'http': (IoArgoprojEventsV1alpha1HTTPTrigger,),  # noqa: E501
            'k8s': (IoArgoprojEventsV1alpha1StandardK8STrigger,),  # noqa: E501
            'kafka': (IoArgoprojEventsV1alpha1KafkaTrigger,),  # noqa: E501
            'log': (IoArgoprojEventsV1alpha1LogTrigger,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'nats': (IoArgoprojEventsV1alpha1NATSTrigger,),  # noqa: E501
            'open_whisk': (IoArgoprojEventsV1alpha1OpenWhiskTrigger,),  # noqa: E501
            'pulsar': (IoArgoprojEventsV1alpha1PulsarTrigger,),  # noqa: E501
            'slack': (IoArgoprojEventsV1alpha1SlackTrigger,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'argo_workflow': 'argoWorkflow',  # noqa: E501
        'aws_lambda': 'awsLambda',  # noqa: E501
        'azure_event_hubs': 'azureEventHubs',  # noqa: E501
        'conditions': 'conditions',  # noqa: E501
        'conditions_reset': 'conditionsReset',  # noqa: E501
        'custom': 'custom',  # noqa: E501
        'http': 'http',  # noqa: E501
        'k8s': 'k8s',  # noqa: E501
        'kafka': 'kafka',  # noqa: E501
        'log': 'log',  # noqa: E501
        'name': 'name',  # noqa: E501
        'nats': 'nats',  # noqa: E501
        'open_whisk': 'openWhisk',  # noqa: E501
        'pulsar': 'pulsar',  # noqa: E501
        'slack': 'slack',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IoArgoprojEventsV1alpha1TriggerTemplate - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            argo_workflow (IoArgoprojEventsV1alpha1ArgoWorkflowTrigger): [optional]  # noqa: E501
            aws_lambda (IoArgoprojEventsV1alpha1AWSLambdaTrigger): [optional]  # noqa: E501
            azure_event_hubs (IoArgoprojEventsV1alpha1AzureEventHubsTrigger): [optional]  # noqa: E501
            conditions (str): [optional]  # noqa: E501
            conditions_reset ([IoArgoprojEventsV1alpha1ConditionsResetCriteria]): [optional]  # noqa: E501
            custom (IoArgoprojEventsV1alpha1CustomTrigger): [optional]  # noqa: E501
            http (IoArgoprojEventsV1alpha1HTTPTrigger): [optional]  # noqa: E501
            k8s (IoArgoprojEventsV1alpha1StandardK8STrigger): [optional]  # noqa: E501
            kafka (IoArgoprojEventsV1alpha1KafkaTrigger): [optional]  # noqa: E501
            log (IoArgoprojEventsV1alpha1LogTrigger): [optional]  # noqa: E501
            name (str): Name is a unique name of the action to take.. [optional]  # noqa: E501
            nats (IoArgoprojEventsV1alpha1NATSTrigger): [optional]  # noqa: E501
            open_whisk (IoArgoprojEventsV1alpha1OpenWhiskTrigger): [optional]  # noqa: E501
            pulsar (IoArgoprojEventsV1alpha1PulsarTrigger): [optional]  # noqa: E501
            slack (IoArgoprojEventsV1alpha1SlackTrigger): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """IoArgoprojEventsV1alpha1TriggerTemplate - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            argo_workflow (IoArgoprojEventsV1alpha1ArgoWorkflowTrigger): [optional]  # noqa: E501
            aws_lambda (IoArgoprojEventsV1alpha1AWSLambdaTrigger): [optional]  # noqa: E501
            azure_event_hubs (IoArgoprojEventsV1alpha1AzureEventHubsTrigger): [optional]  # noqa: E501
            conditions (str): [optional]  # noqa: E501
            conditions_reset ([IoArgoprojEventsV1alpha1ConditionsResetCriteria]): [optional]  # noqa: E501
            custom (IoArgoprojEventsV1alpha1CustomTrigger): [optional]  # noqa: E501
            http (IoArgoprojEventsV1alpha1HTTPTrigger): [optional]  # noqa: E501
            k8s (IoArgoprojEventsV1alpha1StandardK8STrigger): [optional]  # noqa: E501
            kafka (IoArgoprojEventsV1alpha1KafkaTrigger): [optional]  # noqa: E501
            log (IoArgoprojEventsV1alpha1LogTrigger): [optional]  # noqa: E501
            name (str): Name is a unique name of the action to take.. [optional]  # noqa: E501
            nats (IoArgoprojEventsV1alpha1NATSTrigger): [optional]  # noqa: E501
            open_whisk (IoArgoprojEventsV1alpha1OpenWhiskTrigger): [optional]  # noqa: E501
            pulsar (IoArgoprojEventsV1alpha1PulsarTrigger): [optional]  # noqa: E501
            slack (IoArgoprojEventsV1alpha1SlackTrigger): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
