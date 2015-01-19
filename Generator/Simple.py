def squares(top=10):
    for i in range(1,top):
        yield i*i

# pull data
result=squares(12)

for s in result:
    print(s)