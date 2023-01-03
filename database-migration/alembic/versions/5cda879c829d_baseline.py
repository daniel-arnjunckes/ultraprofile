"""baseline

Revision ID: 5cda879c829d
Revises: 
Create Date: 2023-01-03 18:43:36.219470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cda879c829d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'profile',
        sa.Column('id',sa.Integer, primary_key=True),
        sa.Column('name',sa.String, nullable=False),
        sa.Column('created', sa.DateTime, default=sa.func.now())
    )


def downgrade() -> None:
    pass
