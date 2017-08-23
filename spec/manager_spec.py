# -*- encoding utf-8 -*-
from CraftManager import manager
from expects import *

with description('CraftManager Class'):
    with context('Models'):
        with it('must have a _MODEL_PRODUCT as specified in the docs'):
            pars = {
                'self_id': 1,
                'name': 'demo',
                'stock': 0,
                'recipe_id': 1,
            }
            product_obj = manager._MODEL_PRODUCT(
                self_id=pars['self_id'], name=pars['name'],
                stock=pars['stock'], recipe_id=pars['recipe_id']
            )
            product_dict = product_obj._asdict()
            expect(len(product_dict.keys())).to(equal(len(pars.keys())))
            for key, value in product_dict.items():
                expect(value).to(equal(pars[key]))

        with it('must have a _MODEL_RECIPE as specified in the docs'):
            pars = {
                'self_id': 1,
                'result_id': 1,
                'requirement_id_1': 1,
                'requirement_amount_1': 1,
                'requirement_id_2': 2,
                'requirement_amount_2': 1,
                'requirement_id_3': 3,
                'requirement_amount_3': 1,
                'requirement_id_4': False,
                'requirement_amount_4': False,
            }
            recipe_obj = manager._MODEL_RECIPE(
                self_id=pars['self_id'], result_id=pars['result_id'],
                requirement_id_1=pars['requirement_id_1'],
                requirement_amount_1=pars['requirement_amount_1'],
                requirement_id_2=pars['requirement_id_2'],
                requirement_amount_2=pars['requirement_amount_2'],
                requirement_id_3=pars['requirement_id_3'],
                requirement_amount_3=pars['requirement_amount_3'],
                requirement_id_4=pars['requirement_id_4'],
                requirement_amount_4=pars['requirement_amount_4'],
            )
            recipe_dict = recipe_obj._asdict()
            expect(len(recipe_dict.keys())).to(equal(len(pars.keys())))
            for key, value in recipe_dict.items():
                expect(value).to(equal(pars[key]))

