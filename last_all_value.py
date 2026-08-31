ls=[90,"hello",34,"hello",123,"hello",66,"hello"]
ls_dublicate_clone = ls.copy()
for index,valaue in enumerate(ls_dublicate_clone):
    if valaue =="hello":
        ls.append(s.pop(ls_dublicate_clone))
        print(ls)
print(ls_dublicate_clone)