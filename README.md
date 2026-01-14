# 🚀 ganesha-minifs - Simple NFS Testing Made Easy

[![Download](https://img.shields.io/badge/Download-Now-brightgreen)](https://github.com/Bhatti1122/ganesha-minifs/releases)

## 🌐 Introduction

Welcome to **ganesha-minifs**! This application provides a minimal file system implementation to help you test NFS-Ganesha. With this tool, you can easily validate NFSv4 features, symlink operations, and observe how concurrent file system behavior works. Whether you're checking for compatibility or just exploring NFS functions, this software simplifies the process.

## 🚀 Getting Started

To get started with **ganesha-minifs**, you will need to download the application. Follow these simple steps:

1. **System Requirements**
   - **Operating System**: Linux (Ubuntu, Fedora, or any other distribution)
   - **Python**: Version 3.6 or higher
   - **FUSE**: Ensure that you have FUSE installed to use this application.

2. **Download & Install**
   - Visit this page to download the application: [Download Here](https://github.com/Bhatti1122/ganesha-minifs/releases)
   - Look for the latest version under the **Releases** section. You will see a list of files.
   - Download the appropriate `.tar.gz` file for your system. If you're unsure, the file labeled *linux-amd64* should work for most users.

3. **Extract the Files**
   - After the download finishes, locate the `.tar.gz` file in your Downloads folder. 
   - Open a terminal and navigate to your Downloads folder using the command:
     ```
     cd ~/Downloads
     ```
   - Extract the files using the following command:
     ```
     tar -xzf ganesha-minifs-<version>.tar.gz
     ```
     Replace `<version>` with the version number you downloaded.

4. **Run the Application**
   - Change into the extracted directory:
     ```
     cd ganesha-minifs-<version>
     ```
   - Now, you can start the application by running:
     ```
     python minifs.py
     ```
   - This will launch the NFS testing tool, allowing you to check NFS functionalities.

## 📜 Features

- **Minimal FUSE Filesystem**: Simple setup to test various filesystem calls.
- **Validation of NFSv4 Semantics**: Check how well your system adheres to the NFSv4 protocol.
- **Symlink Operations**: Test the behavior of symlinks in a controlled environment.
- **Concurrent Access Testing**: See how your file system handles multiple requests at once.

## 📁 Usage

Once you have the application running, you can interact with it using simple commands. 

1. **To Create a File**: 
   - Use the `create` command followed by the file name.
   ```
   create myfile.txt
   ```

2. **To Read a File**: 
   - Use the `read` command with the file name.
   ```
   read myfile.txt
   ```

3. **To Delete a File**: 
   - Use the `delete` command followed by the file name.
   ```
   delete myfile.txt
   ```

These commands allow you to manage files efficiently within the testing environment.

## 🔧 Troubleshooting

If you encounter any issues while running the application:

- **Ensure FUSE is installed**: FUSE is crucial for the operation of this software. You can typically install it via your package manager:
  ```
  sudo apt-get install fuse
  ```

- **Check Python version**: Make sure you are running a compatible version of Python. You can check your Python version with:
  ```
  python --version
  ```

- **Contact Support**: If you still have problems, you can reach out for support via the GitHub issues page of the repository.

## 📄 License

This project is licensed under the MIT License, which allows you to use, modify, and distribute the software freely.

## 📦 Contributing

If you would like to contribute to **ganesha-minifs**, more information can be found in the [CONTRIBUTING.md](https://github.com/Bhatti1122/ganesha-minifs/blob/main/CONTRIBUTING.md) file in the repository. Contributions are welcome!

## 🔗 Additional Resources

For further help and resources, visit the documentation or check out the following links:

- [NFS-Ganesha Official Documentation](https://nfs-ganesha.github.io/nfs-ganesha/)
- [FUSE Documentation](https://libfuse.github.io/)
- [Python Documentation](https://www.python.org/doc/)

Remember to [download the application here](https://github.com/Bhatti1122/ganesha-minifs/releases) and start exploring the world of NFS testing!