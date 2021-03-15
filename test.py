try:
    f = open("try.txt")
    r = f.read()
except:
    print("File Error exists please che")
    
finally:
    f.close()

lst = r.split(",")

lst = [*map(int, lst)]
print(lst)


lst.sort(key=lambda  x : x%100)
print(lst)

f = open("output.txt","w")
for i in lst:
    f.write(str(i)+",")
    
f.close()



