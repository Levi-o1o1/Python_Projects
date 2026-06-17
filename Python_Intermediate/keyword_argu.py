# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# hello("hello", "mr.","spanch","squarpants")


def phone_num(country, area , first , last):
    return f"{country}-{area}-{first}-{last}"

get_phone = phone_num(country=1, area=123, last=8908, first=3122)
print(get_phone)


# this is a keyword arguments does't care about where you type the first or last is example for that 