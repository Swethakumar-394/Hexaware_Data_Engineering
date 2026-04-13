db.products.find()

db.products.find({ category: "Electronics" })

db.products.find({ city: "Hyderabad" })

db.products.find({ price: { $gt: 30000 } })

db.products.find({ price: { $lt: 20000 } })

db.products.find({ price: { $gte: 10000, $lte: 50000 } })

db.products.find({ category: "Furniture" })

db.products.find({ category: "Electronics", city: "Hyderabad" })

db.products.find({ city: { $in: ["Hyderabad", "Bangalore"] } })

db.products.find({ category: { $ne: "Furniture" } })

db.products.find({}, { _id: 0, name: 1, price: 1 })

db.products.find({}, { _id: 0, name: 1, category: 1, city: 1 })

db.products.find().sort({ price: 1 })

db.products.find().sort({ price: -1 })

db.products.find().sort({ price: -1 }).limit(3)

db.products.find().sort({ price: 1 }).limit(2)

db.products.find().skip(2)

db.products.find({ stock: { $gt: 10 } })

db.products.find({ stock: { $lte: 10 } })

db.products.find({ category: "Electronics", price: { $gt: 40000 } })

db.products.updateOne(
  { name: "Laptop" },
  { $set: { price: 80000 } }
)

db.products.updateMany(
  { category: "Electronics" },
  { $set: { discount: 10 } }
)

db.products.deleteOne({ name: "Printer" })

db.products.deleteMany({ category: "Furniture" })

db.products.countDocuments()

db.products.countDocuments({ category: "Electronics" })

db.products.aggregate([
  {
    $group: {
      _id: "$category",
      total_stock: { $sum: "$stock" }
    }
  }
])

db.products.aggregate([
  {
    $group: {
      _id: "$category",
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

db.products.aggregate([
  {
    $project: {
      name: 1,
      inventory_value: { $multiply: ["$price", "$stock"] }
    }
  },
  {
    $group: {
      _id: null,
      total_inventory_value: { $sum: "$inventory_value" }
    }
  }
])
