import ifcopenshell
import os

# Find stien til modellen
models_directory = r'C:\Users\julie\Google Drev\10.Semester\41934 Advanced BIM'
# Filnavnet på modellen
model_filename = 'CES_BLD_24_06_STR.ifc'
# Saml hele stien til IFC-filen
model_path = os.path.join(models_directory, model_filename)
model = ifcopenshell.open(model_path)

from external.BIManalyst_g_xy.rules import doorRule
from external.BIManalyst_g_22.rules import group22_function_get_columns_on_level
from external.BIManalyst_g_23.rules import TotalHeightWallsRule
from external.BIManalyst_g_24.rules import Calcualting_surfaceload_slabs
from external.BIManalyst_g_25.rules import nameElement
#from external.BIManalyst_g_26.rules import A1_python_code
from external.BIManalyst_g_27.rules import column_AreaRule
from external.BIManalyst_g_28.rules import slabheightRule

# Run all functions
doorResult = doorRule.checkRule(model)
colOnLvResult = group22_function_get_columns_on_level.get_columns_on_level(model, 3)
totalHResult = TotalHeightWallsRule.checkRule(model)
#slabResult = Calcualting_surfaceload_slabs.checkRule(model)
#nameResult = nameElement.specifikElement(model)
#beamResult = A1_python_code.checkRule(model)
columnResult = column_AreaRule.checkRule(model)
slabHeightResult = slabheightRule.checkRule(model)

# see the results
print("Door result:", doorResult)
print("colOnLvResult:", colOnLvResult)
print("total height Result ", totalHResult)
#print("slab result:",slabResult)
#print("name result:",nameResult)
#print("beam Result", beamResult)
print("column result", columnResult)
print("slab Result", slabHeightResult)
