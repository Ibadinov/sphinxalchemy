""" PyMySQL connector"""

from __future__ import absolute_import

from sqlalchemy.dialects.mysql import pymysql
from sphinxalchemy.dialect import SphinxDialect

__all__ = ("Dialect",)

class Dialect(SphinxDialect, pymysql.MySQLDialect_pymysql):
    def _get_default_schema_name(self, connection):
        raise NotImplementedError()

    def get_isolation_level(self, connection):
        raise NotImplementedError()

    def _detect_charset(self, connection):
        pass

    def _detect_casing(self, connection):
        pass

    def _detect_collations(self, connection):
        pass

    def _detect_ansiquotes(self, connection):
        self._server_ansiquotes = False
