"""create task table

Revision ID: 45621fa54f33
Revises: 65f9ad310bf6
Create Date: 2024-08-28 11:05:12.712401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45621fa54f33'
down_revision: Union[str, None] = '65f9ad310bf6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.create_table(
        'tasks',
        sa.Column('id', sa.Uuid, primary_key=True, nullable=False),
        sa.Column('summary', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('status', sa.Enum('ACTIVE', 'COMPLETED', 'PENDING', 'INACTIVE', name='taskstatus'), nullable=False, server_default='ACTIVE'),
        sa.Column('priority', sa.Enum('LOW', 'MEDIUM', 'HIGH', name='taskpriority'), nullable=False, server_default='LOW'),
        sa.Column('user_id', sa.Uuid, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=sa.func.now(), nullable=True),
    )


def downgrade() -> None:
    # Drop the tasks table
    op.drop_table('tasks')
     # Drop the enums
    op.execute("DROP TYPE taskstatus")
    op.execute("DROP TYPE taskpriority")
