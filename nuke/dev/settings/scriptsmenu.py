from pydantic import Field
from openpype.settings import BaseSettingsModel


class ScriptsmenuSubmodel(BaseSettingsModel):
    """Item Definition"""
    _isGroup = True

    type: str = Field(title="Type")
    command: str = Field(title="Command")
    sourcetype: str = Field(title="Source Type")
    title: str = Field(title="Title")
    tooltip: str = Field(title="Tooltip")
    tags: list[str] = Field(default_factory=list, title="A list of tags")


class ScriptsmenuSettings(BaseSettingsModel):
    """Nuke script menu project settings."""
    _isGroup = True

    name: str = Field(title="Name")
    definition: list[ScriptsmenuSubmodel] = Field(
        default_factory=list, title="Definition", description="Scriptmenu Items Definition")


DEFAULT_SCRIPTSMENU_SETTINGS = {
    "name": "OpenPype Tools",
    "definition": [
        {
            "type": "action",
            "sourcetype": "python",
            "title": "OpenPype Docs",
            "command": "import webbrowser;webbrowser.open(url='https://openpype.io/docs/artist_hosts_nuke_tut')",
            "tooltip": "Open the OpenPype Nuke user doc page",
            "tags": [
                "OpenPype",
                "docs"
            ]
        }
    ]
}
