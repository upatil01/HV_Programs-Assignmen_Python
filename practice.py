def writefile(data):
    fileObject = open("Student2.csv", "a")
    data = "\n" + data
    fileObject.write(data)
data = input()    
writefile(data)    

