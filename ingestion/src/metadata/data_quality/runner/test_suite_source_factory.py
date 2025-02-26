#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Factory class for creating test suite source objects
"""

from metadata.data_quality.runner.base_test_suite_source import BaseTestSuiteRunner
from metadata.utils.logger import test_suite_logger

logger = test_suite_logger()

class TestSuiteRunnerFactory:
    """Creational factory for test suite source objects"""

    def __init__(self):
        self._source_type = {"base": BaseTestSuiteRunner}

    def register_source(self, source_type: str, source_class):
        """Register a new source type"""
        self._source_type[source_type] = source_class

    def create(self, source_type: str, *args, **kwargs) -> BaseTestSuiteRunner:
        """Create source object based on source type"""
        source_class = self._source_type.get(source_type)
        logger.error(f"SOURCE CLASS : {source_class} ---  SOURCE TYPE: {source_type}")
        if not source_class:
            source_class = self._source_type["base"]
            logger.error(f"not_source_Class : {source_class}")
            return source_class(*args, **kwargs)
        return source_class(*args, **kwargs)


test_suite_source_factory = TestSuiteRunnerFactory()
logger.error(f"test_suite_source_factory.py - TEST - {test_suite_source_factory}")