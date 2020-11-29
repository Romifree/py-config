#! /usr/bin/python3.9
import os
import sys
sys.path.append(f"{os.path.dirname(os.path.realpath(__file__))}/../config")
import config

print(config.get("keyVault.name"))
print(config.get("keyVault.uri"))
print(config.get("test.name"))
print(config.get("test.secLevel"))
print(config.get("test.secLevel.third"))
print(config.get("non.exist", "default"))
print(config.get("test.name", "not default"))
try:
    print(config.get("non-exist"))
except KeyError:
    pass
