"""add restaurant_category

Revision ID: a9351040cbbc
Revises: d41d74196339
Create Date: 2024-11-16 17:45:10.837313

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a9351040cbbc'
down_revision = 'd41d74196339'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_category',
    sa.Column('category_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category_uuid', mysql.CHAR(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('category_id'),
    sa.UniqueConstraint('category_uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant_category')
    # ### end Alembic commands ###