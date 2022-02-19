def add(*args):
    result = 0
    for num in args:
        result += num
    return result

# print(add(1, 2, 445, 453, 2323))

def calculate(n, **kwargs):
    # print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key, value)
    n /= kwargs["divide"]
    n **= kwargs["exponent"]
    print(n)


class School:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.location = kwargs.get("location")


calculate(34, divide=4, exponent=7)

cool_dict = {
    "names": ["shyam", "rahul"],
    "age":[50, 45]
}

print(cool_dict.get("age"))
sav = School(name="Sri Akilandeswari Vidayala", location="Thiruvanaikovil")
print(sav.name, sav.location)

