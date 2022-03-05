"""empty message

Revision ID: aa5bb4b43372
Revises: d209a87e37ea
Create Date: 2022-02-23 20:14:42.976792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa5bb4b43372'
down_revision = 'd209a87e37ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'description')
    # ### end Alembic commands ###
