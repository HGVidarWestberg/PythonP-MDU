import math

normal_packsize = 8
normal_packcost = 20.95
veg_packsize = 4
veg_packcost = 34.95
drink_cost = 13.95

normal2 = int(input("hur många vill ha två vanliga korvar: "))
normal3 = int(input("hur många vill ha tre vanliga korvar: "))
veg2 = int(input("hur många vill ha två vegetariska korvar: "))
veg3 = int(input("hur många vill ha tre vegetariska korvar: "))

normal_sausages = normal2*2+normal3*3
veg_sausages = veg2*2+veg3*3
total_students = normal2+normal3+veg2+veg3

normal_packages = math.ceil(normal_sausages/normal_packsize)
veg_packages = math.ceil(veg_sausages/veg_packsize)

total_cost = normal_packages * normal_packcost + veg_packages * veg_packcost + total_students * drink_cost

print(normal_packages, " normala packet behövs")
print(veg_packages, " vegetariska packet behövs")
print(total_students, "drickor behövs")
print(total_cost, " sek kostar det")