# Crafting
This repo will try to talk with a PostgreSQL database to check and show requirements and materials to craft an item.
Based on a simple interface and backend.

The interface may allow the user to:

- Show the current amount of a _Product_.
- Show the requirements to craft a _Product_ using a _Recipe_.
- Show a % of materials obtained of the required to craft a _Product_ using a _Recipe_.
- Show the % of materials obtained of the recursively required to craft a _Product_ using a _Recipe_.

# Database Schema

- _Product_ may be crafted using a _Recipe_.
- All _Recipes_ may need 1-4 _Product_ types and an specific amount.

## PRODUCT

| Field | Type          |
|-------|---------------|
| id    | int           |
| name  | text          | 
| craft | :fk:recipe_id |
| stock | int           |

## RECIPE

| Field | Type           |
|-------|----------------|
| id    | int            |
| name  | :fk:product_id |
| req.1 | :fk:product_id |
| num.1 | int            |
| req.2 | :fk:product_id |
| num.2 | int            |
| req.3 | :fk:product_id |
| num.3 | int            |
| req.4 | :fk:product_id |
| num.4 | int            |

