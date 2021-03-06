"""grocery table

Revision ID: 11b2559002f3
Revises: 
Create Date: 2018-01-07 13:15:40.550331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11b2559002f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grocery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('best_before_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grocery_best_before_date'), 'grocery', ['best_before_date'], unique=False)
    op.create_index(op.f('ix_grocery_name'), 'grocery', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_grocery_name'), table_name='grocery')
    op.drop_index(op.f('ix_grocery_best_before_date'), table_name='grocery')
    op.drop_table('grocery')
    # ### end Alembic commands ###
