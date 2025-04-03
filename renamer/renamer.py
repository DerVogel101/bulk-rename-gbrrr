from .interface import bulkTransaction, RenameExecutor, RenameHandler, FileInfo
import os

class Renamer(RenameHandler):
    def __init__(self, folderPath: str = ""):
        super().__init__()

        self.__folderPath: str = folderPath

        self.__includeHiddenFiles: bool = False
        self.__includeFolders: bool = False

        self.__preserveFileTypeIndicator: bool = False
        self.__replaceWithValue: str = ""

        
        try: 
            folder_content = self.getFileList()
        except: 
            folder_content = []
        self.__currentTransaction: bulkTransaction = bulkTransaction(
            totalChangedNames=0,
            currentNames=folder_content,
            futureNames=set(),
        )
        self.__currentTransaction = self.executeRename(dry_run=True)

    def getFileList(self):
        content = os.listdir(self.__folderPath)
        filelist = []
        for file in content:
            filelist.append(FileInfo(
                name=file,
                isFolder=os.path.isdir(os.path.join(self.__folderPath, file)),
                lastModified=os.path.getmtime(os.path.join(self.__folderPath, file)),
                isHidden=file[0] == "."
                )
            )
        self.__currentTransaction.currentNames = filelist
        self.__currentTransaction = self.executeRename(dry_run=True)
        return filelist

    @property
    def folderPath(self) -> str:
        return self.__folderPath
    
    @folderPath.setter
    def folderPath(self, value: str) -> None:
        self.__folderPath = value
        self.getFileList()
        
    @property
    def includeHiddenFiles(self) -> bool:
        return self.__includeHiddenFiles

    @includeHiddenFiles.setter
    def includeHiddenFiles(self, hidden) -> None:
        self.__includeHiddenFiles = hidden
        self.__currentTransaction = self.executeRename(dry_run=True)
    
    @property
    def includeFolders(self) -> bool:
        return self.__includeFolders

    @includeFolders.setter
    def includeFolders(self, folders) -> None:
        self.__includeFolders = folders
        self.__currentTransaction = super(Renamer, self).executeRename(dry_run=True)

    @property
    def preserveFileTypeIndicator(self) -> bool:
        return self.__preserveFileTypeIndicator

    @preserveFileTypeIndicator.setter
    def preserveFileTypeIndicator(self, preserve) -> None:
        self.__preserveFileTypeIndicator = preserve
        self.__currentTransaction = super(Renamer, self).executeRename(dry_run=True)

    @property
    def replaceWithValue(self) -> str:
        return self.__replaceWithValue

    @replaceWithValue.setter
    def replaceWithValue(self, value) -> None:
        self.__replaceWithValue = value
        self.__currentTransaction = super(Renamer, self).executeRename(dry_run=True)

    @property
    def currentTransaction(self) -> bulkTransaction:
        return self.__currentTransaction



class RegExRenamer(RenameExecutor, Renamer):
    def __init__(self):
        super().__init__()
        self.__regex: str = ""

    def executeRename(self, dry_run: bool = False) -> bulkTransaction:
        pass
    
    @property
    def condition(self, value) -> str:
        self.__regex = value
