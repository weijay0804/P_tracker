"""新增 record_type 與 record 一對多關聯

Revision ID: 18f8b75779c2
Revises: 16037bdb6864
Create Date: 2023-06-06 05:14:36.592380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18f8b75779c2'
down_revision = '16037bdb6864'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('record', 'record_type', ['type_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('type_id')

    # ### end Alembic commands ###
