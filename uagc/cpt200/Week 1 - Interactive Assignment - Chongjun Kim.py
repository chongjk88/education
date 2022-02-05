'''
CPT200 - Week 1 - Interactive Assignment
Author: Chongjun Kim
Date: 08/19/2021
Title: Calculating Profit Amount
'''
print('Please enter the annual amount of sale to calculate the estimated profit amount.')
print('Total Sale:', end=' $') # input format
sale = int(input()) # prompting entry of sale

profit = "${:,.2f}".format(sale * 0.19) # converting to currency format
print('Profit Amount:', profit) # output format
