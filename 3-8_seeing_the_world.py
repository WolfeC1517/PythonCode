locations = ['paris', 'dubai', 'rome', 'machu picchu', 'dublin', 'geneva']

print(f"Here is the original list:\n---------------------------------------------------------")
print(locations)
print(f"\nHere is the sorted list:\n---------------------------------------------------------")
print(sorted(locations))
print(f"\nHere is the reverse order list:\n---------------------------------------------------------")
print(sorted(locations, reverse=True))
print(f"\nAgain here is the original list:\n---------------------------------------------------------")
print(locations)


locations.reverse()
print(f"\n\n\nReverse the order of the list:\n---------------------------------------------------------")
print(locations)
locations.reverse()
print(f"\nBack to the original list:\n---------------------------------------------------------")
print(locations)


locations.sort()
print(f"\n\n\nSort the order of the list Alphabetical order:\n---------------------------------------------------------")
print(locations)
locations.sort(reverse=True)
print(f"\nSort the order of the list Reverse-alphabetical order:\n---------------------------------------------------------")
print(locations)


