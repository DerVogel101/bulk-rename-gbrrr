from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class FileInfo:
    name: str
    isFolder: bool
    isHidden: bool
    lastModified: str

@dataclass
class bulkTransaction():
    totalChangedNames: str
    currentNames: list[FileInfo]
    futureNames: set



class RenameHandler(ABC):
    """
    Interface to store rename configuration
    """

    @abstractmethod
    def getFileList(self) -> list[FileInfo]:
        """
        Get the list of files to be renamed.

        :return: List of file paths.
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
    def preserveFileTypeIndicator(self) -> bool:
        """Get whether to preserve file type indicator."""
        pass

    @preserveFileTypeIndicator.setter
    @abstractmethod
    def preserveFileTypeIndicator(self, value: bool):
        """Set whether to preserve file type indicator."""
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


class RenameExecutor(ABC):
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
    def condition(self, value):
        """Set the condition."""
        pass

