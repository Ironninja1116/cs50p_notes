#Practice Set 1 Problem 3

#get input from user
filename = input("Enter a filename: ")

#make input non-case sensitive and non whitespace sensitive
filename = filename.strip().lower()

#shorten filename until last dot is found
while filename.find(".") != -1:
    filename = filename[filename.find(".")+1:]

#find suffix, which occurs after a dot
suffix = filename

#use a match statement to link each extension to its media type
match(suffix):
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
