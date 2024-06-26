"""user table

Revision ID: feee9254f925
Revises: 34c93a80f7e8
Create Date: 2024-04-28 14:37:48.681657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feee9254f925'
down_revision = '34c93a80f7e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=False),
    sa.Column('FirstName', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('lastname', sa.String(length=80), nullable=False),
    sa.Column('Gender', sa.Boolean(), nullable=False),
    sa.Column('Birthdate', sa.Date(), nullable=False),
    sa.Column('FamilyID', sa.Integer(), nullable=False),
    sa.Column('FamilyRole', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['FamilyID'], ['family.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_FamilyID'), ['FamilyID'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))
        batch_op.drop_index(batch_op.f('ix_user_FamilyID'))

    op.drop_table('user')
    # ### end Alembic commands ###
