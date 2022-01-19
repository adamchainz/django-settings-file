from __future__ import annotations

import os


class DjangoSettingsFileError(Exception):
    pass


def setup() -> None:
    if "DJANGO_SETTINGS_MODULE" in os.environ:
        raise DjangoSettingsFileError(
            "DJANGO_SETTINGS_MODULE should not be defined, only "
            + "DJANGO_SETTINGS_FILE is obeyed"
        )
    if "DJANGO_SETTINGS_FILE" not in os.environ:
        raise DjangoSettingsFileError("DJANGO_SETTINGS_FILE is not defined")
    os.environ["DJANGO_SETTINGS_MODULE"] = "django_settings_file.settings"
