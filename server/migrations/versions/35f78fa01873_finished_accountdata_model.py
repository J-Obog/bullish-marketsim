"""finished AccountData model

Revision ID: 35f78fa01873
Revises: fc7395ceb567
Create Date: 2021-10-06 14:03:58.455878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35f78fa01873'
down_revision = 'fc7395ceb567'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('equity_prev_close', sa.Float(decimal_return_scale=2), nullable=False),
    sa.Column('portfolio_equity', sa.Float(decimal_return_scale=2), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account_data')
    # ### end Alembic commands ###