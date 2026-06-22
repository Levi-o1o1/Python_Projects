# pyhton credit card validator program

# 1 remove any '-' or " "
# add all digits in the odd places from right to left 

sum_odd = 0
sum_even = 0
total = 0 


card_num = input("Enter a credit card number :")
card_num = card_num.replace("-", "")
card_num = card_num.replace(" ", "")
card_num = card_num[:: -1]  # reverse the string 


print(card_num)