from .interface import IncrementPossitions, FileInfo, FilenameFormatter, FilenNameOptions
import re
import datetime

DEFAULT_FORMAT_OPTIONS = FilenNameOptions(
    increment_at=IncrementPossitions.START,
    seperator_char="_",
    preserve_file_indicator=True,
    replace_with=None
)

class StandartNameFormatter(FilenameFormatter):
    """
    Implementation of the rename operation.
    """

    def __init__(self, options: FilenNameOptions = DEFAULT_FORMAT_OPTIONS, expected_entries: int = -1):
        self.__iterator = -1
        self.__iterator_size = len(str(expected_entries))
        self.options = options

    @staticmethod
    def unix_to_timestamp(unix_time: str) -> str:
        """
        Convert a Unix timestamp to a human-readable date string.

        :param unix_time: The Unix timestamp to convert.
        :return: The formatted date string.
        """
        try:
            return datetime.datetime.fromtimestamp(float(unix_time)).strftime("%Y-%m-%d_%H:%M:%S")
        except ValueError:
            return unix_time

    def format(self, file: FileInfo) -> str:
        """
        Format the filename based on the provided options.

        :param file: The file to format.
        :return: The formatted filename.
        """
        if self.__iterator >= 0:
            self.__iterator += 1
        used_iter: str = str(self.__iterator).zfill(self.__iterator_size) if self.__iterator >= 0 else ""
        if self.options.replace_with:
            # Negatve lookbehind, ensurin \\ is escaped 
            name = re.sub(r"(?<!\\)(%n)", file.name, self.options.replace_with)
            name = re.sub(r"(?<!\\)(%e)", file.extention, name)
            name = re.sub(r"(?<!\\)(%d)", self.unix_to_timestamp(file.lastModified), name)
        else:
            name = file.name
        match self.options.increment_at:
            case IncrementPossitions.START:
                return f"{used_iter}{self.options.seperator_char}{name}"
            case IncrementPossitions.END:
                return f"{name}{self.options.seperator_char}{used_iter}"
            case _:
                return name
            
    def postProcess(self, newName: str, file: FileInfo):
        if self.options.preserve_file_indicator \
            and not file.isFolder:
            lookup = re.search(r"^(?!\.[^\.]*$).+(\.[^\.]+)+$", newName)
            if not lookup or lookup.group(0) != file.extention:
                # Search the last . followed by any char if the filename dose not start with a dot
                # or the filname contains more then one dot
                newName = f"{newName}{file.extention}"
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
