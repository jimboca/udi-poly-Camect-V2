# Camect Nodeserver

This is a Polyglot Nodeserver for the [Universal Devices](https://www.universal-devices.com/) ISY to integrate the [Camect](http://camect.com) System.

This is the initial version so it may change drastically but you are welcome to test and give feedback.

## Installation

Install from the Polyglot Store.  See [Configuration](POLYGLOT_CONFIG.md) on the configuration page after installing.

## Requirements

This has been tested on an RPI running the latest Buster release and the Polisy.  

- You must have Python verison 3.6 or newer.
- This uses the [Camect Python Library](https://github.com/camect/camect-py)

## Using this Nodeserver

After configuring you should get a Node for each Camera, and under each Camera an ObjectDetected node for each type of object currently detected by Camect.

### Controller

The main controller node.

- The Status shows:
  - Nodeserver Online: Nodeserver connected to Polyglot
  - Camect Connected: Status of connection to all your Camects
  - Logger Level: The current Logging level

- The Controls available:
  - Logger Level
      Usually set to Warning, unless you are debugging issues and want to see all information, but this will use up a lot of disk space.
    - Debug + Modules: All Debug including referenced modules
    - Debug
    - Info
    - Warning
    - Error

![The Controller](pics/Controller.png)

### Host

A node is created for each Camect Host device.

- The Satus shows:
  - Camect Connected: Status of connection to your Camect

### Camera

A node is created for each Camera.

- The Status shows:
  - Enabled: If the Camera is enabled
  - Alerting: If the Camera is sending Alerts
  - Streaming: If the Camera is streaming
- The Controls Available:
  - Enabled: [Coming soon](https://github.com/jimboca/udi-poly-Camect/issues/1)
  - Alerting: [Coming soon](https://github.com/jimboca/udi-poly-Camect/issues/2)

![A Camera Node](pics/OutFrontDoor.png)

### Detected Object

The Camera nodes all have a child node for major type of object that can be detect; animal, human, insect, vehicle.  Each of those contain the object type by Camect.  
When the object is detected the status for that objec is set to True and a DON is sent.  The status remains True until a different type of detection event is sent by Camect.

- The Status Shows:
  - Detected: True when object has been detected

![A Detected Animal Object](pics/OutFrontDoor_animal.png)
![A Detected Human Object](pics/OutFrontDoor_human.png)
![A Detected Insect Object](pics/OutFrontDoor_insect.png)
![A Detected Vehicle Object](pics/OutFrontDoor_vehicle.png)

#### How to use Detected Objects

You can create a program to know when a Skunk enters your front yard ![Skunk Program](pics/ProgramSkunk.png)

You can add the nodes to a scene to know when a Person shows up [Person Scene](pics/ScenePerson.png)

## Version History

- 0.1.1
  - Enable/Disable Alerting working
- 0.1.0
  - __IMPORTANT__ If using previous version you should delete the nodeserver and add it again.
  - Group detected objects by major types, person, vehicle, animal, insect
- 0.0.4
  - Changed methods used to send DON so it's clear in the log
  - Fixed profile for Controller GV2 name
- 0.0.3
  - Fixed event passing, and receiving DON/DOF's in DetectedObject's
- 0.0.2
  - First working version
- 0.0.1
  - First release
