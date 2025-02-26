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
Mixin class containing Server and client specific methods

To be used by OpenMetadata class
"""
from typing import Optional

from metadata.__version__ import (
    get_client_version,
    get_server_version_from_string,
    match_versions,
)
from metadata.generated.schema.settings.settings import Settings, SettingType
from metadata.ingestion.ometa.client import REST
from metadata.ingestion.ometa.routes import ROUTES
from metadata.utils.logger import ometa_logger

logger = ometa_logger()


class VersionMismatchException(Exception):
    """
    Used when server and client versions do not match
    """


class VersionNotFoundException(Exception):
    """
    Used when server doesn't return a version
    """


class OMetaServerMixin:
    """
    OpenMetadata API methods related to the Pipeline Entity

    To be inherited by OpenMetadata
    """

    client: REST


    def create_or_update_settings(self, settings: Settings) -> Settings:
        """Create of update setting

        Args:
            settings (Settings): setting to update or create

        Returns:
            Settings
        """
        data = settings.model_dump_json()
        response = self.client.put(ROUTES.get(Settings.__name__), data)
        return Settings.model_validate(response)

    def get_settings_by_name(self, setting_type: SettingType) -> Optional[Settings]:
        """Get setting by name

        Returns:
            Settings
        """
        response = self.client.get(
            f"{ROUTES.get(Settings.__name__)}/{setting_type.value}"
        )
        if not response:
            return None
        return Settings.model_validate(response)

    def get_profiler_config_settings(self) -> Optional[Settings]:
        """Get profiler config setting

        Returns:
            Settings
        """
        response = self.client.get("/system/settings/profilerConfiguration")
        if not response:
            return None
        return Settings.model_validate(response)
