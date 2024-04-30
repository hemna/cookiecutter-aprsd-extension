#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import re
import sys
from rich.console import Console

cs = Console()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pre_gen_project")



def validate():
    PLUGIN_REGEX = r"^(?!pytest)[-_a-zA-Z][-_a-zA-Z0-9]+$"

    extension_name = "{{cookiecutter.extension_name}}"

    if not re.match(PLUGIN_REGEX, extension_name):
        logger.error(f'Invalid value for extension_name "{extension_name}"')
        logger.debug('Please do not prepend extension_name with "pytest"!')
        return 1

    MODULE_REGEX = r"^[a-z][_a-z0-9]+$"

    module_name = "{{cookiecutter.module_name}}"

    if not re.match(MODULE_REGEX, module_name):
        link = "https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
        logger.error("Module name should be pep-8 compliant.")
        logger.error("  More info: {}".format(link))
        return 1
    return 0


def main():
    result = validate()
    return result


if __name__ == "__main__":
    sys.exit(main())
    logger.info("Project generation complete!")