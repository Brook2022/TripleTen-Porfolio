# SQL PROJECT
## Question 1

**Print the `company_name` field. Find the number of taxi rides for each taxi company for November 15-16, 2017. Name the resulting field `trips_amount` and print it, too. Sort the results by the `trips_amount` field in descending order.**

###SQL QUERY

```sql
SELECT 
    company_name,
    COUNT(*) AS trips_amount
FROM
    cabs
JOIN
    trips ON cabs.cab_id = trips.cab_id
WHERE 
    CAST(start_ts AS DATE) IN ('2017-11-15', '2017-11-16')
GROUP BY 
    Company_name
ORDER BY
    trips_amount DESC;
```

**Result**

company_name                                 | trips_amount
---------------------------------------------|--------------
Flash Cab                                    | 19,558
Taxi Affiliation Services                    | 11,422
Medallion Leasing                            | 10,367
Yellow Cab                                   | 9,888
Taxi Affiliation Service Yellow              | 9,299
Chicago Carriage Cab Corp                    | 9,181
City Service                                 | 8,448
Sun Taxi                                     | 7,701
Star North Management LLC                    | 7,455
Blue Ribbon Taxi Association Inc.            | 5,953
Choice Taxi Association                      | 5,015
Globe Taxi                                   | 4,383
Dispatch Taxi Affiliation                    | 3,355
Nova Taxi Affiliation LLC                    | 3,175
Patriot Taxi Dba Peace Taxi Associat         | 2,235
Checker Taxi Affiliation                     | 2,216
Blue Diamond                                 | 2,070
Chicago Medallion Management                 | 1,955
24 Seven Taxi                                | 1,775
Chicago Medallion Leasing INC                | 1,607
Checker Taxi                                 | 1,486
American United                              | 1,404
Chicago Independents                         | 1,296
KOAM Taxi Association                        | 1,259
Chicago Taxicab                              | 1,014
Top Cab Affiliation                          | 978
Gold Coast Taxi                              | 428
Service Taxi Association                     | 402
5 Star Taxi                                  | 310
303 Taxi                                     | 250
Setare Inc                                   | 230
American United Taxi Affiliation             | 210
Leonard Cab Co                               | 147
Metro Jet Taxi A                             | 146
Norshore Cab                                 | 127
6742 - 83735 Tasha Ride Inc                  | 39
3591 - 63480 Chuks Cab                       | 37
1469 - 64126 Omar Jada                       | 36
0118 - 42111 Godfrey S.Awir                  | 33
6743 - 78771 Luhak Corp                      | 33
6574 - Babylon Express Inc.                  | 31
Chicago Star Taxicab                         | 29
1085 - 72312 N and W Cab Co                  | 29
2809 - 95474 C & D Cab Co Inc.               | 29
2092 - 61288 Sbeih Company                   | 27
3011 - 66308 JBL Cab Inc.                    | 25
3620 - 52292 David K. Cab Corp.              | 21
4615 - 83503 Tyrone Henderson                | 21
3623 - 72222 Arrington Enterprises           | 20
5074 - 54002 Ahzmi Inc                       | 16
2823 - 73307 Lee Express Inc                 | 15
4623 - 27290 Jay Kim                         | 15
3721 - Santamaria Express, Alvaro Santamaria | 14
5006 - 39261 Salifu Bawa                     | 14
2192 - 73487 Zeymane Corp                    | 14
6057 - 24657 Richard Addo                    | 13
5997 - 65283 AW Services Inc.                | 12
Metro Group                                  | 11
5062 - 34841 Sam Mestas                      | 8
4053 - 40193 Adwar H. Nikola                 | 7
2733 - 74600 Benny Jona                      | 7
5874 - 73628 Sergey Cab Corp.                | 5
2241 - 44667 - Felman Corp, Manuel Alonso    | 3
3556 - 36214 RC Andrews Cab                  | 2

## Question 2

**Find the number of rides for every taxi companies whose name constains the words "Yellow" or "Blue" for November 1-7, 2017. Name the resulting variable trips_amount. Group the results by the company_name field.**

###SQL QUERY

```sql
SELECT 
    company_name,
    COUNT(*) AS strips_amount
FROM 
    cabs
JOIN
    trips ON cabs.cab_id = trips.cab_id
WHERE 
    CAST(start_ts AS DATE) BETWEEN '2017-11-1' AND '2017-11-7'
    AND
        Company_name LIKE '%Yellow%'
GROUP BY
    company_name
```

**Result**

company_name                                                | trips_amount
------------------------------------------------------------|--------------
Yellow Cab                                                  | 33,668
Taxi Affilation Service Yellow                              | 29,213
Blue Ribbon Taxi Association Inc                            | 17,675
Blue Diamond                                                | 6,764

## Question 3

**For November 1-7, 2017, the most popular taxi companies were Flash Cab and Taxi Affiliation Services. Find the number of rides for these two companines and name the resulting variable trips_amount. Join the rides for all other companies in the group "Other." Group the data by taxi company names. Name the field with taxi company names company. Sort the result in descending order by trips_amount**

###SQL QUERY

```sql
SELECT 
    company_name,
    COUNT(*) AS strips_amount
FROM 
    cabs
JOIN
    trips ON cabs.cab_id = trips.cab_id
WHERE 
    CAST(start_ts AS DATE) BETWEEN '2017-11-1' AND '2017-11-7'
    AND
        Company_name IN ('Flash Cab', 'Taxi Affilation Services')
GROUP BY
    company_name

UNION

SELECT 
    CASE
   WHEN company_name NOT IN ('Flash Cab', 'Taxi Affiliation Services') THEN 'Other'
    END AS company, 
    COUNT(*) AS trips_amount
FROM 
    cabs
JOIN
    trips ON cabs.cab_id = trips.cab_id
WHERE 
    CAST(start_ts AS DATE) BETWEEN '2017-11-1' AND '2017-11-7'
    AND 
    company_name NOT IN ('Flash Cab', 'Taxi Affiliation Services') 
GROUP BY 
   company
ORDER BY 
    trips_amount DESC;
```

**Result**

company_name                                                | trips_amount
------------------------------------------------------------|--------------
Other                                                       | 33,668
Flash Cab                                                   | 29,213
Taxi Affilation Services                                    | 17,675

## Question 4

**Retrieve the identifiers of the O'Hare and Loop neighborhoods from the neighborhoods table.**

###SQL QUERY

```sql
SELECT *
FROM
    neighborhoods
WHERE name LIKE '%Hare'
    OR name LIKE 'Loop';
```

**Result**

neighborhood_id                                              | name
-------------------------------------------------------------|--------------
50                                                           | Loop
63                                                           | O'Hare

## Question 5

**For each hour, retrieve the weather condition records from the weather_records table. Using the CASE operator, break all hours into two groups: Bad if the description field contains the words rain or storm, and Good for others. Name the resulting field weather_conditions. The final table must include two fields: date and hour(ts) and weather_conditions.**


###SQL QUERY

```sql
SELECT 
    ts,
    CASE
    WHEN description LIKE '%rain' OR description LIKE '%storm%' THEN 'Bad' ELse 'Good'
FROM
    weather_records;
```

**Result**

| ts                   | weather_conditions |
|----------------------|--------------------|
| 2017-11-01 00:00:00  | Good               |
| 2017-11-01 01:00:00  | Good               |
| 2017-11-01 02:00:00  | Good               |
| 2017-11-01 03:00:00  | Good               |
| 2017-11-01 04:00:00  | Good               |
| 2017-11-01 05:00:00  | Good               |
| 2017-11-01 06:00:00  | Good               |
| 2017-11-01 07:00:00  | Good               |
| 2017-11-01 08:00:00  | Good               |
| 2017-11-01 09:00:00  | Good               |
| 2017-11-01 10:00:00  | Good               |
| 2017-11-01 11:00:00  | Good               |
| 2017-11-01 12:00:00  | Good               |
| 2017-11-01 13:00:00  | Good               |
| 2017-11-01 14:00:00  | Good               |
| 2017-11-01 15:00:00  | Good               |
| 2017-11-01 16:00:00  | Good               |
| 2017-11-01 17:00:00  | Good               |
| 2017-11-01 18:00:00  | Good               |
| 2017-11-01 19:00:00  | Good               |
| 2017-11-01 20:00:00  | Good               |
| 2017-11-01 21:00:00  | Good               |
| 2017-11-01 22:00:00  | Good               |
| 2017-11-01 23:00:00  | Good               |
| 2017-11-02 00:00:00  | Good               |
| 2017-11-02 01:00:00  | Good               |
| 2017-11-02 02:00:00  | Good               |
| 2017-11-02 03:00:00  | Bad                |
| 2017-11-02 04:00:00  | Bad                |
| 2017-11-02 05:00:00  | Bad                |
| 2017-11-02 06:00:00  | Bad                |
| 2017-11-02 07:00:00  | Bad                |
| 2017-11-02 08:00:00  | Good               |
| 2017-11-02 09:00:00  | Good               |
| 2017-11-02 10:00:00  | Good               |
| 2017-11-02 11:00:00  | Good               |
| 2017-11-02 12:00:00  | Bad                |
| 2017-11-02 13:00:00  | Good               |
| 2017-11-02 14:00:00  | Good               |
| 2017-11-02 15:00:00  | Good               |
| 2017-11-02 16:00:00  | Good               |
| 2017-11-02 17:00:00  | Good               |
| 2017-11-02 18:00:00  | Good               |
| 2017-11-02 19:00:00  | Good               |
| 2017-11-02 20:00:00  | Bad                |
| 2017-11-02 21:00:00  | Bad                |
| 2017-11-02 22:00:00  | Good               |
| 2017-11-02 23:00:00  | Good               |
| 2017-11-03 00:00:00  | Bad                |
| 2017-11-03 01:00:00  | Good               |
| 2017-11-03 02:00:00  | Good               |
| 2017-11-03 03:00:00  | Good               |
| 2017-11-03 04:00:00  | Good               |
| 2017-11-03 05:00:00  | Good               |
| 2017-11-03 06:00:00  | Good               |
| 2017-11-03 07:00:00  | Good               |
| 2017-11-03 08:00:00  | Good               |
| 2017-11-03 09:00:00  | Good               |
| 2017-11-03 10:00:00  | Good               |
| 2017-11-03 11:00:00  | Good               |
| 2017-11-03 12:00:00  | Good               |
| 2017-11-03 13:00:00  | Good               |
| 2017-11-03 14:00:00  | Good               |
| 2017-11-03 15:00:00  | Good               |
| 2017-11-03 16:00:00  | Good               |
| 2017-11-03 17:00:00  | Good               |
| 2017-11-03 18:00:00  | Good               |
| 2017-11-03 19:00:00  | Good               |
| 2017-11-03 20:00:00  | Good               |
| 2017-11-03 21:00:00  | Good               |
| 2017-11-03 22:00:00  | Good               |
| 2017-11-03 23:00:00  | Good               |
| 2017-11-04 00:00:00  | Good               |
| 2017-11-04 01:00:00  | Good               |
| 2017-11-04 02:00:00  | Good               |
| 2017-11-04 03:00:00  | Good               |
| 2017-11-04 04:00:00  | Good               |
| 2017-11-04 05:00:00  | Good               |
| 2017-11-04 06:00:00  | Good               |
| 2017-11-04 07:00:00  | Good               |
| 2017-11-04 08:00:00  | Good               |
| 2017-11-04 09:00:00  | Good               |
| 2017-11-04 10:00:00  | Good               |
| 2017-11-04 11:00:00  | Good               |
| 2017-11-04 12:00:00  | Good               |
| 2017-11-04 13:00:00  | Good               |
| 2017-11-04 14:00:00  | Good               |
| 2017-11-04 15:00:00  | Good               |
| 2017-11-04 16:00:00  | Bad                |
| 2017-11-04 17:00:00  | Bad                |
| 2017-11-04 18:00:00  | Bad                |
| 2017-11-04 19:00:00  | Good               |
| 2017-11-04 20:00:00  | Good               |
| 2017-11-04 21:00:00  | Good               |
| 2017-11-04 22:00:00  | Good               |
| 2017-11-04 23:00:00  | Good               |
| 2017-11-05 00:00:00  | Good               |
| 2017-11-05 01:00:00  | Bad                |
| 2017-11-05 02:00:00  | Good               |
| 2017-11-05 03:00:00  | Good               |
| 2017-11-05 04:00:00  | Bad                |
| 2017-11-05 05:00:00  | Bad                |
| 2017-11-05 06:00:00  | Good               |
| 2017-11-05 07:00:00  | Good               |
| 2017-11-05 08:00:00  | Good               |
| 2017-11-05 09:00:00  | Good               |
| 2017-11-05 10:00:00  |


## Question 6

**Retrieve from the trips table all the rides that started in the Loop(pickup_location_id:50) on a Saturday and ended at O'Hare(dropoff_location_id:63). Get the weather conditions for each ride. Use the method you applied in the previous task. Also, retrieve the duration of each ride. Ignore rides for which data on weather conditions is not available**


**The table columns should be in the following order:**

-   start_ts
-   weather_conditions
-   duration_seconds


**sort by `trip_id`.**

###SQL QUERY

```sql
SELECT 
    start_ts,
    T.weather_conditions,
    duration_seconds
From trips
JOIN
    ( SELECT ts,
        CASE
        WHEN description LIKE '%rain% OR description LIKE %storm%' THEN 'Bad'
        ELSE 'Good'
        END AS weather_conditions
        FROM weather_records ) T
            ON trips.start_ts = T.ts
WHERE 
    pickup_location_id = 50
AND 
    dropoff_location_id = 63
AND
    EXTRACT(DOW FROM trips.start_ts) = 6
ORDER BY
    trip_id ;
```

**Result**

```markdown
| start_ts            | weather_conditions | duration_seconds |
|---------------------|--------------------|------------------|
| 2017-11-25 12:00:00 | Good               | 1380             |
| 2017-11-25 16:00:00 | Good               | 2410             |
| 2017-11-25 14:00:00 | Good               | 1920             |
| 2017-11-25 12:00:00 | Good               | 1543             |
| 2017-11-04 10:00:00 | Good               | 2512             |
| 2017-11-11 07:00:00 | Good               | 1440             |
| 2017-11-11 04:00:00 | Good               | 1320             |
| 2017-11-04 16:00:00 | Bad                | 2969             |
| 2017-11-18 11:00:00 | Good               | 2280             |
| 2017-11-04 16:00:00 | Bad                | 3120             |
| 2017-11-11 15:00:00 | Good               | 4800             |
| 2017-11-04 05:00:00 | Good               | 1260             |
| 2017-11-11 06:00:00 | Good               | 1346             |
| 2017-11-04 04:00:00 | Good               | 1333             |
| 2017-11-04 11:00:00 | Good               | 2574             |
| 2017-11-11 12:00:00 | Good               | 2441             |
| 2017-11-04 14:00:00 | Good               | 3300             |
| 2017-11-11 14:00:00 | Good               | 2460             |
| 2017-11-11 12:00:00 | Good               | 2040             |
| 2017-11-18 06:00:00 | Good               | 1500             |
| 2017-11-04 11:00:00 | Good               | 2040             |
| 2017-11-11 08:00:00 | Good               | 1470             |
| 2017-11-04 08:00:00 | Good               | 1546             |
| 2017-11-11 16:00:00 | Good               | 2100             |
| 2017-11-25 13:00:00 | Good               | 60               |
| 2017-11-04 12:00:00 | Good               | 2640             |
| 2017-11-25 10:00:00 | Good               | 1502             |
| 2017-11-11 12:00:00 | Good               | 1915             |
| 2017-11-04 12:00:00 | Good               | 2769             |
| 2017-11-11 13:00:00 | Good               | 2250             |
| 2017-11-11 04:00:00 | Good               | 1260             |
| 2017-11-18 14:00:00 | Good               | 2826             |
| 2017-11-04 14:00:00 | Good               | 3360             |
| 2017-11-04 14:00:00 | Good               | 3180             |
| 2017-11-25 20:00:00 | Good               | 2100             |
| 2017-11-04 10:00:00 | Good               | 1800             |
| 2017-11-11 12:00:00 | Good               | 2289             |
| 2017-11-04 08:00:00 | Good               | 1494             |
| 2017-11-11 11:00:00 | Good               | 1560             |
| 2017-11-18 12:00:00 | Bad                | 1980             |
| 2017-11-11 13:00:00 | Good               | 2115             |
| 2017-11-11 10:00:00 | Good               | 1506             |
| 2017-11-04 12:00:00 | Good               | 2580             |
| 2017-11-04 17:00:00 | Bad                | 2460             |
| 2017-11-11 09:00:00 | Good               | 1620             |
| 2017-11-04 06:00:00 | Good               | 1163             |
| 2017-11-04 05:00:00 | Good               | 1533             |
| 2017-11-11 04:00:00 | Good               | 1477             |
| 2017-11-11 19:00:00 | Good               | 1984             |
| 2017-11-04 13:00:00 | Good               | 2940             |
| 2017-11-04 07:00:00 | Good               | 1320             |
| 2017-11-04 06:00:00 | Good               | 1440             |
| 2017-11-11 06:00:00 | Good               | 1260             |
| 2017-11-11 08:00:00 | Good               | 1560             |
| 2017-11-04 09:00:00 | Good               | 1683             |
| 2017-11-11 05:00:00 | Good               | 1343             |
| 2017-11-18 06:00:00 | Good               | 1742             |
| 2017-11-04 09:00:00 | Good               | 1560             |
| 2017-11-11 08:00:00 | Good               | 1358             |
| 2017-11-11 12:00:00 | Good               | 1980             |
| 2017-11-04 16:00:00 | Bad                | 2760             |
| 2017-11-18 12:00:00 | Bad                | 2460             |
| 2017-11-18 10:00:00 | Bad                | 1440             |
| 2017-11-25 14:00:00 | Good               | 1620             |
| 2017-11-11 08:00:00 | Good               | 1415             |
| 2017-11-25 05:00:00 | Good               | 1325             |
| 2017-11-18 06:00:00 | Good               | 2100             |
| 2017-11-11 08:00:00 | Good               | 1320             |
| 2017-11-11 10:00:00 | Good               | 1260             |
| 2017-11-11 06:00:00 | Good               | 1260             |
| 2017-11-11 08:00:00 | Good               | 1200             |
| 2017-11-25 08:00:00 | Good               | 1320             |
| 2017-11-11 18:00:00 | Good               | 2280             |
| 2017-11-25 10:00:00 | Good               | 1320             |
| 2017-11-04 06:00:00 | Good               | 1140             |
| 2017-11-11 18:00:00 | Good               | 2520             |
| 2017-11-18 16:00:00 | Bad                | 3000             |
| 2017-11-11 19:00:00 | Good               | 1920             |
| 2017-11-04 18:00:00 | Bad                | 2363             |
| 2017-11-04 14:00:00 | Good               | 3084             |
| 2017-11-11 08:00:00 | Good               | 1380             |
| 2017-11-11 08:00:00 | Good               | 1380             |
| 2017-11-04 09:00:00 | Good               | 1380             |
| 2017-11-04 09:00:00 | Good               | 1380             |
| 2017-11-11 12:00:00 | Good               | 2213             |
| 2017-11-11 08:00:00 | Good               | 1140             |
| 2017-11-11 10:00:00 | Good               | 1435             |
| 2017-11-04 10:00:00 | Good               | 2460             |
| 2017-11-11 07:00:00 | Good               | 1200             |
| 2017-11-04 15:00:00 | Good               | 3201             |
| 2017-11-11 11:00:00 | Good               | 2074             |
| 2017-11-18 11:00:00 | Good               | 2843             |
| 2017-11-11 17:00:00 | Good               | 2426             |
| 2017-11-04 09:00:00 | Good               | 1740             |
| 2017-11-25 07:00:00 | Good               | 2340             |
| 2017-11-18 05:00:00 | Good               | 2075             |
| 2017-11-18 07:00:00 | Bad                | 1511             |
| 2017-11-11 18:00:00 | Good               | 2220             |
| 2017-11-04 10:00:00 | Good               | 2551             |
| 2017-11-11 16:00:00 | Good               | 2062             |
| 2017-11-04 12:00:00 | Good               | 2999             |
| 2017-11-04 08:00:00 | Good               | 1677             |
| 2017-11-04 06:00:00 | Good               | 1177             |
| 2017-11-11 06:00:00 | Good               | 1475             |
| 2017-11-25 08:00:00 | Good               | 1277             |
| 2017-11-11 04:00:00 | Good               | 1213             |
| 2017-11-18 13:00:00 | Bad                | 4044             |
| 2017-11-04 21:00:00 | Good               | 1680             |
| 2017-11-04 18:00:00 | Bad                | 1980             |
| 2017-11-25 18:00:00 | Good               | 2760             |
| 2017-11-11 09:00:00 | Good               | 1380             |
| 2017-11-11 07:00:00 | Good               | 1380             |
| 2017-11-18 08:00:00 | Bad                | 1320             |
| 2017-11-11 16:00:00 | Good               | 2591             |
| 2017-11-11 08:00:00 | Good               | 1260             |
| 2017-11-11 07:00:00 | Good               | 1380             |
| 2017-11-11 10:00:00 | Good               | 1440             |
| 2017-11-04 14:00:00 | Good               | 3240             |
| 2017-11-04 16:00:00 | Bad                | 2782             |
| 2017-11-04 14:00:00 | Good               | 3120             |
| 2017-11-04 19:00:00 | Good               | 1869             |
| 2017-11-11 06:00:00 | Good               | 1218             |
| 2017-11-11 11:00:00 | Good               | 1620             |
| 2017-11-11 10:00:00 | Good               | 1380             |
| 2017-11-11 08:00:00 | Good               | 1380             |
| 2017-11-11 09:00:00 | Good               | 1380             |
| 2017-11-11 07:00:00 | Good               | 1320             |
| 2017-11-04 14:00:00 | Good               | 3300             |
| 2017-11-04 13:00:00 | Good               | 3060             |
| 2017-11-11 13:00:00 | Good               | 2100             |
| 2017-11-18 14:00:00 | Good               | 3540             |
| 2017-11-11 21:00:00 | Good               | 1920             |
| 2017-11-11 17:00:00 | Good               | 2160             |
| 2017-11-11 13:00:00 | Good               | 2123             |
| 2017-11-11 07:00:00 | Good               | 1384             |
| 2017-11-11 10:00:00 | Good               | 1260             |
| 2017-11-18 15:00:00 | Good               | 3480             |
| 2017-11-11 12:00:00 | Good               | 2071             |
| 2017-11-18 13:00:00 | Bad                | 3300             |
| 2017-11-25 13:00:00 | Good               | 1560             |
| 2017-11-04 12:00:00 | Good               | 2760             |
| 2017-11-18 12:00:00 | Bad                | 3024             |
| 2017-11-11 11:00:00 | Good               | 1380             |
| 2017-11-25 06:00:00 | Good               | 1200             |
| 2017-11-11 06:00:00 | Good               | 1667             |
| 2017-11-18 18:00:00 | Good               | 2056             |
| 2017-11-11 10:00:00 | Good               | 1473             |
| 2017-11-11 17:00:00 | Good               | 2460             |
| 2017-11-11 10:00:00 | Good               | 1740             |
| 2017-11-11 14:00:00 | Good               | 2340             |
| 2017-11-04 16:00:00 | Bad                | 3180             |
| 2017-11-04 11:00:00 | Good               | 2220             |
| 2017-11-11 12:00:00 | Good               | 2240             |
| 2017-11-04 14:00:00 | Good               | 2778             |
| 2017-11-18 06:00:00 | Good               | 1420             |
| 2017-11-04 14:00:00 | Good               | 3480             |
| 2017-11-25 20:00:00 | Good               | 1980             |
| 2017-11-18 10:00:00 | Bad                | 2055             |
| 2017-11-11 15:00:00 | Good               | 2380             |
| 2017-11-04 08:00:00 | Good               | 1539             |
| 2017-11-25 10:00:00 | Good               | 1591             |
| 2017-11-18 14:00:00 | Good               | 2588             |
| 2017-11-11 07:00:00 | Good               | 0                |
| 2017-11-04 22:00:00 | Good               | 1380             |
| 2017-11-04 12:00:00 | Good               | 2220             |
| 2017-11-04 08:00:00 | Good               | 1380             |
| 2017-11-04 14:00:00 | Good               | 2820             |
| 2017-11-11 09:00:00 | Good               | 0                |
| 2017-11-18 09:00:00 | Bad                | 1260             |
| 2017-11-18 13:00:00 | Bad                | 2940             |
| 2017-11-18 16:00:00 | Bad                | 2340             |
| 2017-11-18 12:00:00 | Bad                | 2220             |
| 2017-11-25 11:00:00 | Good               | 1140             |
| 2017-11-11 10:00:00 | Good               | 1239             |
| 2017-11-04 16:00:00 | Bad                | 3130             |
| 2017-11-18 15:00:00 | Good               | 2877             |
| 2017-11-11 03:00:00 | Good               | 1162             |
| 2017-11-04 14:00:00 | Good               | 3060             |
| 2017-11-11 13:00:00 | Good               | 1680             |
| 2017-11-04 10:00:00 | Good               | 2112             |
| 2017-11-04 11:00:00 | Good               | 2328             |
| 2017-11-11 05:00:00 | Good               | 1504             |
| 2017-11-04 06:00:00 | Good               | 1439             |
| 2017-11-18 16:00:00 | Bad                | 2811             |
| 2017-11-18 11:00:00 | Good               | 2094             |
| 2017-11-11 06:00:00 | Good               | 1430             |
| 2017-11-18 12:00:00 | Bad                | 3026             |
| 2017-11-04 14:00:00 | Good               | 3120             |
| 2017-11-25 12:00:00 | Good               | 1380             |
| 2017-11-18 14:00:00 | Good               | 2994             |
| 2017-11-11 11:00:00 | Good               | 1620             |
| 2017-11-04 12:00:00 | Good               | 2640             |
| 2017-11-18 00:00:00 | Bad                | 480              |
| 2017-11-18 19:00:00 | Good               | 0                |
| 2017-11-11 10:00:00 | Good               | 1414             |
| 2017-11-11 12:00:00 | Good               | 1981             |
| 2017-11-11 08:00:00 | Good               | 1200             |
| 2017-11-04 11:00:00 | Good               | 2160             |
| 2017-11-11 15:00:00 | Good               | 2400             |
| 2017-11-11 20:00:00 | Good               | 1500             |
```

