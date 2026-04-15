// Create & Use Database
use("library_db")

// 1. CREATE MEMBERS COLLECTION

db.members.insertMany([
  { member_id: 1, name: "Aarav", city: "Hyderabad", membership_type: "Gold" },
  { member_id: 2, name: "Priya", city: "Bangalore", membership_type: "Silver" },
  { member_id: 3, name: "Rahul", city: "Mumbai", membership_type: "Gold" },
  { member_id: 4, name: "Sneha", city: "Delhi", membership_type: "Silver" },
  { member_id: 5, name: "Kiran", city: "Hyderabad", membership_type: "Gold" }
])

// 2. CREATE BOOKS COLLECTION

db.books.insertMany([
  { book_id: 101, title: "MongoDB Basics", category: "Database", author: "John Smith", price: 500 },
  { book_id: 102, title: "Python Fundamentals", category: "Programming", author: "Alice Brown", price: 650 },
  { book_id: 103, title: "Data Engineering Intro", category: "Data", author: "Mark Lee", price: 800 },
  { book_id: 104, title: "SQL for Beginners", category: "Database", author: "David Miller", price: 450 },
  { book_id: 105, title: "Machine Learning Start", category: "AI", author: "Sara Khan", price: 900 }
])

// 3. CREATE BORROWINGS COLLECTION

db.borrowings.insertMany([
  { borrow_id: 1001, member_id: 1, book_id: 101, days_borrowed: 5, borrow_date: "2026-03-01" },
  { borrow_id: 1002, member_id: 2, book_id: 102, days_borrowed: 3, borrow_date: "2026-03-02" },
  { borrow_id: 1003, member_id: 1, book_id: 103, days_borrowed: 7, borrow_date: "2026-03-03" },
  { borrow_id: 1004, member_id: 3, book_id: 104, days_borrowed: 4, borrow_date: "2026-03-05" },
  { borrow_id: 1005, member_id: 5, book_id: 105, days_borrowed: 10, borrow_date: "2026-03-07" },
  { borrow_id: 1006, member_id: 5, book_id: 101, days_borrowed: 2, borrow_date: "2026-03-08" }
])

// 1. Display all members
db.members.find()

// 2. Display all books
db.books.find()

// 3. Display all borrowings
db.borrowings.find()

// 4. Show members from Hyderabad
db.members.find({ city: "Hyderabad" })

// 5. Show books in the Database category
db.books.find({ category: "Database" })

// 6. Show books whose price is greater than 600
db.books.find({ price: { $gt: 600 } })

// 7. Show borrowings where days_borrowed is greater than 5
db.borrowings.find({ days_borrowed: { $gt: 5 } })

// 8. Display books sorted by price descending
db.books.find().sort({ price: -1 })

// 9. Display members sorted by name ascending
db.members.find().sort({ name: 1 })

// 10. Count the total number of members
db.members.countDocuments()

// 11. Count the total number of books
db.books.countDocuments()

// 12. Count how many books belong to the Database category
db.books.countDocuments({ category: "Database" })

// 13. Find the average price of all books
db.books.aggregate([
  {
    $group: {
      _id: null,
      average_price: { $avg: "$price" }
    }
  }
])

// 14. Find the maximum book price
db.books.aggregate([
  {
    $group: {
      _id: null,
      max_price: { $max: "$price" }
    }
  }
])

// 15. Find the minimum book price
db.books.aggregate([
  {
    $group: {
      _id: null,
      min_price: { $min: "$price" }
    }
  }
])

// 16. Find the total days borrowed per member
db.borrowings.aggregate([
  {
    $group: {
      _id: "$member_id",
      total_days_borrowed: { $sum: "$days_borrowed" }
    }
  }
])

// 17. Display borrowings along with member details
db.borrowings.aggregate([
  {
    $lookup: {
      from: "members",
      localField: "member_id",
      foreignField: "member_id",
      as: "member_details"
    }
  }
])

// 18. Display borrowings along with book details
db.borrowings.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book_details"
    }
  }
])

// 19. Display member name and book title for each borrowing
db.borrowings.aggregate([
  {
    $lookup: {
      from: "members",
      localField: "member_id",
      foreignField: "member_id",
      as: "member"
    }
  },
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $project: {
      _id: 0,
      member_name: { $arrayElemAt: ["$member.name", 0] },
      book_title: { $arrayElemAt: ["$book.title", 0] }
    }
  }
])

// 20. Display book title and total times it was borrowed
db.borrowings.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $group: {
      _id: "$book_id",
      total_times_borrowed: { $sum: 1 },
      book_title: { $first: { $arrayElemAt: ["$book.title", 0] } }
    }
  },
  {
    $project: {
      _id: 0,
      book_title: 1,
      total_times_borrowed: 1
    }
  }
])

// 21. Find the total number of books borrowed by each member
db.borrowings.aggregate([
  {
    $group: {
      _id: "$member_id",
      total_books_borrowed: { $sum: 1 }
    }
  }
])

// 22. Find the most borrowed book
db.borrowings.aggregate([
  {
    $group: {
      _id: "$book_id",
      total_borrowed: { $sum: 1 }
    }
  },
  {
    $sort: { total_borrowed: -1 }
  },
  {
    $limit: 1
  },
  {
    $lookup: {
      from: "books",
      localField: "_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $project: {
      _id: 0,
      book_title: { $arrayElemAt: ["$book.title", 0] },
      total_borrowed: 1
    }
  }
])

// 23. Find the total borrowing count by category
db.borrowings.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $group: {
      _id: { $arrayElemAt: ["$book.category", 0] },
      total_borrowings: { $sum: 1 }
    }
  },
  {
    $project: {
      _id: 0,
      category: "$_id",
      total_borrowings: 1
    }
  }
])

// 24. Find members who borrowed more than one book
db.borrowings.aggregate([
  {
    $group: {
      _id: "$member_id",
      total_books_borrowed: { $sum: 1 }
    }
  },
  {
    $match: {
      total_books_borrowed: { $gt: 1 }
    }
  },
  {
    $lookup: {
      from: "members",
      localField: "_id",
      foreignField: "member_id",
      as: "member"
    }
  },
  {
    $project: {
      _id: 0,
      member_name: { $arrayElemAt: ["$member.name", 0] },
      total_books_borrowed: 1
    }
  }
])

// 25. Display member name, city, total books borrowed
// Sort by highest books borrowed first
db.borrowings.aggregate([
  {
    $group: {
      _id: "$member_id",
      total_books_borrowed: { $sum: 1 }
    }
  },
  {
    $lookup: {
      from: "members",
      localField: "_id",
      foreignField: "member_id",
      as: "member"
    }
  },
  {
    $project: {
      _id: 0,
      member_name: { $arrayElemAt: ["$member.name", 0] },
      city: { $arrayElemAt: ["$member.city", 0] },
      total_books_borrowed: 1
    }
  },
  {
    $sort: { total_books_borrowed: -1 }
  }
])
