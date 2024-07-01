"""add name column

Revision ID: 2f0ce2620850
Revises: 986efc0bd0c9
Create Date: 2024-07-01 15:13:11.372009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f0ce2620850'
down_revision = '986efc0bd0c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.drop_column('namme')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('namme', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('name')

    # ### end Alembic commands ###