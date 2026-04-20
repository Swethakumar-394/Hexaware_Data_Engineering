def analyze_students(names):
    print("All Student Names:")
    for name in names:
        print(name)

    total_entries = len(names)
    unique_names = set(names)

    name_count = {}
    for name in names:
        name_count[name] = name_count.get(name, 0) + 1

    with open("unique_students.txt", "w") as file:
        for name in unique_names:
            file.write(name + "\n")

    print("\nTotal Entries:", total_entries)
    print("Unique Student Names:", unique_names)
    print("Name Count:", name_count)

    return total_entries, unique_names, name_count