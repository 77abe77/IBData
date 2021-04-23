# -*- coding: utf-8 -*-
from app.extensions import api
from app.controllers import (
    health,
    stock
)


# Health Routes
api.add_resource(health.HealthResource, '/', '/health')
api.add_resource(stock.EquityListResource , '/', '/equity')