# Example 2: Attain a Wikipedia Page’s Image Links and
# Use urllib to Download the Images

import wikipedia
import urllib.request as re

# Step 1: Create the output html file and images folder
peruFile = open("peru.txt", "w")

# Step 2: Create the WikipediaPage Object
peruPage = wikipedia.WikipediaPage("Peru")

# Step 3: Get the Page's Image Links and Export it to the file
images = peruPage.images
for link in images:
	print(link, file=peruFile)
peruFile.close() # Close the file

# Step 4: Read all of the lines in the file
with open("peru.txt", "r") as f:
	unparsed_urls = f.readlines()

# Step 5: Remove the newline characters
parsed_urls = [url.replace("\n", "") for url in unparsed_urls]

# Step 6: Call the urllib library's urlretrieve method
# to request the image from the specified URL
image_filename = ""
for i in range(len(parsed_urls)):
	image_filename = "Image" + str(i+1)
	url = parsed_urls[i]
	re.urlretrieve(parsed_urls[i], image_filename)

	
