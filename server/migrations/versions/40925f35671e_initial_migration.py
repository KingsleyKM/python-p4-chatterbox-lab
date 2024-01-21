"""initial migration

Revision ID: 40925f35671e
Revises: 
Create Date: 2024-01-16 13:29:31.407440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40925f35671e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###