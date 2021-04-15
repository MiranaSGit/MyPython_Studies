sales = {
    "cost_value" : 31.87,
    "sell_value" : 45.00,
    "inventory" : 1000
}
cost, sale, inv = sales.values()
print("Total profit is: ", "$", round(cost * (sale - cost)), sep = "")


payrolls = [3 , 29.99, 4.1]
print("Payrolls is \n ${:.2f} \n ${:.2f} \n ${:.2f}".format (payrolls[0], payrolls[1], payrolls[2]))
