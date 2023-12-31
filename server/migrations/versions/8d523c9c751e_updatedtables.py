"""updatedtables

Revision ID: 8d523c9c751e
Revises: 6aa4a6db1caa
Create Date: 2023-09-25 12:19:11.235179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d523c9c751e'
down_revision = '6aa4a6db1caa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant_pizza_association')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_pizza_association',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('restaurant_id', sa.INTEGER(), nullable=True),
    sa.Column('pizza_id', sa.INTEGER(), nullable=True),
    sa.Column('price', sa.FLOAT(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizza.id'], name='fk_restaurant_pizza_association_pizza_id_pizza'),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], name='fk_restaurant_pizza_association_restaurant_id_restaurant'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
