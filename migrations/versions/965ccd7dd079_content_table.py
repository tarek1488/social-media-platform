"""Content table

Revision ID: 965ccd7dd079
Revises: feee9254f925
Create Date: 2024-04-28 14:39:02.644276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '965ccd7dd079'
down_revision = 'feee9254f925'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('visibility', sa.Boolean(), nullable=False),
    sa.Column('Type', sa.Boolean(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_content_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_content_userId'), ['userId'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_content_userId'))
        batch_op.drop_index(batch_op.f('ix_content_timestamp'))

    op.drop_table('content')
    # ### end Alembic commands ###
