"""add a column

Revision ID: fa6686c205e4
Revises: a2b978bd68f6
Create Date: 2024-04-02 17:03:45.052014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa6686c205e4'
down_revision: Union[str, None] = 'a2b978bd68f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
