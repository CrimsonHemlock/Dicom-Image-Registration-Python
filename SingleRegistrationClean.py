#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:15:36 2020

@author: Wayan A. Fontaine-Seiler

Simple Program for dual image registration using the SimpleElastix module integrated in SimpleITX with minimal customization option

Dependencies: PILLOW, numpy and custom SimpleITK compiled from source with SimpleElastix module
"""

## Single image Simple registration program using the SITK with SimpleElastix extension

## IMPORT PRE-COMPILED EXTENSIONS & LIBRARIES##
import SimpleITK as sitk # Loads the SimpleITK module compiled from source with the addition of the SimpleElastix addition
print(sitk.__file__) # Tests the version of SimpleITK (Should be SimpleITK-2.0.0rc2.dev908+g8244e-py[your_version_of_python])

import numpy as np
import matplotlib as plt
from PIL import Image # Image manipulation in Python using PILLOW (For of unmaintained PIL)

##IMPORT CUSTOM EXTENSIONS##
from ImageCleanup import ImageCleanup

# IMPORT IMAGES #
fixedImage = sitk.ReadImage('MRIm15Target.png',sitk.sitkInt32)
movingImage = sitk.ReadImage('MRIm15Moving.png',sitk.sitkInt32)

#SET THE PARAMETER MAP (Transformation to apply)#
parameterMap = sitk.GetDefaultParameterMap('translation')
#parameterMap["numberOfResolutions"].append(16)

#Or(To apply successive Registration protocols -- Useful for bspline registration)#
parameterMapVector = sitk.VectorOfParameterMap()
parameterMapVector.append(sitk.GetDefaultParameterMap("affine"))
test = sitk.GetDefaultParameterMap("bspline")
#test["Metric"].append("CorrespondingPointsEuclideanDistanceMetric")
parameterMapVector.append(test)

# APPLY THE PARAMETERS #
elastixImageFilter = sitk.ElastixImageFilter()
elastixImageFilter.SetFixedImage(fixedImage)
elastixImageFilter.SetMovingImage(movingImage)
elastixImageFilter.SetParameterMap(parameterMap) # OR parameterMap for only one step registration

#EXECUTE & GET THE RESULTS #
elastixImageFilter.Execute()
resultImage = elastixImageFilter.GetResultImage()
transformParameterMap = elastixImageFilter.GetTransformParameterMap()

#EXPORT in array #
ndares = sitk.GetArrayFromImage(resultImage)
nda1 = sitk.GetArrayFromImage(fixedImage)
nda2 = sitk.GetArrayFromImage(movingImage)

#
nda1 = nda1.astype(np.uint8)
nda2 = nda2.astype(np.uint8)
ndares = ndares.astype(np.uint8)

ndares=ImageCleanup(ndares,254,128) # Rought Cleanup using the ImageCleanup.py extension module

im1 = Image.fromarray(nda1)
im2 = Image.fromarray(nda2)
imres = Image.fromarray(ndares)

print (imres)

im1.convert('L')
im2.convert('L')
imres.convert('L')


immerge = Image.blend(im1, imres, 0.5)

im1.show()
im2.show()
imres.show()
immerge.show()

immerge.save("MERGESIMPLE","TIFF")