# Flask REST API

The APIs availabe are the following:
* GET:
  * `rpm`: return the current speed of the motor
  * `logger`: return the current status of the motor depending on the configuration chosen in the logger
* POST:
  * `rpm`: set a reference for the PI controller (velocity mode)
  * `torque`: set a reference for the PI controller (torque mode)
  * `reset`: stop the motor and reset the HW registers value 
