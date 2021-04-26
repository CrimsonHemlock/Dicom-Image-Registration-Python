import SimpleITK as sitk
import numpy as np
import matplotlib as plt
from PIL import Image

fixedImage = sitk.ReadImage('BrainProtonDensity_mod.png',sitk.sitkInt32)
movingImage = sitk.ReadImage('BrainProtonDensity2_mod.png',sitk.sitkInt32)
parameterMap = sitk.GetDefaultParameterMap('translation')

print('done1')

elastixImageFilter = sitk.ElastixImageFilter()
elastixImageFilter.SetFixedImage(fixedImage)
elastixImageFilter.SetMovingImage(movingImage)
elastixImageFilter.SetParameterMap(parameterMap)
print('done2')
elastixImageFilter.Execute()
print('done3')


resultImage = elastixImageFilter.GetResultImage()
transformParameterMap = elastixImageFilter.GetTransformParameterMap()
