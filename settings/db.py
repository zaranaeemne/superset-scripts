# This is for db configuration only
from sqlalchemy import create_engine

# DB Host
# This should be normally in the env file. This is For Demo Only
"""
host = "127.0.0.1"
port = 5432
username = **
password = "Super Super Difficult Password With Spaces"
"""

engine = create_engine(
    "postgresql://**:**@**:5432/**"
)
