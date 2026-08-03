import math
name=str(input("enter your name:"))
id=int(input("enter your electricity id:"))
pvr=float(input("enter the price per unit:"))
cmr=float(input("enter the current meter reading:"))
cost=float(input("enter the cost of electricity:"))

fixed_meter_charge=100
total_units_consumed=cmr-pvr
energy_charge=total_units_consumed*cost
electricity_duty=total_units_consumed*cost*0.05

print(f"total units consumed={total_units_consumed}")
print(f"energy_charge={energy_charge}")
print(f"electricity_duty={electricity_duty}")
print(f"fixed_meter_charge={fixed_meter_charge}")
print(f"net_bill_amount={energy_charge+electricity_duty+fixed_meter_charge}")   






