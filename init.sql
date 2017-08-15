-- PRODUCT TABLE --

CREATE TABLE product (
    id           integer         NOT NULL UNIQUE PRIMARY KEY,
    name         varchar(40)     NOT NULL,
    stock        integer         NOT NULL DEFAULT 0
);

-- RECIPE TABLE --

CREATE TABLE recipe (
    id           integer         NOT NULL UNIQUE PRIMARY KEY,
    result       integer         NOT NULL REFERENCES product(id),
    req_1        integer         NOT NULL REFERENCES product(id),
    req_2        integer         REFERENCES product(id),
    req_3        integer         REFERENCES product(id),
    req_4        integer         REFERENCES product(id),
    num_1        integer         NOT NULL DEFAULT 1,
    num_2        integer,
    num_3        integer,
    num_4        integer
);

-- ADD product constraint to recipe --

ALTER TABLE product
    ADD COLUMN recipe_id integer REFERENCES recipe(id);

