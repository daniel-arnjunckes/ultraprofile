"""feat: new table adress

Revision ID: eb4c14dffca7
Revises: 5cda879c829d
Create Date: 2023-01-03 20:26:39.238835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb4c14dffca7'
down_revision = '5cda879c829d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('bug_tracker_url', sa.String(), nullable=True),
    sa.Column('who', sa.String(), nullable=True),
    sa.Column('when', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bug_tracker_url')
    )
    op.create_index(op.f('ix_bug_profile_id'), 'bug', ['profile_id'], unique=False)
    op.alter_column('profile', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('profile', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_index(op.f('ix_bug_profile_id'), table_name='bug')
    op.drop_table('bug')
    # ### end Alembic commands ###