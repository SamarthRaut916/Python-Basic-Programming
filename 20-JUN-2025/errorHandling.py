# dataRead = open("Notes/1.txt","r+").read()


# print(dataRead)

# isProges = True
# try:

#     # dataRead = open("Notes/1.txt","a+").write("okkkk\n")
#     dataRead = open("Notes/1.txt","r+").read()
#     print(dataRead)
#     # show

# except Exception as e:
#     print(e)
#     isProges = False

# finally:
#     print("i am done")
#     isProges = False


try:
    n = 5 / 0
    print(n)

except ZeroDivisionError as zd:

    print(zd)
    n = 0 / 5
    print(n)





n = 10
n2 = 100
print(n+n2)


