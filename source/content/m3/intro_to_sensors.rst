======================================
Introduction to Physiological Sensors
======================================

**How can we use technology to help diagnose disorders, improve athletic performance, and guide rehabilitation?** We will start to answer this question in this section of the tutorial by giving an overview of the sensors used to measure physiological information about the human body. By studying how strong muscles are, how much air the lungs can circulate, how fast the heart can pump blood throughout the body, and more, we can gain a better understanding of how the human body behaves and design tools that help people achieve their goals.

The information on each sensor will be organized as follows: first, we'll give a brief overview of what it's used for, then some instruction on how it is worn and what it measures (including reliability of the data), and perhaps most importantly, some discussion on what you could study or build using it.

---------------------------------------
Surface Electromyography: Delsys Trigno
---------------------------------------

Surface electromyography (sEMG) is a technique used to measure electromyographic signals that correspond to muscle activity. Muscles throughout the human body are activated in response to neural stimulation from the brain, and as they contract, they release an electrical impulse that circulates throughout bones and tissue. These impulses are captured by the sEMG sensor, and after applying some signal processing techniques that we'll see later in this tutorial, they can be incredibly useful in studying the patterns of our muscles.

^^^^^^^^^^^^^^^^^^^^^^^
Placement & Measurement
^^^^^^^^^^^^^^^^^^^^^^^

For the purposes of this tutorial, we'll be using the Delsys sEMG sensors, widely regarded for their clinical-grade quality in research and industrial settings. Specifically, three of their most common products are the Trigno Avanti, Trigno Mini, and Trigno Quattro sensors.

* The `Trigno Avanti <https://delsys.com/trigno-avanti/>`_ is their "standard" sEMG sensor.
* The `Trigno Mini <https://delsys.com/trigno-mini/>`_ is a smaller form factor sensor, allowing you to get data from muscles that may be harder to reach with the Avanti.
* The `Trigno Quattro <https://delsys.com/trigno-quattro/>`_ is similar to the Trigno Mini, but there are four sensing heads, allowing you to get precise data from multiple locations.

Each of these devices also contains an **IMU (inertial measurement unit)** sensor, which reports data on acceleration and orientation. This can be used in conjunction with the sEMG signal to understand the motion of the muscle. 

The sensors are placed on the surface of the skin and stick via a simple adhesive. Be careful as to where you place them, since they should be placed as close to the muscle as possible to achieve high-quality results. The surface of the skin should also be cleaned with an alcohol wipe before placing the sensor to remove any oils or contaminants which could interfere with the electrical signal. For more information on placing the sensors, consult the user guides that come with the products.

.. or consult Matt's tutorial once we have a link to it

Traditionally, intramuscular electromyography (iEMG) is another technique used to measure muscle activity by sticking a needle inside the skin next to a particular muscle. While this is still used in some clinical applications, especially when muscles are deep into the skin or have a small cross-sectional area, it is becoming an increasingly less popular approach as it is more invasive for data collection.

Finally, an important concept in most sEMG applications is **maximum voluntary contraction (MVC)**. In order to measure muscle strength, especially in patients with neuromuscular disorders, we have the patient flex a certain muscle as much as they can and use the resulting sEMG value as a baseline. Then, all future readings are compared as a percentage of MVC.

^^^^^^^^^^^^
Applications
^^^^^^^^^^^^

As mentioned previously, sEMG can be used to study a wide variety of behaviors. We'll provide some examples here. Many of these applications involve developing machine learning algorithms for automated classification based on sEMG signals, though this is not necessary.

* It can help diagnose certain muscular disorders, including muscular dystrophy and chronic pain [#]_ [#]_.
* It can help identify nerve dysfunction and muscle fatigue [#]_ [#]_ [#]_ [#]_.
* It can be used as a control signal for prosthetic and other robotic devices [#]_ [#]_ [#]_.
* It can be used to help understand human motions via the collection of large-scale sEMG datasets to train machine learning algorithms [#]_ [#]_.

---------------------
Heart Rate: Polar H10
---------------------

Heart rate sensors are used to record the natural frequency at which a person's heart beats, usually in reported in the unit of Beats per Minute (BPM).

^^^^^^^^^^^^^^^^^^^^^^^
Placement & Measurement
^^^^^^^^^^^^^^^^^^^^^^^


^^^^^^^^^^^^^^^^^^^^^^^^^^
Reliability & Alternatives
^^^^^^^^^^^^^^^^^^^^^^^^^^


^^^^^^^^^^^^
Applications
^^^^^^^^^^^^


---------------------------
Muscle Oxygen: Moxy Monitor
---------------------------

A Muscle Oxygen sensor is used to measure the saturation of oxygen levels within various muscle groups in the human body.

^^^^^^^^^^^^^^^^^^^^^^^
Placement & Measurement
^^^^^^^^^^^^^^^^^^^^^^^


^^^^^^^^^^^^^^^^^^^^^^^^^^
Reliability & Alternatives
^^^^^^^^^^^^^^^^^^^^^^^^^^


^^^^^^^^^^^^
Applications
^^^^^^^^^^^^


----------------------------------
Oxygen Volume: VO2 Master Analyzer
----------------------------------

Oxygen Volume (Vo2) sensors, are used to measure oxygen consumption during aerobic and anaerobic physical activity.

^^^^^^^^^^^^^^^^^^^^^^^
Placement & Measurement
^^^^^^^^^^^^^^^^^^^^^^^


^^^^^^^^^^^^^^^^^^^^^^^^^^
Reliability & Alternatives
^^^^^^^^^^^^^^^^^^^^^^^^^^


^^^^^^^^^^^^
Applications
^^^^^^^^^^^^


---------------
Section Review
---------------


----------
References
----------

^^^^^^^^^^^^^^^^^^^^^^^^
Surface Electromyography
^^^^^^^^^^^^^^^^^^^^^^^^

.. [#] M.F. Antwi-Afaria, H. Lib, D.J. Edwardsc, E.A. Pärnc, J. Seod, and A.Y.L. Wong. "Biomechanical analysis of risk factors for work-related musculoskeletal disorders during repetitive lifting task in construction workers." *Automation in Construction*, vol. 83, pp. 41-47, Nov. 2017, doi: 10.1016/j.autcon.2017.07.007.

.. [#] D. Barmpakos, P. Kaplanis, S.A. Karkanis, and C. Pattichis. "Classification of neuromuscular disorders using features extracted in the wavelet domain of sEMG signals: a case study." *Health and Technology*, vol. 7, pp. 33-39, 2017, doi: 10.1007/s12553-016-0153-3.

.. [#] S. Wang, H. Tang, B. Wang, and J. Mo. "A Novel Approach to Detecting Muscle Fatigue Based on sEMG by Using Neural Architecture Search Framework." *IEEE Transactions on Neural Networks and Learning Systems*, vol. 34, no. 8, pp. 4932-4943, Aug. 2023, doi: 10.1109/TNNLS.2021.3124330.

.. [#] G. Venugopal, M. Navaneethakrishna, and S. Ramakrishnan. "Extraction and analysis of multiple time window features associated with muscle fatigue conditions using sEMG signals." *Expert Systems with Applications*, vol. 41, no. 6, pp. 2652-2659, May 2014, doi: 10.1016/j.eswa.2013.11.009.

.. [#] M. Shariatzadeh, E.H. Hafshejani, C.J. Mitchell, M. Chiao, and D. Grecov. "Predicting muscle fatigue during dynamic contractions using wavelet analysis of surface electromyography signal." *Biocybernetics and Biomedical Engineering*, vol. 43, no. 2, pp. 428-441, Jun. 2023, doi: 10.1016/j.bbe.2023.04.002.

.. [#] S. Huang, S. Cai, G. Li, Y. Chen, K. Ma, and L. Xie. "sEMG-Based Detection of Compensation Caused by Fatigue During Rehabilitation Therapy: A Pilot Study." *IEEE Access*, vol. 7, pp. 127055-127065, 2019, doi: 10.1109/ACCESS.2019.2933287.

.. [#] M.A. Delph II, S.A. Fischer, P.W. Gauthier, C.H. Martinez Luna, E.A. Clancy, and G.S. Fischer. "A Soft Robotic Exomusculature Glove with Integrated sEMG Sensing for Hand Rehabilitation." *IEEE 13th International Conference on Rehabilitation Robotics (ICORR)*, Jun. 2013, doi: 10.1109/ICORR.2013.6650426.

.. [#] R. Bos, K. Nizamis, B.F.J.M. Koopman, J.L. Herder, M. Sartori, and D.H. Plettenburg. "A Case Study With Symbihand: An sEMG-Controlled Electrohydraulic Hand Orthosis for Individuals With Duchenne Muscular Dystrophy." *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, vol. 28, no. 1, pp. 258-266, Jan. 2020, doi: 10.1109/TNSRE.2019.2952470.

.. [#] V. Khoshdel, A. Akbarzadeh, N. Naghavi, A. Sharifnezhad, and M. Souzanchi-Kashani. "sEMG-based impedance control for lower-limb rehabilitation robot." *Intelligent Service Robotics*, vol. 11, pp. 97-108, 2018, doi: 10.1007/s11370-017-0239-4.

.. [#] M.A. Ozdemir, D.H. Kisaa, O. Gurena, and A. Akanb. "Dataset for multi-channel surface electromyography (sEMG) signals of hand gestures." *Data in Brief*, vol. 41, Apr. 2022, doi: 10.1016/j.dib.2022.107921.

.. [#] Y. Luan, Y. Shi, W. Wu, Z. Liu, H. Chang, and J. Cheng. "HAR-sEMG: A Dataset for Human Activity Recognition on Lower-Limb sEMG." *Knowledge and Information Systems*, vol. 63, pp. 2791-2814, Sep. 2021, doi: 10.1007/s10115-021-01598-w.