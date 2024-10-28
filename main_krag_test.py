import ifcopenshell
import os

# Find stien til modellen
models_directory = r'C:\Users\kaspe\Desktop'
# Filnavnet på modellen
model_filename = 'CES_BLD_24_06_STR.ifc'
# Saml hele stien til IFC-filen
model_path = os.path.join(models_directory, model_filename)
model = ifcopenshell.open(model_path)

from external.BIManalyst_g_xy.rules import doorRule
#from external.BIManalyst_g_22.rules import group22_function_get_columns_on_level
#from external.BIManalyst_g_23.rules import TotalHeightWallsRule
#from external.BIManalyst_g_26.rules import 
#from external.BIManalyst_g_25.rules import numberElementCheck
from external.BIManalyst_g_27.rules import column_AreaRule
#from external.BIManalyst_g_28.rules import storeysRule

# Run all functions
doorResult = doorRule.checkRule(model)
#colOnLvResult = group22_function_get_columns_on_level.get_columns_on_level(model, 3)
#totalHResult = TotalHeightWallsRule.checkRule(model)
#amountElResult = numberElementCheck.amountElement(model, IfcBeam, 25)
column_AreaRuleResult = column_AreaRule.checkRule(model)
#storeysRuleResult = storeysRule.checkRule(model)

# see the results
print("Door result:", doorResult)
#print("colOnLvResult:", colOnLvResult)
#print("total height Result ", totalHResult)
#print("amount el Result ", amountElResult)
print("column Area Result", column_AreaRuleResult)
#print("storeys Result", storeysRuleResult)
