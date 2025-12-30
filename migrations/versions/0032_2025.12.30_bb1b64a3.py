"""Add a license check mode to release policies

Revision ID: 0032_2025.12.30_bb1b64a3
Revises: 0031_2025.12.22_0f049a07
Create Date: 2025-12-30 14:25:09.373904+00:00
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# Revision identifiers, used by Alembic
revision: str = "0032_2025.12.30_bb1b64a3"
down_revision: str | None = "0031_2025.12.22_0f049a07"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("releasepolicy", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "license_check_mode",
                sa.Enum("LIGHTWEIGHT", "RAT", "BOTH", name="licensecheckmode"),
                server_default="BOTH",
                nullable=False,
            )
        )


def downgrade() -> None:
    with op.batch_alter_table("releasepolicy", schema=None) as batch_op:
        batch_op.drop_column("license_check_mode")
