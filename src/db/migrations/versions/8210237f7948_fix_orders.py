"""fix orders

Revision ID: 8210237f7948
Revises: 52034d9e6e26
Create Date: 2023-05-18 14:17:19.650892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8210237f7948"
down_revision = "52034d9e6e26"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("orders_orders_id_fk_3", "orders", type_="foreignkey")
    op.drop_column("orders", "running_no")
    op.drop_column("orders", "source_order_id")
    op.drop_column("orders", "is_subscription")
    op.drop_column("orders", "last_paid_rebilling_number")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "orders",
        sa.Column(
            "last_paid_rebilling_number",
            sa.NUMERIC(precision=18, scale=0),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "orders",
        sa.Column("is_subscription", sa.BOOLEAN(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "orders",
        sa.Column("source_order_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "orders",
        sa.Column("running_no", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        "orders_orders_id_fk_3", "orders", "orders", ["source_order_id"], ["id"]
    )
    # ### end Alembic commands ###
