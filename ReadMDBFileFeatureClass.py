
# Import arcpy module
import arcpy

dir = r"C:\\Users\\s.rajaei\\Desktop\\Hadi_Gilan"
layer = "\\Present\\Rurallimit_pre"
out = "C:\\Users\\s.rajaei\\Desktop\\New_(3)"
env.workspace = r"C:\Users\s.rajaei\Desktop\Hadi_Gilan"
fileDir = arcpy.ListFiles()

for mdb in fileDir:
    filePath = os.path.join(dir, mdb+layer)
    print(filePath)
    
    arcpy.FeatureClassToShapefile_conversion(filePath, out)
