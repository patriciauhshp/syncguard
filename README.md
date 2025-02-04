# SyncGuard

SyncGuard is a Python program designed to provide batch renaming capabilities for files and folders to enhance organization on Windows systems. It allows users to add prefixes, suffixes, and change file extensions in bulk, offering a convenient way to standardize naming conventions across directories.

## Features

- **Batch File Renaming**: Add prefixes and suffixes to file names and change file extensions in a specified directory.
- **Batch Folder Renaming**: Add prefixes and suffixes to folder names in a specified directory.
- **Simple and Efficient**: Easily manage and organize files and folders with minimal effort.

## Requirements

- Python 3.x
- Windows OS

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/syncguard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd syncguard
   ```

## Usage

1. Open the `syncguard.py` file in a text editor.
2. Modify the example usage section with the path to your target directory and desired renaming parameters.
3. Run the script:
   ```bash
   python syncguard.py
   ```

## Example

To rename all files in a directory by adding "New_" as a prefix and "_v1" as a suffix while changing their extension to `.txt`, and similarly rename folders with "Project_" as a prefix and "_2023" as a suffix, use the following code:

```python
# Example usage:
sync_guard = SyncGuard('path_to_your_directory')
sync_guard.rename_files(prefix='New_', suffix='_v1', extension='.txt')
sync_guard.rename_folders(prefix='Project_', suffix='_2023')
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.