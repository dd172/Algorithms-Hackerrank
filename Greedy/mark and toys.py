# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  #Compute and return final answer over here
  prices.sort()
  answer = 0
  spent = 0
  for i in range(len(prices)):
  	spent += prices[i]
  	if spent > rupees:
  		break
  	elif spent < rupees:
  		answer += 1
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
