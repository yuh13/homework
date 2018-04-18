USE sakila;

SELECT * FROM actor;

#1a)
SELECT first_name, last_name FROM actor;

#1b)
SELECT CONCAT(first_name,' ', last_name) AS Actor_name FROM actor;

#2a)
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = 'JOE';

#2b)
SELECT actor_id, first_name, last_name FROM actor WHERE last_name LIKE '%GEN%';

#2c)
SELECT actor_id, first_name, last_name FROM actor WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name;


SELECT * FROM country;
#2d)
SELECT country_id, country FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

#3a)
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(30);

SELECT actor_id, first_name, middle_name, last_name FROM actor;

#3b)
ALTER TABLE actor
MODIFY COLUMN middle_name BLOB;

#3c)
ALTER TABLE actor
DROP COLUMN middle_name;

#4a)
SELECT last_name, count(*) as total FROM actor GROUP BY last_name;

#4b)
SELECT last_name, count(*) as total FROM actor GROUP BY last_name HAVING COUNT(last_name) >= 2;

#4c)
UPDATE actor SET first_name = 'GROUCHO' WHERE first_name = 'HARPO';
SELECT first_name, last_name FROM actor WHERE last_name = 'WILLIAMS';

#4d)
UPDATE actor SET first_name = CASE WHEN first_name = 'GROUCHO' THEN 'HARPO' ELSE 'MUCHO GROUCHO' END WHERE first_name = 'GROUCHO';


#5a)
SHOW CREATE TABLE address;
-- 
-- CREATE TABLE `address` (
--   `address_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
--   `address` varchar(50) NOT NULL,
--   `address2` varchar(50) DEFAULT NULL,
--   `district` varchar(20) NOT NULL,
--   `city_id` smallint(5) unsigned NOT NULL,
--   `postal_code` varchar(10) DEFAULT NULL,
--   `phone` varchar(20) NOT NULL,
--   `location` geometry NOT NULL,
--   `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--   PRIMARY KEY (`address_id`),
--   KEY `idx_fk_city_id` (`city_id`),
--   SPATIAL KEY `idx_location` (`location`),
--   CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
-- ) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8

#6a)
SELECT * FROM staff;
SELECT * FROM address;

SELECT s.first_name, s.last_name, a.address FROM staff as s JOIN address as a USING(address_id);

#6b)
SELECT * FROM payment;
SELECT s.first_name, s.last_name, SUM(amount) as total_amount 
	FROM staff as s 
    JOIN payment as p 
    USING(staff_id) 
    WHERE payment_date 
    BETWEEN '2005-08-01' 
    AND '2005-08-31' 
    GROUP BY staff_id;

#6c)
SELECT * FROM film;
SELECT * FROM film_actor;

SELECT f.title, count(*) as num_actors 
	FROM film as f 
    JOIN film_actor as fa 
    USING(film_id) 
    GROUP BY fa.film_id;

#6d)
SELECT * FROM inventory;
SELECT f.title, count(*) as copies 
	FROM inventory 
	JOIN film as f 
	USING(film_id) 
	WHERE film_id = (
		SELECT film_id 
        FROM film 
        WHERE title = 'Hunchback Impossible'
        ) 
	GROUP BY film_id;
    
#6e)
SELECT * FROM customer;
SELECT c.first_name, c.last_name, SUM(amount) as total_paid 
	FROM customer as c 
    JOIN payment as p
    USING(customer_id)
    GROUP BY customer_id
    ORDER BY last_name, first_name;
    
#7a)
SELECT * FROM film;
SELECT * FROM language;

SELECT f.title, l.name 
	FROM film as f
    JOIN language as l
    USING(language_id)
    WHERE f.title LIKE 'L%' OR 'Q%' AND l.language_id = (
		SELECT language_id 
		FROM language
		WHERE name = 'English'
        )
	;

#7b)
SELECT * FROM film;
SELECT * FROM actor;
SELECT a.first_name, a.last_name 
	FROM actor as a
    WHERE a.actor_id IN (
		SELECT fa.actor_id
        FROM film_actor as fa
        WHERE film_id = (
			SELECT film_id
            FROM film
            WHERE title = 'Alone Trip'
            )
		)
	;

#7c)
SELECT * FROM customer;
SELECT * FROM address;
SELECT * FROM city;
SELECT * FROM country;

SELECT first_name, last_name, email
	FROM customer as c
    WHERE address_id IN (
		SELECT address_id
        FROM address
        WHERE city_id IN (
			SELECT city_id
            FROM city
            WHERE country_id = (SELECT country_id FROM country WHERE country = 'Canada')
            )
		)
	;

#7d)
SELECT * FROM film_category;
SELECT * FROM category;
SELECT title
	FROM film
    WHERE film_id IN (
		SELECT film_id
        FROM film_category
        WHERE category_id IN (
			SELECT category_id
            FROM category
            WHERE name = 'Family'
            )
		)
	;
    
#7e)
SELECT * FROM rental;
SELECT f.title, count(r.rental_id) as num_rented
	FROM film as f
    JOIN inventory as i
    USING(film_id)
    JOIN rental as r
    USING(inventory_id)
    GROUP BY film_id
    ORDER BY num_rented DESC;
    
-- SELECT title, sum(counts) as total_rents
-- 	FROM(
-- 	SELECT f.title, count(r.rental_id) as counts
-- 		FROM rental as r
-- 		JOIN inventory as i
-- 		USING(inventory_id)
-- 		JOIN film as f
-- 		USING (film_id)
-- 		GROUP BY r.inventory_id
-- 	) as rental_counts
--     GROUP BY title
--     ORDER BY total_rents DESC
--     ;

#7f)
SELECT * FROM store;
SELECT * FROM payment;
SELECT * FROM staff;
SELECT store.store_id, sum(payment.amount) as revenue_$
	FROM store
    JOIN staff
    USING(store_id)
    JOIN payment
    USING(staff_id)
    GROUP BY store_id;
    
#7g)
SELECT store.store_id, city.city, country.country
	FROM store
    JOIN address
    USING(address_id)
    JOIN city
    USING (city_id)
    JOIN country
    USING(country_id);
    
#7h) List the top five genres in gross revenue in descending order. 
#(Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT category.name, sum(payment.amount) as revenue_$
	FROM category
    JOIN film_category
    USING(category_id)
    JOIN inventory
    USING(film_id)
    JOIN rental
    USING(inventory_id)
    JOIN payment
    USING(rental_id)
    GROUP BY category_id
    ORDER BY revenue_$ DESC
    LIMIT 5;
 
 #8a)
CREATE VIEW TOP_5_GENRES AS 
	SELECT category.name, sum(payment.amount) as revenue_$
		FROM category
		JOIN film_category
		USING(category_id)
		JOIN inventory
		USING(film_id)
		JOIN rental
		USING(inventory_id)
		JOIN payment
		USING(rental_id)
		GROUP BY category_id
		ORDER BY revenue_$ DESC
		LIMIT 5;

#8b)
SELECT * FROM TOP_5_GENRES;

#8c)
DROP VIEW TOP_5_GENRES;
