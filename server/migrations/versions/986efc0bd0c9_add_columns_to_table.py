"""add columns to table

Revision ID: 986efc0bd0c9
Revises: 67f5d67aea55
Create Date: 2024-07-01 15:07:34.943086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '986efc0bd0c9'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('namme', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###