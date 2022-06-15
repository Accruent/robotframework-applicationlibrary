robotframework-applicationlibrary
===========
[![PyPI version](https://badge.fury.io/py/robotframework-applicationlibrary.svg)](https://badge.fury.io/py/robotframework-applicationlibrary)
[![Downloads](https://pepy.tech/badge/robotframework-applicationlibrary)](https://pepy.tech/project/robotframework-applicationlibrary)
[![Build Status](https://github.com/Accruent/robotframework-applicationlibrary/workflows/tests/badge.svg?branch=master)](https://github.com/Accruent/robotframework-applicationlibrary/actions?query=workflow%3Atests)
[![Coverage Status](https://coveralls.io/repos/github/Accruent/robotframework-applicationlibrary/badge.svg?branch=master)](https://coveralls.io/github/Accruent/robotframework-applicationlibrary?branch=master)
[![CodeFactor](https://www.codefactor.io/repository/github/accruent/robotframework-applicationlibrary/badge)](https://www.codefactor.io/repository/github/accruent/robotframework-applicationlibrary)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/Accruent/robotframework-applicationlibrary.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Accruent/robotframework-applicationlibrary/alerts/)

Introduction
--------------

Robotframework-ApplicationLibrary is a collection of libraries spanning Mobile and Windows Desktop (WinAppDriver) automation using [Robot Framework](https://github.com/robotframework/robotframework).
These libraries are and extensions of the existing [AppiumLibrary](https://github.com/serhatbolsu/robotframework-appiumlibrary). ApplicationLibrary extends the functionality 
of AppiumLibrary for Mobile app testing and adds support Windows desktop automation.

In those course of our own automation as a team, we found that out-of-the-box AppiumLibrary did not fit our needs for mobile testing and needed major rework inorder to get it working with WinAppDriver for Desktop testing.
Originally this code was a part of [RobotFramework-Zoomba](https://github.com/Accruent/robotframework-zoomba) but diverging dependency requirements lead to a need for two separate repositories.

See the **Keyword Documentation** for the [Mobile](https://accruent.github.io/robotframework-applicationlibrary/MobileLibraryDocumentation.html) or [Desktop](https://accruent.github.io/robotframework-applicationlibrary/DesktopLibraryDocumentation.html) libraries for more specific information about the functionality.

Example tests can be found in the [samples directory](https://github.com/Accruent/robotframework-applicationlibrary/tree/master/samples).

Some Features of the Library
--------------
#### [Mobile Library](https://accruent.github.io/robotframework-applicationlibrary/MobileLibraryDocumentation.html):
Extending the [AppiumLibrary](https://github.com/serhatbolsu/robotframework-appiumlibrary) we added some quality of life 'Wait For And' type keywords:
```robotframework
Wait For And Click Element      locator
Wait For And Click Text         text
Wait Until Element Contains     locator     text
```
As well as additional features that have yet to be implemented in AppiumLibrary:
```robotframework
Drag and Drop      source_locator     target_locator
Drag And Drop By Offset     locator    x_offset     y_offset
Scroll Down To Text       text
Scroll Up To Text         text
```

#### [Desktop Library](https://accruent.github.io/robotframework-applicationlibrary/DesktopLibraryDocumentation.html):
Also extends [AppiumLibrary](https://github.com/serhatbolsu/robotframework-appiumlibrary) to tailor it Windows desktop automation. This includes enhancements to base keywords such as [Open Application](https://accruent.github.io/robotframework-applicationlibrary/DesktopLibraryDocumentation.html#Open%20Application) or [Click Element](https://accruent.github.io/robotframework-applicationlibrary/DesktopLibraryDocumentation.html#Click%20Element) to perform better for windows. Other notable additions include:

Start and Stop the WinAppDriver as needed (best used for suite setup/teardown):
```robotframework
Driver Setup
Driver Teardown
```
Easily switching to new windows or the desktop session:
```robotframework
Switch Application      Desktop
Switch Application By Name     remote_url    new_window_name
```
A variety of keywords for controlling the mouse:
```robotframework
Mouse Over Element     locator
Mouse Over and Click Element    locator
Mouse over and Context Click Element    locator
Mouse Over By Offset     x_offset    y_offset
```
Keywords for dragging and dropping:
```robotframework
Drag and Drop      source_locator     target_locator
Drag And Drop By Offset     locator    x_offset     y_offset
```
The ability to send key commands to the application:
```robotframework
Send Keys     \\ue00      p     \\ue00
Send Keys To Element    locator     a     b     c
```
Selecting an element from a combobox or a menu:
```robotframework
Select Element From ComboBox     combobox_locator      element_locator
Select Elements From Menu     locator_1    locator_2   locator_n
Select Elements From Context Menu     locator_1    locator_2   locator_n
```

Selecting an element by an image file (Appium v1.18.0 and higher only):
```robotframework
Wait For And Click Element     image=file.png
```

For WebView2 applications we can control both the application view and the Edge browser view:

<a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/3010366/122806407-e4759700-d28f-11eb-8b72-779660606d9f.gif"><img src="https://user-images.githubusercontent.com/3010366/122806407-e4759700-d28f-11eb-8b72-779660606d9f.gif" alt="rbmzmun3cR" style="max-width:60%;"></a>

With the split from [RobotFramework-Zoomba](https://github.com/Accruent/robotframework-zoomba), the support for this exact example won't work in this current code. An example of this [can be found in the samples directory for robotframework-zoomba version 2.14.3 or lower](https://github.com/Accruent/robotframework-zoomba/blob/2.14.3/samples/WebView-DesktopTest.robot).

Getting Started
----------------

The Application library is easily installed using the [`setup.py`](https://github.com/Accruent/robotframework-applicationlibrary/blob/master/setup.py) file in the home directory.
Simply run the following command to install ApplicationLibrary and it's dependencies:

```python
pip install robotframework-applicationlibrary
```

If you decide to pull the repo locally to make contributions or just want to play around with the code
you can install ApplicationLibrary by running the following from the *root directory*:
```python
pip install .
```

or if you intend to run unit tests:
```python
pip install .[testing]
```

To access the keywords in the library simply add the following to your robot file settings (depending on what you are testing):
```python
*** Settings ***
Library    ApplicationLibrary.MobileLibrary
Library    ApplicationLibrary.DesktopLibrary
```

Additional Setup Information
---------------------------------

If you plan to run Mobile automation you will need to have a running appium server. To do so first have [Node](https://nodejs.org/en/download/)
installed and then run the following:
```python
npm install -g appium
appium
```

To use the `image` locator strategy you will need to install [opencv4nodejs](https://github.com/justadudewhohacks/opencv4nodejs) via the following command:
```python
npm install -g opencv4nodejs
```

Alternatively [Appium Desktop](https://github.com/appium/appium-desktop/releases) can be used.

For Windows automation we suggest [installing and using the WinAppDriver](https://github.com/Microsoft/WinAppDriver/releases) without Appium as it seems to be a bit faster and more stable.

Make sure to [enable developer mode on your system](https://www.howtogeek.com/292914/what-is-developer-mode-in-windows-10/#:~:text=How%20to%20Enable%20Developer%20Mode,be%20put%20into%20Developer%20Mode.) to allow the WinAppDriver to work.

Examples
------------
Example tests can be found in the [samples directory](https://github.com/Accruent/robotframework-applicationlibrary/tree/master/samples).

The [test directory](https://github.com/Accruent/robotframework-applicationlibrary/tree/master/test) may also contain tests but be aware that these are used for testing releases and may not be as straight forward to use as the ones in the [samples directory](https://github.com/Accruent/robotframework-applicationlibrary/tree/master/samples).


Contributing
-----------------

To make contributions please refer to the [CONTRIBUTING](https://github.com/Accruent/robotframework-applicationlibrary/blob/master/CONTRIBUTING.rst) guidelines.

See the [.githooks](https://github.com/Accruent/robotframework-applicationlibrary/tree/master/.githooks) directory for scripts to help in development. 

Support
---------------
General Robot Framework questions should be directed to the [community forum](https://forum.robotframework.org/).

For questions and issues specific to ApplicationLibrary please create an [issue](https://github.com/Accruent/robotframework-applicationlibrary/issues) here on Github.
