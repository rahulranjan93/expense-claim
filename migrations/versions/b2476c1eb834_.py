"""empty message

Revision ID: b2476c1eb834
Revises: 35d84fb87e0d
Create Date: 2019-11-28 12:00:21.333576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2476c1eb834'
down_revision = '35d84fb87e0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('claim', sa.Column('claim_data', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('claim', 'claim_data')
    # ### end Alembic commands ###
