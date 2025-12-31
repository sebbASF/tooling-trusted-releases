"""Add subject template options to release policies

Revision ID: 0034_2025.12.31_ac4dcf44
Revises: 0033_2025.12.31_f2d97d96
Create Date: 2025-12-31 18:59:47.025592+00:00
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# Revision identifiers, used by Alembic
revision: str = "0034_2025.12.31_ac4dcf44"
down_revision: str | None = "0033_2025.12.31_f2d97d96"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("releasepolicy", schema=None) as batch_op:
        batch_op.add_column(sa.Column("start_vote_subject", sa.String(), nullable=False, server_default=""))
        batch_op.add_column(sa.Column("announce_release_subject", sa.String(), nullable=False, server_default=""))


def downgrade() -> None:
    with op.batch_alter_table("releasepolicy", schema=None) as batch_op:
        batch_op.drop_column("announce_release_subject")
        batch_op.drop_column("start_vote_subject")
