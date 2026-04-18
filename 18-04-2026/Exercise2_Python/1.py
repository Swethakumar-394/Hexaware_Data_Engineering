# Exercise 1 — TXT File (Login Logs)

with open("logins.txt", "r") as file:
    names = [line.strip() for line in file]

print("All names:")
for name in names:
    print(name)

print("\nTotal number of login records:", len(names))

login_count = {}
for name in names:
    login_count[name] = login_count.get(name, 0) + 1

print("\nLogin count per user:")
print(login_count)

most_logged_user = max(login_count, key=login_count.get)
print("\nUser who logged in the most:", most_logged_user)

unique_users = set(names)
print("\nUnique users:")
print(unique_users)