.. _install_to_new:

==================
Unity Orientation
==================

---------------------------
Creating Your First Project
---------------------------

For our first project, we'll be designing a simple mobile mobile application for Android. Use the following steps to get started:

#. Launch Unity Hub and login to your Unity account. If you do not have either of these completed, see :ref:`new_to_install`.

#. On the sidebar on the left side of the application, select the "Projects" tab.

#. On the top right of the application, press the button titled "New project".

#. Under the templates section, select the "2D Mobile" option. You may have to download the template if you have not used it already. The button to download it can be seen on the right side of the application after clicking on the template.

#. Choose a name for your project. It can be anything you like, but we recommend naming it with one word in order to make file access easier. An example of a good project title would be *MyFirstProject*.
#. Choose the location where to store your project. Be sure to pick a location that is easy to find.
#. Click the "Create project" button in the bottom right corner of the application. This will create the project and launch the editor.

--------------------------
Understanding the Editor
--------------------------

The Unity Editor can seem overwelming at first, but it can actually be broken down into four simple pieces. The image below visualizes these pieces.

.. image:: ../../../../../../../docs/source/images/Unity2DEditorFilled.png
  :width: 800
  :alt: An Image of the Unity Editor: Highlighted are: Project Window, Inspector Window, Scene View, and Object Hierarchy.

^^^^^^^^^^^^^^^
Project Window
^^^^^^^^^^^^^^^

Shaded blue in the image above, the project window contains the file structure of your project. On the left hand side of the window, you will see a sidebar. This sidebar contains the folders located within your project folder. By default, this is the assets folder and the packages folder. The assets folder contains many subfolders with useful files in them. These are where you can create and access any folders, scripts, materials, scenes, and prefabs you use in your project. Additionally, if you install any packages from the package manager, a folder for that package will show up here. Do not worry about these terms now, they will be explained later. Common practice is to keep these folders organized, so that you do not lose track of your files. 

Try exploring the project window, and seeing what files are contained in it.

^^^^^^^^^^^^^^^^
Inspector Window
^^^^^^^^^^^^^^^^

^^^^^^^^^^^^^^^^
Scene View
^^^^^^^^^^^^^^^^

^^^^^^^^^^^^^^^^^^
Object Hierarchy
^^^^^^^^^^^^^^^^^^
Shaded in red in the image above, the object hierarchy contains any GameObjects you currently have loaded into the scene. GameObjects are the building blocks of Unity, and can be created using the "+" button in the top left of the window. Additionally, you can right click anywhere in the window to open the GameObject creation menu. There are many built in GameObject types, but savvy users can create their own type of object if it is not available. 

The reason for the "hierarchy" in the name is because of the parent-child relationships that objects have. An object can be a "parent" or "child" of another object, and each object can have many levels of parents and children, creating "grandparents" and "grandchildren", so to speak. The purpose of these relationships are that some actions, such as transforming an object, will apply to the children of the object as well. For example, if you had a snowman object, but wanted to add a hat on the snowman, if you made the hat a child of the snowman, moving the snowman would move the hat along with it. To make an object a child of another, click on the object you want to be the parent in the hierarchy, then right click and create a new object. The created object will be this object's child. 

Try exploring with adding different types of GameObjects to the scene, and creating multiple levels of parents and children until you feel comfortable. Note that you can delete any object you create by right clicking on it in the hierarchy and clicking delete.

---------------------------------
Setting Up For Mobile Development
---------------------------------

Mobile development can be hard, here's how to set it up.

-----------------
Basic Techniques
-----------------

Here are some basic techniques for mobile development in Unity.


^^^^^^^^^^^^^^^
Object Creation
^^^^^^^^^^^^^^^

^^^^^^^^^^^^^
C# Scripting
^^^^^^^^^^^^^

^^^^^^^^^^^^^^^
Physics System
^^^^^^^^^^^^^^^

^^^^^^^^^^^^^^^
Tips and Tricks
^^^^^^^^^^^^^^^

------------------
Section Review
------------------