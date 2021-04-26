import SimpleITK as sitk
import numpy as np
import matplotlib as plt
from PIL import Image

resultImage = sitk.Elastix(sitk.ReadImage("BrainProtonDensity_mod.png",sitk.sitkInt32), \
                           sitk.ReadImage("BrainProtonDensity2_mod.png",sitk.sitkInt32), \
                           "affine")
print(resultImage)
#sitk.Show(resultImage)
nda = sitk.GetArrayFromImage(resultImage)
print(nda)
im = Image.fromarray(nda)
im.convert("RGB")
im.save("mergeMOD","TIFF")