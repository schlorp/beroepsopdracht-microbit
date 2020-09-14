import time
repeat = "ja" 

while repeat[0] not in ("nee") :

	print("Hello You!, ik ben Thom")
	naam = input("wie ben jij? \n")
	print("hello " + naam)

	tijd = time.asctime( time.localtime(time.time()) )

	print("de datum en tijd is " + tijd )

	vraag = input(naam + " wil jij dit programma nog een keer? type Y/N")


