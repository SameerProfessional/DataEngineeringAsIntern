# RDBMS Question Bank for Data Engineers
*Comprehensive Questions for Real-World Project Scenarios*

---

## 1. RDBMS Fundamentals & Architecture

### Conceptual Questions
1. **What are the key differences between RDBMS and NoSQL databases, and when would you choose each for a data engineering project?**
2. **Explain how RDBMS fits into a modern data architecture alongside data lakes and data warehouses.**
3. **What are the limitations of RDBMS that data engineers should be aware of when designing scalable systems?**
4. **How does RDBMS handle concurrent users in a high-traffic application, and what are the implications for data pipeline design?**

### Practical Scenarios
5. **Your company is migrating from a legacy file-based system to RDBMS. What factors would you consider in the migration strategy?**
6. **You're designing a data warehouse. Would you use RDBMS or consider alternatives? Justify your decision.**
7. **How would you handle the situation where your RDBMS becomes a bottleneck in your ETL pipeline?**

---

## 2. ACID Properties - Deep Dive

### Understanding ACID in Practice
8. **A bank transfer involves debiting one account and crediting another. How do ACID properties ensure data consistency?**
9. **Your ETL job processes 1 million records. If it fails at record 750,000, how does Atomicity help, and what's your recovery strategy?**
10. **Explain how Isolation levels (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE) affect data pipeline performance.**
11. **What happens to Consistency when you have multiple databases involved in a distributed transaction?**
12. **How does Durability impact your backup and disaster recovery strategy for critical data pipelines?**

### Real-World Scenarios
13. **You notice phantom reads in your reporting queries. Which ACID property is being violated, and how would you fix it?**
14. **During a data migration, some transactions are rolled back due to constraint violations. How would you handle partial failures?**
15. **Your application requires eventual consistency rather than strong consistency. Would traditional RDBMS be suitable?**

---

## 3. Database Models Comparison

### Model Selection Questions
16. **You need to store employee hierarchy data (CEO → VP → Manager → Staff). Compare how Hierarchical, Network, and Relational models would handle this.**
17. **For a social media platform where users can have multiple relationships, which database model would be most efficient?**
18. **When would you consider a Hierarchical model over a Relational model in modern data engineering?**
19. **How would you represent a many-to-many relationship in each database model?**

### Migration Scenarios
20. **You're migrating from a hierarchical database to a relational one. What challenges would you face?**
21. **How would you design a data pipeline that needs to integrate data from systems using different database models?**

---

## 4. Relational Database Design

### Schema Design
22. **Design a database schema for an e-commerce platform including customers, orders, products, and inventory. What tables and relationships would you create?**
23. **How would you design a schema to track data lineage in your ETL pipelines?**
24. **You need to store time-series sensor data from IoT devices. How would you design the relational schema for optimal query performance?**
25. **Design a schema for a data catalog that tracks all tables, columns, and their business definitions across multiple databases.**

### Optimization Questions
26. **Your fact table has 100 million rows and queries are slow. How would you optimize the table structure?**
27. **How would you design tables to support both OLTP and OLAP workloads efficiently?**
28. **What's the trade-off between normalization and denormalization in a data warehouse context?**

---

## 5. Data Integrity & Constraints

### Constraint Design
29. **Design constraints for a customer orders system ensuring data quality for downstream analytics.**
30. **How would you implement soft delete functionality while maintaining referential integrity?**
31. **You're loading data from multiple sources with different ID formats. How would you handle primary key conflicts?**
32. **Design a constraint strategy for a slowly changing dimension (SCD) table.**

### Data Quality Scenarios
33. **Your ETL job violates foreign key constraints during data loading. What are your options to handle this?**
34. **How would you implement data validation rules that go beyond standard database constraints?**
35. **You need to ensure that the sum of order line items equals the order total. How would you implement this constraint?**
36. **Design constraints for a temporal table that tracks changes over time.**

### Troubleshooting
37. **A unique constraint is preventing your data load. How would you identify and resolve duplicate records?**
38. **Your application allows NULL values, but your analytics queries produce incorrect results. How would you handle this?**

---

## 6. DDL Operations

### CREATE Statements
39. **Write DDL to create a partitioned table for storing daily sales data with appropriate indexes.**
40. **Create a database schema for a data lake catalog including metadata tables.**
41. **Design DDL for a staging area that can handle schema changes from source systems.**
42. **Create tables with appropriate data types for storing JSON, XML, and binary data.**

### ALTER Operations
43. **Your production table needs a new column for compliance reporting. Write the safest ALTER statement approach.**
44. **How would you add a foreign key constraint to a table with existing data that might violate the constraint?**
45. **You need to change a column from VARCHAR(50) to VARCHAR(200) in a 10GB table. What's your strategy?**
46. **How would you modify a table structure to support horizontal partitioning?**

### DROP Operations
47. **Write a script to safely drop a table that's referenced by multiple foreign keys.**
48. **You need to drop a column that's used in several views and stored procedures. What's your approach?**
49. **How would you implement a soft drop strategy for tables in a data warehouse?**

---

## 7. DML Operations - Advanced Scenarios

### INSERT Operations
50. **Write an INSERT statement that handles conflicts using UPSERT logic.**
51. **How would you bulk insert 10 million records efficiently while maintaining data quality?**
52. **Design an INSERT strategy for loading slowly changing dimension data.**
53. **Write an INSERT statement that populates a fact table from multiple dimension tables.**

### UPDATE Operations
54. **Update all records in a 50 million row table efficiently without locking the entire table.**
55. **Write an UPDATE statement that implements slowly changing dimension Type 2 logic.**
56. **How would you update records based on complex business rules involving multiple tables?**
57. **Design an UPDATE strategy for handling late-arriving data in a data warehouse.**

### DELETE Operations
58. **Write a DELETE statement that removes old partitions while maintaining referential integrity.**
59. **How would you implement a cascading delete across multiple related tables safely?**
60. **Design a DELETE strategy for GDPR compliance (right to be forgotten).**

---

## 8. SELECT Statements & Data Retrieval

### Complex Queries
61. **Write a query to find the top 10 customers by revenue for each region and month.**
62. **Create a query that identifies gaps in sequential data (missing order numbers, dates, etc.).**
63. **Write a query to detect duplicate records based on business logic rather than exact matches.**
64. **Design a query to calculate running totals and moving averages for time-series data.**

### Performance Optimization
65. **Your SELECT query with multiple JOINs is slow. How would you optimize it?**
66. **Write a query that efficiently handles large result sets without overwhelming memory.**
67. **How would you modify a query to take advantage of partitioned tables?**

---

## 9. WHERE Clause & Filtering

### Complex Filtering
68. **Write WHERE clauses to handle NULL values in different business scenarios.**
69. **Create filters for date ranges that handle different time zones and daylight saving changes.**
70. **Design WHERE conditions for fuzzy matching of customer names and addresses.**
71. **Write efficient WHERE clauses for filtering large datasets with multiple optional parameters.**

### Data Quality Filtering
72. **Write WHERE conditions to identify data quality issues in your source data.**
73. **Create filters to exclude test data and system-generated records from production queries.**
74. **Design WHERE clauses for data profiling and anomaly detection.**

---

## 10. ORDER BY & DISTINCT

### Sorting Strategies
75. **Design ORDER BY clauses for large result sets that won't cause memory issues.**
76. **Write queries with custom sorting logic for business-specific ordering requirements.**
77. **How would you implement stable sorting for paginated results in a data application?**

### Deduplication
78. **Use DISTINCT to remove duplicates while preserving the most recent record for each entity.**
79. **Write queries to identify and handle different types of duplicate data scenarios.**
80. **Design DISTINCT strategies for hierarchical or nested data structures.**

---

## 11. Aggregate Functions

### Business Calculations
81. **Calculate customer lifetime value using aggregate functions across multiple tables.**
82. **Write queries to compute data quality metrics (completeness, accuracy ratios).**
83. **Design aggregations for real-time dashboard metrics with proper handling of NULL values.**
84. **Create queries that calculate percentiles and quartiles for performance metrics.**

### Performance Considerations
85. **Optimize aggregate queries on large datasets using appropriate indexing strategies.**
86. **Write aggregate queries that work efficiently with partitioned tables.**
87. **Design streaming aggregations for real-time data processing scenarios.**

---

## 12. GROUP BY & HAVING

### Advanced Grouping
88. **Write GROUP BY queries that handle hierarchical grouping (year/month/day rollups).**
89. **Create queries that group by calculated fields and complex expressions.**
90. **Design GROUP BY logic for pivot-like operations without using PIVOT syntax.**
91. **Write queries that group by date ranges and time windows for time-series analysis.**

### HAVING Clause Applications
92. **Use HAVING to identify outliers and anomalies in aggregated data.**
93. **Write HAVING clauses that implement business rules on grouped data.**
94. **Design queries that use HAVING to filter groups based on statistical measures.**

---

## 13. Subqueries

### Correlated Subqueries
95. **Write correlated subqueries to find customers who haven't placed orders in the last 6 months.**
96. **Create queries using EXISTS to efficiently check for related data across large tables.**
97. **Design correlated subqueries for calculating running totals and rankings.**

### Performance Optimization
98. **Rewrite slow subqueries as JOINs and compare performance.**
99. **Optimize IN subqueries that are causing performance issues.**
100. **Design subquery strategies for data validation and quality checks.**

### Complex Nested Queries
101. **Write multi-level nested subqueries for complex business logic implementation.**
102. **Create subqueries that handle hierarchical data relationships.**
103. **Design subqueries for data reconciliation between different source systems.**

---

## 14. Advanced Operators

### IN Operator
104. **Use IN efficiently with large lists of values from other tables or applications.**
105. **Handle NULL values properly when using IN and NOT IN operators.**
106. **Optimize IN queries that are causing performance bottlenecks.**

### BETWEEN Operator
107. **Use BETWEEN for date range queries that handle edge cases properly.**
108. **Design BETWEEN queries for numeric ranges in data validation scenarios.**
109. **Handle timezone considerations when using BETWEEN with datetime data.**

### LIKE Operator
110. **Write LIKE patterns for data cleansing and standardization tasks.**
111. **Use LIKE efficiently for searching large text fields without causing full table scans.**
112. **Design pattern matching logic for data quality and validation rules.**

---

## 15. Integration & System Design Questions

### ETL Pipeline Integration
113. **How would you design database interactions in an ETL pipeline that processes 1TB of data daily?**
114. **What database design patterns would you use for a CDC (Change Data Capture) implementation?**
115. **How would you handle schema evolution in your database when source systems change frequently?**

### Performance & Scalability
116. **Your database queries are becoming the bottleneck in your data pipeline. What solutions would you consider?**
117. **How would you design a database solution that can scale from 1GB to 100TB of data?**
118. **What database partitioning strategy would you implement for a time-series data warehouse?**

### Data Quality & Monitoring
119. **Design a database solution for monitoring data quality across your entire data pipeline.**
120. **How would you implement data lineage tracking using database tables?**
121. **What database design would you use for storing and querying data profiling results?**

---

## 16. Troubleshooting & Problem-Solving

### Common Issues
122. **Your production database is running out of storage space. What immediate and long-term solutions would you implement?**
123. **A critical ETL job is failing due to constraint violations. How would you diagnose and fix the issue?**
124. **Users report that their queries are returning different results at different times. How would you investigate?**

### Performance Issues
125. **A report that used to run in 2 minutes now takes 2 hours. What's your troubleshooting approach?**
126. **Your database server CPU is at 100% during ETL loads. How would you optimize the process?**
127. **Memory usage is constantly high on your database server. What would you investigate?**

### Data Consistency Issues
128. **You discover that aggregate tables don't match the source detail tables. How would you identify the root cause?**
129. **Data loaded yesterday is missing from today's reports. What's your investigation strategy?**
130. **You find duplicate records in a table that should have unique constraints. How would you resolve this?**

---

## Answer Guidelines for Self-Assessment

When answering these questions, consider:

1. **Performance Impact**: How does your solution affect query performance and system resources?
2. **Scalability**: Will your approach work as data volume grows?
3. **Maintainability**: How easy is it to modify and support your solution?
4. **Data Quality**: Does your approach ensure data accuracy and consistency?
5. **Business Impact**: How does your technical solution support business requirements?
6. **Error Handling**: What happens when things go wrong?
7. **Monitoring**: How would you detect issues with your implementation?
8. **Documentation**: How would you document your solution for other team members?

---

*Practice these questions to build confidence in handling real-world data engineering challenges with RDBMS systems.*
