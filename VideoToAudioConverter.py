import os
from moviepy.editor import VideoFileClip

class VideoToAudioConverter:
    def __init__(self, video_file, output_folder=None, output_filename=None):
        self.video_file = video_file
        self.output_folder = output_folder if output_folder else "audios"  # Default to "audios"
        self.output_filename = output_filename

    def _check_and_create_folder(self):
        # Checks if the output folder exists and creates it if it does not exist.
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def _split_filename_extension(self, filename):
        # Splits the filename into base name and extension
        base_name, extension = os.path.splitext(filename)
        return base_name, extension

    def _generate_output_mp3_filename(self):
        # Generates the output MP3 filename based on user input or default behavior
        if self.output_filename:
            base_name, ext = self._split_filename_extension(self.output_filename)
            output_mp3 = os.path.join(self.output_folder, base_name + ".mp3")
        else:
            base_name, ext = self._split_filename_extension(os.path.basename(self.video_file))
            output_mp3 = os.path.join(self.output_folder, base_name + ".mp3")
        
        # Handle filename collisions by appending _1, _2, etc.
        count = 1
        while os.path.exists(output_mp3):
            base, ext = os.path.splitext(output_mp3)
            output_mp3 = f"{base}_{count}{ext}"
            count += 1
        
        return output_mp3

    def _convert_to_mp3(self):
        # Performs the video to MP3 conversion process.
        try:
            self._check_and_create_folder()  # Ensure output folder exists

            # Generate the output MP3 filename
            output_mp3 = self._generate_output_mp3_filename()

            # Load video, extract audio, and save as MP3
            video = VideoFileClip(self.video_file)
            audio = video.audio
            audio.write_audiofile(output_mp3)

            print(f"MP3 file saved as: {output_mp3}")

        except Exception as e:
            print(f"Error converting video to mp3: {e}")

    def convert_to_mp3(self):
        # Public method to initiate the conversion process
        self._convert_to_mp3()

    @staticmethod
    def convert_video_to_mp3(video_file, output_folder=None, output_filename=None):
        # Static method to convert video to MP3
        try:
            output_folder = output_folder if output_folder else "audios"  # Default to "audios"
            # Create the output folder if it does not exist
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Generate the output MP3 filename
            if output_filename:
                base_name, ext = os.path.splitext(output_filename)
                output_mp3 = os.path.join(output_folder, base_name + ".mp3")
            else:
                base_name, ext = os.path.splitext(os.path.basename(video_file))
                output_mp3 = os.path.join(output_folder, base_name + ".mp3")

            # Handle filename collisions by appending _1, _2, etc.
            count = 1
            while os.path.exists(output_mp3):
                base, ext = os.path.splitext(output_mp3)
                output_mp3 = f"{base}_{count}{ext}"
                count += 1

            # Load video, extract audio, and save as MP3
            video = VideoFileClip(video_file)
            audio = video.audio
            audio.write_audiofile(output_mp3)

            print(f"MP3 file saved as: {output_mp3}")

        except Exception as e:
            print(f"Error converting video to mp3: {e}")

if __name__ == "__main__":
    # Example usage
    video_file = "videos/happy-nation.mp4"

    # Conversion via non-static method with custom output filename
    convertor = VideoToAudioConverter(video_file, output_filename="custom_output_name.mp3")
    convertor.convert_to_mp3()

    # Conversion via non-static method without specifying output filename
    convertor_default = VideoToAudioConverter(video_file, output_folder="audios")
    convertor_default.convert_to_mp3()

    # Conversion via static method with custom output filename
    VideoToAudioConverter.convert_video_to_mp3(video_file, output_filename="static_custom_output.mp3")

    # Conversion via static method without specifying output filename
    VideoToAudioConverter.convert_video_to_mp3(video_file, output_folder="audios")