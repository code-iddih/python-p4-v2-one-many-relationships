"""add foreign key to onboarding

Revision ID: fbad85bd664f
Revises: 534fbbfe5c2c
Create Date: 2024-10-02 12:38:34.733622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbad85bd664f'
down_revision = '534fbbfe5c2c'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(op.f('fk_onboardings_employee_id_employees'), 'employees', ['employee_id'], ['id'])

def downgrade():
    # Use batch mode for SQLite
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')
