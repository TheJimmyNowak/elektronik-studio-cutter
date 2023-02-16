from moviepy.video.io.VideoFileClip import VideoFileClip
import os

input_dir = "filmy"
output_dir = "converted"
subpart_duration = 5
number_of_subparts = 2

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for root, dirs, files in os.walk(input_dir):
    for f in files:
        if f.endswith(('.vob', '.VOB')):
            # Load the video clip
            clip = VideoFileClip(root + "/" + f)
            
            subpart_output = os.path.join(output_dir, root)
            if not os.path.exists(subpart_output):
                os.makedirs(subpart_output)

            for i in range(number_of_subparts):
                # Get the duration of the video
                duration = clip.duration

                # Calculate the start and end times for the 10 second clip
                start = (duration / 2) - (subpart_duration/2) - i*subpart_duration
                end = (duration / 2) + (subpart_duration/2) - i*subpart_duration

                output_path = os.path.join(subpart_output, "{}{}".format(i, f))
                subclip = clip.subclip(start, end)
                subclip = subclip.without_audio()
                subclip.write_videofile(output_path, codec='mpeg2video')

