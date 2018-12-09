import datetime

szakirodalom=[]
array=[]

now = datetime.datetime.now()
date = str(now.strftime("%Y-%m-%d"))

array.append(input("Részfeladat megnevezése: "))
array.append(input("Elvégzett munka rövid leírása: "))
array.append(input("Tapasztalatok: "))

while True:
    x = input("Felhasznált irodalom: ")
    if x=="":
        break
    else:
        szakirodalom.append("<a target=\"_blank\" href=\"")
        szakirodalom.append(x)
        szakirodalom.append("\">") 
        szakirodalom.append(x) 
        szakirodalom.append("</a> ") 

tmp = ""

for i in range(len(szakirodalom)):
    tmp+=szakirodalom[i]

array.append(tmp)

file = open("C:\\Users\\louvre\\Documents\\GitHub\\lorincm.github.io\\munka.html", "r", 10, 'utf-8')
filelines = file.readlines()
file.close()

filelines.insert(len(filelines)-3, "<br></br><table><tr><th>Dátum</th><th>A részfeladat megnevezése</th><th>Elvégzett munka rövid leírása</th><th>Tapasztalatok</th><th>Igénybe vett szakirodalom</th></tr><tr><td>" 
                + date + "</td><td>" + array[0] + "</td><td>" + array[1] + "</td><td>" + array[2] + "</td><td>" + array[3] + "</td></table>\n")

file = open("C:\\Users\\louvre\\Documents\\GitHub\\lorincm.github.io\\munka.html", "w", 10, 'utf-8')

file.writelines(filelines)
file.close()
