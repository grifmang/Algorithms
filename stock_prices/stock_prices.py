#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_price = prices[0]
  max_profit = -999999999

  for index, num in enumerate(prices):
    for i in range(index+1, len(prices)):
      if prices[i] - num > max_profit:
        max_profit = prices[i] - num
        min_price = num
  
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))