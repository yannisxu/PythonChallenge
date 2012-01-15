#3th
filter="abcdefghijklmnopqrstuvwxyz";
fileHandle = open('sources/2.txt');
string = fileHandle.read();
for char in filter:
    if(string.count(char)>0):
        print char;


