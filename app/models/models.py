from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class ToDo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)
    starred = Column(Boolean, default=False)