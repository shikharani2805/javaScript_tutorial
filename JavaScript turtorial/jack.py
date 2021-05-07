N = int(input()) # total no. of tickets issued for lottery
D = int(input()) # whose buy the ticket
X = int(input()) # people that will be given prizes

def fun():
	sum=0
	while(N>0):
		dig=N%10
		sum=sum+dig
		N=N//10
		return ((D // X) % sum)
fun()
