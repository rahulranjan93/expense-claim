"""empty message

Revision ID: 9bfcb8c3a8d9
Revises: 1abef5adae21
Create Date: 2019-11-27 15:26:55.003915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bfcb8c3a8d9'
down_revision = '1abef5adae21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('role', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    # ### end Alembic commands ###
