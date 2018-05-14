#coding=utf-8
import xml.etree.ElementTree as ET
import os

pathh = "hebing2\\Annotations\\"
for filenames in os.walk(pathh):
	filenames = list(filenames)
	filepath = filenames[0]
	filenames = filenames[2]
	#os.mkdir(path = "labels\\")
	for filename in filenames:
		print(filepath+filename)
		with open(filepath+filename,encoding='utf-8') as infile:
			tree = ET.parse(infile)
			root = tree.getroot()
			#n = 0
			number = []
			for obj in root.findall("object"):
				number.append(obj.find('name').text)
				print(number)
				#n += 1
			for i in range(len(number)):
				#print("labels\\"+filename[:-4]+'-'+str(i)+".txt")
				with open("labels\\"+filename[:-4]+'-'+str(i)+".txt",'w',encoding='utf-8') as outfile:
					outfile.write(number[i])
