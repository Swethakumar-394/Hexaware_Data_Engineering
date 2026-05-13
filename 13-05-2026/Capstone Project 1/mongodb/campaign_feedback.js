use retail_feedback_db

db.campaign_feedback.insertMany([
{
    customer_name: "Swetha",
    campaign_name: "Summer Sale",
    feedback: "Good discounts on electronics",
    rating: 5
},
{
    customer_name: "Rahul",
    campaign_name: "Festival Offer",
    feedback: "Need more fashion products",
    rating: 3
},
{
    customer_name: "Anitha",
    campaign_name: "Mega Electronics Sale",
    feedback: "Excellent offers",
    rating: 4
}
])

db.campaign_feedback.createIndex({campaign_name: 1})
