weight = 4.8
cost_ground = 0
#Ground Shipping
if weight <= 2:
  cost_ground = weight * 4.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20
else: 
  print("Error. Please enter a valid weight.")

print(cost_ground)
ground_shipping_premium = 125.00
print(ground_shipping_premium)
#Drone Shipping 
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
elif weight > 10:
  cost_drone = weight * 14.75
else: 
  print("Error. Please enter a valid weight.")
print(cost_drone)






