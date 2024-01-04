
# Create the secret
kubectl create secret generic mysql-secret --from-literal=username=root --from-literal=password='mV>Z6bKXe1}w?a^.' --from-literal=hostname='74.220.17.164' --from-literal=db_name='goals_database'

# Verify the secret
kubectl get secret mysql-secret -o yaml

# Create Table 
mysql -u root -h <host> -p

```
CREATE DATABASE goals_database;


USE goals_database;

CREATE TABLE goals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    goal_name VARCHAR(255) NOT NULL
);

```


