import os
import subprocess
import sys
from textwrap import dedent
from unittest import mock

import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(autouse=True)
def in_project_dir():
    project_dir = os.path.join(module_dir, "example_project")
    orig_dir = os.getcwd()
    os.chdir(project_dir)
    try:
        yield
    finally:
        os.chdir(orig_dir)


def patch_environment(**kwargs):
    return mock.patch.dict(os.environ, kwargs)


def call_example_command():
    proc = subprocess.Popen(
        [sys.executable, "manage.py", "example_command"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return proc.returncode, out.decode("utf-8"), err.decode("utf-8")


def test_project_working(tmpdir):
    test_py = tmpdir.join("test.py")
    test_py.write(
        dedent(
            """\
        from example_project.settings import *
        MY_EXAMPLE_SETTING = 'foobar'
    """
        )
    )

    with patch_environment(DJANGO_SETTINGS_FILE=str(test_py)):
        retcode, out, err = call_example_command()

        print(out)
        print(err)
    assert retcode == 0
    assert out == "foobar\n"


def test_project_fails_with_django_settings_module(tmpdir):
    with patch_environment(DJANGO_SETTINGS_MODULE="justfail"):
        retcode, out, err = call_example_command()

    assert retcode != 0
    assert (
        "DJANGO_SETTINGS_MODULE should not be defined, only "
        + "DJANGO_SETTINGS_FILE is obeyed"
    ) in err


def test_project_fails_no_django_settings_file(tmpdir):
    retcode, out, err = call_example_command()

    assert retcode != 0
    assert "DJANGO_SETTINGS_FILE is not defined" in err
