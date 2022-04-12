acctual_h=0    # acctual height
model_h=0      # Model height
acctual_v=0    # Volume of the tank at the top of the acctual building
model_v=0      # Volume of the tank at the top of the model building
model_h=int(input("1. Enter height of model : "))
actual_h=model_h*30
print("Heieght of the acctual building is ",actual_h," centimeter.\n")

actual_v=int(input("2. Enter the accual volume of tank at the top of the building in metercube : "))
"""
as (1/30) = model height/acctual height
as (1/30) = model weidth/acctual weidth
as (1/30) = model length/acctual length
==> model volume = l*w*h
so acctual volume =(l*30)*(w*30)*(h*30)
==> Model volume = acctual volume /27000
and also we know that on converting a volume from meter square to centimeter square
we multiplty it by 100*100*100
"""

model_v=(actual_v*1000000)/27000
print("Volume of the model tank at the top of the building is",model_v,"centimeter cube.")
