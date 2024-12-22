import os
import shutil
import re

def create_file_path_dict(root_dir="."):
    """Creates a dictionary of file names and their full paths."""
    file_path_dict = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            if full_path.startswith(".\\"):
                full_path = full_path[2:]
            file_path_dict[file] = full_path
    return file_path_dict

def replace_file_names_with_paths_in_file(file_path, file_path_dict):
    """Replaces file names in a given file (HTML or CSS) with their full paths."""
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    # Create a regex pattern to match file names
    file_name_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, file_path_dict.keys())) + r')\b')

    # counts the numbers of directories deep a file in compared to the root.
    num_directories = (file_path.count('\\') - 1)
    # prefix added to a files path to escape back to the root.
    escape_prefix = "../" * num_directories

    def flask_pattern(path):
        return f"{{{{ url_for('static', filename='{path.replace('\\', '/')}') }}}}"

    # Replace file names with their paths
    updated_file_content = file_name_pattern.sub(lambda match: flask_pattern(escape_prefix+file_path_dict[match.group()]), file_content)

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_file_content)

    print(f"Updated {file_path} with asset paths.")


def process_files(file_types, file_path_dict, root_dir="."):
    """Processes all files of specified types in the directory."""
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(file_types):
                full_path = os.path.join(dirpath, file)
                replace_file_names_with_paths_in_file(full_path, file_path_dict)


def organize_files_by_extension(folder_name, folder_path='./'):
    """
    Organize files in the given folder by their extensions.
    
    Args:
        folder_path (str): The path to the folder to organize.
    """
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Get full path of the file
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Extract the file extension (lowercase to avoid case issues)
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower().strip('.')
        
        if file_extension not in ("py", "html"):
            if not file_extension:
                # For files without an extension, group into "no_extension"
                file_extension = "no_extension"
            
            extension_folder = os.path.join(folder_path, f'{folder_name}')
            os.makedirs(extension_folder, exist_ok=True)
            
            # Move the file to the corresponding directory
            shutil.move(file_path, os.path.join(extension_folder, filename))
    
    print("Files have been organized by their extensions.")


if __name__ == "__main__":
    organize_files_by_extension('class_results_assets')

    # Generate the file path dictionary
    file_dict = create_file_path_dict()

    # Process HTML and CSS files
    process_files(file_types=(".html"), file_path_dict=file_dict)
