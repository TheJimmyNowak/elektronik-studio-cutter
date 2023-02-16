from moviepy.editor import *
import os

# Input directory
input_dir = "converted"

# Output file
output_file = "output.mp4"

# Get a list of all the .vob files in the input directory and its subdirectories
input_files = []
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith((".vob", ".VOB")):
            input_files.append(os.path.join(root, file))

# Create an empty list to store the video clips
clips = []

# Loop through the input files and add each one to the list of clips
for input_file in input_files:
    clip = VideoFileClip(input_file)
    clips.append(clip)

# Concatenate the clips together
final_clip = concatenate_videoclips(clips)

# Write the final clip to the output file
final_clip.write_videofile(output_file, codec='mpeg4')

