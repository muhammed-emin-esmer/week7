shopping_list = ["milk", "eggs", "bread", "butter"]
shopping_list[1] = "cheese"

# print(len(shopping_list))  # Output: 4

# shopping_list.append("apples")
# print(len(shopping_list))  # Output: 5

# shopping_list.remove("bread")
# print(len(shopping_list))  # Output: 4

for item in shopping_list:
    print(f"To buy: {item}")