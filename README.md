**Project: File Organizer**

**Description:**
The File Organizer is a Python script that helps you organize your files based on their extensions into specific folders. It categorizes files into different types such as images, videos, documents, audios, executables, and zip files and moves them to corresponding destination folders.

**Features:**
- Organize files into different categories based on their extensions.
- Move files to corresponding folders for images, videos, documents, audios, executables, and zip files.
- Handle unknown file types and move them to an "others" folder.
- Skip moving system files like "desktop.ini" to avoid errors.

**How to Use:**
1. Ensure you have Python 3.x installed on your system.
2. Clone or download the "File Organizer" project to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.

**File Structure:**
```
File_Organizer/
│-- main.py
│-- README.md
```

**Usage:**
1. Modify the source and destination directories in the `file_organizer.py` script:
   ```python
   source_directory = r" "
   destination_directory = r" "
   ```

2. Run the script by executing the following command:
   ```
   python file_organizer.py
   ```

**Notes:**
- Make sure to replace `YourUsername` in the `source_directory` with your actual Windows username.
- If the script is unable to move certain files (e.g., system files or files with special permissions), it will print an error message. You can safely ignore these files, and they will remain in the source directory.

**License:**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for the full license text.

**Disclaimer:**
The File Organizer script is provided as-is, without any warranties or guarantees. The author is not responsible for any damage or loss caused by the usage of this script.

**Author:**
Aakash Joshi
