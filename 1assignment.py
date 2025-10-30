# 1

# user = input("Enter : ")
# letter =0
# number = 0
# special = 0

#2
# if user.isalpha():
#     letter =+ len(user)
#     print(f"Your string have {letter} alphabets")
# elif user.isdigit():
#     number =+ len(user)
#     print(f"Your string have {number} alphabets")
# else:
#     special =+ len(user)
#     print(f"Your string have {special} alphabets")

#3
# first= int(input("Enter your start digit :"))
# second = int(input("Enter your end digit :"))
# for a in range(first,second+1):
#     if (a % 4 == 0 or a % 6 == 0) and not (a % 4 == 0 and a % 6 == 0):
#         print(a)
  
#4 
# sentence = input("Enter a sentence: ")
# upper = 0
# lower = 0
# for char in sentence:
#     if char.isupper():
#         upper += 1
#     elif char.islower():
#         lower += 1
# print("Uppercase letters:", upper)
# print("Lowercase letters:", lower)

#5
# s = input("Enter a string: ")
# total = 0
# for ch in s:
#     if ch.isdigit():
#         total += int(ch)
# print("Sum of digits =", total)


#6
# s = input("Enter a string: ")
# total = sum(int(ch) for ch in s if ch.isdigit())
# print("Sum of digits :", total)

# 7
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# vowels = 'aeiouAEIOU'
# count = sum(1 for w in words if w[0] in vowels)
# print("Words starting with a vowel:", count)

# 8
# user = input("Enter a string: ")
# freq = {}

# for a in user:
#     freq[a] = freq.get(a, 0) + 1

# for a in sorted(freq):
#     print(f"{a}: {freq[a]}")

# 9
# start = int(input("Enter start: "))
# end = int(input("Enter end: "))
# print("Numbers containing 3:")
# for num in range(start, end + 1):
#     if '3' in str(num):
#             print(num, end=" ")
# print()

# 10
# start = int(input("Enter start: "))
# end = int(input("Enter end: "))
# print("Numbers meeting all conditions:")
# for num in range(start, end + 1):
#     divisible_4 = num % 4 == 0
#     divisible_6 = num % 6 == 0
#     sum_digits = sum(int(d) for d in str(num))
#     if (divisible_4 ^ divisible_6) and (sum_digits % 2 != 0) and (num % 9 != 0):
#         print(num, end=" ")
# print()




