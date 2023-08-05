<<<<<<< HEAD
from utils import get_data, get_filtered_data, get_last_values, get_date, encoding_from, encoding_to, get_amount
=======
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data
>>>>>>> develop

def main():
    data = get_data()
    data = get_filtered_data(data)
    data_ = get_last_values(data, 5)
<<<<<<< HEAD
    for line in data_:
        transaction_description = line["description"]
        print(get_date(line), transaction_description)
        if transaction_description == "Открытие вклада":
            print(encoding_to(line))
        else:
            print(encoding_from(line), '->', encoding_from(line))
        print(get_amount(line))
=======
    data = get_formatted_data(data_)
>>>>>>> develop
    print()


if __name__ == "__main__":
    main()