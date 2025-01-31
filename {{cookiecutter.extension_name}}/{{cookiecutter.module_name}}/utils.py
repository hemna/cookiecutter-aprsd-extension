import update_checker

import {{cookiecutter.module_name}}


def _check_version():
    # check for a newer version
    try:
        check = update_checker.UpdateChecker()
        result = check.check("{{cookiecutter.extension_name}}", {{cookiecutter.module_name}}.__version__)
        if result:
            # Looks like there is an updated version.
            return 1, result
        else:
            return 0, "APRSD {{cookiecutter.extension_group_name }} extension is up to date"
    except Exception:
        # probably can't get in touch with pypi for some reason
        # Lets put up an error and move on.  We might not
        # have internet in this aprsd deployment.
        return 1, "Couldn't check for new version of APRSD Extension ({{cookiecutter.extension_name}})"
