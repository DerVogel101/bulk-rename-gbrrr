from .interface import bulkTransaction, RenameExecutor, RenameHandler, FileInfo, FilenNameOptions
from .name_changer import StandartNameFormatter
import os
import re

class Renamer(RenameHandler):
    def __init__(self, folderPath: str = ""):
        super().__init__()

        self._folderPath: str = folderPath

        self._includeHiddenFiles: bool = False
        self._includeFolders: bool = False

        self._replaceWithValue: str = ""

        
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
            extentions = re.findall(r"(?<=\.)[^./\s]+$", file)
            
            filelist.append(FileInfo(
                name=file,
                extention=extentions[0] if len(extentions) > 0 else None,
                isFolder=os.path.isdir(os.path.join(self._folderPath, file)),
                lastModified=os.path.getmtime(os.path.join(self._folderPath, file)),
                isHidden=file[0] == "."
                )
            )
        self._currentTransaction.currentNames = filelist
        self.executeRename(dry_run=True)
        return filelist

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
    def replaceWithValue(self) -> str:
        return self._replaceWithValue

    @replaceWithValue.setter
    def replaceWithValue(self, value) -> None:
        self._replaceWithValue = value
        self.executeRename(dry_run=True)

    @property
    def currentTransaction(self) -> bulkTransaction:
        return self._currentTransaction



class RegExRenamer(RenameExecutor, Renamer):
    def __init__(self):
        super().__init__()
        self.__regex: str = ""

    def executeRename(self, dry_run: bool = False) -> bulkTransaction:
        """
        Execute the rename operation.
        """
        self._currentTransaction.totalChangedNames = 0
        self._currentTransaction.futureNames = set()
        for file, renamer in zip(self._currentTransaction.currentNames, self._nameFormatter):
            if file.isFolder and not self.includeFolders:
                continue
            if file.isHidden and not self.includeHiddenFiles:
                continue

            newName = file.name
            if self.__regex:
                if re.search(self.__regex, file.name):
                    newName = re.sub(self.__regex, renamer.format(file), file.name)
                    newName = renamer.postProcess(newName, file)
            if newName == file.name:        
                self._currentTransaction.totalChangedNames += 1

            if dry_run:
                self._currentTransaction.futureNames.add(newName)
            else:
                os.rename(os.path.join(self.folderPath, file.name), os.path.join(self.folderPath, newName))
        if not dry_run:
            self._getFileList()
        return self._currentTransaction

    @property
    def condition(self) -> str:
        """
        Get the regex condition.
        """
        return self.__regex

    @condition.setter
    def condition(self, value) -> str:
        self.__regex = value
        self.executeRename(dry_run=True)
