from ..renamer import Renamer
from ..interface import RenameExecutor, bulkTransaction
import re

class RegExRenamer(RenameExecutor, Renamer):
    def __init__(self):
        super().__init__()

    def _applyNewFilename(self, file, renamer) -> str:
        """
        Execute the rename operation.
        """
        newName = file.name
        if self.match_for:
            if re.search(self.match_for, file.name):
                newName = re.sub(self.match_for, renamer.format(file), file.name)
                newName = renamer.postProcess(newName, file)
        return newName

