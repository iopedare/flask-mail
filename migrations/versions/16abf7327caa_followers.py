"""followers

Revision ID: 16abf7327caa
Revises: 5fdf9cdf334f
Create Date: 2021-07-30 16:21:42.779174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16abf7327caa'
down_revision = '5fdf9cdf334f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###