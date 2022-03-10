import base64
import binascii

#REPLACE THE FILE PATH BELOW
a_file = open("C:/Users/YOUR USER NAME HERE/WHERE YOUR INPUT TXT IS/yourfilename.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(stripped_line)

a_file.close()


decode = "non"
liste_finale = []

def process(list_of_lists):
    for chose in list_of_lists:
        if chose.startswith("aHR0") == True:
            truc = base64.b64decode(chose + '==')
            decodi = truc.decode('UTF-8', errors='replace')
            liste_finale.append(decodi)
        else:
            liste_finale.append(chose)

process(list_of_lists)
#REPLACE THE FILE PATH BELOW
f=open('C:/Users/YOUR USER NAME HERE/WHERE YOU WANT YOUR OUTPUT TXT TO BE/export.txt','w', encoding="utf-8")
for ele in liste_finale:
    f.write(ele+'\n')
f.close()

print(liste_finale)
