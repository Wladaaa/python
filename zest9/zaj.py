# import logging
# import other

# print("main"+__name__)

# def main():
# 	logging.basicConfig(filename = 'app.log', level = logging.INFO)
# 	logging.info("Start")
# 	other.function()
# 	logging.warning("Stop")
# 	logging.debug("A problem occured")

# if __name__ == "__main__":
# 	main()

# import pdb

# def function():
# 	pdb.set_trace()
# 	i = 0
# 	while i < 5:
# 		i += 1
# 		print i

# a = "a"
# pdb.set_trace()
# b = "b"
# function()
# c = "c"
# pdb.set_trace()
# result = a + b + c
# print (result)

def num2text(n):
	return {
		1: "jeden"
		2: "dwa"
		3: "trzy"
	}.get(n)