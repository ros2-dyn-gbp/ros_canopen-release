Name:           ros-lunar-canopen-motor-node
Version:        0.7.8
Release:        0%{?dist}
Summary:        ROS canopen_motor_node package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://wiki.ros.org/canopen_motor_node
Source0:        %{name}-%{version}.tar.gz

Requires:       muParser-devel
Requires:       ros-lunar-canopen-402
Requires:       ros-lunar-canopen-chain-node
Requires:       ros-lunar-canopen-master
Requires:       ros-lunar-controller-manager
Requires:       ros-lunar-controller-manager-msgs
Requires:       ros-lunar-filters
Requires:       ros-lunar-hardware-interface
Requires:       ros-lunar-joint-limits-interface
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-urdf
BuildRequires:  muParser-devel
BuildRequires:  ros-lunar-canopen-402
BuildRequires:  ros-lunar-canopen-chain-node
BuildRequires:  ros-lunar-canopen-master
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-controller-manager
BuildRequires:  ros-lunar-controller-manager-msgs
BuildRequires:  ros-lunar-filters
BuildRequires:  ros-lunar-hardware-interface
BuildRequires:  ros-lunar-joint-limits-interface
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rosunit
BuildRequires:  ros-lunar-urdf

%description
canopen_chain_node specialization for handling of canopen_402 motor devices. It
facilitates interface abstraction with ros_control.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri May 04 2018 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.8-0
- Autogenerated by Bloom

* Fri May 04 2018 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.7-0
- Autogenerated by Bloom

* Wed Aug 30 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.6-0
- Autogenerated by Bloom

* Mon May 29 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.5-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.4-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.3-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.2-0
- Autogenerated by Bloom

