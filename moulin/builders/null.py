# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 EPAM Systems
"""
Null build generator. Used mostly for testing
"""

from typing import List
from moulin.yaml_wrapper import YamlValue
from moulin import ninja_syntax


def get_builder(conf: YamlValue, name: str, build_dir: str, src_stamps: List[str],
                generator: ninja_syntax.Writer):
    """
    Return configured Null builder
    """
    return NullBuilder(conf, name, build_dir, src_stamps, generator)


def gen_build_rules(generator: ninja_syntax.Writer):
    """
    Generate yocto build rules for ninja
    """
    generator.newline()


class NullBuilder:
    """
    NullBuilder class generates no Ninja rules
    """
    def __init__(self, conf: YamlValue, name: str, build_dir: str, src_stamps: List[str],
                 generator: ninja_syntax.Writer):
        pass

    def gen_build(self):
        """Generate no Ninja rules"""

        return []

    def get_targets(self):
        "Return list of targets that are generated by this build"
        return []

    def capture_state(self):
        """
        This method should capture state for reproducible builds.
        """
