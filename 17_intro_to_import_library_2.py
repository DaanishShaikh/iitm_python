import random
# Seeding
random.seed(42)
    
# Random Numbers
print("random.random():", random.random())  # 0.6394267984578837
print("random.uniform(1, 10):", random.uniform(1, 10))  # 1.0253449218110241
print("random.randint(1, 10):", random.randint(1, 10))  # 2
print("random.randrange(1, 10, 2):", random.randrange(1, 10, 2))  # 1
print("random.expovariate(1.5):", random.expovariate(1.5))  # 0.05198124573220175
print("random.gauss(0, 1):", random.gauss(0, 1))  # 0.2566636477931025
print("random.betavariate(2, 5):", random.betavariate(2, 5))  # 0.33297086599039466
print("random.gammavariate(2, 5):", random.gammavariate(2, 5))  # 14.166994472080957
print("random.lognormvariate(0, 1):", random.lognormvariate(0, 1))  # 0.5866293875597789
print("random.normalvariate(0, 1):", random.normalvariate(0, 1))  # -0.5227681427695596
print("random.triangular(1, 10, 5):", random.triangular(1, 10, 5))  # 4.775467447414219
    
# Random Choice and Shuffle
sample_list = [1, 2, 3, 4, 5]
print("random.choice(sample_list):", random.choice(sample_list))  # 4
print("random.choices(sample_list, k=3):", random.choices(sample_list, k=3))  # [2, 4, 3]
print("random.sample(sample_list, k=3):", random.sample(sample_list, k=3))  # [1, 5, 3]
random.shuffle(sample_list)
print("random.shuffle(sample_list):", sample_list)  # [5, 1, 4, 3, 2]
    
# Boolean and Bytes
print("random.getrandbits(8):", random.getrandbits(8))  # 177
print("random.choice([True, False]):", random.choice([True, False]))  # False
print("random.randbytes(5):", random.randbytes(5))  # b'\xa1\x1b\xe7\x94P'