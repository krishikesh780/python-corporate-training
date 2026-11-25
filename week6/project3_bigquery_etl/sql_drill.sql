-- Interview SQL (SQLite / BigQuery dialect tweaks OK)

-- Latest row per policy_number (dedup)
WITH ranked AS (
    SELECT
        policy_number,
        name,
        premium,
        status,
        updated_at,
        ROW_NUMBER() OVER (
            PARTITION BY policy_number
            ORDER BY updated_at DESC
        ) AS rn
    FROM customers
)
SELECT * FROM ranked WHERE rn = 1;

-- Premium delta vs average
SELECT
    policy_number,
    premium,
    premium - AVG(premium) OVER () AS diff_from_avg
FROM customers;