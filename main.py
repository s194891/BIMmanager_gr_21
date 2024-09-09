import ifcopenshell

from .external.BIManalyst_g_xy.rules import windowRule
from .external.BIManalyst_g_xy.rules import doorRule

model = ifcopenshell.open("path/to/ifcfile.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
