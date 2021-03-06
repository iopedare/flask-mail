"""add language to posts

Revision ID: 51a711affe89
Revises: 16abf7327caa
Create Date: 2021-07-30 18:48:31.844314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51a711affe89'
down_revision = '16abf7327caa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
