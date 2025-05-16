from renamer import RegExRenamer, IncrementPossitions, MatchRenamer
from pprint import pprint

if __name__ == "__main__":
    #renamer = MatchRenamer(mode="exact")
    renamer = RegExRenamer()
    renamer.folderPath = "/var/home/someone/Code/bulk_rename/documentation"
    renamer.includeHiddenFiles = False
    renamer.includeFolders = False
    #renamer.condition = "app design.png"
    renamer.condition = r"^(.*)$"
    renamer.setNameFormatterOptions(
        increment_at = IncrementPossitions.NO,
        seperator_char = "+++",
        preserve_file_indicator = True,
        replace_with = "NEW: %n-%d",)
    
    # Execute the rename operation
    pprint(renamer.executeRename(dry_run=True))