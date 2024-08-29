"""create company table

Revision ID: 0fff49936b52
Revises: fb5030c31ac7
Create Date: 2024-08-28 10:37:35.362116

"""
from uuid import uuid4
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fff49936b52'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the companies table
    company_table = op.create_table(
        'companies',
        sa.Column('id', sa.Uuid, primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), unique=True, index=True, nullable=False),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('mode', sa.Enum('ACTIVE', 'INACTIVE', name='companymode'), nullable=False, server_default='ACTIVE'),
        sa.Column('rating', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=sa.func.now(), nullable=True),
    )

    # Insert data into the companies table
    op.bulk_insert(
       company_table,
        [
            {
                "id": str(uuid4()),
                "name": "Admin Company",
                "description": "Description of Admin Company",
                "mode": "ACTIVE",
                "rating": 5.0,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        ],
    )


def downgrade() -> None:
    
    # Drop the companies table
    op.drop_table('companies')
    
    # Drop the enums
    op.execute("DROP TYPE companymode")
