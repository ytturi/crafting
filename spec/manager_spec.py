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
            man_product = manager._MODEL_PRODUCT(
                self_id=pars['self_id'], name=pars['name'],
                stock=pars['stock'], recipe_id=pars['recipe_id']
            )
            product_dict = man_product._asdict()
            expect(len(product_dict.keys())).to(equal(len(pars.keys())))
            for key, value in product_dict.items():
                expect(value).to(equal(pars[key]))
