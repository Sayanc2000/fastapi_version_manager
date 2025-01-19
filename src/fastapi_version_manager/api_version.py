from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict

from packaging import version


@dataclass
class VersionInfo:
    """Stores metadata about an API version"""
    version: str
    released_date: date
    supported: bool = True
    deprecated: bool = False
    sunset_date: Optional[date] = None
    description: Optional[str] = None


class APIVersions:
    """Central version management"""
    # TODO: to have support of external source for version defination
    VERSIONS: Dict[str, VersionInfo] = {}  # Empty dict that will be initialized by ManagedApp

    @classmethod
    def initialize_versions(cls, versions: Dict[str, VersionInfo]):
        """Initialize the versions dictionary"""
        cls.VERSIONS = versions

    @classmethod
    def get_version_info(cls, ver: str) -> Optional[VersionInfo]:
        return cls.VERSIONS.get(ver)

    @classmethod
    def is_supported(cls, ver: str) -> bool:
        info = cls.get_version_info(ver)
        return info is not None and info.supported

    @classmethod
    def is_deprecated(cls, ver: str) -> bool:
        info = cls.get_version_info(ver)
        return info is not None and info.deprecated

    @classmethod
    def get_latest_version(cls) -> str:
        return max(cls.VERSIONS.keys(), key=version.parse)

    @classmethod
    def get_supported_versions(cls) -> list[str]:
        return [ver for ver, info in cls.VERSIONS.items() if info.supported]
