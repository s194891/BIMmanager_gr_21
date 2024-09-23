import ifcopenshell
import sys
import os

# Få den nuværende sti til 'main.py'
#current_directory = os.path.dirname(os.path.abspath(__file__))

# Tilføj 'rules'-mappen til sys.path
#sys.path.append(os.path.join(current_directory, 'external'))
#sys.path.append(os.path.join(current_directory, 'GROUP_27'))
#sys.path.append(os.path.join(current_directory, 'rules'))

#from external.GROUP_27.rules.doorRule import doorRule
import helloVstudio
helloVstudio.checkRule()
from external.BIManalyst_g_xy.rules import doorRule
from external.GROUP_27.rules import columnRule


# Find stien til modellen
models_directory = r'C:\Users\julie\Google Drev\10.Semester\41934 Advanced BIM'
# Filnavnet på modellen

model_filename = 'CES_BLD_24_06_STR.ifc'
#model_filename = 'LLYN - STRU.ifc'

# Saml hele stien til IFC-filen
model_path = os.path.join(models_directory, model_filename)
model = ifcopenshell.open(model_path)

# Run all functions
doorResult = doorRule.checkRule(model)
#elNrResult = amountElement(model, IfcBeam, 2)
columnResult = columnRule.checkRule(model)

# see the results
print("Door result:", doorResult)
print("column result:", columnResult)
