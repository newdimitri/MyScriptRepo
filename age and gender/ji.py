#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from sys import argv
from skimage import io
from abc import ABCMeta,abstractmethod
import json
from validation import * #has been init when import
import logging as lg
from PIL import Image, ImageDraw
import dlib
import cv2

caffe.set_mode_cpu()
lg.info("ok")
class ji(object):
    __metaclass__ = ABCMeta
    #@abstractmethod
    def __init__(self):
        pass
    '''
    def calc(self, address, jsonn, out_file=None):
        #jsonn = '{"face_num" : 103,"image_height" : 1080,"image_width" : 1920,"info" : "FOR EVALUATION ONLY","result" : [{"angry" : 0.0,"disgust" : 0.0,"fear" : 0.09375,"happy" : 0.0625,"neutral" : 0.15625,"pos_lt" : {"x" : 108,"y" : 787},"pos_rb" : {"x" : 161,"y" : 848},"sad" : 0.0,"surprise" : 0.640625},{"angry" : 0.0,"disgust" : 0.03125,"fear" : 0.0,"happy" : 0.953125,"neutral" : 0.0,"pos_lt" : {"x" : 1127,"y" : 769},"pos_rb" : {"x" : 1170,"y" : 821},"sad" : 0.0,"surprise" : 0.0}],"status" : "OK"}'
        res = json.loads(jsonn,encoding="utf-8")
        print ('i: '+str(len(res['result'])))
        llist = []
        for i in range(len(res['result'])):
            print ("round: ",i,':')
            ress = []
            ress.append(res['result'][i]['pos_lt']['x'])
            ress.append(res['result'][i]['pos_lt']['y'])
            ress.append(res['result'][i]['pos_rb']['x'])
            ress.append(res['result'][i]['pos_rb']['y'])
            print (ress)
            img = Image.open(address)
            img2 = img.crop(ress)
            img2.save("tmp.jpg")
            resss = {}
            try:
                input_image = caffe.io.load_image("tmp.jpg")
                gender_prediction = gender_net.predict([input_image])
                resss["gender"] = gender_list[gender_prediction[0].argmax()]
                llist.append(resss)
                #resss["gender"+str(i)] = gender_list[gender_prediction[0].argmax()]
                #return json.dumps({"gender" : gender_list[gender_prediction[0].argmax()]})
            except IOError:
                return -1
            except Exception:
                return 0
            #else:
                #return 1
        sdf = {}
        sdf["result"] = llist
        sdf = json.dumps(sdf)
        return sdf
    '''
    def calc(self, address, out_file = None):
        llist = []
        detector = dlib.get_frontal_face_detector()
        f = address
        #print("Processing file: {}".format(f))
        img = io.imread(f)
        # The 1 in the second argument indicates that we should upsample the image
        # 1 time.  This will make everything bigger and allow us to detect more
        # faces.
        word = Image.open(address)
        draw = ImageDraw.Draw(word)
        dets = detector(img, 1)
        #print("Number of faces detected: {}".format(len(dets)))
        ressss = {}
        for i, d in enumerate(dets):
            #print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(i, d.left(), d.top(), d.right(), d.bottom()))
            ress = []
            ress=[d.left(), d.top(), d.right(), d.bottom()]
            img = Image.open(address)
            img2 = img.crop(ress)
            img2.save("tmp.jpg")
            resss = {}
            try:
                input_image = caffe.io.load_image("tmp.jpg")
                gender_prediction = gender_net.predict([input_image])
                resss["gender"] = gender_list[gender_prediction[0].argmax()]
                
                if(gender_list[gender_prediction[0].argmax()]=="f"):
                    draw.text((d.left(),d.top()-50),u'Female',fill = "#00ff00")
                    word.save("out.jpg")
                if(gender_list[gender_prediction[0].argmax()]=="m"):
                    draw.text((d.left(),d.top()-50),u'Male',fill = "#00ff00")
                    word.save("out.jpg")
                resss["coordinate"] = ress
                llist.append(resss)
                #resss["gender"+str(i)] = gender_list[gender_prediction[0].argmax()]
                #return json.dumps({"gender" : gender_list[gender_prediction[0].argmax()]})
            except IOError:
                return -1
            except Exception:
                return 0
        #imgout = Image.open(address)
        #draw =ImageDraw.Draw(imgout)
        imgout = cv2.imread("out.jpg")
        for i, d in enumerate(dets):
            aa = d.left()
            bb = d.top()
            cc = d.right()
            dd = d.bottom()
            #print((aa,bb),(cc,dd))
            draw0 = cv2.rectangle(imgout,(aa,bb),(cc,dd),(0,255,0),2)
        cv2.imwrite("out.jpg",draw0)
        sdf = {}
        sdf["result"] = llist
        sdf = json.dumps(sdf)
        return sdf
        
if __name__ == '__main__':
    shi = ji()
    print(shi.calc(argv[1]))
    try:
        if argv[1] == "test":
            print("in")
            shi = ji()
            linelist = open('lable.txt').readlines()
            for i in range(2,4480):
                everylinelist = linelist[i].split('	')
                #print(everylinelist[0])
                address = '/root/aligned/'+ everylinelist[0] + '/landmark_aligned_face.' + everylinelist[2] + '.' + everylinelist[1]
                #优化：加入全局变量在存出结果，不用调用一次跑一次
                print(json.loads(shi.calc(address)))
    except Exception as e:
        lg.info("wrong")
    else:
        lg.info("non-existent")
