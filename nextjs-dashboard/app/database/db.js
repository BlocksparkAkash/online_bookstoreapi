const mysql = require("mysql");

const db =mysql.createConnection({
    host:"localhost",
    user: "root",
    password: "1234",
    database: "online_bookstore"
})

db.connect(err => {
    if (err) {
        console.error("Error connecting to MYSQL database:", err);
    } else{
        console.log("Connected to Mysql database");
    }
});

module.exports = db;
