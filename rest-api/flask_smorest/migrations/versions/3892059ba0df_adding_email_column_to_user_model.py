"""Adding email column to user model

Revision ID: 3892059ba0df
Revises: 7195ebc2a6e6
Create Date: 2024-09-09 02:22:27.497263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3892059ba0df'
down_revision = '7195ebc2a6e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.create_unique_constraint('email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint("email", type_='unique')
        
        batch_op.alter_column('password',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
        batch_op.drop_column('email')
    # ### end Alembic commands ###
