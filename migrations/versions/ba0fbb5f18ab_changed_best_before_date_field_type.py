"""changed best_before_date field type

Revision ID: ba0fbb5f18ab
Revises: 11b2559002f3
Create Date: 2018-01-07 14:17:29.437066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba0fbb5f18ab'
down_revision = '11b2559002f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grocery', sa.Column('best_before', sa.Date(), nullable=True))
    op.create_index(op.f('ix_grocery_best_before'), 'grocery', ['best_before'], unique=False)
    op.drop_index('ix_grocery_best_before_date', table_name='grocery')
    op.drop_column('grocery', 'best_before_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grocery', sa.Column('best_before_date', sa.DATETIME(), nullable=True))
    op.create_index('ix_grocery_best_before_date', 'grocery', ['best_before_date'], unique=False)
    op.drop_index(op.f('ix_grocery_best_before'), table_name='grocery')
    op.drop_column('grocery', 'best_before')
    # ### end Alembic commands ###