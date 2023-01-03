from pydantic import Field, validator

from openpype.settings import BaseSettingsModel, ensure_unique_names


class WorkfileBuilderSettings(BaseSettingsModel):
    """Nuke templated workfile build project settings. """

    sub_input_field_one: str = Field(
        title="Sub input field one"
    )


DEFAULT_WORKFILE_BUILDER_SETTINGS = {
    "sub_input_field_one": "This Text"
}
