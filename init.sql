-- PRODUCT TABLE --

CREATE TABLE product (
    id           integer         NOT NULL UNIQUE PRIMARY KEY,
    name         varchar(40)     NOT NULL,
    stock        integer         NOT NULL DEFAULT 0,
    recipe_id    integer
);

