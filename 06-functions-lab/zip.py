if __name__ == '__main__':
    first_name = ['Joe', 'Earnst', 'Thomas', 'Martin', 'Charles']
    last_name = ['Schmoe', 'Ehlmann', 'Fischer', 'Walter', 'Rogan', 'Green']
    age = [23, 65, 11, 36, 83]
    full_name_list = list(zip(first_name, last_name, age))
    print( full_name_list)

    # unzip
    first_name, last_name, age = list(zip(*full_name_list))
    print(f"first name: {first_name}\nlast name: {last_name} \nage: {age}")