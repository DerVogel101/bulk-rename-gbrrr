from .interface import IncrementPossitions, FileInfo, FilenameFormatter, FilenNameOptions
import re

DEFAULT_FORMAT_OPTIONS = FilenNameOptions(
    increment_at=IncrementPossitions.START,
    seperator_char="_",
    preserve_file_indicator=True
)

class StandartNameFormatter(FilenameFormatter):
    """
    Implementation of the rename operation.
    """

    def __init__(self, options: FilenNameOptions = DEFAULT_FORMAT_OPTIONS, expected_entries: int = -1):
        self.__iterator = -1
        self.__iterator_size = len(str(expected_entries))
        self.options = options

    def format(self, file: FileInfo) -> str:
        """
        Format the filename based on the provided options.

        :param file: The file to format.
        :return: The formatted filename.
        """
        if self.__iterator >= 0:
            self.__iterator += 1
        used_iter: str = str(self.__iterator).zfill(self.__iterator_size) if self.__iterator >= 0 else ""

        match self.options.increment_at:
            case IncrementPossitions.START:
                return f"{used_iter}{self.options.seperator_char}{file.name}"
            case IncrementPossitions.END:
                return f"{file.name}{self.options.seperator_char}{used_iter}"
            case _:
                return file.name
            
    def postProcess(self, newName: str, file: FileInfo):
        if self.options.preserve_file_indicator \
            and not file.isFolder:
            if not re.search(rf"\.{re.escape(file.extention)}$", file.name):
                newName = f"{newName}.{file.extention}"
        return newName

    @property
    def iterator(self) -> int:
        return self.__iterator
    
    @iterator.setter
    def iterator(self, value: int|None) -> None:
        if value is not None:
            self._iterator = value
        else:
            self._iterator = -1
        
    def __iter__(self):
        self.__iterator = 0
        return self
    
    def __next__(self):
        return self
