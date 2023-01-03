from typing import Type

from openpype.addons import BaseServerAddon

from .settings import BlenderSettings, DEFAULT_VALUES


class BlenderAddon(BaseServerAddon):
    name = "blender"
    title = "Blender"
    version = "1.0.0"
    settings_model: Type[BlenderSettings] = BlenderSettings
    frontend_scopes = {}
    services = {}

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)