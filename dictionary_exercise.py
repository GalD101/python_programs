from datetime import date


def calculateAge(birth_date):
    days_in_year = 365.2425
    age = int((date.today() - birth_date).days / days_in_year)
    return age

# 8.3.2


def print_values_by_code(dictionary):
    action_code = int(input("Please enter a number between 1 and 7:"))
    if action_code == 1:
        print(dictionary["last_name"])
    elif action_code == 2:
        months = ["Unknown",
                  "January",
                  "February",
                  "March",
                  "April",
                  "May",
                  "June",
                  "July",
                  "August",
                  "September",
                  "October",
                  "November",
                  "December"]

        birth_date = dictionary["birth_date"]
        month_num = int(
            birth_date[birth_date.find('.') + 1:birth_date.find('.', birth_date.find('.') + 1)])
        month_name = months[month_num]
        print(month_name)
    elif action_code == 3:
        print(len(dictionary["hobbies"]))
    elif action_code == 4:
        print(dictionary["hobbies"][len(dictionary["hobbies"]) - 1])
    elif action_code == 5:
        updated_hobbies = dictionary["hobbies"]
        updated_hobbies.append("Cooking")
        dictionary["hobbies"] = updated_hobbies
    elif action_code == 6:
        birth_date_tuple = tuple()

        # Seprate day, month and year
        dd = int(dictionary["birth_date"]
                 [:dictionary["birth_date"]
                  .find('.')])
        mm = int(dictionary["birth_date"]
                 [dictionary["birth_date"]
                  .find('.') + 1:dictionary["birth_date"]
                  .find('.', dictionary["birth_date"]
                        .find('.') + 1)])
        yyyy = int(dictionary["birth_date"]
                   [dictionary["birth_date"]
                    .find('.', dictionary["birth_date"]
                          .find('.') + 1) + 1:])

        birth_date_tuple = (dd, mm, yyyy)
        print(birth_date_tuple)
    elif action_code == 7:
        dd = int(dictionary["birth_date"][:dictionary["birth_date"].find('.')])
        mm = int(dictionary["birth_date"][dictionary["birth_date"].find(
            '.') + 1:dictionary["birth_date"].find('.', dictionary["birth_date"].find('.') + 1)])
        yyyy = int(dictionary["birth_date"][dictionary["birth_date"].find(
            '.', dictionary["birth_date"].find('.') + 1) + 1:])
        dictionary["age"] = calculateAge(date(yyyy, mm, dd))
        print(dictionary["age"], "years old")


def main():
    my_dict = {"first_name": "Mariah", "last_name": "Carey",  # pylint: disable = unused-variable
               "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}
    print_values_by_code(my_dict)


if __name__ == "__main__":
    main()
