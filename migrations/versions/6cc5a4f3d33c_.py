"""empty message

Revision ID: 6cc5a4f3d33c
Revises: 8e193ee1057b
Create Date: 2019-12-26 12:55:04.839885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cc5a4f3d33c'
down_revision = '8e193ee1057b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_test_email', table_name='test')
    op.drop_index('ix_test_username', table_name='test')
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='test_pkey')
    )
    op.create_index('ix_test_username', 'test', ['username'], unique=True)
    op.create_index('ix_test_email', 'test', ['email'], unique=True)
    # ### end Alembic commands ###
