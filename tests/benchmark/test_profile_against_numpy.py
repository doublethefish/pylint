""" Profiles basic -jX functionality """
# Copyright (c) 2020 Frank Harrison <doublethefish@gmail.com>

# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

# pylint: disable=protected-access,missing-function-docstring,no-self-use

import os

import pytest

from pylint.lint import Run
from pylint.testutils import TestReporter as Reporter


def _get_py_files(scanpath):
    assert os.path.exists(scanpath), "Dir not found %s" % scanpath

    filepaths = []
    for _dirpath, dirnames, filenames in os.walk(scanpath):
        dirnames[:] = [dirname for dirname in dirnames if dirname != "__pycache__"]
        filepaths.extend(
            [filename for filename in filenames if filename.endswith(".py")]
        )
    return filepaths


@pytest.mark.skipif(
    os.environ.get("PYTEST_PROFILE_NUMPY", False),
    reason="PYTEST_PROFILE_NUMPY, not set, assuming not a profile run",
)
class TestEstablishBaselineBenchmarks:
    """ Runs against numpy """

    def test_run(self):

        numpy_checkout_path = os.path.abspath(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        )
        filepaths = _get_py_files(scanpath=numpy_checkout_path)

        Run(filepaths, reporter=Reporter(), do_exit=False)

        # assert runner.linter.msg_status == 0, (
        #    "Expected no errors to be thrown: %s"
        #    % pprint.pformat(runner.linter.reporter.messages)
        # )
