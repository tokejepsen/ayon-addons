from ayon_server.settings import (
    BaseSettingsModel,
    task_types_enum,
    Field
)
from .common import PathsTemplate


class CustomTemplateModel(BaseSettingsModel):
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=task_types_enum
    )
    path: PathsTemplate = Field(
        default_factory=PathsTemplate,
        title="Gizmo Directory Path"
    )


class BuilderProfileItemModel(BaseSettingsModel):
    subset_name_filters: list[str] = Field(
        default_factory=list,
        title="Subset name"
    )
    families: list[str] = Field(
        default_factory=list,
        title="Families"
    )
    repre_names: list[str] = Field(
        default_factory=list,
        title="Representations"
    )
    loaders: list[str] = Field(
        default_factory=list,
        title="Loader plugins"
    )


class BuilderProfileModel(BaseSettingsModel):
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=task_types_enum
    )
    tasks: list[str] = Field(
        default_factory=list,
        title="Task names"
    )
    current_context: list[BuilderProfileItemModel] = Field(
        title="Current context")
    linked_assets: list[BuilderProfileItemModel] = Field(
        title="Linked assets/shots")


class WorkfileBuilderModel(BaseSettingsModel):
    create_first_version: bool = Field(
        title="Create first workfile")
    custom_templates: list[CustomTemplateModel] = Field(
        title="Custom templates")
    builder_on_start: bool = Field(
        title="Run Builder at first workfile")
    profiles: list[BuilderProfileModel] = Field(
        title="Builder profiles")


class WorkfileBuilderSettings(BaseSettingsModel):
    """Nuke templated workfile build project settings. """

    workfile_builder: WorkfileBuilderModel = Field(
        default_factory=WorkfileBuilderModel,
        title="Workfile Builder",
    )


DEFAULT_WORKFILE_BUILDER_SETTINGS = {
    "workfile_builder": {
        "create_first_version": False,
        "custom_templates": [],
        "builder_on_start": False,
        "profiles": [
            {
                "task_types": [],
                "tasks": [],
                "current_context": [
                    {
                        "subset_name_filters": [],
                        "families": [
                            "render",
                            "plate"
                        ],
                        "repre_names": [
                            "exr",
                            "dpx",
                            "mov",
                            "mp4",
                            "h264"
                        ],
                        "loaders": [
                            "LoadClip"
                        ]
                    }
                ],
                "linked_assets": []
            }
        ]
    }
}
