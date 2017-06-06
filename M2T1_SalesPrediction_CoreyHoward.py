# Sales Prediction Program
# 5/6/2017
# CTI-110 M2T1 - Sales Prediction
# Corey Howard
#

# Request the total amount of projected sales.
total_sales = float(input("Please enter the total amount of sales."))

# Calculate the profit by multiplying the total sales by 23%(.23).
profit = total_sales * .23

# Print the profit that will be made from that amount.
print("Profit for ${0:,.2f} is ${1:.2f}." .format(total_sales,profit))
