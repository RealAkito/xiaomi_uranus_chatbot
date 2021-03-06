from sqlalchemy import Column, Integer, String

from .. import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    user_id = Column(Integer, nullable=False, index=True)
    chat_type = Column(String, nullable=False)
    sub_type = Column(String, nullable=False)
    device = Column(String, nullable=False)
    last_updates = Column(String)

    def __repr__(self):
        return f"<Subscription(id={self.id}, chat_type={self.chat_type}, " \
               f"sub_type={self.sub_type}, device={self.device})>"
