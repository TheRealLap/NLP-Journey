# Library Imports
import re
# re is used though regex is more up to date and more powerful

# Define key words to look for

# Match greetings that starts with hi or hello or hey, follow by any number of space, follow by any letter/numbers
r = "(hi|hello|hey)[ ]*([a-z]*)"

# Example Message
Prompt = [None]*3
Prompt[0] = "Hello Rosa"
Prompt[1] = "Hi ho, hi ho, blah blah blah" 
Prompt[2] = "Hey, what's up"

# Check match
for message in Prompt:
    print(re.match(r,message,flags=re.IGNORECASE))
 