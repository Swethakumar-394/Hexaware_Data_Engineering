#Email Domain Extractor

emails = [
    "user1@gmail.com",
    "user2@yahoo.com",
    "user3@gmail.com",
    "user4@outlook.com"
]

domain_count = {}

for email in emails:
    domain = email.split("@")[1]
    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1

print("Users per domain:", domain_count)