import re
stg = "Hello world. this is python."
new = re.sub("python", "django", stg)
print(new)