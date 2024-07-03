
<a id="readme-top"></a>

![GitHub repo size](https://img.shields.io/github/repo-size/krishujeniya/PHOTO-EDITOR-USING-CTk)
![GitHub contributors](https://img.shields.io/github/contributors/krishujeniya/PHOTO-EDITOR-USING-CTk)
![GitHub stars](https://img.shields.io/github/stars/krishujeniya/PHOTO-EDITOR-USING-CTk?style=social)
![GitHub forks](https://img.shields.io/github/forks/krishujeniya/PHOTO-EDITOR-USING-CTk?style=social)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="path_to_logo_image" alt="Logo" width="80" height="80">

  <h1 align="center">PHOTO-EDITOR-USING-CTk</h1>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

The PHOTO-EDITOR-USING-CTk is a graphical user interface (GUI) application developed using Python's CustomTkinter library. This application provides a range of photo editing functionalities such as removing backgrounds, cropping, applying filters, adding text, and rotating images. The integration with Docker ensures a consistent environment for running the application.

### Key Features

- **User-Friendly Interface:**
  - Developed using CustomTkinter for a modern and visually appealing interface.
  - Easy-to-use controls for a seamless editing experience.

- **Remove Background:**
  - Automatically removes the background from images using advanced algorithms.

- **Crop:**
  - Crop images to the desired dimensions with simple drag-and-drop functionality.

- **Filters:**
  - Apply various filters to enhance the look of your photos.

- **Add Text:**
  - Insert text with customizable fonts, colors, and sizes.

- **Rotate:**
  - Rotate images to any angle for the perfect composition.

## Built With

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
- [![CustomTkinter](https://img.shields.io/badge/CustomTkinter-2C2255?style=for-the-badge&logo=python&logoColor=white)](https://github.com/TomSchimansky/CustomTkinter)
- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- **Python**: Ensure you have the latest version of Python installed. [Python Installation Guide](https://www.python.org/downloads/)
- **Docker**: Ensure you have the latest version of Docker installed. [Docker Installation Guide](https://docs.docker.com/get-docker/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/krishujeniya/PHOTO-EDITOR-USING-CTk.git
   cd PHOTO-EDITOR-USING-CTk
   ```

2. Build the Docker image
   ```sh
   docker build -t photo_editor_ctk .
   ```

3. Step-by-Step Guide to Enable X11 Forwarding in Docker

   **Install XQuartz (macOS) or Xming (Windows)**:
   - **macOS**: Install XQuartz from [XQuartz.org](https://www.xquartz.org/).
   - **Windows**: Install Xming from [Xming.org](https://sourceforge.net/projects/xming/).

   **Allow Connections**:
   - **macOS**: Open XQuartz, go to **Preferences > Security**, and check "Allow connections from network clients".
   - **Windows**: Start Xming with default settings.

   **Run Docker Container with X11 Forwarding**:

   **On Linux**:
   ```sh
   xhost +local:docker
   docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix photo_editor_ctk
   ```

   **On macOS with XQuartz**:
   ```sh
   xhost + 127.0.0.1
   docker run -it --rm -e DISPLAY=host.docker.internal:0 photo_editor_ctk
   ```

   **On Windows with Xming**:
   ```sh
   docker run -it --rm -e DISPLAY=host.docker.internal:0 photo_editor_ctk
   ```

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgments

* [Python](https://www.python.org/)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* [Docker](https://www.docker.com/)
* [Open Source Community](https://opensource.org/)
* [Contributors](https://github.com/krishujeniya/PHOTO-EDITOR-USING-CTk/graphs/contributors)
