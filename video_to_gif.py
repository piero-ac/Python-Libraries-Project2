# Main Program: Video to GIF based on User Input
# Expansion of MoviePy Example 1

# Prerequisites:
# install moviepy using <pip install moviepy>
# install pygame using <pip install pygame>
# install ImageMagick (different for MacOS and Windows Users)
# Make sure video is in the same folder as the script

# Necessary imports
from moviepy.editor import *
import pygame # For previewing the video

# Welcome Message
print("Welcome to the Video to GIF Convertor")

# Step 1: Ask for the filename from the user
filename = input("Please enter the Name of the Video File including the Extension\n")
print()

# Loop to redo the GIF creation until the user is satisfied
while True:

	# Step 2: Ask for the start and end times of the subclip 
	# the user wants to convert to a GIF
	print("\nNow enter the start and end times for the subclip in the following format: min, sec")
	print("Ex: For 19 seconds enter: 0, 19.00")
	start = input("Please enter the START TIME: ")
	start = start.split(", ")
	start = [float(start[0]), float(start[1])] # Convert the string values to floats
	end = input("Please enter the END TIME: ")
	end = end.split(", ")
	end = [float(end[0]), float(end[1])] # Convert the string values to floats
	print()

	# Step 3: Ask the user for the speed they'd like to have in the GIF
	speed = float(input("Please enter the speed you'd like for the GIF.\nEx: For 0.5x speed enter 0.5, For 2x speed enter 2\n"))

	# Step 4: Create the GIF based on the user inputs
	clip = (VideoFileClip(filename)
					# Select the clip between the user specified times
					.subclip((start[0], start[1]), (end[0], end[1]))
					 # Speed up the video to the user specifed speed 
					.speedx(speed))
	print()

	# Step 5: Ask the user whether they'd like to add text to the GIF
	add_text = input("Would you like to add text to the GIF? (y/n) ")

	if add_text.lower() == "y":
		text = input("Enter the text to add to the GIF:\n")
		fontsize = int(input("Enter the fontsize (integer) for the text : "))
		color = input("Enter the color for the text: ")
		v_position = input("Enter the vertical positioning of the text.\nOptions: 'center', 'top', 'bottom'\n")

		# Text and its properties
		gif_text = (TextClip(text, fontsize=fontsize, color=color, font="Arial")
					.set_pos(("center", v_position)) # Positioning of the text
					.set_duration(clip.duration)) # Duration of the text

		# Composite the video AKA. Add the text to the GIF
		composition = CompositeVideoClip([clip, gif_text])
	print()

	# Step 6: Ask the user whether they'd like to preview the GIF
	preview = input("Would you like to preview the GIF? (y/n) ")

	# Preview the GIF with the text
	if preview.lower() == "y" and add_text.lower() == "y":
		composition.preview(fps=25, audio=False)
	# Preview just the clip, no text
	else: 
		clip.preview(fps=25, audio=False)
	print()

	# Step 7: Ask the user if they are satisfied with the GIF
	satisfied = input("Are you satisfied with the GIF? (y/n) ")

	# Write the clip to a GIF if the user is satisfied
	if satisfied.lower() == "y":
		gif_filename = input("Save as: ")
		gif_filename += ".gif"

		# Write the clip to a GIF with text
		if add_text.lower() == "y":
			composition.write_gif(gif_filename, fps=25)
		# Write the clip to a GIF without text
		else:
			clip.write_gif(gif_filename, fps=25)

		break # Break out of the loop if the user is satisfied






