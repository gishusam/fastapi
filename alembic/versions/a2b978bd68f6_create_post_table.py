"""create post table

Revision ID: a2b978bd68f6
Revises: 
Create Date: 2024-04-02 16:55:16.499851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2b978bd68f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        # sa.Column('description', sa.Unicode(200)),
    )
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass
