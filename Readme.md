# Video to Audio Converter
> [!NOTE]
> This project contains a python class `VideoToAudioConverter`, that can convert a .mp4 file into .mp3

## Features

- Convert video files to MP3 format.
- Handle filename collisions by appending `_1`, `_2`, etc. to the output file.
- Specify custom output folder and output filename.
- Automatically create the output folder if it does not exist.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Muhammad-Shah-zaib/video-to-audio-converter
    cd video-to-audio-converter
    ```

2. Installing the moviepy:
    ```sh
    pip install moviepy
    ```

## Usage

### Example Usage

#### Using Instance Methods

1. Convert a video to MP3 with a custom output filename:
    ```python
    from converter import VideoToAudioConverter

    video_file = "videos/happy-nation.mp4"
    converter = VideoToAudioConverter(video_file, output_filename="custom_output_name.mp3")
    converter.convert_to_mp3()
    ```

2. Convert a video to MP3 with custom output foldername:
    ```python
    from converter import VideoToAudioConverter

    video_file = "videos/happy-nation.mp4"
    converter = VideoToAudioConverter(video_file, output_folder="custom-folder-name")
    converter.convert_to_mp3()
    ```
3. Converter a video to MP3 with default filename and foldername:
    ```python
    ffrom converter import VideoToAudioConverter

    video_file = "videos/happy-nation.mp4"
    converter = VideoToAudioConverter(video_file)
    '''
     THE DEFAULT FILENAME IS EXTRACTED FROM THE VIDEO BASENAME
     AND THE DEFAULT FOLDER NAME IS 'audios'
    '''
    converter.convert_to_mp3()
    ``` 


#### Using Static Method

1. Convert a video to MP3 with a custom output filename:
    ```python
    from converter import VideoToAudioConverter

    video_file = "videos/happy-nation.mp4"
    VideoToAudioConverter.convert_video_to_mp3(video_file, output_filename="static_custom_output.mp3")
    ```

2. Convert a video to MP3 without specifying the output filename:
    ```python
    from converter import VideoToAudioConverter

    video_file = "videos/happy-nation.mp4"
    VideoToAudioConverter.convert_video_to_mp3(video_file, output_folder="audios")

## File strcuture
project_folder/
│
├── converter.py # Contains the VideoToAudioConverter class
├── videos/ # Directory containing video files
│ └── happy-nation.mp4 # Example video file for testing purposes
└── audios/ # Directory to save the converted MP3 files

> [!TIP]
> I also have provided a **happy-nation.mp4** file in **videos** folder that you can use for testing.