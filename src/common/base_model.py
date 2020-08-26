from datetime import datetime
from src import db


class BaseModel:
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, comment="ID")
    raw_data = db.Column(db.JSON, default={}, comment="扩展字段")
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
    deleted = db.Column(db.Integer, default=0, comment="是否已删除")