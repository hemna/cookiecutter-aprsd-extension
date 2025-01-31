{%- macro heading(text) -%} {{text}} {% for \_ in text %}={% endfor %}
{%- endmacro -%} {{ heading(cookiecutter.friendly_name) }}

[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.extension_name}}.svg)](https://pypi.org/project/{{cookiecutter.extension_name}}/)
[![Status](https://img.shields.io/pypi/status/{{cookiecutter.extension_name}}.svg)](https://pypi.org/project/{{cookiecutter.extension_name}}/)
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.extension_name}})](https://pypi.org/project/{{cookiecutter.extension_name}})
[![License](https://img.shields.io/pypi/l/{{cookiecutter.extension_name}})](https://opensource.org/licenses/{{cookiecutter.license}})

[![Read the documentation at https://{{cookiecutter.extension_name}}.readthedocs.io/](https://img.shields.io/readthedocs/{{cookiecutter.extension_name}}/latest.svg?label=Read%20the%20Docs)](https://{{cookiecutter.extension_name}}.readthedocs.io/)
[![Tests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.extension_name}}/workflows/Tests/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.extension_name}}/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.extension_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.extension_name}})

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

---

> [!WARNING]
> Legal operation of this software requires an amateur radio license and a valid call sign.

> [!NOTE]
> Star this repo to follow our progress! This code is under active development, and contributions are both welcomed and appreciated. See [CONTRIBUTING.md](<https://github.com/craigerl/aprsd/blob/master/CONTRIBUTING.md>) for details.

# Features

-   TODO

# Requirements

-   TODO

# Installation

You can install *{{cookiecutter.friendly_name}}* via
[pip](https://pip.pypa.io/) from [PyPI](https://pypi.org/):

``` console
$ pip install {{cookiecutter.extension_name}}
```

# Usage

Please see the [Command-line
Reference](https://{{cookiecutter.extension_name}}.readthedocs.io/en/latest/usage.html)
for details.

# Contributing

Contributions are very welcome. To learn more, see the [Contributor
Guide](CONTRIBUTING.rst).

# License

Distributed under the terms of the
[{{cookiecutter.license.replace(\"-\", \" \")}}
license](https://opensource.org/licenses/{{cookiecutter.license}}),
*{{cookiecutter.friendly_name}}* is free and open source software.

# Issues

If you encounter any problems, please [file an
issue](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.extension_name}}/issues)
along with a detailed description.

# Credits

This project was generated from [\@hemna](https://github.com/hemna)\'s
[APRSD Extension Python Cookiecutter]() template.
