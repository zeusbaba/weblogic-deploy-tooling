"""
Copyright (c) 2017, 2019, Oracle and/or its affiliates. All rights reserved.
The Universal Permissive License (UPL), Version 1.0
"""
from wlsdeploy.aliases import alias_utils
from wlsdeploy.aliases.model_constants import OIM_KEYSTORE_PASSWORD
from wlsdeploy.aliases.model_constants import OIM_KEYSTORE_USER
from wlsdeploy.aliases.model_constants import OIM_SCHEMA_PASSWORD
from wlsdeploy.aliases.model_constants import OIM_SCHEMA_USER
from wlsdeploy.aliases.model_constants import OIM_SYSADMIN_PASSWORD
from wlsdeploy.aliases.model_constants import OIM_SYSADMIN_USER
from wlsdeploy.aliases.model_constants import OIM_WEBLOGICADMIN_PASSWORD
from wlsdeploy.aliases.model_constants import OIM_WEBLOGICADMIN_USER


class OIMCredentials(object):
    """
    Accesses the fields of the domainInfo/OIMCredentials section of the model.
    Decrypts fields if the model was encrypted.
    Returns default values for some unspecified fields.
    """

    def __init__(self, alias_helper, oimcred_properties):
        self.alias_helper = alias_helper
        self.oimcred_properties = oimcred_properties

    def get_keystore_user(self):
        return self.oimcred_properties[OIM_KEYSTORE_USER]

    def get_keystore_password(self):
        password = self.oimcred_properties[OIM_KEYSTORE_PASSWORD]
        return self.alias_helper.decrypt_password(password)

    def get_schema_user(self):
        return self.oimcred_properties[OIM_SCHEMA_USER]

    def get_schema_password(self):
        password = self.oimcred_properties[OIM_SCHEMA_PASSWORD]
        return self.alias_helper.decrypt_password(password)

    def get_sysadmin_user(self):
        return self.oimcred_properties[OIM_SYSADMIN_USER]

    def get_sysadmin_password(self):
        password = self.oimcred_properties[OIM_SYSADMIN_PASSWORD]
        return self.alias_helper.decrypt_password(password)

    def get_weblogic_admin_user(self):
        return self.oimcred_properties[OIM_WEBLOGICADMIN_USER]

    def get_weblogic_admin_password(self):
        password = self.oimcred_properties[OIM_WEBLOGICADMIN_PASSWORD]
        return self.alias_helper.decrypt_password(password)
