"""empty message

Revision ID: cb2d04cc4cda
Revises: 4c8ff6aed37b
Create Date: 2021-11-12 16:27:49.499341

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cb2d04cc4cda'
down_revision = '4c8ff6aed37b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rental', sa.Column('due_date', sa.DateTime(), nullable=True))
    op.drop_column('rental', 'date_due')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rental', sa.Column('date_due', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('rental', 'due_date')
    # ### end Alembic commands ###
