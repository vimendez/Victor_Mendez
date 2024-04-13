vlans_de_sw1 = [99, 10, 20, 30] 
vlans_de_sw2 = [200, 40, 50, 60]

if vlans_de_sw1[0] == 99:
	print("La vlan nativa de sw1 es igual a la vlan creada")
else:
	print("La vlan nativa de sw1 es diferente a la vlan creada")

vlans_requeridas_sw1 = [10, 100, 30]

if set(vlans_de_sw1[1:]) == set(vlans_requeridas_sw1):
	print("Las vlans de sw1 son iguales a las vlans requeridas")
else:
	print("Las vlans de sw1 son diferentes a las vlans requeridas")

if vlans_de_sw2[0] == 99:
	print("La vlan nativa de sw2 es igual a la vlan creada")
else:
	print("La vlan nativa de sw2 es diferente a la vlan creada")

vlans_requeridas_sw2 = [40, 50, 60]
if set(vlans_de_sw2[1:]) == set(vlans_requeridas_sw2):
	print("Las vlans de sw2 son iguales a las vlans requeridas")
else:
	print("Las vlans de sw2 son diferentes a las vlans requeridas")
