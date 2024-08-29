def ip_address(address):
    new_address= ""
    split_address= address.split(".")
    seperator= "[.]"
    new_address= seperator.join(split_address)
    return new_address

my_new_ip= ip_address("input ip_address")
print(my_new_ip)