import json
mpath = "MPI.json"


with open(mpath, 'r') as f:
    data = json.load(f)
for i in range(len(data["root"])):
	print("第%d轮:"%i)
	cocotype= []
	MPIdata = data["root"][i]['joint_self']
	zzero = [0.000,0.000,2.000]
	if (len(MPIdata) == 16):
		cocotype.append(MPIdata[9])
		cocotype.append(zzero)
		cocotype.append(zzero)
		cocotype.append(zzero)
		cocotype.append(zzero)
		cocotype.append(MPIdata[13])
		cocotype.append(MPIdata[12])
		cocotype.append(MPIdata[14])	
		cocotype.append(MPIdata[11])
		cocotype.append(MPIdata[15])
		cocotype.append(MPIdata[10])
		cocotype.append(MPIdata[3])
		cocotype.append(MPIdata[2])
		cocotype.append(MPIdata[4])
		cocotype.append(MPIdata[1])
		cocotype.append(MPIdata[5])
		cocotype.append(MPIdata[0])
		data["root"][i]['joint_self'] = cocotype
	else:
		print("joint_self有多个")
		
	print("第%d轮的joint_self结束"%i)

	cocotype= []
	print(MPIdata,"1")
	try:
		MPIdata = data["root"][i]['joint_others']
	except Exception as e:
		print("wwwwwwwwww")
	else:
		pass
	
	print(MPIdata)
	zzero = [0.000,0.000,2.000]
	if type(MPIdata) == type([]):
		if (str(type(MPIdata[0][0])) == "<class 'float'>" ):
			cocotype.append(MPIdata[9])
			cocotype.append(zzero)
			cocotype.append(zzero)
			cocotype.append(zzero)
			cocotype.append(zzero)
			try:
				cocotype.append(MPIdata[13])
			except Exception as e:
				cocotype.append(zzero)
			finally:
				pass
			try:
				cocotype.append(MPIdata[12])
			except Exception as e:
				cocotype.append(zzero)
			finally:
				pass
			try:
				cocotype.append(MPIdata[14])
			except Exception as e:
				cocotype.append(zzero)
			finally:
				pass	
			try:
				cocotype.append(MPIdata[11])
			except Exception as e:
				cocotype.append(zzero)
			finally:
				pass
			try:
				cocotype.append(MPIdata[15])
			except Exception as e:
				cocotype.append(zzero)
			finally:
				pass
			try:
				cocotype.append(MPIdata[10])
			except Exception as e:
				cocotype.append(zzero)
			finally:
				pass
			cocotype.append(MPIdata[3])
			cocotype.append(MPIdata[2])
			cocotype.append(MPIdata[4])
			cocotype.append(MPIdata[1])
			cocotype.append(MPIdata[5])
			cocotype.append(MPIdata[0])
			data["root"][i]['joint_others'] = cocotype
			print("第%d轮的joint_others只有一组，结束"%i)
			print("头部为",MPIdata[0])
		else:
			tempcocotype = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
			if (str(type(MPIdata)) == "<class 'list'>"):
				for ii in range(len(MPIdata)):
					print("第%d轮的joint_others有%d组,现在在第%d组"%(i,len(MPIdata),ii))
					print("第%d轮的joint_others的头部为"%i,MPIdata[ii][0])
					#print(ii,MPIdata[ii][14])
					tempcocotype[ii].append(MPIdata[ii][9])
					tempcocotype[ii].append(zzero)
					tempcocotype[ii].append(zzero)
					tempcocotype[ii].append(zzero)
					tempcocotype[ii].append(zzero)
					try:
						tempcocotype[ii].append(MPIdata[ii][13])
					except Exception as e:
						tempcocotype[ii].append(zzero)
					finally:
						pass
					tempcocotype[ii].append(MPIdata[ii][12])
					try:
						tempcocotype[ii].append(MPIdata[ii][14])
					except Exception as e:
						tempcocotype[ii].append(zzero)
					finally:
						pass

					tempcocotype[ii].append(MPIdata[ii][11])
					try:
						tempcocotype[ii].append(MPIdata[ii][15])
					except Exception as e:
						tempcocotype[ii].append(zzero)
					finally:
						pass
					
					tempcocotype[ii].append(MPIdata[ii][10])
					tempcocotype[ii].append(MPIdata[ii][3])
					tempcocotype[ii].append(MPIdata[ii][2])
					tempcocotype[ii].append(MPIdata[ii][4])
					tempcocotype[ii].append(MPIdata[ii][1])
					tempcocotype[ii].append(MPIdata[ii][5])
					tempcocotype[ii].append(MPIdata[ii][0])
			cocotype.append(tempcocotype)
	#print(data["root"][i],'\n---------------------------------------------------------------------------------------------------------------')
with open("out.json", 'a') as f:
	f.write(json.dumps(data))
#print (json.dumps(data))



print (data)
# for i in enumerate(cocotype):
# 	print (i)
            # % In coco-mpi:(1<-9, 2<-00, 3<-00, 4<-00, 5<-00, 6<-13, 7<-12, 8<-14, 9<-11, 10<-15, 
            # %            11<-10, 12<-3, 13<-2, 14<-4, 15<-1, 16<-5, 17<-0

