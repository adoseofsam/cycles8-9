"""empty message

Revision ID: 065ddc95423a
Revises: 
Create Date: 2021-08-01 00:50:05.111005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '065ddc95423a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('venue', sa.String(length=50), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('website_url', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('profile_photo', sa.String(length=80), nullable=True),
    sa.Column('role', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('events')
    # ### end Alembic commands ###