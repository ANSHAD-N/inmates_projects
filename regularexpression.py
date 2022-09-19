import re

pattern = "python"

if re.match(pattern, "world of python programming"):
    print("matched")
else:
    print("not matched")