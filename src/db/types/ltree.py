from abc import ABC

from sqlalchemy import cast, type_coerce
from sqlalchemy.sql import sqltypes
from sqlalchemy.sql.sqltypes import Concatenable
from sqlalchemy.dialects.postgresql import ARRAY


class LtreeTypeComparator(Concatenable.Comparator):
    def ancestor_of(self, other):
        if isinstance(other, list):
            return self.op("@>")(cast(other, ARRAY(LtreeType)))
        else:
            return self.op("@>")(other)

    def descendant_of(self, other):
        if isinstance(other, list):
            return self.op("<@")(cast(other, ARRAY(LtreeType)))
        else:
            return self.op("<@")(other)

    def lquery(self, other):
        if isinstance(other, list):
            return self.op("?")(cast(other, ARRAY(LQUERY)))
        else:
            if isinstance(other, str):
                return self.op("~")(type_coerce(other, LTXTQUERY))
            return self.op("~")(other)

    def ltxtquery(self, other):
        return self.op("@")(other)


class LtreeType(sqltypes.TypeEngine, ABC):
    __visit_name__ = "LTREE"

    cache_ok = True
    comparator_factory = LtreeTypeComparator

    def literal_processor(self, dialect):
        def process(value):
            value = value.replace("'", "''")
            return "'%s'" % value

        return process


class LQUERY(sqltypes.TypeEngine, ABC):
    __visit_name__ = "LQUERY"

    def literal_processor(self, dialect):
        def process(value):
            value = value.replace("'", "''")
            return "'%s'" % value

        return process


class LTXTQUERY(sqltypes.TypeEngine, ABC):
    __visit_name__ = "LTXTQUERY"

    def literal_processor(self, dialect):
        def process(value):
            value = value.replace("'", "''")
            return "'%s'" % value

        return process


Lquery = LQUERY
LTXTquery = LTXTQUERY
