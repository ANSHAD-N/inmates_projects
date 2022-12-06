import re

pattern = "[A-Z][0-9][a-z]"


if re.search(pattern,"A6k"):
    print("matched")
else:
    print("not matched")
