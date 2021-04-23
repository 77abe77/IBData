# -*- coding: utf-8 -*-
import re
import json
from functools import reduce
from dateutil.parser import parse
from flask_restful import (
    fields,
    marshal,
    marshal_with,
    Resource,
    reqparse
)
from app.models.Equity import (
    Equity,
    EquityHistoricalData
)

from app.extensions import db

import requests

session = db.session

class EquityListResource(Resource):
    def get(self):
        return dict(equities=[]), 200


class EquityResource(Resource):
    def get(self, project_id):
        return {}, 200