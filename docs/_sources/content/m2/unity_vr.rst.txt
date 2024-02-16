====================
Unity VR Development
====================

--------------------------------
Introduction to VR Development
--------------------------------

Virtual Reality(VR) is a rapidly expanding technology that is becoming more and more integrated into everyday life. As such, application development for this medium is at an all-time high. Learning how to create applications for VR is more important now than ever, and Unity is the best tool for beginning this journey. Follow this tutorial closely, as the techniques learned here will not only be critical to being successful in future tutorials, but also in building skills for the incoming VR boom.

-----------
Why Unity?
-----------

.. image:: ../../images/UnityLogo.png
  :width: 400
  :alt: An Image of the Unity logo.

As stated in the introduction, Unity will be the tool of choice for development in VR. Unity is *the* best pick for anyone looking to develop for VR, for a multitude of reasons. First, Unity has a large variety of actively updated packages to facilitate building out a VR package, something that other engines lack. Second, Unity has multiple ways to build and test a VR application, by controlling the build of the project. Unity VR projects can be built as standalone Android applications, meaning that they do not require a computer to be connected to the headset to run the app. They can also be built for Windows, allowing them to run alongside a computer for easier testing and modification. Lastly, Unity was chosen due to its thriving development community and ease of access, both of which offer newcomers a level of support that you would be unlikely to come accross elsewhere. These are the main reasons Unity was chosen, and why most VR developers opt to use Unity as well.

.. _to_create_vr:
----------------------
Creating a VR Project
----------------------

Creating a new Unity project for VR is very similar to the way you created the mobile project in the last section. Do the following to get your VR project created:

.. image:: ../../images/UnityLogin.png
  :width: 800
  :alt: An Image of the Unity login screen.

1. Launch Unity Hub and login to your Unity account. If you do not have either of these completed, see :ref:`new_to_install`.

.. image:: ../../images/EmptyProjects.png
  :width: 800
  :alt: An Image of the projects tab in Unity Hub.

2. On the sidebar on the left side of the application, select the *Projects* tab.

3. On the top right of the application, press the button titled *New project*.

.. image:: ../../images/NewVRProject.png
  :width: 800
  :alt: An Image of a 2D Mobile template for a project in Unity Hub.

4. Under the templates section, select the *VR Core* option. You may have to download the template if you have not used it already. The button to download it can be seen on the right side of the application after clicking on the template.

5. Choose a name for your project. It can be anything you like, but we recommend naming it with one word in order to make file access easier. For now, let's call it *MyFirstVRProject*.

6. Choose the where you'd like to store your project. Be sure to pick a location that is easy to find.

7. Click the *Create project* button in the bottom right corner of the application. This will create the project and launch the editor, which will contain a pre-made sample scene for you to start with.

-------------------
Pre-Project Setup
-------------------

Unlike the simple mobile game you saw in :ref:`install_to_new`, a VR project will require a larger setup process before you begin work. These steps are not optional, and should be followed closely.

^^^^^^^^^^^^^^^^^^^^
Essential Packages
^^^^^^^^^^^^^^^^^^^^

There are some packages you will need for this project, and since you likely haven't used the Unity package manager yet, the following steps will teach you how to verify the packages you need for this project are properly installed, and how to install them if they are not. It will also serve as a template for installing any Unity package from the package manager:

1. Launch Unity Hub and login to your Unity account.

#. On the sidebar to the left of the application, select the *Projects* tab.

#. Open the project you created in :ref:`to_create_vr`.

#. On the ribbon in the top left of the editor, select the *Window* option. This will open a drop-down menu with several options.

.. image:: ../../images/package_manager.png
  :width: 800
  :alt: An Image of the package manager tab in the Unity Editor.

5. In the drop-down menu that appears, select the *Package Manager* option. This will open the Unity package manager in a new window. The Unity package manager is used to install, disable, update, and remove packages from a project.

#. Within the package manager, press the drop-down labeled `Packages:`. This should bring up a menu of sources where packages are located. Select the `Packages: In Project` option. You will now see a list of the packages currently installed for this project appear. 

.. image:: ../../images/package_manager_select.png
  :width: 800
  :alt: An Image of the necessary packages in the package manager of the Unity Editor.

7. Verify that the following packages are installed in your project. If all of them are installed, you can skip the rest of these steps - however, the steps below will teach you how to install a package, so if you plan on using additional packages for your project, it is useful information. 

    * XR Interaction Toolkit

    * XR Core Utility

    * XR Legacy Input Helpers

    * XR Plugin Management

    * OpenXR Plugin

    * Oculus XR Plugin

.. note::
    Many other VR integration packages exist in Unity, such as the Oculus integration package. However, these packages are mostly limited to the specific brand headset that the package is for. The Oculus integration package only works on Meta Quest devices, for example. The benefit of using the XR toolkit instead is that it allows the application to be run on almost any VR capable device. 
    
    The only caveat with using the XR toolkit is that you lose access to some headset-specific features. This is an acceptable compromise for this set of tutorials, which aims to teach the basics of Unity VR development for a wide variety of devices. If you instead wish to use headset-specific features in your project, you will have to learn how to use their proprietary packages instead. 

8. If you found that any of the previously listed packages were missing from your project, Click on the "+" button in the top left corner of the package manager. This will present you with options to add a package to your project.

#. Select the *Add package by name...* option. This will prompt you to input the name and version of the package you would like to add. 

#. Enter the name of the missing package and leave the version field blank. Ensure the information you provided is correct, and press the *Add* button. This will install the most recent version of the package to your project.

#. Repeat steps 8 through 10 until all the missing packages are installed. You have now successfully installed the packages you will need for VR development.


^^^^^^^^^^^^^^^^^^^^^^^^^^
Project Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you recall the :ref:`to_mobile_setup` subsection of module one, you will remember the mention of *Project Settings* and *Build Settings*. While the simple mobile application that was made in that module did not require any modification of these settings, that is not the case for this more advanced tutorial. Some of the changes found in this and the following section are necessary for your project to run correctly, so please make sure to do all of them.


#. Launch Unity Hub and login to your Unity account.

#. On the sidebar to the left of the application, select the *Projects* tab.

#. Open the project you created in :ref:`to_create_vr`.

#. On the ribbon in the top left of the editor, select the *Edit* option. This will open a drop-down menu with several options.

.. image:: ../../images/project_settings.png
  :width: 400
  :alt: An Image of the project settings tab in the Unity Editor.

5. In the drop-down menu that appears, select the *Project Settings* option. This will open the settings for your project in a new window. There are a few changes you will need to make to the default settings to allow your development to run smoothly.

6. In the sidebar on the left side of the project settings menu, select the *XR Plugin-Management* option. 

.. image:: ../../images/xr_plugin_management.png
  :width: 800
  :alt: An Image of the XR Plugin Management settings in the settings menu of the Unity Editor.

7. In the settings that appear for this package, make sure that the box labeled *Initialize XR on Startup* is checked for all platforms.

#. To the left of *XR-Plugin Management* option that you selected before, there is a right-facing arrow. Click this arrow. This will reveal additional options for the package.

#. In the list of new options that appear, select the *XR Interaction Toolkit* option.

.. image:: ../../images/xr_interaction_toolkit.png
  :width: 800
  :alt: An Image of the XR Interaction Toolkit settings in the settings menu of the Unity Editor.

10. In the settings that appear for this package, check the box labeled *Use XR Device Simulator in scenes*. This may prompt you to add the *XR Device Simulator* prefab to your project. If this appears, select OK. This will allow you to test your game from the the computer without using a headset by using the simulator prefab mentioned earlier when the game is run in play mode.

#. In the same menu where you found the *XR Interaction Toolkit* option, select the *Project Validation* option. 

.. image:: ../../images/project_validation.png
  :width: 800
  :alt: An Image of the Project Validation settings in the settings menu of the Unity Editor.

12. In the settings that appear, select the *Windows, Mac, Linux settings* tab, and check the box labeled *Show All*. Do the same for the *Android settings* tab. This will display any issues found with your project and can help you fix any that occur. This tab is extremely useful for finding bugs in your project, so refer back to it if you ever have errors compiling your project. 

#. Those are all the project settings you need to move froward, but feel free to peruse the menus and see what otehr options there are. Just be careful, because checking certain options could mess with your projects ability to run correctly. The next section will help you set up your projects build settings.


^^^^^^^^^^^^^^^^^^^^
Build Settings
^^^^^^^^^^^^^^^^^^^^

At this point in the process, you will have to decide how you want to build your project. VR projects can be built to be run on a standalone headset, or in tandem with a PC. Both build methods have their merits, but the tutorial here will teach you how to develop for a standalone Android device, as this option is more widely accessible. Android does not require a powerful computer, nor does it require a constant connection to the computer to run. If you wish to create a non-standalone application, you will have to adjust your build and project settings according to your desired platform. You can find out more in the Unity documention on `Platform Development <https://docs.unity3d.com/Manual/PlatformSpecific.html>`_.  Otherwise, follow the steps below to set your project up for an Android build:

#. Launch Unity Hub and login to your Unity account.

#. On the sidebar to the left of the application, select the *Projects* tab.

#. Open the project you created in :ref:`to_create_vr`.

#. On the ribbon in the top left of the editor, select the *File* option. This will open a drop-down menu with several options.

.. image:: ../../images/build_settings.png
  :width: 800
  :alt: An Image of the build settings in the top ribbon of the Unity Editor.

5. In the drop-down menu that appears, select the *Build Settings* option. This will open the build settings in a new window. This is where you will change your desired platform to Android.

#. In the window that appears containing the build settings, look to the bottom right corner of the window. You should see a list titled *Platform*, with multiple clickable options below it. Select the *Android* option.

.. image:: ../../images/android_build.png
  :width: 800
  :alt: An Image of the build settings window with the Android platform selected.

7. In the same window, in the bottom right corner, there will be a button the says *Switch Platform*. Click this button. This will change your platform to Android and cause the editor to rebuild the domain for this new platform. This could take a little bit to do.

.. note::
    If you ever need to change the build platform for your project, it is a good idea to do this when you first create the project or early on in its development. This is because changing platforms can take a very long time for large projects and increases the likelihood of bugs appearing when the domain is rebuilt. If you do have to change your build late into development of your application, be ready to wait a while for the swap and to sift through small bugs that appear when the platform change occurs.

8. That is all you have to do to change your build platform. While you changed your build to Android here, the process is the same for switching to any platform; Selecting your desired platform from the *Platform* list before clicking the *Switch Platform* button. 

When you are ready to actually build your project, return to the build settings window and select the *Build* button. Since your project is for Android, this will produce an APK file that you can then store on your headset and access to run the project. Building the APK can take some time, so it is good practice to perform most basic testing in the Unity editor using the *XR Device Simulator*, building infrequently and only using the actual headset for more complicated testing.


--------------------------
Advanced Techniques in VR
--------------------------

VR development has a lot more moving pieces than traditional application development. Having a strong foundation in the Unity basics from the last section is a prerequisite to understanding the more advanced techniques discussed here. If you feel you need more practice in the basics, don't hesitate to return to :ref:`install_to_new` to refresh. There is no shame in extra practice. If you think you have mastered the previous module and are ready to move on, continue reading to delve in to the advanced techniques found in VR development.

^^^^^^^^
XR Rig
^^^^^^^^

The XR rig is a prefab object included in the XR Interaction Toolkit. This object allows the user to interact with the virtual environment by providing input in the form of sight, sound, and touch. The XR rig is how the user connects their actions in the headset to the Unity application. As such, it is absolutely necessary for any VR application. The XR rig has two child objects called `Camera Offset` and `Locomotion System` that provide the previously mentioned inputs through their own child objects and their attached scripts. There are a lot of parameters you can change within the XR rig object and its child object, and exploring these can further customize your VR control scheme, but the default parameter settings are completely acceptable for most use cases.

You can access the XR rig individually by searching for `XR Origin (XR Rig)` in the assets folder of the project manager, however, the template project provided by default when using the Unity VR Core project type has an prefab called `Complete XR Origin Set Up Variant` that already has the XR rig as a child object, and has it already set up for use alongside other useful objects you will learn more about in the upcoming subsections. This tutorial will be using this prefab instead, since it facilitates set-up, and provides additional actions for the player. If you wish to set up your own player rig without the extra objects, you can always use the XR rig by itself.

^^^^^^^^^^^^^^^^^^^
XR UI Input Module
^^^^^^^^^^^^^^^^^^^
Included in the afformentioned `Complete XR Origin Set Up Variant` is an empty child object called `EventSystem`. This object has a script attached to it called the `XR UI Input Module`. This script allows the player to use UI elements in virtual reality. The script has multiple parameters set up to control UI actions, connecting each to a preset for that specific action. These actions, like `Point Action` and `Left Click Action` allow you to control what happens when that action occurs. However, the default presets for these actions are intuitive and should remain as-is for most projects. 

.. note::
    If you add the `XR UI Input Module` to another object, you will have to manually add these presets for the actions, which can be found by searching `XRI UI` in the project window search bar and dragging each Input Ation Reference that appears to its corresponding parameter in the script component. This can be confusing, so it is highly recommended to just use the `Complete XR Origin Set Up Variant` prefab instead.

^^^^^^^^^^^^^^^^^^

^^^^^^^^^^^^^^^^^^


---------------
Section Review
---------------
