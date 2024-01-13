'''(Financial application: compute future tuition) Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.'''

current_tuition = 10000
annual_increase = 0.05  # 5% increase

# Calculate tuition in 10 years
for i in range(10):
    current_tuition *= (1 + annual_increase)

tuition_in_ten_years = current_tuition

# Calculate total cost of four years' tuition starting in 10 years
total_cost_four_years = 0
for i in range(4):
    total_cost_four_years += tuition_in_ten_years
    tuition_in_ten_years *= (1 + annual_increase)  # Apply annual increase for each year

# Print the results
print("Tuition in ten years: $", format(tuition_in_ten_years, ",.2f"))
print("Total cost of four years' tuition starting in ten years: $", format(total_cost_four_years, ",.2f"))










