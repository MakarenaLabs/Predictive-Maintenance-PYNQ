# Flask REST API

The APIs availabe are the following:
* GET:
  * `/rpm`: return the current speed of the motor
  * `/logger`: return the current status of the motor depending on the configuration chosen in the logger
* POST:
  * `/rpm`: set a reference for the PI controller (velocity mode); you need to pass a JSON like this: { 'rpm': float_value }
  * `/torque`: set a reference for the PI controller (torque mode); you need to pass a JSON like this: { 'torque': float_value }
  * `/reset`: stop the motor and reset the HW registers value; you need to pass a JSON like this: { 'reset': float_value }

If you need a software for Rest API client, please use [Postman](https://www.postman.com/)
