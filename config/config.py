#! /usr/bin/python3.9
import os
import yaml

# default to DEV and current folder config_DEV.yml
env = os.getenv("APP_ENV", "DEV")
config_path = os.getenv("APP_CONFIG_PATH", f"{os.path.dirname(os.path.realpath(__file__))}")

with open(f"{config_path}/config_{env}.yml") as ymlfile:
    _config = yaml.safe_load(ymlfile)


def get(name, default=None):
    try:
        return _search_node(_config, name.split("."))
    except KeyError as e:
        if default:
            return default
        else:
            raise e


def _search_node(node, lst):
    nod = node[lst.pop(0)]
    return _search_node(nod, lst) if len(lst) > 0 else nod
