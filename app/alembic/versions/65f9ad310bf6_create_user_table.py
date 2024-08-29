"""create user table

Revision ID: 65f9ad310bf6
Revises: 0fff49936b52
Create Date: 2024-08-28 10:52:21.103153

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from uuid import uuid4
from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = '65f9ad310bf6'
down_revision: Union[str, None] = '0fff49936b52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        # Create the users table
    user_table = op.create_table(
        'users',
        sa.Column('id', sa.Uuid, primary_key=True, nullable=False),
        sa.Column('email', sa.String(255), unique=True, index=True, nullable=False),
        sa.Column('username', sa.String(50), unique=True, index=True, nullable=False),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.Column('is_active', sa.Boolean, server_default='true', nullable=False),
        sa.Column('is_admin', sa.Boolean, server_default='false', nullable=False),
        sa.Column('company_id', sa.Uuid, sa.ForeignKey('companies.id'), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=sa.func.now(), nullable=True),
    )
    op.bulk_insert(
        user_table,
        [
            {
                "id": str(uuid4()),
                "email": "admin@example.com",
                "username": "admin",
                "first_name": "Admin",
                "last_name": "User",
                "hashed_password": "hashed_password_1",  # Replace with an actual hashed password
                "is_active": True,
                "is_admin": True,
                "company_id": None,  # Set to a valid company ID if needed
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            },
            {
                "id": str(uuid4()),
                "email": "user@example.com",
                "username": "user",
                "first_name": "Regular",
                "last_name": "User",
                "hashed_password": "hashed_password_2",  # Replace with an actual hashed password
                "is_active": True,
                "is_admin": False,
                "company_id": None,  # Set to a valid company ID if needed
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        ],
    )



def downgrade() -> None:
    # Drop the users table
    op.drop_table('users')
