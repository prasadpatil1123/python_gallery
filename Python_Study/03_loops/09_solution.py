items = ["app", "bana","app","hunt"]
uniq = set()

for item in items:
    if item in uniq:
        print("Duplicate :", item)
        break
    uniq.add(item)