"""empty message

Revision ID: bad7f8528e58
Revises: 
Create Date: 2022-06-24 19:00:27.587701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bad7f8528e58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('genres', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_movies'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('movieid', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movieid'], ['movies.id'], name=op.f('fk_ratings_movieid_movies'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], name=op.f('fk_ratings_userid_users'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_ratings'))
    )
    op.create_table('suggests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('suggest_movie', sa.String(length=200), nullable=True),
    sa.Column('suggest_time', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], name=op.f('fk_suggests_userid_users'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_suggests'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('suggests')
    op.drop_table('ratings')
    op.drop_table('users')
    op.drop_table('movies')
    # ### end Alembic commands ###