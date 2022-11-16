sql
---


#1 user
CREATE TABLE "user"(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ NOT NULL DEFAULT Now(),
is_active BOOLEAN NOT NULL DEFAULT true,

created_by bigint NOT NULL,

type VARCHAR (100) NOT NULL,
role VARCHAR (100),
mobile VARCHAR (50) UNIQUE,
password VARCHAR (50) NOT NULL,
google_auth VARCHAR (100) UNIQUE,
name VARCHAR(50),
email VARCHAR (100),
gender VARCHAR(50),
dob VARCHAR(25),
profile_pic_url VARCHAR (500),
weight  VARCHAR (10),
height  VARCHAR (10),
tnc_accepted boolean,

data jsonb
);


# tbl_coal_port
CREATE TABLE tbl_coal_port(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ DEFAULT Now(),
is_active BOOLEAN DEFAULT true,
created_by bigint,
name VARCHAR (100) NOT NULL,
data jsonb
);

# tbl_coal_grade
CREATE TABLE tbl_coal_grade(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ DEFAULT Now(),
is_active BOOLEAN DEFAULT true,
created_by bigint,
name VARCHAR (100) NOT NULL,
data jsonb
);


# tbl_coal_origin
CREATE TABLE tbl_coal_origin(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ DEFAULT Now(),
is_active BOOLEAN DEFAULT true,
created_by bigint,
name VARCHAR (100) NOT NULL,
data jsonb
);


CREATE TABLE tbl_coal_competitor(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ DEFAULT Now(),
is_active BOOLEAN DEFAULT true,
created_by bigint,
name VARCHAR (100) NOT NULL,
grade_id bigint,
origin_id bigint,
port_id bigint,
base_price float,
sale_price float,
total_quantity float,
data jsonb
);


CREATE TABLE tbl_coal_purchase_detail(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ DEFAULT Now(),
is_active BOOLEAN DEFAULT true,
created_by bigint,
grade_id bigint,
origin_id bigint,
port_id bigint,
base_price float,
total_quantity float,
data jsonb
);


# sale price
CREATE TABLE tbl_coal_sale_price(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ DEFAULT Now(),
is_active BOOLEAN DEFAULT true,
created_by bigint,
grade_id bigint,
origin_id bigint,
port_id bigint,
base_price float,
sale_price float,
total_quantity float,
handling_charge float,
other_cost float,
premium_cost float,
fright_cost float,
rate_usd_inr float,
data jsonb
);







CREATE TABLE tbl_demand(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ NOT NULL DEFAULT Now(),
is_active BOOLEAN NOT NULL DEFAULT true,
created_by bigint,
grade_id INTEGER,
port_id INTEGER,
origin_id INTEGER,
importer VARCHAR (50),
dispatch_qty float,
net_physical_stock float,
demandent_name VARCHAR (50),
data jsonb
)



CREATE TABLE tbl_supply(
id BIGSERIAL PRIMARY KEY NOT NULL,
created_at TIMESTAMPTZ NOT NULL DEFAULT Now(),
is_active BOOLEAN NOT NULL DEFAULT true,

created_by bigint,

grade_id INTEGER,
port_id INTEGER,
origin_id INTEGER,
importer VARCHAR (50),
stock_qty float,
stock_status varchar(50),
in_transit_vessel_name varchar(50),
in_transit_eta_date  VARCHAR (50),
in_transit_status varchar(50),
in_transit_origin_id integer,
in_transit_mines varchar(50),
in_transit_qty float,

demandent_name VARCHAR (50),

data jsonb
);



