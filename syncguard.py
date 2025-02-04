import os

class SyncGuard:
    def __init__(self, target_directory):
        self.target_directory = target_directory

    def rename_files(self, prefix='', suffix='', extension=None):
        """
        Rename files in the target directory with a specified prefix, suffix, and/or extension.
        
        :param prefix: String to be added at the beginning of each file name.
        :param suffix: String to be added at the end of each file name, before the extension.
        :param extension: New file extension to be used for all files. If None, the original extension is retained.
        """
        for filename in os.listdir(self.target_directory):
            if os.path.isfile(os.path.join(self.target_directory, filename)):
                base, ext = os.path.splitext(filename)
                new_ext = extension if extension else ext
                new_name = f"{prefix}{base}{suffix}{new_ext}"
                self._rename_item(filename, new_name)

    def rename_folders(self, prefix='', suffix=''):
        """
        Rename folders in the target directory with a specified prefix and/or suffix.
        
        :param prefix: String to be added at the beginning of each folder name.
        :param suffix: String to be added at the end of each folder name.
        """
        for foldername in os.listdir(self.target_directory):
            if os.path.isdir(os.path.join(self.target_directory, foldername)):
                new_name = f"{prefix}{foldername}{suffix}"
                self._rename_item(foldername, new_name)

    def _rename_item(self, old_name, new_name):
        """
        Rename an item (file or folder) from old_name to new_name.
        
        :param old_name: The current name of the item.
        :param new_name: The new name of the item.
        """
        old_path = os.path.join(self.target_directory, old_name)
        new_path = os.path.join(self.target_directory, new_name)
        os.rename(old_path, new_path)
        print(f'Renamed: {old_name} -> {new_name}')

# Example usage:
# sync_guard = SyncGuard('path_to_your_directory')
# sync_guard.rename_files(prefix='New_', suffix='_v1', extension='.txt')
# sync_guard.rename_folders(prefix='Project_', suffix='_2023')