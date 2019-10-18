import re
a = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for i in a:
    print(re.sub(r" ?\([^)]+\)", "", i))
