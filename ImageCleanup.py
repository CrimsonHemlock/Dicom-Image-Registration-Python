#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:16:19 2020

@author: Wayan A. Fontaine-Seiler

EXTENSION

Image Cleanup Extension for use in the main registration program

Dependencies: None
"""
## ROUGHT IMAGE CLEANUP PROGRAM (AFTER TRANSFORM BY SIMPLEELASTIX)##

import numpy as np
import matplotlib as plt
from PIL import Image # Image manipulation in Python

def IsArtefact(image_nda_unint8,i,j,aggres):
    sum_pix=0
    sum_pix=sum_pix+image_nda_unint8[i,j+1]
    sum_pix=sum_pix+image_nda_unint8[i,j-1]
    sum_pix=sum_pix+image_nda_unint8[i+1,j]
    sum_pix=sum_pix+image_nda_unint8[i-1,j]
    sum_pix=sum_pix+image_nda_unint8[i-1,j-1]
    sum_pix=sum_pix+image_nda_unint8[i-1,j+1]
    sum_pix=sum_pix+image_nda_unint8[i+1,j+1]
    sum_pix=sum_pix+image_nda_unint8[i+1,j-1]
    
    avg_pix=sum_pix/8
    if avg_pix<aggres:
        return True
    else:
        return False
    
def AveragePix(image_nda_unint8,i,j):
    sum_pix=0
    sum_pix=sum_pix+image_nda_unint8[i,j+1]
    sum_pix=sum_pix+image_nda_unint8[i,j-1]
    sum_pix=sum_pix+image_nda_unint8[i+1,j]
    sum_pix=sum_pix+image_nda_unint8[i-1,j]
    sum_pix=sum_pix+image_nda_unint8[i-1,j-1]
    sum_pix=sum_pix+image_nda_unint8[i-1,j+1]
    sum_pix=sum_pix+image_nda_unint8[i+1,j+1]
    sum_pix=sum_pix+image_nda_unint8[i+1,j-1]
    
    avg_pix=sum_pix/8
    return avg_pix


def ImageCleanup(img_nda_unint8,thres,aggres):  
    img_nda=img_nda_unint8
    for i in range(1,len(img_nda[0])-1):
        for j in range(1,len(img_nda)-1):
            if img_nda[i][j]>=thres:     
                if IsArtefact(img_nda, i, j,aggres)==True:
                    img_nda[i][j]=AveragePix(img_nda, i, j)
    return img_nda

            
