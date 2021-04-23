# -*- coding: utf-8 -*-
from app.appfactory import create_app
from app.fixers import BrainProxyFix

app = create_app()

@app.after_request
def apply_cross_origin(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    response.headers["Access-Control-Allow-Methods"] = "PUT, POST, GET, DELETE, OPTIONS"
    return response
