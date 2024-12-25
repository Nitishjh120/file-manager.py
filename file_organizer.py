import os
import shutil

def organize_files(directory):
    """
    Organize files in the given directory into subfolders based on their extensions.

    :param directory: Path to the directory to organize
    """
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Define file type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Others": []
    }

    # Create folders for each category if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files into respective folders
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            # Determine file category
            moved = False
            for category, extensions in file_types.items():
                if os.path.splitext(file)[1].lower() in extensions:
                    shutil.move(file_path, os.path.join(directory, category, file))
                    moved = True
                    break
            if not moved:  # Move to 'Others' if no matching category
                shutil.move(file_path, os.path.join(directory, "Others", file))

    print("Files have been organized successfully.")

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = input("Enter the path of the directory to organize: ").strip()
    organize_files(target_directory)
