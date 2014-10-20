"""
Authors: Tim Bedin, Tim Erwin

Copyright 2014 CSIRO

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This module registers all the VisTrails modules that can be
added to the GUI.

"""

# Vistrails imports
from vistrails.core.packagemanager import get_package_manager
from vistrails.gui.preferences import QPackageConfigurationDialog
from vistrails.core.modules.module_registry import get_module_registry

# Available Tools
import cwsl.vt_modules.drs_dataset as drs
from cwsl.vt_modules.vt_dataset import VtDataSet
from cwsl.vt_modules.vt_cdscan import CDScan
from cwsl.vt_modules.vt_seas_vars import SeasVars
from cwsl.vt_modules.vt_climatology import Climatology
from cwsl.vt_modules.vt_nino34 import IndiciesNino34
from cwsl.vt_modules.vt_general_command_pattern import GeneralCommandPattern
from cwsl.vt_modules.vt_constraintbuilder import ConstraintBuilder


def initialize(*args, **keywords):

    # We'll first create a local alias for the module_registry so that
    # we can refer to it in a shorter way.
    reg = get_module_registry()

    # VisTrails cannot currently automatically detect your derived
    # classes, and the ports that they support as input and
    # output. Because of this, you as a module developer need to let
    # VisTrails know that you created a new module. This is done by calling
    # function addModule:
    reg.add_module(VtDataSet, abstract=True)
    reg.add_module(drs.DataReferenceSyntax, abstract=True)

    reg.add_module(drs.RegionalClimateModel, namespace='DataSets|Generic',
                   name='Regional Climate Model DataSet')
    reg.add_module(drs.RegionalClimateModel_CCAM_NRM,
                   name='CSIRO-CCAM-NRM', namespace='DataSets|RCM')
    reg.add_module(drs.RegionalClimateModel_SDMa_NRM,
                   name='BOM-SDMa-NRM', namespace='DataSets|RCM')
    reg.add_module(drs.GlobalClimateModel, namespace='DataSets|Generic',
                   name="Global Climate Model Dataset")

    reg.add_module(CDScan, name='Merge Timeseries', namespace='Aggregation')
    reg.add_module(SeasVars, name='Seasonal Timeseries',
                   namespace='Aggregation')
    reg.add_module(Climatology, name='Climatology', namespace='Aggregation')

    reg.add_module(IndiciesNino34, name='Nino3.4', namespace='Indicies')

    reg.add_module(ConstraintBuilder, name='Constraint Builder',
                   namespace='Utilities')
    reg.add_module(GeneralCommandPattern, name='General Command Line Program',
                   namespace='Utilities')


def menu_items():
    """
    menu_items() -> tuple of (str,function)
    It returns a list of pairs containing text for the menu and a
    callback function that will be executed when that menu item is selected.
    """
    def package_configuration():
        """
        Create a shortcut to Edit->Preferences->Module Package->Enabled Packages->Configure in menu.
        """
        pkgmgr = get_package_manager()
        package = pkgmgr.get_package(identifier)
        dlg = QPackageConfigurationDialog(None, package)
        dlg.exec_()

    lst = []
    lst.append(("Configure", package_configuration))
    return tuple(lst)
