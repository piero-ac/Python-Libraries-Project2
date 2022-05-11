# Example 2: Insert a title and end credits to a video

# Import the library
from moviepy.editor import * 
import pygame # For previewing the video

# Step 1: Open the video file
cop = VideoFileClip("cultofpersonality.mp4")

# Step 2: Create the Title and End Credits
# Title text and its properties
title_txt = (TextClip("Cult of Personality\nby\nLiving Colour",
				fontsize=40, font="Calibri", color="yellow", size=(640, 480))
			# Center the text vertically and horizontally
			.set_position(("center", "center"))) 
title_clip = title_txt.set_duration(3)

# Title text and its properties
end_txt = (TextClip("Writers:\nCorey Glover\nWilliam Calhoun\nMuzz Skillings\nVernon Reid",
				fontsize=30, font="Calibri", color="yellow", size=(640, 480))
			# Center the text vertically and horizontally
			.set_position(("center", "center")))
end_clip = end_txt.set_duration(3)

# Step 3: Add the Title and End Credits to the video
render = concatenate_videoclips([title_clip, cop, end_clip])

###############################################
#  Circumvent an audio bug with the library   #
#        when previewing the clip             #
###############################################
# aud = render.audio.set_fps(44100)
# render = render.without_audio().set_audio(aud)

# Step 4: Write the video file
# Preview the clip before creating it
# render.preview() 
render.write_videofile("cop_with_credits.mp4")


