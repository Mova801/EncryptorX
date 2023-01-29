from enum import StrEnum
from dataclasses import dataclass


class RequestType(StrEnum):
    BUG_REPORT = '<bug_report>'


@dataclass
class Link:
    """Class containing default app links."""
    github_app_issues: str = "https://github.com/Mova801/SimpleGUIApplication/issues"
