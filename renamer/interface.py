from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

@dataclass
class FileInfo:
    name: str
    extention: str | None
    isFolder: bool
    isHidden: bool
    lastModified: str

@dataclass
class bulkTransaction():
    totalChangedNames: str
    currentNames: list[FileInfo]
    futureNames: set

class IncrementPossitions(Enum):
    START = "start",
    END = "end",
    NO = "no"

@dataclass
class FilenNameOptions:
    increment_at: IncrementPossitions | None
    seperator_char: str | None
    preserve_file_indicator: bool | None

class RenameHandler(ABC):
    """
    Interface to store rename configuration
    """

    @abstractmethod
    def _getFileList(self) -> list[FileInfo]:
        """
        Get the list of files to be renamed.

        :return: List of file paths.
        """
        pass

    @property
    @abstractmethod
    def nameFormatter(self) -> FilenNameOptions:
        """
        Get the name formatter.

        :return: The name formatter.
        """
        pass

    @abstractmethod
    def setNameFormatterOptions(self, **FilenNameOptions):
        """
        Set the name formatter.

        :param value: The name formatter.
        """
        pass

    @property
    @abstractmethod
    def folderPath(self) -> str:
        """Get the path of the parent Fodler."""
        pass

    @folderPath.setter
    @abstractmethod
    def folderPath(self, value: str):
        """Set the path of the parent folder."""
        pass

    @property
    @abstractmethod
    def currentTransaction(self) -> bulkTransaction:
        """Get the current transaction."""
        pass

    @property
    @abstractmethod
    def includeHiddenFiles(self) -> bool:
        """Get whether to include hidden files."""
        pass

    @includeHiddenFiles.setter
    @abstractmethod
    def includeHiddenFiles(self, value: bool):
        """Set whether to include hidden files."""
        pass

    @property
    @abstractmethod
    def includeFolders(self) -> bool:
        """Get whether to include folders."""
        pass

    @includeFolders.setter
    @abstractmethod
    def includeFolders(self, value: bool):
        """Set whether to include folders."""
        pass

    @property
    @abstractmethod
    def replaceWithValue(self) -> str:
        """Get the replacement value."""
        pass

    @replaceWithValue.setter
    @abstractmethod
    def replaceWithValue(self, value: str):
        """Set the replacement value."""
        pass

class FilenameFormatter(ABC):

    @abstractmethod
    def __init__(self, options: FilenNameOptions):
        """
        """
        pass

    @abstractmethod
    def format(self, file: FileInfo) -> str:
        """
        Format the filename based on the provided options.

        :param file: The file to format.
        :return: The formatted filename.
        """
        pass


class RenameExecutor(RenameHandler,ABC):
    """
    Implementation of the rename operation.
    """

    @abstractmethod
    def executeRename(self, dry_run: bool) -> bulkTransaction:
        """
        Execute the rename operation.

        :throws: Exception if the rename operation fails.

        :param dry_run: If True, perform a dry run without making any changes.
        :return: The number of files renamed.
        """
        pass

    @property
    @abstractmethod
    def condition(self):
        """Get the condition."""
        pass
    
    @condition.setter
    @abstractmethod
    def condition(self, value: str):
        """Set the condition."""
        pass


"""
Incrementaition with equal Width


"""