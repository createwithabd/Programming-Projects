
even = []
for n in range(1, 101):
    if n%2 ==0:
        even.append(n)

sum_of_even_numbers = sum(even)
print(f"Sum of even numbers between 1 and 100: {sum_of_even_numbers} ")