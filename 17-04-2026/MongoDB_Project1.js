//MongoDB Capstone Project 1
//Online Store Order Analytics

//Created a connection online_store_db
//Using the created connection

use("online_store_db")

// Customers collection
db.customers.insertMany([
  { customer_id: 1, name: "Aarav", city: "Hyderabad", membership: "Gold", age: 25 },
  { customer_id: 2, name: "Priya", city: "Bangalore", membership: "Silver", age: 28 },
  { customer_id: 3, name: "Rahul", city: "Mumbai", membership: "Gold", age: 30 },
  { customer_id: 4, name: "Sneha", city: "Delhi", membership: "Silver", age: 27 },
  { customer_id: 5, name: "Kiran", city: "Hyderabad", membership: "Gold", age: 32 },
  { customer_id: 6, name: "Meera", city: "Chennai", membership: "Bronze", age: 24 }
])

// Products collection
db.products.insertMany([
  { product_id: 101, name: "Laptop", category: "Electronics", price: 75000, stock: 10 },
  { product_id: 102, name: "Phone", category: "Electronics", price: 50000, stock: 15 },
  { product_id: 103, name: "Desk", category: "Furniture", price: 15000, stock: 8 },
  { product_id: 104, name: "Chair", category: "Furniture", price: 7000, stock: 20 },
  { product_id: 105, name: "Tablet", category: "Electronics", price: 30000, stock: 12 },
  { product_id: 106, name: "Printer", category: "Electronics", price: 12000, stock: 5 }
])

// Orders collection
db.orders.insertMany([
  { order_id: 1001, customer_id: 1, product_id: 101, quantity: 1, order_date: "2026-03-01", status: "Delivered" },
  { order_id: 1002, customer_id: 2, product_id: 102, quantity: 2, order_date: "2026-03-02", status: "Pending" },
  { order_id: 1003, customer_id: 1, product_id: 105, quantity: 1, order_date: "2026-03-03", status: "Delivered" },
  { order_id: 1004, customer_id: 3, product_id: 103, quantity: 1, order_date: "2026-03-04", status: "Cancelled" },
  { order_id: 1005, customer_id: 5, product_id: 102, quantity: 3, order_date: "2026-03-05", status: "Delivered" },
  { order_id: 1006, customer_id: 6, product_id: 104, quantity: 4, order_date: "2026-03-06", status: "Pending" },
  { order_id: 1007, customer_id: 4, product_id: 106, quantity: 2, order_date: "2026-03-07", status: "Cancelled" },
  { order_id: 1008, customer_id: 3, product_id: 101, quantity: 1, order_date: "2026-03-08", status: "Delivered" }
])

//Basic Queries
// 1. All customers
db.customers.find()

// 2. All products
db.products.find()

// 3. All orders
db.orders.find()

// 4. Customers from hyderabad
db.customers.find({ city: "Hyderabad" })

// 5. Products in electronics category
db.products.find({ category: "Electronics" })

// 6. Orders with delivered status
db.orders.find({ status: "Delivered" })


//Filtering Queries
// 7. Products with price greater than 30000
db.products.find({ price: { $gt: 30000 } })

// 8. Products with price between 10000 and 50000
db.products.find({ price: { $gte: 10000, $lte: 50000 } })

// 9. Customers whose age is greater than 26
db.customers.find({ age: { $gt: 26 } })

// 10. Orders whose quantity is greater than 1
db.orders.find({ quantity: { $gt: 1 } })

// 11. Products whose stock is less than or equal to 10
db.products.find({ stock: { $lte: 10 } })

// 12. Orders whose status is not cancelled
db.orders.find({ status: { $ne: "Cancelled" } })

// 13. Customers from hyderabad or mumbai
db.customers.find({ city: { $in: ["Hyderabad", "Mumbai"] } })

//Projection Queries
// 14. Customer name and city
db.customers.find({}, { _id: 0, name: 1, city: 1 })

// 15. Product name, category and price
db.products.find({}, { _id: 0, name: 1, category: 1, price: 1 })

// 16. Order id, quantity and status
db.orders.find({}, { _id: 0, order_id: 1, quantity: 1, status: 1 })

//Sorting, Limit, Skip
// 17.Sorted by price in ascending order
db.products.find().sort({ price: 1 })

// 18. Sorted by price in descending order
db.products.find().sort({ price: -1 })

// 19.The 3 most expensive products
db.products.find().sort({ price: -1 }).limit(3)

// 20. The 2 cheapest products
db.products.find().sort({ price: 1 }).limit(2)

// 21.Skip first 2 products
db.products.find().skip(2)

// 22. Sorted by age descending
db.customers.find().sort({ age: -1 })

// 23. Updated laptop price to 78000
db.products.updateOne({ name: "Laptop" },{ $set: { price: 78000 }})

// 24. Add discount field to all electronics products
db.products.updateMany({ category: "Electronics" },{ $set: { discount: 10 }})

// 25. Add priority high to pending orders
db.orders.updateMany({ status: "Pending" },{ $set: { priority: "High" }})

// 26. Change meera membership from bronze to silver
db.customers.updateOne({ name: "Meera" },{ $set: { membership: "Silver" }})

//Delete Operations
// 27. Delete product named printer
db.products.deleteOne({ name: "Printer" })

// 28. Delete all furniture products
db.products.deleteMany({ category: "Furniture" })

// 29. Delete cancelled orders
db.orders.deleteMany({ status: "Cancelled" })

//Count Queries
// 30. Count total customers
db.customers.countDocuments()

// 31. Count electronics products
db.products.countDocuments({ category: "Electronics" })

// 32. Count delivered orders
db.orders.countDocuments({ status: "Delivered" })

// 33. Count customers from hyderabad
db.customers.countDocuments({ city: "Hyderabad" })

//Aggregation Queries
// 34. Total stock available in each category
db.products.aggregate([{$group: {_id: "$category",total_stock: { $sum: "$stock" }}}])

// 35. Average product price in each category
db.products.aggregate([{$group: {_id: "$category",average_price: { $avg: "$price" }}}])

// 36. Maximum product price
db.products.aggregate([{$group: {_id: null,max_price: { $max: "$price" }}}])

// 37. Minimum product price
db.products.aggregate([{$group: {_id: null,min_price: { $min: "$price" }}}])

// 38. Total inventory value
db.products.aggregate([{$project: {name: 1,total_value: { $multiply: ["$price", "$stock"]}}},{$group: { _id: null,total_inventory_value: { $sum: "$total_value" }}}])

// 39. Total quantity ordered for each product
db.orders.aggregate([{$group: {_id: "$product_id",total_quantity: { $sum: "$quantity" }}}])

// 40. Total quantity ordered by each customer
db.orders.aggregate([{$group: {_id: "$customer_id",total_quantity: { $sum: "$quantity" }}}])

//Lookup Queries
// 41. Orders with customer details
db.orders.aggregate([{$lookup: {from: "customers",localField: "customer_id",foreignField: "customer_id",as: "customer_details"}}])

// 42. Orders with product details
db.orders.aggregate([{$lookup: {from: "products",localField: "product_id",foreignField: "product_id",as: "product_details"}}])

// 43. Customer name and product name for each order
db.orders.aggregate([
  {$lookup: {from: "customers",localField: "customer_id",foreignField: "customer_id",as: "customer"}},
  {$lookup: {from: "products",localField: "product_id",foreignField: "product_id",as: "product"}},
  {$project: {_id: 0,order_id: 1,customer_name: { $arrayElemAt: ["$customer.name", 0] },product_name: { $arrayElemAt: ["$product.name", 0] }}}
])

// 44. Customer name, city, product name, quantity and order status
db.orders.aggregate([
  {$lookup: {from: "customers",localField: "customer_id",foreignField: "customer_id",as: "customer"}},
  {$lookup: {from: "products",localField: "product_id",foreignField: "product_id",as: "product"}},
  {$project: {_id: 0,customer_name: { $arrayElemAt: ["$customer.name", 0] },city: { $arrayElemAt: ["$customer.city", 0] },product_name: { $arrayElemAt: ["$product.name", 0] },quantity: 1,order_status: "$status"}}
])
