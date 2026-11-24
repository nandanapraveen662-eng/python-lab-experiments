try:
    units = int(input("Enter electricity units: "))

    if units < 0:
        raise ValueError("Negative units are not allowed")

    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 300:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 5

    print("Total Electricity Bill: Rs.", bill)

except ValueError as e:
    print("Invalid input:", e)

finally:
    print("Bill calculation completed")