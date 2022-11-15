from difflib import SequenceMatcher
with open("textfile2.txt") as file1, open("testfile2.txt") as file2:
    file1data=file1.read()
    file2data=file2.read()
    similarity=SequenceMatcher(None,file1data,file2data).ratio()
    per=similarity*100
    print(per)
    allowed=int(input("ENTER THE PERCENT OF PLAGIARISM ALLOWED"))
if(per<allowed):
    print("THIS CODE IS NOT COPIED")
elif(per>allowed):
    print("YOU COPIED")
else:
    print(":)")
