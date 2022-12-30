import sqlite3
from moviepy.editor import *
from PIL import Image, ImageOps, ImageDraw, ImageFilter
import numpy
import ffmpeg
import os
import sys
import os.path
import base64
from io import BytesIO
import requests

BAS_DIR = os.path.abspath(os.path.dirname(__file__))
SCRIPTS_DIR = os.path.join(os.path.dirname(BAS_DIR), "script")

def makeBookFrame(pathtoimageOne):
    
    

    rawimg_1 = Image.open(pathtoimageOne)
    
    basewidth = 600
    
 
    
    wpercent = (basewidth/float(rawimg_1.size[0]))
    hsize = int((float(rawimg_1.size[1])*float(wpercent)))
    img_1 = rawimg_1.resize((basewidth,hsize), Image.ANTIALIAS)
    img_1.copy()
    img_1.save(os.path.join(SCRIPTS_DIR,'photo_1/img_b_1.jpg'))

    img_w, img_h = img_1.size
    background_1 = Image.new('RGB', (1920, 1080), (255, 255, 255))
    bg_w, bg_h = background_1.size
    offset_1 = ((bg_w - img_w)//2, (bg_h - img_h)//2)
    background_1.paste(img_1, offset_1)
    background_1.copy()

    width_1, height_1 = background_1.size
    background_1.save(os.path.join(SCRIPTS_DIR,'photo_1/perspective_pre_1.jpg'))

    def find_coeffs(pa, pb):
        matrix = []
        for p1, p2 in zip(pa, pb):
            matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
            matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

        A = numpy.matrix(matrix, dtype=numpy.float)
        B = numpy.array(pb).reshape(8)

        res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
        return numpy.array(res).reshape(8)

    coeffs_1 = find_coeffs(
            [(610, 206), (981, 84), (1354, 574), (952, 737)], # результат координаты
            [(660, 91), (1260, 91), (1260, 988), (659, 988)]) # исходные координаты

    background_1.transform((width_1, height_1), Image.PERSPECTIVE, coeffs_1,
            Image.BICUBIC).save(os.path.join(SCRIPTS_DIR,'photo_1/perspective_b_1.jpg'))

    mask = Image.open(os.path.join(SCRIPTS_DIR, 'materials/alpha050.png'))
    im1 = Image.open(os.path.join(SCRIPTS_DIR,'photo_1/perspective_b_1.jpg'))
    im2 = Image.open(os.path.join(SCRIPTS_DIR,'materials/1050.png'))
    
    im = Image.composite(im1, im2, mask).save(os.path.join(SCRIPTS_DIR,'testimage_1.png'))
    



def makeBookFrameTwo(pathtoimageOne):

    basewidth = 600
    rawimg_2 = Image.open(pathtoimageOne)
    wpercent = (basewidth/float(rawimg_2.size[0]))
    hsize = int((float(rawimg_2.size[1])*float(wpercent)))
    img_2 = rawimg_2.resize((basewidth,hsize), Image.ANTIALIAS)
    img_2.copy()
    img_2.save(os.path.join(SCRIPTS_DIR,'photo_2/img_b_2.jpg'))

    img_w, img_h = img_2.size
    background_2 = Image.new('RGB', (1920, 1080), (255, 255, 255))
    bg_w, bg_h = background_2.size
    offset_2 = ((bg_w - img_w)//2, (bg_h - img_h)//2)
    background_2.paste(img_2, offset_2)
    background_2.copy()

    width_2, height_2 = background_2.size
    background_2.save(os.path.join(SCRIPTS_DIR,'photo_2/perspective_pre_2.jpg'))

    def find_coeffs(pa, pb):
        matrix = []
        for p1, p2 in zip(pa, pb):
            matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
            matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

        A = numpy.matrix(matrix, dtype=numpy.float)
        B = numpy.array(pb).reshape(8)

        res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
        return numpy.array(res).reshape(8)

    coeffs_1 = find_coeffs(
            [(610, 206), (981, 84), (1354, 574), (952, 737)], # результат координаты
            [(660, 91), (1260, 91), (1260, 988), (659, 988)]) # исходные координаты

    background_2.transform((width_2, height_2), Image.PERSPECTIVE, coeffs_1,
            Image.BICUBIC).save(os.path.join(SCRIPTS_DIR,'photo_2/perspective_b_2.jpg'))

    mask = Image.open(os.path.join(SCRIPTS_DIR,'materials/alpha050.png'))
    im1 = Image.open(os.path.join(SCRIPTS_DIR,"photo_2/perspective_b_2.jpg"))
    im2 = Image.open(os.path.join(SCRIPTS_DIR,'materials/1050.png'))
    im = Image.composite(im1, im2, mask).save(os.path.join(SCRIPTS_DIR,'testimage_1.png'))



def makeLetterShoot(pathtoimageOne):

    basewidth = 600
    
    rawimg_3 = Image.open(pathtoimageOne)    
    wpercent = (basewidth/float(rawimg_3.size[0]))
    hsize = int((float(rawimg_3.size[1])*float(wpercent)))
    img_3 = rawimg_3.resize((basewidth,hsize), Image.ANTIALIAS)
    img_3.copy()
    img_3.save(os.path.join(SCRIPTS_DIR,'photo_3/img_b_3.jpg'))

    img_w, img_h = img_3.size
    background_3 = Image.new('RGB', (1920, 1080), (255, 255, 255))
    bg_w, bg_h = background_3.size
    offset_3 = ((bg_w - img_w)//2, (bg_h - img_h)//2)
    background_3.paste(img_3, offset_3)
    background_3.copy()

    width_3, height_3 = background_3.size
    background_3.save(os.path.join(SCRIPTS_DIR,'photo_3/perspective_pre_3.jpg'))


    def find_coeffs(pa, pb):
        matrix = []
        for p1, p2 in zip(pa, pb):
            matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
            matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

        A = numpy.matrix(matrix, dtype=numpy.float)
        B = numpy.array(pb).reshape(8)

        res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
        return numpy.array(res).reshape(8)

    coeffs_1 = find_coeffs(
            [(844, 288), (1264, 405), (1055, 918), (590, 760)], # результат координаты
            [(660, 91), (1260, 91), (1260, 988), (659, 988)]) # исходные координаты

    background_3.transform((width_3, height_3), Image.PERSPECTIVE, coeffs_1,
            Image.BICUBIC).save(os.path.join(SCRIPTS_DIR,'photo_3/perspective_b_3.jpg'))

    mask = Image.open(os.path.join(SCRIPTS_DIR,'materials/letter_alpha.png'))
    im1 = Image.open(os.path.join(SCRIPTS_DIR,"photo_3/perspective_b_3.jpg"))
    im2 = Image.open(os.path.join(SCRIPTS_DIR,'materials/letter.png'))
    im = Image.composite(im1, im2, mask).save(os.path.join(SCRIPTS_DIR,'testimage_2.png'))

if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SCRIPTS_DIR = os.path.join(os.path.dirname(BASE_DIR), "script")
    print( SCRIPTS_DIR)
    # makeBookFrameTwo(os.path.join(SCRIPTS_DIR,"test2.jpg"))
    # makeLetterShoot(os.path.join(SCRIPTS_DIR,"test3.jpg"))

