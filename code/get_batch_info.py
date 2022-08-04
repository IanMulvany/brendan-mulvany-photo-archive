# get some metdata about BM image batch information.

# use raw_input to ask the user for info about the photo batch


def get_batch_number():
    batch_number = input("What is the batch number? ")
    try:
        int_batch_number = int(batch_number)
    except ValueError:
        print("That's not a valid number? ")
        return get_batch_number()
    return int_batch_number


def get_batch_year():
    batch_year = input("What year were the images taken? ")
    try:
        int_batch_year = int(batch_year)
    except ValueError:
        print("That's not a valid year.")
        return get_batch_year()
    return int_batch_year


def get_batch_note():
    batch_note = input("Enter the note about the batch if there is one? ")
    return batch_note


def get_batch_info():
    batch_number = get_batch_number()
    batch_year = get_batch_year()
    batch_note = get_batch_note()
    return batch_number, batch_year, batch_note


def main():
    batch_number, batch_year, batch_note = get_batch_info()
    print(batch_number, batch_year, batch_note)


if __name__ == "__main__":
    main()
