"""empty message

Revision ID: 52e6577a8d1f
Revises: 1a44f08ee976
Create Date: 2020-03-26 00:10:33.557162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52e6577a8d1f'
down_revision = '1a44f08ee976'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doner_id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=128), nullable=True),
    sa.Column('quantity', sa.String(length=128), nullable=True),
    sa.Column('needy_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['doner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['needy_id'], ['needy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donation')
    # ### end Alembic commands ###
