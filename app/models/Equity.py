import enum
from app.extensions import db
from sqlalchemy.orm import validates
from app.database import (
    DefaultBase,
    Column,
    relationship,
    reference_col,
)

class HistoricalDataType(enum.Enum):
    TRADES = 0
    MIDPOINT = 1
    BID = 2
    ASK = 3
    BID_ASK = 4
    HISTORICAL_VOLATILITY = 5
    OPTION_IMPLIED_VOLATILITY = 6

class BarSizes(enum.Enum):
    SEC_1 = 0
    SEC_5 = 1
    SEC_10 = 2
    SEC_15 = 3
    SEC_30 = 4
    MIN_1 = 5
    MIN_2 = 6
    MIN_3 = 7
    MIN_5 = 8
    MIN_10 = 9
    MIN_15 = 10
    MIN_20 = 11
    MIN_30 = 12
    HOUR_1 = 13
    HOUR_2 = 14
    HOUR_3 = 15
    HOUR_4 = 16
    HOUR_8 = 17
    DAY_1 = 18
    WEEK_1 = 19
    MONTH_1 = 20


class EquityHistoricalData(DefaultBase):
    equity_id = reference_col("equity")
    date = Column(db.DateTime, nullable=False)
    bar_size = Column(db.Enum(BarSizes), default=BarSizes.MIN_1, nullable=False)
    data_type = Column(db.Enum(HistoricalDataType), nullable=False)
    open = Column(db.Float, nullable=False)
    high = Column(db.Float, nullable=False)
    low = Column(db.Float, nullable=False)
    close = Column(db.Float, nullable=False)
    volume = Column(db.Float, nullable=False)
    bar_count = Column(db.Float, nullable=False)
    average = Column(db.Float, nullable=False)

class Equity(DefaultBase):
    name = Column(db.String(256), nullable=False)
    ticker = Column(db.String(32), nullable=False, unique=True)
    ib_con_id = Column(db.Integer, nullable=False)
    granular = Column(db.Boolean, default=False, nullable=False)
    should_update = Column(db.Boolean, default=True, nullable=False)

class OptionType(enum.Enum):
    PUT = 0
    CALL = 1

class OptionsContract(DefaultBase):
    equity_id = reference_col("equity")
    strike = Column(db.Float, nullable=False)
    exp = Column(db.Date, nullable=False)
    type = Column(db.Enum(OptionType), nullable=False)

class OptionsContractData(DefaultBase):
    options_contract_id = reference_col("options_contract")
    date = Column(db.DateTime, nullable=False)
    bar_size = Column(db.Enum(BarSizes), default=BarSizes.MIN_1, nullable=False)
    data_type = Column(db.Enum(HistoricalDataType), nullable=False)
    open = Column(db.Float, nullable=False)
    high = Column(db.Float, nullable=False)
    low = Column(db.Float, nullable=False)
    close = Column(db.Float, nullable=False)
    volume = Column(db.Float, nullable=False)
    bar_count = Column(db.Float, nullable=False)
    average = Column(db.Float, nullable=False) 
