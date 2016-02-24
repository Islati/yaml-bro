from collections import OrderedDict, Hashable
from yaml import MappingNode, ScalarNode
import yaml
from yaml.constructor import ConstructorError

__YAML_MAP_TAG = 'tag:yaml.org,2002:map'


def __construct_yaml_map_ordered(self, node, deep=False):
    if not isinstance(node, MappingNode):
        raise ConstructorError(None, None,
                               "expected a mapping node, but found %s" % node.id,
                               node.start_mark)
    mapping = OrderedDict()
    for key_node, value_node in node.value:
        key = self.construct_object(key_node, deep=deep)
        if not isinstance(key, Hashable):
            raise ConstructorError("while constructing a mapping", node.start_mark,
                                   "found unacceptable key (%s)" % key, key_node.start_mark)
        value = self.construct_object(value_node, deep=deep)
        mapping[key] = value
    return mapping


def __represent_yaml_map_ordered(self, mapping, flow_style=None):
    value = []
    node = MappingNode(__YAML_MAP_TAG, value, flow_style=flow_style)
    if self.alias_key is not None:
        self.represented_objects[self.alias_key] = node
    best_style = True
    if hasattr(mapping, 'items'):
        mapping = mapping.items()
    for item_key, item_value in mapping:
        node_key = self.represent_data(item_key)
        node_value = self.represent_data(item_value)
        if not (isinstance(node_key, ScalarNode) and not node_key.style):
            best_style = False
        if not (isinstance(node_value, ScalarNode) and not node_value.style):
            best_style = False
        value.append((node_key, node_value))
    if flow_style is None:
        if self.default_flow_style is not None:
            node.flow_style = self.default_flow_style
        else:
            node.flow_style = best_style
    return node


def __represent_none(self, data):
    """Represent a None value with nothing instead of 'none'.
    """
    return self.represent_scalar('tag:yaml.org,2002:null', '')


def install():
    # Add all the representers for data types
    yaml.add_constructor('tag:yaml.org,2002:map', __construct_yaml_map_ordered)
    yaml.add_constructor('tag:yaml.org,2002:omap', __construct_yaml_map_ordered)
    yaml.add_representer(OrderedDict, __represent_yaml_map_ordered)

    yaml.add_representer(type(None), __represent_none)

    yaml.SafeLoader.add_constructor('tag:yaml.org,2002:map', __construct_yaml_map_ordered)
    yaml.SafeLoader.add_constructor('tag:yaml.org,2002:omap', __construct_yaml_map_ordered)

    yaml.SafeDumper.add_representer(OrderedDict, __represent_yaml_map_ordered)
    yaml.SafeDumper.add_representer(type(None), __represent_none)

    # Add all the constructors for data types.

    # yaml.add_constructor('tag:yaml.org,2002:str', Loader._construct_unicode)

    # yaml.SafeLoader.add_constructor('tag:yaml.org,2002:str', Loader._construct_unicode)
