name = "ravikumar" # String
### String is immutable

# 0,1,...n indexing
# -n, -(n - 1), ..... -1 negative indexing

# slicing
nameshort = name[0:4] # substring 0->4
print(nameshort)

#length of string
print(len(name))

# character from string
c = name[0]
print(c)
c = nameshort[-4] 
print(c)


# Slicing with skip value
num = "012345678"
print(num[1:7:3]) # 123456

# ends with check if string ends with this string
print(name.endswith("kumar"))
print(name.startswith("rave")) # check if i start with this string


# convert first char to Capital letter.
print(name.capitalize())


a = "Ravi is \"good\" boy \nbut not a bad boy"

print(a)