SELECT *
FROM Users
WHERE mail LIKE '[a-zA-Z]%'
      AND mail LIKE '%@leetcode.com'
      AND mail NOT LIKE '%[^a-zA-Z0-9_.-]@leetcode.com'
      AND mail NOT LIKE '%.@%'
      AND mail NOT LIKE '%-.@%'
      AND mail NOT LIKE '%@%@%'
      AND mail NOT LIKE '%[%!#$()*+=/&^]%';
