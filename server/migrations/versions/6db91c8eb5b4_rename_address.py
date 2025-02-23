"""rename address

Revision ID: 6db91c8eb5b4
Revises: 1d0c899810a6
Create Date: 2025-01-15 11:13:43.816234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6db91c8eb5b4'
down_revision = '1d0c899810a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('location', sa.String(), nullable=False))
    op.drop_column('departments', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    op.drop_column('departments', 'location')
    # ### end Alembic commands ###
