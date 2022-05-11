# Example 1: Attain a Wikipedia Page’s Information In Your Desired Language
# Link for language prefixes: 
# https://meta.wikimedia.org/wiki/List_of_Wikipedias

# import the library
import wikipedia

# Step 1: Create the output file
portugal_file = open("pt_output.txt", "w")
mexico_file = open("es_output.txt", "w")

# Step 2: Change the language for the Wikipedia API
wikipedia.set_lang("pt") # pt - Portuguese

# Step 3: Create the Wikipedia Page
portugal = wikipedia.WikipediaPage("Portugal")
print("\nPORTUGAL\n", file=portugal_file)

# Step 4: Attain the page's content
print(portugal.content, file=portugal_file)
print("\n\n", file=portugal_file)

# Step 2: Change the language for the Wikipedia API
wikipedia.set_lang("es") # es - Spanish

# Step 3: Create the Wikiepdia Page
mexico = wikipedia.WikipediaPage("Mexico")
print("\nMEXICO\n", file=mexico_file)

# # Step 4: Attain the page's content
print(mexico.content, file=mexico_file)
print("\n\n", file=mexico_file)

portugal_file.close() # Close the file
mexico_file.close() # Close the file



