from oslo_config import cfg


extension_group = cfg.OptGroup(
    name="{{cookiecutter.module_name}}",
    title="APRSD {{cookiecutter.extension_short_name}} extension settings",
)

extension_opts = [
    cfg.BoolOpt(
        "enabled",
        default=True,
        help="Enable the extension?",
    ),
]

ALL_OPTS = extension_opts


def register_opts(cfg):
    cfg.register_group(extension_group)
    cfg.register_opts(ALL_OPTS, group=extension_group)


def list_opts():
    return {
        extension_group.name: extension_opts,
    }
