"""add some number column

Revision ID: 642f3220adee
Revises: f1559ea6469e
Create Date: 2018-09-26 16:19:56.856759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642f3220adee'
down_revision = 'f1559ea6469e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('some_number', sa.Integer))

def downgrade():
    op.drop_column('account', 'some_number')
