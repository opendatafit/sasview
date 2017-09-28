function main() {
    startApplication("sasview");
    activateItem(waitForObjectItem(":MainWindow.menubar_QMenuBar", "Tool"));
    activateItem(waitForObjectItem(":MainWindow.menuTool_QMenu", "SLD Calculator"));
    test.compare(waitForObjectExists(":SldPanel_SldPanel").windowTitle, "SLD Calculator");
    test.compare(waitForObjectExists(":SldPanel_SldPanel").visible, true);
    test.compare(waitForObjectExists(":groupBoxInput.editMolecularFormula_QLineEdit").displayText, "H2O");
    test.compare(waitForObjectExists(":groupBoxInput.editMolecularFormula_QLineEdit").readOnly, false);
    test.compare(waitForObjectExists(":groupBoxInput.editMolecularFormula_QLineEdit").enabled, true);
    test.compare(waitForObjectExists(":groupBoxInput.editMassDensity_QLineEdit").text, "1");
    test.compare(waitForObjectExists(":groupBoxInput.editWavelength_QLineEdit").text, "6");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronSldReal_QLineEdit").text, "-5.61e-07");
    test.compare(waitForObjectExists(":groupBoxOutput.editCuKaSldReal_QLineEdit").text, "9.47e-06");
    test.compare(waitForObjectExists(":groupBoxOutput.editMoKaSldReal_QLineEdit").text, "9.43e-06");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronIncXs_QLineEdit").text, "5.37");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronAbsXs_QLineEdit").text, "0.0742");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronLength_QLineEdit").text, "0.175");
    type(waitForObject(":groupBoxInput.editMolecularFormula_QLineEdit"), "2");
    type(waitForObject(":groupBoxInput.editMolecularFormula_QLineEdit"), "<Tab>");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronSldReal_QLineEdit").text, "7.31e-07");
    test.compare(waitForObjectExists(":groupBoxOutput.editCuKaSldReal_QLineEdit").text, "9.03e-06");
    test.compare(waitForObjectExists(":groupBoxOutput.editMoKaSldReal_QLineEdit").text, "8.99e-06");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronIncXs_QLineEdit").text, "2.84");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronAbsXs_QLineEdit").text, "0.0393");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronLength_QLineEdit").text, "0.323");
    type(waitForObject(":groupBoxInput.editMassDensity_QLineEdit"), "5");
    type(waitForObject(":groupBoxInput.editMassDensity_QLineEdit"), "<Tab>");
    type(waitForObject(":groupBoxInput.editWavelength_QLineEdit"), "10");
    type(waitForObject(":groupBoxInput.editWavelength_QLineEdit"), "<Tab>");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronSldReal_QLineEdit").text, "3.65e-06");
    test.compare(waitForObjectExists(":groupBoxOutput.editCuKaSldReal_QLineEdit").text, "4.52e-05");
    test.compare(waitForObjectExists(":groupBoxOutput.editMoKaSldReal_QLineEdit").text, "4.5e-05");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronIncXs_QLineEdit").text, "14.2");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronAbsXs_QLineEdit").text, "0.328");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronLength_QLineEdit").text, "0.0641");
    clickButton(waitForObject(":SldPanel.Reset_QPushButton"));
    test.compare(waitForObjectExists(":groupBoxInput.editMolecularFormula_QLineEdit").text, "H2O");
    test.compare(waitForObjectExists(":groupBoxInput.editMassDensity_QLineEdit").text, "1");
    test.compare(waitForObjectExists(":groupBoxInput.editWavelength_QLineEdit").text, "6");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronSldReal_QLineEdit").text, "-5.61e-07");
    test.compare(waitForObjectExists(":groupBoxOutput.editNeutronIncXs_QLineEdit").text, "5.37");
    sendEvent("QWheelEvent", waitForObject(":SldPanel_SldPanel"), -1835, 357, 120, 0, 2);
    sendEvent("QWheelEvent", waitForObject(":SldPanel_SldPanel"), -1456, 356, -120, 0, 2);
    clickButton(waitForObject(":SldPanel.Close_QPushButton"));
}
