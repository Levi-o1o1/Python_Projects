# def net_price(list_price, disc, tax):
#     return list_price * (1 - disc) * (1 + tax)
# print(net_price(500, 0, 0.05))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def malls(total , discount , tax = 0.18):
    return total * (1 - discount) * (1 + tax)
print(malls(1000, 0.20))




# breakdown in details 

# Original Price: ₹1000
# Discount applied (20%): 1000 × 0.20 = ₹200
# Sale Price (Subtotal): 1000 - 200 = ₹800
# Tax applied (18% GST): 800 × 0.18 = ₹144
# Final Price You Pay: 800 + 144 = ₹944