import os
import shutil

def move_file_by_extension(source_dir, dest_dir):
	
	file_extension = {
		"Image": [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
				".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"],
		"Video": [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"],
		"Document": [".doc", ".docx", ".odt", ".txt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"],
		"Audio" : [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"],
		"Executable" : [".exe"],	
		"Zip" : [".zip"]
	}

	for folder in file_extension.keys():
		folder_path = os.path.join(dest_dir, folder)
		os.makedirs(folder_path, exist_ok=True)

	for filename in os.listdir(source_dir):
		if filename.lower() == "desktop.ini":
			continue

		file_path = os.path.join(source_dir, filename)

		if os.path.isfile(file_path):
			_, file_ext = os.path.splitext(filename)
			file_ext = file_ext.lower()

			file_type = None
			for ftype, extension in file_extension.items():
				if file_ext in extension:
					file_type = ftype
					break

			if file_type:
				destination_folder = os.path.join(dest_dir, file_type)
				destination_path = os.path.join(destination_folder, filename)

				shutil.move(file_path, destination_path)
				print(f"Moved '{filename}' to '{destination_folder}.'")

			else:
				destination_folder = os.path.join(dest_dir, "others")
				destination_path = os.path.join(destination_folder, filename)

				shutil.move(file_path, destination_path)
				print(f"Moved '{filename}' to '{destination_folder}.'")

if __name__ == "__main__":

	source_directory = r"C:\Users\Your Username\Downloads"
	dest_dir = r"Any\folder\path"

	move_file_by_extension(source_directory, dest_dir)
