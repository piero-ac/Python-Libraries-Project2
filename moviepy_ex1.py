# Example 1: Get a clip from a video file, turn it into a GIF
# and add text

# Import the library
from moviepy.editor import *
import pygame # For previewing the video

# Step 1: Open the video file
# Select the video file located in the same folder
surfing_clip = (VideoFileClip("surfing-fails.mp4")
				# Select the clip between 19s and 27s 
				.subclip((0,19.00), (0,27.00))
				# Resize the video to 90% of its original size 
				.resize(0.9)
				 # Speed up the video to 1.5x 
				.speedx(1.5))

# Step 2: Add text to the GIF 
# Text and text properties
text = (TextClip("WHEN YOU TRY SURFING WITH FRIENDS",
				 fontsize=30, color='black', font='Arial', interline=-25)
		.set_pos((60, 0)) # Positioning of the text
		.set_duration(surfing_clip.duration)) # Duration of the text

# Step 3: Composite the video (requires ImageMagick)
composition = CompositeVideoClip([surfing_clip, text])
# Preview the clip before creating it
# composition.preview(fps=25, audio=False) 
composition.write_gif('surfing_clip.gif', fps=25)

