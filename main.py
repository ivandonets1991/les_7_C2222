# for i in range(1,11,1):
#     print(i, end=" ")
# print(i)

# i=1
# while i<11:
#     print(i, end=" ")
#     i+=1
# print(i)

# spusok = [666,777,888]
# i = iter(spusok)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# spusok = [666,777,888]
# i = iter(spusok)
#
# for j in i:
#     print(j)
# for j in i:
#     print(j)

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# for elem in count:
#     print(elem)

# def raise_to_the_degrees(number, max_degree):
#     i=0
#     for _ in range(max_degree):
#         yield number**i
#         i+=1
# res = raise_to_the_degrees(2, 500)
# print(res)
# for _ in res:
#     print(_)

# def trublend():
#     print(123)
#     trublend()
#
# trublend()

# def raise_to_the_degrees(number):
#  i=0
#  while True:
#      yield number**i
#      i+=1
# res = raise_to_the_degrees(2)
# print(res)
# for _ in res:
#  print(_)

def raise_to_the_degrees(number):
 i=0
 while True:
     result = number**i
     yield result
     if result> 100**20:
        return
     i+=1
res = raise_to_the_degrees(2)
print(res)
for _ in res:
 print(_)
