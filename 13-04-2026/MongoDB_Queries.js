use retail_db

db.customers.insertMany([
{ customer_id:1, name:"Arjun", city:"Hyderabad" },
{ customer_id:2, name:"Rahul", city:"Bangalore" },
{ customer_id:3, name:"Sneha", city:"Mumbai" },
{ customer_id:4, name:"Amit", city:"Delhi" },
{ customer_id:5, name:"Priya", city:"Hyderabad" }
])

db.products.insertMany([
{ product_id:101, name:"Laptop", category:"Electronics", price:75000 },
{ product_id:102, name:"Phone", category:"Electronics", price:50000 },
{ product_id:103, name:"Desk", category:"Furniture", price:15000 },
{ product_id:104, name:"Chair", category:"Furniture", price:7000 },
{ product_id:105, name:"Tablet", category:"Electronics", price:30000 }
])

db.orders.insertMany([
{ order_id:1001, customer_id:1, product_id:101, quantity:1, order_date:"2024-03-01" },
{ order_id:1002, customer_id:2, product_id:102, quantity:1, order_date:"2024-03-02" },
{ order_id:1003, customer_id:1, product_id:105, quantity:2, order_date:"2024-03-03" },
{ order_id:1004, customer_id:3, product_id:103, quantity:1, order_date:"2024-03-05" },
{ order_id:1005, customer_id:5, product_id:102, quantity:3, order_date:"2024-03-07" }
])

db.customers.find()
db.products.find()
db.orders.find()

db.customers.find({ city: "Hyderabad" })
db.products.find({ category: "Electronics" })
db.products.find({ price: { $gt: 30000 } })
db.orders.find({ quantity: { $gt: 1 } })

db.products.find().sort({ price: -1 })
db.customers.find().sort({ name: 1 })

db.orders.countDocuments()

db.products.aggregate([
{
  $group: {
    _id: null,
    average_price: { $avg: "$price" }
  }
}
])

db.products.aggregate([
{
  $group: {
    _id: null,
    max_price: { $max: "$price" }
  }
}
])

db.orders.aggregate([
{
  $group: {
    _id: "$product_id",
    total_quantity: { $sum: "$quantity" }
  }
}
])

db.orders.aggregate([
{
  $lookup: {
    from: "customers",
    localField: "customer_id",
    foreignField: "customer_id",
    as: "customer_details"
  }
}
])

db.orders.aggregate([
{
  $lookup: {
    from: "products",
    localField: "product_id",
    foreignField: "product_id",
    as: "product_details"
  }
}
])

db.orders.aggregate([
{
  $lookup: {
    from: "customers",
    localField: "customer_id",
    foreignField: "customer_id",
    as: "customer"
  }
},
{
  $lookup: {
    from: "products",
    localField: "product_id",
    foreignField: "product_id",
    as: "product"
  }
},
{
  $project: {
    _id: 0,
    customer_name: { $arrayElemAt: ["$customer.name", 0] },
    product_name: { $arrayElemAt: ["$product.name", 0] },
    quantity: 1,
    order_date: 1
  }
}
])

db.orders.aggregate([
{
  $group: {
    _id: "$product_id",
    total_quantity: { $sum: "$quantity" }
  }
},
{
  $lookup: {
    from: "products",
    localField: "_id",
    foreignField: "product_id",
    as: "product"
  }
},
{
  $project: {
    _id: 0,
    product_name: { $arrayElemAt: ["$product.name", 0] },
    total_quantity: 1
  }
}
])

db.orders.aggregate([
{
  $lookup: {
    from: "products",
    localField: "product_id",
    foreignField: "product_id",
    as: "product"
  }
},
{
  $project: {
    product_name: { $arrayElemAt: ["$product.name", 0] },
    revenue: {
      $multiply: [
        "$quantity",
        { $arrayElemAt: ["$product.price", 0] }
      ]
    }
  }
},
{
  $group: {
    _id: "$product_name",
    total_revenue: { $sum: "$revenue" }
  }
}
])

db.orders.aggregate([
{
  $lookup: {
    from: "customers",
    localField: "customer_id",
    foreignField: "customer_id",
    as: "customer"
  }
},
{
  $lookup: {
    from: "products",
    localField: "product_id",
    foreignField: "product_id",
    as: "product"
  }
},
{
  $project: {
    customer_name: { $arrayElemAt: ["$customer.name", 0] },
    revenue: {
      $multiply: [
        "$quantity",
        { $arrayElemAt: ["$product.price", 0] }
      ]
    }
  }
},
{
  $group: {
    _id: "$customer_name",
    total_revenue: { $sum: "$revenue" }
  }
}
])

db.orders.aggregate([
{
  $group: {
    _id: "$product_id",
    total_quantity: { $sum: "$quantity" }
  }
},
{
  $sort: { total_quantity: -1 }
},
{
  $limit: 1
},
{
  $lookup: {
    from: "products",
    localField: "_id",
    foreignField: "product_id",
    as: "product"
  }
},
{
  $project: {
    _id: 0,
    product_name: { $arrayElemAt: ["$product.name", 0] },
    total_quantity: 1
  }
}
])
