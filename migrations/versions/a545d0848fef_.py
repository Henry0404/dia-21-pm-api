"""empty message

Revision ID: a545d0848fef
Revises: fdeb72133674
Create Date: 2021-04-29 18:33:27.750890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a545d0848fef'
down_revision = 'fdeb72133674'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('model', sa.String(length=250), nullable=True),
    sa.Column('manufacturer', sa.String(length=250), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=250), nullable=True),
    sa.Column('length', sa.String(length=250), nullable=True),
    sa.Column('max_atmosphering_speed', sa.String(length=250), nullable=True),
    sa.Column('crew', sa.String(length=250), nullable=True),
    sa.Column('passengers', sa.String(length=250), nullable=True),
    sa.Column('cargo_capacity', sa.String(length=250), nullable=True),
    sa.Column('consumables', sa.String(length=250), nullable=True),
    sa.Column('hyperdrive_rating', sa.String(length=250), nullable=True),
    sa.Column('MGLT', sa.String(length=250), nullable=True),
    sa.Column('starship_class', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ships')
    # ### end Alembic commands ###
