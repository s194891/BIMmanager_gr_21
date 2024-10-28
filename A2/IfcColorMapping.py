##--- Author
# Kasper Krag, s194883, DTU

# script to recolor IfcObjects by globalId in Ifc model

# manual opening of file necerary to veiw changes
# globalIds are coloured so heights value attached are red 
# and lowest value attached are green


##--- Import libraries
import ifcopenshell
import os
import ifcopenshell.api
import ifcopenshell.api.style


##--- Import IFC-model

# Find file-path to model
Models_directory = r'C:\Users\julie\Google Drev\10.Semester\41934 Advanced BIM'

# File name of model
Model_filename = 'CES_BLD_24_06_STR.ifc'

# Join filepath to IFC-file
Model_path = os.path.join(Models_directory, Model_filename)

# Load model
Model = ifcopenshell.open(Model_path)


##--- Import globalId(s)  

# Turn on or off (TotalHeightWallsRule)
GlobalIdSource = 1

# Use of group 21 function "TotalHeightWAllsRule" to get GlobalIds 
if GlobalIdSource == 1:
        
    # Find file-path to Rules 
    Rules_directory = r'C:\Users\julie\Documents\GitHub\BIMmanager_gr_21'
    
    # Change directory
    os.chdir(Rules_directory)
    
    # Import TotalHeightWallsRule 
    from external.BIManalyst_g_23.rules import TotalHeightWallsRule

    # Run TotalHeightWallsRule for model
    totalHResult = TotalHeightWallsRule.checkRule(Model)
    
    # Create list of GlobalId
    GlobalId = totalHResult
    
    # Convert list of turple(s) to list of list(s)
    GlobalId = [list(i) for i in GlobalId ]
    
    #Changing height of walls for ilustrative purposes
    GlobalId[3][1] = 65
    GlobalId[4][1] = 60
    GlobalId[5][1] = 40
    GlobalId[6][1] = 30
    GlobalId[7][1] = 28
    GlobalId[8][1] = 20
    
# Use of alternative method to get GlobalIds
else:

    # Use alternative method for getting GlobalId example
    GlobalId = [['2ej4540sDCUxtwmylyvA1m'],[25]]


##--- Color scale
# Find min/max values for color pallet
MinColVal = min(row[1] for row in GlobalId)
MaxColVal = max(row[1] for row in GlobalId)


##--- Set color
for i in GlobalId:
    
    # Color value converter
    ColVal = 100/(MaxColVal-MinColVal)*(i[1]-MinColVal)
    
    #RGB converter    
    if ColVal <=50:
        Red = 1
        Green = ColVal/50
        Blue = 0
    else:
        Red = (100-ColVal)/50  
        Green = 1
        Blue = 0
    
    # Find the thing by its Global ID
    Thing = Model.by_guid(i[0])    

    # Create a new surface style
    style = ifcopenshell.api.style.add_style(Model)

    # Create a simple grey shading colour and transparency.
    ifcopenshell.api.style.add_surface_style(Model, style=style, ifc_class="IfcSurfaceStyleShading", attributes={"SurfaceColour": { "Name": None, "Red": Red, "Green": Green, "Blue": Blue }, "Transparency": 0.,})

    # Sets the color
    ifcopenshell.api.style.assign_representation_styles(Model, shape_representation=Thing.Representation, styles=[style])

# New file name of model
Model_filename = 'CES_BLD_24_06_STR_Recolor.ifc'

# Join filepath to IFC-file
Model_path = os.path.join(Models_directory, Model_filename)

##--- Save the modified IFC file
Model.write(Model_path)