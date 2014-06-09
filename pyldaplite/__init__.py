#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals
import ldap

DEFAULT_SEARCH_SCOPE = ldap.SCOPE_SUBTREE
FILTER_BY_DISPLAY = 'displayName={}'
FILTER_BY_NAME = "sAMAccountName={}"


class PyLDAPLite(object):
    def __init__(self, **kwargs):
        self.server = 'ldap://{}'.format(kwargs.get('server'))
        self.base_dn = kwargs.get('base_dn')
        self.search_scope = kwargs.get('search_scope') or DEFAULT_SEARCH_SCOPE
        self.retrive_attrs = kwargs.get('retrive_attrs', None)
        self.version_no = kwargs.get('version', 3)

    @property
    def version(self):
        return getattr(ldap, 'VERSION{}'.format(self.version_no))

    def connect(self, username, password):
        self.conn = ldap.initialize(self.server)
        self.conn.set_option(ldap.OPT_REFERRALS, 0)
        self.conn.protocol_version = self.version
        self.conn.simple_bind_s(username, password)

    def close(self):
        self.conn.unbind_s()

    def search_by(self, filter_value, **kwargs):
        limit = kwargs.get('limit', 0)
        self.result_id = self.conn.search(self.base_dn,
                                          self.search_scope,
                                          filter_value,
                                          self.retrive_attrs,
                                          )
        results = []
        while 1:
            result_type, result_data = self.conn.result(self.result_id, 0)
            if (result_data == []) or (limit and len(results) >= limit):
                break
            elif result_type == ldap.RES_SEARCH_ENTRY:
                results.append(result_data)

        return results

    def search_name(self, name, limit=0):
        filter_value = FILTER_BY_NAME.format(name)
        return self.search_by(filter_value, limit=limit)

    def search_display(self, display_name, limit=0):
        filter_value = FILTER_BY_DISPLAY.format(display_name)
        return self.search_by(filter_value, limit=limit)
