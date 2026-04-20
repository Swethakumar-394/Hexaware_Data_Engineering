def analyze_visits(visits):
    print("All Visitors:")
    for visitor in visits:
        print(visitor)

    total_visits = len(visits)
    unique_visitors = set(visits)

    visit_count = {}
    for visitor in visits:
        visit_count[visitor] = visit_count.get(visitor, 0) + 1

    most_frequent_visitor = max(visit_count, key=visit_count.get)

    return total_visits, unique_visitors, visit_count, most_frequent_visitor