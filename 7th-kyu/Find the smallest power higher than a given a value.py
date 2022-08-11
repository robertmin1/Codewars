def find_next_power(val, pow_):
    for i in range(2, val):
        next_power_value = i**pow_

        if next_power_value > val:
            break
        
    return next_power_value
