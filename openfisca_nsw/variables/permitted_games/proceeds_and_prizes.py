# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class gross_proceeds_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Gross proceeds from gaming activity"
    definition_period = MONTH


class proceeds_to_benefitting_organisation(Variable):
    value_type = int
    entity = Organisation
    label = u"Gross proceeds deposited with benefiting organisation"
    definition_period = MONTH


class total_prize_value_of_all_prizes_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Total prize value of all prizes"
    definition_period = MONTH


class total_prize_value_of_all_prizes_from_single_gaming_session(Variable):
    value_type = int
    entity = Organisation
    label = u"Total prize value of all prizes from a single gaming session"
    definition_period = MONTH