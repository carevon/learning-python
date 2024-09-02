"""empty message

Revision ID: 7195ebc2a6e6
Revises: 29196b7c9147
Create Date: 2024-09-02 00:27:55.397095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7195ebc2a6e6'
down_revision = '29196b7c9147'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
