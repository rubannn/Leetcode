delete from Person
where id not in (select min(id) id from Person group by email)
