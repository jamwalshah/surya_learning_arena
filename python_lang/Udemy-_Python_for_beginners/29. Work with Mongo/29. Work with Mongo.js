db; // shows current database
use products; // to use specified database, creates database if not exists
show dbs; // lists all databases
db.product.insert({"name":"IPhone", "price":1200}); // creates collection on the go with inserting document
show dbs; 
show collections; // lists all collections
db.product.find(); // lists all documents in collection
db.product.insertOne({"name":"Samsung", "price":1000}); // inserts one document in collection
db.product.find();
db.product.find({"name":"IPhone"}); // lists all the documents as per specified filter
db.product.find({"name":"IPhone"}).count(); // returns the count of documents returned by the find()
db.product.update({"name":"IPhone"}, {$set:{"price":1500}}); // updates or sets if not exists by the specified JSON to the set to all the documents as per specified filter
db.product.find({"name":"IPhone"});
cls; // clears screen
db.product.find();
db.product.remove({}); // removes all the documents as filter is empty
db.product.insertOne({"name":"Samsung", "price":1000});
db.product.find();
db.product.remove({"name":"Samsung"}); // removes the documents as per specified filter
