# LinuxCNC-Yalang-yl620-VFD-rs485-Modbus
# About
This repository should help users with the [Modbus RS485](https://en.wikipedia.org/wiki/RS-485) communication of a Yalang YL620 Variable Frequency Drive VFD and the integration in [LinuxCNC](http://linuxcnc.org/). Some more information is based in the [LinuxCNC Forum](https://forum.linuxcnc.org/24-hal-components/39128-yalang-yl620-vfd-rs485-modbus-communicaiton?start=0).

It is based on [vfdmod](https://github.com/aekhv/vfdmod).
The plan is that this repository will provide you with:
-   The [vfdmod](https://github.com/aekhv/vfdmod) config file.
-   The necessary [HAL](http://linuxcnc.org/docs/2.8/html/hal/intro.html) file for [LinuxCNC](http://linuxcnc.org/).
-   A [PyVCP](http://linuxcnc.org/docs/2.8/html/gui/pyvcp.html) file for the [Axis Ui](http://linuxcnc.org/docs/2.8/html/gui/axis.html). 


# Roadmap
- [X] Create the repository.
- [X] Get the basic communication running. (Start, Stop, Direction, Speed) :tada:
- [X] Have a a basic [PyVCP](http://linuxcnc.org/docs/2.8/html/gui/pyvcp.html). 
- [ ] Translate the Yalang [YL620 Modbus Manual](Modbus.docx) from Chinese to English. (partly done)
- [ ] Read out feedback registers (Voltage, Current,...).
- [ ] Read out the parameter registers.
- [ ] Display Parameter registers in a Axis Tab.
- [ ] Integrate a drop down setting for each parameter in the Axis Tab.

# Changelog
02. November 2021 Repository created
