"""add user creation timestamp

Revision ID: 4e0c9fbe68a3
Revises: e5cd952f00e0
Create Date: 2026-08-26 15:47:56.722065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '4e0c9fbe68a3'
down_revision: Union[str, Sequence[str], None] = 'e5cd952f00e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'usuarios',
        sa.Column(
            'criado_em',
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now()
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('usuarios', 'criado_em')