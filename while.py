#While Looping, if, continue

data = 0

while data < 8:
    print("Looding Looping: ",data)

    if data == 5:
        print(">>> ",data)
        
        data += 1 #Akan dieksekusi jika nilai if terpenuhi
        continue
        
    data += 1 #Menambahkan nilai data sampai nilai if terpenuhi

else:
    print(">>> ",data) 
print("YOLLOW")