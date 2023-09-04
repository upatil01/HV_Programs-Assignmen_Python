import json

def take_user_inputs():
    data = []
    num_entries = int(input("Enter the number of entries: "))

    for _ in range(num_entries):
        entry = {}
        entry['Date'] = input("Enter the date (YYYY-MM-DD): ")
        entry['Department'] = input("Enter the department: ")
        entry['Description'] = input("Enter the description: ")
        entry['Amount'] = float(input("Enter the amount: "))

        data.append(entry)

    return data

def store_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

    print("Data stored successfully!")

# Example usage
data = take_user_inputs()
store_data('expenses.json', data)