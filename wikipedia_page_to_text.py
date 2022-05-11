# Main Program
# Create a text file of the specified Wikipedia Page

# Import the Library
import wikipedia
import pyfiglet # This library is for the banner art

banner = pyfiglet.figlet_format("Wikipedia Page to Text File")
print(banner)

# Step 1. Ask the user for what wikipedia page they'd like to get
user_input = input("What Wikipedia Page would you like? ")

print("-" * 50) # Separate the steps in CLI

# Step 2. Show a list of search suggestions based on input and 
# User choses one of the suggestions
suggestions = wikipedia.search(user_input)
print("List of Suggestion Based on Search Term: ", user_input)
for i in range(len(suggestions)):
	print(f"{i + 1}. {suggestions[i]}")
user_choice = int(input("\nChoose from the list of search suggestions: "))
user_choice = suggestions[user_choice-1]
print("Your choice: ", user_choice)

print("-" * 50) # Separate the steps in CLI

# Step 3. Ask the user what they would like to get from the page
# This includes a summary, image links, references, 
# plain text of the content, and/or the page's html

# Create the Wikipedia Page Object for the user's choice
page = wikipedia.WikipediaPage(user_choice)

# Show a list of things they can get from the page
print(f"What would you like to get \nfrom the Wikipedia Page for {user_choice}?")
print("\nChoices to Choose From:")
print("1. Summary (Enter 'summary')")
print("2. Image Links (Enter 'images')")
print("3. References (Enter 'references')")
print("4. Plain Text Content (Enter 'content')")
print("5. Get the Page's HTML (Enter 'html')")
print("\nEnter choices as a comma separated list. Ex: summary, references, html")

# Save the user's choices
user_page_choices = input("Enter choices here: ")
# Convert the user's choices to a list
user_page_choices = user_page_choices.split(", ")

print("-" * 50) # Separate the steps in CLI

# Step 4. Create a text file of all the content they want
filename = user_choice + ".txt" # filename is Wikipedia Page's Title/ID
# Create the file
f = open(filename, 'w')

# Write the title for the text file
print(f"TEXT FILE FOR {user_choice}\n", file=f)

# Add to the file, what the user requested
if "summary" in user_page_choices:
	print("\nPAGE SUMMARY\n", file=f)
	print(page.summary, file=f)
	print("*Summary added to text file*")

if "images" in user_page_choices:
	print("\nURLS OF IMAGES IN PAGE\n", file=f)
	for i in range(len(page.images)):
		print(f"{i+1}. {page.images[i]}", file=f)
	print("*Image links added to text file*")

if "references" in user_page_choices:
	print("\nURLS OF EXTERNAL LINKS IN PAGE\n", file=f)
	for i in range(len(page.references)):
		print(f"{i+1}. {page.references[i]}", file=f)
	print("*External links added to text file*")

if "content" in user_page_choices:
	print("\nPAGE IN PLAIN TEXT\n", file=f)
	print(page.content, file=f)
	print("*Plain text content added to text file*")

if "html" in user_page_choices:
	print("\nPAGE'S HTML\n", file=f)
	print(page.html(), file=f)
	print("*Page's html added to text file*")

print("Text file successfully created!")
f.close()


