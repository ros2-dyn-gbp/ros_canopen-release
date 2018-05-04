Name:           ros-kinetic-canopen-402
Version:        0.7.7
Release:        0%{?dist}
Summary:        ROS canopen_402 package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://wiki.ros.org/canopen_402
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-canopen-master
Requires:       ros-kinetic-class-loader
BuildRequires:  ros-kinetic-canopen-master
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-class-loader
BuildRequires:  ros-kinetic-rosunit

%description
This implements the CANopen device profile for drives and motion control. CiA(r)
402

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri May 04 2018 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.7-0
- Autogenerated by Bloom

* Wed Aug 30 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.6-0
- Autogenerated by Bloom

* Mon May 29 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.5-0
- Autogenerated by Bloom

* Wed Apr 26 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.4-0
- Autogenerated by Bloom

* Tue Mar 28 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.2-0
- Autogenerated by Bloom

* Mon Mar 20 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.1-0
- Autogenerated by Bloom

* Thu Dec 15 2016 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.0-0
- Autogenerated by Bloom

