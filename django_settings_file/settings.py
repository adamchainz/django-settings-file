import os
from importlib.util import module_from_spec, spec_from_file_location

# Recipe for importing from path as documented in importlib
spec = spec_from_file_location(
    "django_settings_file.settings_real", os.environ["DJANGO_SETTINGS_FILE"]
)
module = module_from_spec(spec)
spec.loader.exec_module(module)

# Take all the attributes
globals().update(module.__dict__)
