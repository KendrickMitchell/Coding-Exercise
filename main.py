# This is a sample Python script.

def mine_key(name_age):
    return name_age[0]


def clean_number_string(num):
    if num[-1] == '\n':
        return num[1:-2]
    return num[1:-1] # Final line only


def get_tuples(names_and_ages):
    tuples = []
    for pair in range(round(len(names_and_ages)/2)):
        tuples.append((names_and_ages[pair*2], names_and_ages[(pair*2)+1]))
    return tuples


def get_address(address_type, words): # 6 is house, 7 is apartment
    place = ""
    if address_type == 6:
        place = words[2].upper().replace('"', " ") + words[3].upper().replace('"', " ") + words[4].upper().replace('"', " ")
        return place.replace(".", " ")
    if address_type == 7:
        place = words[2].upper().replace('"', " ") + words[3].upper().replace('"', " ") + words[4].upper().replace('"', " ") + words[5].upper().replace('"', " ")
        return place.replace(".", " ")
    print("error got address type", address_type)
    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    households = {}
    f = open("People.txt", "r")
    for line in f:
        data = line.split(",")
        home_type = len(data)

        if get_address(home_type, data) in households.keys():  # The household already exists
            # People are stored in tuples of last-first,age
            addition = (data[1].upper() + data[0].upper(), int(clean_number_string(data[-1])))
            households[get_address(home_type, data)] += addition
        else: # The household does not exist yet
            households[get_address(home_type, data)] = [data[1].upper() + data[0].upper(), int(clean_number_string(data[-1]))]

    for household in households.keys():
        print(household, " has ", len(households[household])/2, " people")
        print("Adults in the household are", )
        people = get_tuples(households[household])
        people.sort(key=mine_key)
        for person in people:  # Need the names and ages put together as tuples
            if person[1] >= 18:
                print(person[0].split('"')[3], person[0].split('"')[1], household, person[1])

    # Open people.txt.
    # For each line see if the location is a key in the dict if not then add and associate the person with it.
    # Otherwise just append the associated list with the name. Convert all strings to uppercase. Store as first,last,age
    # For all location keys
        # Print out the length of associated list and then the sorted list of all adult occupants
