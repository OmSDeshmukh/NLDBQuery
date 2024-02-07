few_shots = [
    {'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
     'SQLResult': "Result of the SQL query",
     'Answer': "58 t-shirts have been left for Nike in XS size and white color in the store"},
    {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
     'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
     'SQLResult': "Result of the SQL query",
     'Answer': "The total price of the inventory for all S-size t-shirts is twenty-two thousand two hundred ninety-two"},
    {'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue will our store generate (post discounts)?",
     'SQLQuery': """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "The store will generate a revenue of sixteen thousand seven hundred twenty-five point four after applying discounts to all the Levi’s T-shirts"},
     {'Question': "If we have to sell all the Levi’s T-shirts today. How much revenue will our store generate without discount?",
      'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
      'SQLResult': "Result of the SQL query",
      'Answer': "The store will generate a revenue of seventeen thousand four hundred sixty-two without any discounts for all the Levi’s T-shirts"},
    {'Question': "How many white color Levi's shirts do I have?",
     'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
     'SQLResult': "Result of the SQL query",
     'Answer': "There are 290 white color Levi's shirts in the store"},
    {'Question': "How much sales amount will be generated if we sell all large size t-shirts today in Nike brand after discounts?",
     'SQLQuery': """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Nike' and size="L"
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "The sales amount generated after selling all large size t-shirts today in Nike brand, post discounts, will be 290"} 
]
