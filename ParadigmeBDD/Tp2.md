# TP2 

## Partie 1 :

### 1.
    APPEND 17052001 Corentin

### 2.

    LPUSH R5A10 MongoDB
    LPUSH R5A10 Dynomite
    LPUSH R5A10 Cassandra
    LPUSH R5A10 HBase

    LRANGE R5A10 0 -1

### 3.

    LTRIM R5A10 0 2

### 4.

    SADD C c
    SMEMBERS C

### 5. 
    
    ZADD favoriteDB 1 PostGreSQL 2 OracleDb 3 MariaDB 4 SQLite 5 MySQL
    ZADD favoriteDB 1 MariaDB

### 6.

    ZSCAN favoriteDB 1

### 7. 

    HSET Profils identifiant 01 prenom Corentin nom RICHARD dateNaissance 17/05/2001 email rcorentin63@gmail.com

### 8. 

    HDEL Profils email
    HGETALL Profils


### 9. 

    SUBSCRIBE R5A10

### 10. 

    PUBLISH R5A10

### 11.
    
    EXPIRE 17052001 10

### 12.

    PERSIST 17052001

### 13.

    PEXPIRE 17052001 10

### 14. 

    PERSIST 17052001