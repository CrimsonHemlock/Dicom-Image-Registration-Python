import SimpleITK as sitk
import numpy as np
import matplotlib as plt
from PIL import Image

resultImage = sitk.Elastix(sitk.ReadImage("BrainProtonDensityRot.png",sitk.sitkInt32), \
                           sitk.ReadImage("BrainProtonDensityRot2.png",sitk.sitkInt32), \
                           "rigid")
print(resultImage)
#sitk.Show(resultImage)
nda = sitk.GetArrayFromImage(resultImage)
print(nda)
im = Image.fromarray(nda)
im.convert("L")
im.save("merge","TIFF")