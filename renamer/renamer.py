from .interface import bulkTransaction, RenameExecutor, RenameHandler, FileInfo, FilenNameOptions
from .name_changer import StandartNameFormatter
import os
import re
from typing import Any

class Renamer(RenameHandler):
    def __init__(self, folderPath: str = ""):
        super().__init__()
        if not issubclass(self.__class__, RenameExecutor):
            raise NotImplementedError("This class must be used as base for RenameExecutor")

        self._folderPath: str = folderPath

        self._includeHiddenFiles: bool = False
        self._includeFolders: bool = False

        self._replaceWithValue: str = ""
        self.match_for = None
        
        try: 
            folder_content = self._getFileList()
        except: 
            folder_content = []
        self._currentTransaction: bulkTransaction = bulkTransaction(
            totalChangedNames=0,
            currentNames=folder_content,
            futureNames=set(),
        )
        self._nameFormatter = StandartNameFormatter(
            expected_entries=len(self._currentTransaction.currentNames)
            )
        self.executeRename(dry_run=True)

    @property
    def nameFormatter(self) -> StandartNameFormatter:
        return self._nameFormatter

    def setNameFormatterOptions(self, **FilenNameOptions):
        for key, value in FilenNameOptions.items():
            if hasattr(self._nameFormatter.options, key):
                setattr(self._nameFormatter.options, key, value)
            else:
                raise ValueError(f"Invalid option: {key}")
        self.executeRename(dry_run=True)

    def _getFileList(self):
        content = os.listdir(self._folderPath)
        filelist = []
        for file in content:
            extentions = re.findall(r"^(?!\.[^\.]*$).+(\.[^\.]+)+$", file)
            name = re.findall(r"^([^.]*)\.?.*$", file)
            
            filelist.append(FileInfo(
                name=name[0] if len(name) > 0 else file,
                extention=extentions[0] if len(extentions) > 0 else None,
                isFolder=os.path.isdir(os.path.join(self._folderPath, file)),
                lastModified=os.path.getmtime(os.path.join(self._folderPath, file)),
                isHidden=file[0] == "."
                )
            )
        self._currentTransaction.currentNames = filelist
        self.executeRename(dry_run=True)
        return filelist

    def executeRename(self, dry_run: bool = False) -> bulkTransaction:
        if self.match_for is None:
            return self.currentTransaction
        self._currentTransaction.totalChangedNames = 0
        self._currentTransaction.futureNames = set()
        for file, renamer in zip(self._currentTransaction.currentNames, self._nameFormatter):
            if file.isFolder and not self.includeFolders:
                continue
            if file.isHidden and not self.includeHiddenFiles:
                continue

            new_filename = renamer.postProcess(
                self._applyNewFilename(file, renamer),
                file)
            
            if dry_run:
                self._currentTransaction.futureNames.add(new_filename)
            else:
                os.rename(
                    os.join(self.folderPath,
                        file.name + file.extention),
                    os.join(self.folderPath, new_filename))
        else:
            if not dry_run:
                self._getFileList()
        self._currentTransaction.totalChangedNames = renamer.iterator
        return self.currentTransaction

    @property
    def folderPath(self) -> str:
        return self._folderPath
    
    @folderPath.setter
    def folderPath(self, value: str) -> None:
        self._folderPath = value
        self._getFileList()
        
    @property
    def includeHiddenFiles(self) -> bool:
        return self._includeHiddenFiles

    @includeHiddenFiles.setter
    def includeHiddenFiles(self, hidden) -> None:
        self._includeHiddenFiles = hidden
        self.executeRename(dry_run=True)
    
    @property
    def includeFolders(self) -> bool:
        return self._includeFolders

    @includeFolders.setter
    def includeFolders(self, folders) -> None:
        self._includeFolders = folders
        self.executeRename(dry_run=True)

    @property
    def currentTransaction(self) -> bulkTransaction:
        return self._currentTransaction

    @property
    def condition(self) -> Any:
        return self.match_for

    @condition.setter
    def condition(self, value: Any) -> None:
        self.match_for = value
        self.executeRename(dry_run=True)
