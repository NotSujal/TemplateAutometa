import json
import sys


templatefile  = "template.txt"
infofile = "info.json"

if (len(sys.argv)>2):
    templatefile = sys.argv[1]
    infofile = sys.argv[2]

# load template
with open(templatefile, "r") as f:
    template = f.read()

# load info file
with open(infofile, "r") as f:
    info = json.load(f)

# execution
for key, value in info.items():
    new = template
    for i in range(len(value)):
        new = new.replace(f"${i}", value[i])
    #save files
    with open(key,"w") as f:
        f.write(new)
    print("generated ",key)


print("completed")