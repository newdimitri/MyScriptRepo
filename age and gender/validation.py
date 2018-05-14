#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import numpy as np

caffe_root = '/opt/caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
caffe.set_mode_gpu()


#Loading the mean image
mean_filename='./mean.binaryproto'
proto_data = open(mean_filename, "rb").read()
a = caffe.io.caffe_pb2.BlobProto.FromString(proto_data)
mean = caffe.io.blobproto_to_array(a)[0]

#Loading the age network
age_net_pretrained = './age_net.caffemodel'
age_net_model_file = './deploy_age.prototxt'
age_net = caffe.Classifier(age_net_model_file,age_net_pretrained,
						mean = mean,
						channel_swap = (2,1,0),
						raw_scale=255,
						image_dims=(256, 256))

#Loading the age network
# age_net_pretrained='./age_net.caffemodel'
# age_net_model_file='./deploy_age.prototxt'
# age_net = caffe.Classifier(age_net_model_file, age_net_pretrained,
#                        mean=mean,
#                        channel_swap=(2,1,0),
#                        raw_scale=255,
#                        image_dims=(256, 256))

#Loading the gender network
gender_net_pretrained='./gender_net.caffemodel'
gender_net_model_file='./deploy_gender.prototxt'
gender_net = caffe.Classifier(gender_net_model_file, gender_net_pretrained,
                       mean=mean,
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))

#Labels
age_list=['(0, 2)','(4, 6)','(8, 12)','(15, 20)','(25, 32)','(38, 43)','(48, 53)','(60, 100)']
gender_list=['m','f']


def go():
	#Reading and plotting the input image
	example_image = address
	input_image = caffe.io.load_image(example_image)
	#_ = plt.imshow(input_image)

	#Age prediction
	age_prediction = age_net.predict([input_image])
	#print 'predicted age:', age_list[age_prediction[0].argmax()]

	#Gender prediction
	gender_prediction = gender_net.predict([input_image])
	#print 'predicted gender:', gender_list[gender_prediction[0].argmax()]

	return [age_list[age_prediction[0].argmax()], gender_list[gender_prediction[0].argmax()]]

def cross_validation():
	#init:
	rightage = wrongage = rightgender = wronggender = 0
	#commender:
	linelist = open('lable.txt').readlines()
	for i in range(2,4480):
		#print ("Round"+ str(i) +':--------------------------------------------')
		everylinelist = linelist[i].split('	')
		#print(everylinelist[0])
		address = '/root/aligned/'+ everylinelist[0] + '/landmark_aligned_face.' + everylinelist[2] + '.' + everylinelist[1]
		#优化：加入全局变量在存出结果，不用调用一次跑一次
		prediction = go()
		#print ("go()[0] is:",go()[0],'everylinelist[3] is:',everylinelist[3]) 发现go()执行中的年龄预测与返回的结果不一致

		if prediction[0] == everylinelist[3]:
			#print("age is correct")
			rightage += 1.0
		else:
			#print("age is wrong")
			wrongage += 1.0
		if everylinelist[4] != 'u':
			if prediction[1] == everylinelist[4]:
				#print("gender is correct")
				rightgender += 1.0
			else:
				#print("gender is wrong")
				wronggender += 1.0
		else:
			continue
		#print('rightage:',rightage,"sum",(rightage+wrongage),'-------',"age_Accuracy:",rightage/(rightage+wrongage))
		#print('rightgender',rightgender,'sum',(rightage+wrongage),'-------',"gender_Accuracy:",rightgender/(rightgender+wronggender))
