f=open("Random_seek_tell.txt","rb")
f.seek(4)
print(f.read(3))
f.seek(-5,2)
print(f.read())
print(f.tell())
f.close()
