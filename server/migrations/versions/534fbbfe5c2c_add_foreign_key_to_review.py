"""add foreign key to Review

Revision ID: 534fbbfe5c2c
Revises: ca23dc151942
Create Date: 2024-10-02 11:44:49.127917

"""
from alembic import op
import sqlalchemy as sa
from alembic import context

# revision identifiers, used by Alembic.
revision = '534fbbfe5c2c'
down_revision = 'ca23dc151942'
branch_labels = None
depends_on = None

def upgrade():
    # Use batch mode for SQLite
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'employees', ['employee_id'], ['id'])

def downgrade():
    # Use batch mode for SQLite
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint(op.f('fk_reviews_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')
