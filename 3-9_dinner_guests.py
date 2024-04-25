

f_name = ['f_name:', 'william', 'charles', 'charles', 'john', 'martin', 'jesus']
l_name = ['l_name:', 'wilberforce', 'finney', 'spurgeon', 'calvin', 'luther', 'of nazareth']

for i in range(7):
	if(i > 0):
		names = f"{i}. {f_name[i].title()} {l_name[i].title()}"
		print(names)
	else:
		pass
print(f"Number of guests that we will be attending: {len(f_name) - 1}\n")

print(f"\n-----------------------------------------------------------------------------------------------------------------\n")
print(f"{f_name[2].title()} {l_name[2].title()} and {f_name[5].title()} {l_name[5].title()} are unable to attend. Add Tim Colemen and Christopher Johnson to the invitation list.")
print(f"\n-----------------------------------------------------------------------------------------------------------------\n")

f_name[2], l_name[2] = "tim", "colemen"
f_name[5], l_name[5] = "christopher", "johnson"

for i in range(7):
	if(i > 0):
		names = f"{i}. {f_name[i].title()} {l_name[i].title()}"
		print(names)
	else:
		pass
print(f"Number of guests that we will be attending: {len(f_name) - 1}\n")

print(f"\n-----------------------------------------------------------------------------------------------------------------\n")
print(f"A larger table has been found so we will have room for 3 more guests at the dinner.")
print(f"\n-----------------------------------------------------------------------------------------------------------------\n")

f_name.insert(1, "clive staples")
l_name.insert(1, "lewis")
f_name.insert(5, "john ronald reuel")
l_name.insert(5, "tolkien")
f_name.append("robert charles")
l_name.append("sproul")

for i in range(10):
	if(i > 0):
		message = f"Dear {f_name[i].title()} {l_name[i].title()},\n\nYou are cordially invited to have dinner at my home this Friday, April 19th, at 5:30pm. We sincerly hope that you can attend.\n\nSincerly,\nChristian Wolfe"
		print(message)
		print(f"\n-----------------------------------------------------------------------------------------------------------------\n")
	else:
		pass
print(f"Number of guests that we will be attending: {len(f_name) - 1}\n")

print(f"\n-----------------------------------------------------------------------------------------------------------------\n")
print(f"Due to unforseen cercumstances, the table will not arrive until after the date set for the dinner. Therefore, we will only have room for 2 guests")
print(f"\n-----------------------------------------------------------------------------------------------------------------\n")

uninvited_list = [f_name.pop(1) + " " + l_name.pop(1), f_name.pop(1) + " " + l_name.pop(1), f_name.pop(1) + " " + l_name.pop(1), f_name.pop(1) + " " + l_name.pop(1), f_name.pop(1) + " " + l_name.pop(1), f_name.pop(2) + " " + l_name.pop(2), f_name.pop(3) + " " + l_name.pop(3)]

for i in range(7):
	if(i > 0):
		message = f"Dear {uninvited_list[i].title()},\n\nI hope this message finds you well. I'm writing to extend my sincerest apologies and inform you that, unfortunately, we won't be able to receive you as planned for dinner this Friday evening.\n\nWe truly regret any inconvenience this may cause and appreciate your understanding. Please know that your presence was eagerly anticipated, and we deeply value your involvement.\n\nWarm regards,\nChristian Wolfe"
		print(message)
		print(f"\n-----------------------------------------------------------------------------------------------------------------\n")
	else:
		pass

print(f"Number of guests that we will be attending: {len(f_name) - 1}\n")