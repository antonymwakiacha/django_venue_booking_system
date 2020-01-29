def main():
	with open("course.txt") as f:


		f1=f.readlines()
		for x in f1:
			print(x)
			for y in x:
				print(y)
				

if __name__=="__main__":
	main()
