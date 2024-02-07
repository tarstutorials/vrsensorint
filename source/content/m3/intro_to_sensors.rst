.. _int_to_sensors:

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

Heart rate (HR) sensors are used to record the rate at which the heart pumps blood throughout the body, measured as the number of contractions (beats) per minute (bpm). Various factors can affect a person's heart rate, including fitness, stress, diet, genetics, medications, or disease/illness. The average HR for a normal, healthy person is between 60-100 bpm at rest, and that could drop to 40 bpm or lower in endurance athletes. 

**Heart rate variability (HRV)** is a measure of the variation in time (milliseconds) between consecutive heartbeats. The heartbeat isn't exactly regular all the time, so HRV serves as an indicator for how well your body can respond to stress or exercise. It's usually measured over a period of at least five minutes, and a higher value is better as it indicates a faster recovery.

HR and HRV are widely considered as essential metrics for understanding human health and performance.

^^^^^^^^^^^^^^^^^^^^^^^
Placement & Measurement
^^^^^^^^^^^^^^^^^^^^^^^

For this tutorial, we will focus on the `Polar H10 <https://www.polar.com/us-en/sensors/h10-heart-rate-sensor>`_ HR sensor (some of their older models, such as the H9 or H7, could suffice as well). The device is worn around the chest (typically under the shirt), with a pad placed close to the heart and held in place via a buckle and strap. This relatively unobtrusive design makes it ideal for measuring HR during intense exercise.

The Polar H10 is an example of an **electrocardiograph**, which is a type of HR sensor that measures the electrical potential of the heart's activity in order to extract the HR information. We refer to the resulting electrical signal as an **electrocardiogram (ECG)**. A typical ECG is shown below (figure from [#]_). You can find a detailed description in the paper, but for now, just know that it shows the stages of depolarization and repolarization (changes in electric charge distribution) of different parts of the heart. In particular, notice the **RR interval** on the graph: the time (seconds) between two successive R peaks. To calculate the heart rate, simply divide 60 (seconds per minute) by the RR interval.

.. image:: ../../images/ecg_graph.png
  :width: 800
  :alt: Graph of a typical electrocardiogram, with parts of the waveform labeled.

^^^^^^^^^^^^^^^^^^^^^^^^^^
Reliability & Alternatives
^^^^^^^^^^^^^^^^^^^^^^^^^^

There are a variety of other techniques for measuring HR. One common example is **photoplethysmography (PPG)**, which uses LED lights to detect blood volume changes underneath the skin. You've probably seen this on many different kinds of fitness/smart watches, where it could be used for exercise or sleep monitoring. These devices are nice because they're easier to wear than the chest strap, and in most cases, their accuracy is comparable to the chest strap ECG. However, many studies conclude that PPG is not as accurate as ECG during high-intensity activities, or when clinically assessing HRV [#]_ [#]_ [#]_, though some have shown that they may be acceptably close in certain applications [#]_ [#]_.

Studies [#]_ [#]_ have shown that the Polar H10 chest strap device is comparably accurate to the Holter medical-grade ECG. As such, these wearable sensors are considered the gold standard when it comes to commercial HR sensing.

^^^^^^^^^^^^
Applications
^^^^^^^^^^^^

As we've discussed, there are a wide variety of clinical and fitness-related applications for HR and HRV sensing. We won't attempt to provide an exhaustive list here, but just to get you thinking, here a few mobile and virtual reality applications that integrate heart rate feedback [#]_ [#]_ [#]_ [#]_. We'll explore this more in :ref:`sensors_to_int`.

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

.. [#] \D. Barmpakos, P. Kaplanis, S.A. Karkanis, and C. Pattichis. "Classification of neuromuscular disorders using features extracted in the wavelet domain of sEMG signals: a case study." *Health and Technology*, vol. 7, pp. 33-39, 2017, doi: 10.1007/s12553-016-0153-3.

.. [#] \S. Wang, H. Tang, B. Wang, and J. Mo. "A Novel Approach to Detecting Muscle Fatigue Based on sEMG by Using Neural Architecture Search Framework." *IEEE Transactions on Neural Networks and Learning Systems*, vol. 34, no. 8, pp. 4932-4943, Aug. 2023, doi: 10.1109/TNNLS.2021.3124330.

.. [#] \G. Venugopal, M. Navaneethakrishna, and S. Ramakrishnan. "Extraction and analysis of multiple time window features associated with muscle fatigue conditions using sEMG signals." *Expert Systems with Applications*, vol. 41, no. 6, pp. 2652-2659, May 2014, doi: 10.1016/j.eswa.2013.11.009.

.. [#] \M. Shariatzadeh, E.H. Hafshejani, C.J. Mitchell, M. Chiao, and D. Grecov. "Predicting muscle fatigue during dynamic contractions using wavelet analysis of surface electromyography signal." *Biocybernetics and Biomedical Engineering*, vol. 43, no. 2, pp. 428-441, Jun. 2023, doi: 10.1016/j.bbe.2023.04.002.

.. [#] \S. Huang, S. Cai, G. Li, Y. Chen, K. Ma, and L. Xie. "sEMG-Based Detection of Compensation Caused by Fatigue During Rehabilitation Therapy: A Pilot Study." *IEEE Access*, vol. 7, pp. 127055-127065, 2019, doi: 10.1109/ACCESS.2019.2933287.

.. [#] M.A. Delph II, S.A. Fischer, P.W. Gauthier, C.H. Martinez Luna, E.A. Clancy, and G.S. Fischer. "A Soft Robotic Exomusculature Glove with Integrated sEMG Sensing for Hand Rehabilitation." *IEEE 13th International Conference on Rehabilitation Robotics (ICORR)*, Jun. 2013, doi: 10.1109/ICORR.2013.6650426.

.. [#] \R. Bos, K. Nizamis, B.F.J.M. Koopman, J.L. Herder, M. Sartori, and D.H. Plettenburg. "A Case Study With Symbihand: An sEMG-Controlled Electrohydraulic Hand Orthosis for Individuals With Duchenne Muscular Dystrophy." *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, vol. 28, no. 1, pp. 258-266, Jan. 2020, doi: 10.1109/TNSRE.2019.2952470.

.. [#] \V. Khoshdel, A. Akbarzadeh, N. Naghavi, A. Sharifnezhad, and M. Souzanchi-Kashani. "sEMG-based impedance control for lower-limb rehabilitation robot." *Intelligent Service Robotics*, vol. 11, pp. 97-108, 2018, doi: 10.1007/s11370-017-0239-4.

.. [#] M.A. Ozdemir, D.H. Kisaa, O. Gurena, and A. Akanb. "Dataset for multi-channel surface electromyography (sEMG) signals of hand gestures." *Data in Brief*, vol. 41, Apr. 2022, doi: 10.1016/j.dib.2022.107921.

.. [#] \Y. Luan, Y. Shi, W. Wu, Z. Liu, H. Chang, and J. Cheng. "HAR-sEMG: A Dataset for Human Activity Recognition on Lower-Limb sEMG." *Knowledge and Information Systems*, vol. 63, pp. 2791-2814, Sep. 2021, doi: 10.1007/s10115-021-01598-w.

^^^^^^^^^^
Heart Rate
^^^^^^^^^^

.. [#] \A. Galli, R.J.H. Montree, S. Que, E. Peri, and R. Vullings. "An Overview of the Sensors for Heart Rate Monitoring Used in Extramural Applications." *Sensors*, vol. 22, no. 11, 4035, doi: 10.3390/s22114035.

.. [#] J.F. Horton, P. Stergiou, T.S. FUNG, and L. Katz. "Comparison of Polar M600 Optical Heart Rate and ECG Heart Rate during Exercise." *Medicine & Science in Sports and Exercise*, vol. 49, no. 12, pp. 2600-2607, Dec. 2017, doi: 10.1249/MSS.0000000000001388.

.. [#] H.Y. Jan, M.F. Chen, T.C. Fu, W.C. Lin, C.L. Tsai, and K.P. Lin. "Evaluation of Coherence Between ECG and PPG Derived Parameters on Heart Rate Variability and Respiration in Healthy Volunteers With/Without Controlled Breathing." *Journal of Medical and Biomedical Engineering*, vol. 39, pp. 783-795, 2019, doi: 10.1007/s40846-019-00468-9.

.. [#] K.E. Speer, S. Semple, N. Naumovski, and A.J. McKune. "Measuring Heart Rate Variability Using Commercially Available Devices in Healthy Children: A Validity and Reliability Study." *European Journal of Investigation in Health, Psychology, and Education*, vol. 10, pp. 390-404, 2020, doi: 10.3390/ejihpe10010029.

.. [#] S.A. Ruiz-Alias, F. Garcia-Pinillos, V.M. Soto-Hermoso, and E.J. Ruiz-Malago. "Heart rate monitoring of the endurance runner during high intensity interval training: Influence of device used on training functions." *Proceedings of the Institution of Mechanical Engineers, Part P: Journal of Sports Engineering and Technology*, vol. 237, no. 3, pp. 166-172, 2023, doi: 10.1177/17543371211037035.

.. [#] \F. Sartor, J. Gelissen, R. van Dinther, D. Roovers, G.B. Papini, and G. Coppola. "Wrist-worn optical and chest strap heart rate comparison in a heterogeneous sample of healthy individuals and in coronary artery disease patients." *BMC Sports Science, Medicine and Rehabilitation*, vol. 10, no. 10, 2018, doi: 10.1186/s13102-018-0098-0.

.. [#] \M. Schaffarczyk, B. Rogers, R. Reer, and T. Gronwald. "Validity of the Polar H10 Sensor for Heart Rate Variability Analysis during Resting State and Incremental Exercise in Recreational Men and Women." *Sensors*, vol. 22, no. 17, pp. 6536, 2022, doi: 10.3390/s22176536.

.. [#] \R. Gilgen-Ammann, T. Schweizer, and T. Wyss. "RR interval signal quality of a heart rate monitor and an ECG Holter at rest and during exercise." *European Journal of Applied Physiology*, vol. 119, pp. 1525-1532, 2019, doi: 10.1007/s00421-019-04142-5.

.. [#] \H. Chen, A. Dey, M. Billinghurst and R. Lindeman. "Exploring the Design Space for Multi-Sensory Heart Rate Feedback in Immersive Virtual Reality." *Proceedings of the 29th Australian Conference on Human-Computer Interaction (OzCHI 2017)*, Brisbane, QLD, Australia, 2017, doi: 10.1145/3152771.3152783.

.. [#] U.N. Hashim, L. Salahuddin, R.R.R. Ikram, U.R. Hashim, N.H. Choon, and M.H.N. Mohayat. "The Design and Implementation of Mobile Heart Monitoring Applications using Wearable Heart Rate Sensor." *International Journal of Advanced Computer Science and Applications (IJACSA)*, vol. 12, no. 1, 2021, doi: 10.14569/IJACSA.2021.0120120.

.. [#] \S. Gradl, M. Wirth, T. Zillig, and B.M. Eskofier. "Visualization of Heart Activity in Virtual Reality: a Biofeedback Application using Wearable Sensors." *2018 IEEE 15th International Conference on Wearable and Implantable Body Sensor Networks (BSN)*, Las Vegas, Nevada, USA, pp. 152-155, Mar. 2018, doi: 10.1109/BSN.2018.8329681.

.. [#] \C. Rockstroh, J. Blum, and A.S. Göritz. "Virtual reality in the application of heart rate variability biofeedback." *International Journal of Human-Computer Studies*, vol. 130, pp. 209-220, Oct. 2019, doi: 10.1016/j.ijhcs.2019.06.011.