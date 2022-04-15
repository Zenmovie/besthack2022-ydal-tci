CREATE TABLE IF NOT EXISTS maininfo(
    id integer PRIMARY KEY AUTOINCREMENT,
    email varchar(255) NOT NULL,
    password text NOT NULL,
    cash numeric NOT NULL DEFAULT 10000.0
);


CREATE TABLE IF NOT EXISTS account(
    id REFERENCES maininfo (id),
    symbol text PRIMARY KEY NOT NULL,
    shares integer NOT NULL
);


CREATE TABLE IF NOT EXISTS stock(
    id REFERENCES maininfo (id),
    symbol TEXT NOT NULL,
    stock_name TEXT NOT NULL,
    price numeric NOT NULL
);

INSERT OR REPLACE INTO stock (id, symbol, stock_name, price)
                VALUES
                (1,'IBM', 'International Business Machines Corporation Common Stock', 126.56),
                (2,'MSFT', 'Microsoft Corporation Common Stock', 279.83),
                (3,'APPL', 'Apple Inc. Common Stock',165.29 ),
                (4,'GOOG', 'Alphabet Inc. Class C Capital Stock', 2534.60),
                (5,'AMZN', 'Amazon.com, Inc. Common Stock', 3034.13),
                (6, 'JPM', 'JP Morgan Chase & Co. Common Stock', 126.12 ),
                (7, 'TSLA', 'Tesla, Inc. Common Stock',985.00),
                (8, 'TSM', 'Taiwan Semiconductor Manufacturing Company Ltd.', 98.36 ),
                (9, 'NVDA', 'NVIDIA Corporation Common Stock',  212.58),
                (10, 'BABA', 'Alibaba Group Holding Limited American Depositary Shares each representing eight Ordinary share', 95.49 )
;

