from ..renamer import Renamer
from ..interface import RenameExecutor

class MatchRenamer(RenameExecutor, Renamer):
    def __init__(self, mode: str = "exact"):
        super().__init__()
        self.mode: str = mode
        self.match_for: str = ""

    def _applyNewFilename(self, file, renamer) -> str:
        """
        Execute the rename operation.
        """
        newName = None
        current_full_name = file.name + file.extention
        if self.mode == "exact":
            if current_full_name == self.match_for:
                newName = renamer.format(file)
        elif self.mode == "includes":
            newName = current_full_name.replace(self.match_for, renamer.format(file))
        
        return newName if newName is not None else current_full_name
