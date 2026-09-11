# 🗄️ AiraLang `sqlite` Module
> **Embedded Relational SQL Database**

## Import
```aira
import "sqlite";
```

## Methods
- `sqlite.open(path)`: Open or create database file.
- `sqlite.execute(db, sql, [params])`: Execute DDL/DML statements (INSERT, UPDATE, DELETE).
- `sqlite.query(db, sql, [params])`: Execute SELECT and return rows as dictionary list.
- `sqlite.close(db)`: Close database connection.

## Example
```aira
import "sqlite";

let db = sqlite.open("test.db");
sqlite.execute(db, "CREATE TABLE IF NOT EXISTS logs (msg TEXT);");
sqlite.execute(db, "INSERT INTO logs VALUES (?);", ["System Booted"]);
let rows = sqlite.query(db, "SELECT * FROM logs;");
say rows;
sqlite.close(db);
```
