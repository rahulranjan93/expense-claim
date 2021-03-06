"""empty message

Revision ID: 8e193ee1057b
Revises: 9c791a5e2c56
Create Date: 2019-12-24 14:28:36.692916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e193ee1057b'
down_revision = '9c791a5e2c56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column('employee', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('employee', 'password_hash')
    # ### end Alembic commands ###
