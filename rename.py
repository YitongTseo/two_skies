import os
import re
import pdb

folder_path = "/chapters"  # Replace this with the path to your folder
output_filename = "Full_Text.txt"  # Name for the output combined file

def make_human_readable(text):
    # Regular expression to match only Latin characters, Arabic numbers, and standard punctuation
    pattern = re.compile(r"[\x20-\x7E]+")
    
    # Find all matches of the pattern in the text
    matches = pattern.findall(text)
    
    # Combine the matched characters into a single string
    filtered_text = ''.join(matches)
    return filtered_text

def index_filename(file):
    print(file)
    part = int(re.findall(r'\d+', file.split('_')[0])[0]) * 100
    if '-Title' in file:
        return part - 1
    
    chapter = int(re.findall(r'\d+', file.split('_')[1])[0])
    return part + chapter

files = os.listdir(folder_path)
files.sort(key=index_filename)

# Collect the content of all text files and filter for human-readable characters
all_contents = []
for filename in files:
    if os.path.isfile(os.path.join(folder_path, filename)) and filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            all_contents.append((filename, make_human_readable(content)))  # Store filename along with content

# Combine contents with file names as dividers
combined_content = ""
for filename, content in all_contents:
    combined_content += f"File: {filename}\n\n{content}\n\n{'='*40}\n"

# Write the combined content to the output file
output_filepath = os.path.join(folder_path, output_filename)
with open(output_filepath, 'w', encoding='utf-8') as output_file:
    output_file.write(combined_content)

print(f"Combined content with dividers saved to '{output_filename}'.")
