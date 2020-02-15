final_temperature = 0.0
temperature_type_final = ''
temperature_to_convert = input("Insert the temperature you would like to convert:")
is_celsius = temperature_to_convert[-1].upper() == 'C'
temperature_to_convert = float(temperature_to_convert[0:-1])
if is_celsius:
    temperature_type_final = 'F'
    final_temperature = (9 * temperature_to_convert + (32 * 5)) / 5
else:
    temperature_type_final = 'C'
    final_temperature = (5 * temperature_to_convert - 160) / 9
print(final_temperature, temperature_type_final)