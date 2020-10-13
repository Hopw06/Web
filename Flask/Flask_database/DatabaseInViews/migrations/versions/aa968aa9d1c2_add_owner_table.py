"""Add owner table

Revision ID: aa968aa9d1c2
Revises: 5f90b4e2d2f5
Create Date: 2020-10-06 21:54:39.192508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa968aa9d1c2'
down_revision = '5f90b4e2d2f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('id_pup', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_pup'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owner')
    # ### end Alembic commands ###