import os

list1 = []
img_path = "D:\_code\auto_make_book\_covers"
files = os.listdir(img_path)
for file in files:
  list1.append(file)

list2 = []
pdf_path = "D:\_code\auto_make_book\_books"
files = os.listdir(pdf_path)
for file in files:
  list2.append(file)

list3 = [item.replace(".png","") for item in list1]
list4 = [item.replace(".pdf","") for item in list2]

list5 = [item for item in list3 if item not in list4]

print(list5)
