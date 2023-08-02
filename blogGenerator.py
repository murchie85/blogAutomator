import os
import random
import datetime

# Define the path to the template
template_path = "/Users/adammcmurchie/code/automated_projects/murchie85.github.io/Template.html"

# Define the path to the values file
values_path = "values.txt"

# Read the values from the values file
with open(values_path, "r") as file:
    lines = file.readlines()

# Map the values to their corresponding variables
PROJECTTITLE = lines[0].strip()
URLTITLE = lines[1].strip()
IMAGEPATH = lines[2].strip()
BLOGDESCRIPTION = lines[3].strip()
INLINETITLE = lines[4].strip()
PAGENAME = lines[5].strip()
MAINCONTENT = "".join(lines[6:]).strip()  # Everything from line 6 onwards is considered part of the main content

output_path = os.path.join(os.path.dirname(template_path), f"{PAGENAME}.html")

# Define the remaining variables
DATE = datetime.date.today().strftime("%Y-%m-%d")  # Today's date
BACKGROUNDIMAGE = f"bg{random.randint(1, 18)}"  # Random value between bg1 and bg18

# Create a dictionary of replacements
replacements = {
    "[PROJECTTITLE]": PROJECTTITLE,
    "[PAGENAME]": PAGENAME,
    "[URLTITLE]": URLTITLE,
    "[IMAGEPATH]": IMAGEPATH,
    "[BLOGDESCRIPTION]": BLOGDESCRIPTION,
    "[INLINETITLE]": INLINETITLE,
    "[MAINCONTENT]": MAINCONTENT,
    "[DATE]": DATE,
    "[BACKGROUNDIMAGE]": BACKGROUNDIMAGE,
}

# Read the template
with open(template_path, "r") as file:
    content = file.read()

# Make replacements
for old, new in replacements.items():
    print(f"Replacing '{old}' with '{new}'")
    content = content.replace(old, new)

# Write the new file
with open(output_path, "w") as file:
    print(f"Writing content to '{output_path}'")
    file.write(content)

print("File written successfully.")
