"""Add a column

Revision ID: f1559ea6469e
Revises: b2b8421f5164
Create Date: 2018-09-25 16:45:45.897794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1559ea6469e'
down_revision = 'b2b8421f5164'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')
