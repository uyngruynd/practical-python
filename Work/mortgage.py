principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
m = 0
extra_start = 5 * 12
extra_end = extra_start + 4 * 12
while principal > 0:
    m += 1

    next_payment = payment + extra if extra_start < m <= extra_end else payment
    principal = principal * (1+rate/12) - next_payment

    if principal < 0:
        total_paid = total_paid + next_payment + principal
        principal = 0
    else:
        total_paid = total_paid + next_payment

    print(f'{m} {round(total_paid, 2)} {round(principal, 2)}')

print(f'Total paid {round(total_paid, 2)}')
print(f'Months {m}')

s = 'hello'
s.join()