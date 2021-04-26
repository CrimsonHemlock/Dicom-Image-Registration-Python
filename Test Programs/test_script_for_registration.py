import SimpleITK as sitk
print(sitk.__file__)

import numpy as np
import matplotlib as plt
from PIL import Image

resultImage = sitk.Elastix(sitk.ReadImage("MRIm15TargetMOD.png",sitk.sitkInt32), \
                           sitk.ReadImage("MRIm15MovingMOD.png",sitk.sitkInt32), \
                           "affine") #sitk.sitkInt32
print(resultImage)
#sitk.Show(resultImage)
nda = sitk.GetArrayFromImage(resultImage)
print(nda)
im = Image.fromarray(nda)
im.convert("RGB")
im.save("mergeMOD_MRI","TIFF")