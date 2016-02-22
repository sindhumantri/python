x = "/home/dir1/../dir2/./file1.txt"
y = x.split("/")
absolutePath = []
for ele in y:
    if ele == "..":
        absolutePath.pop()
    elif ele == ".":
        continue
    elif ele == "":
        continue
    else:
        absolutePath.append(ele)
print ("/".join(absolutePath))
  
