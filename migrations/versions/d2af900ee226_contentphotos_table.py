"""ContentPhotos table

Revision ID: d2af900ee226
Revises: 965ccd7dd079
Create Date: 2024-04-28 14:40:01.488634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2af900ee226'
down_revision = '965ccd7dd079'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contentphotos',
    sa.Column('contentId', sa.Integer(), nullable=False),
    sa.Column('photoUrl', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['contentId'], ['content.id'], ),
    sa.PrimaryKeyConstraint('contentId', 'photoUrl')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contentphotos')
    # ### end Alembic commands ###
