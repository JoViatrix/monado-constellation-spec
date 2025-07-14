Name: monado
Version: 1d37e1d
Release: %autorelease
Summary: Monado - XR Runtime (XRT)

License: bsl-1.0
URL: https://monado.freedesktop.org/
Source0: https://gitlab.freedesktop.org/monado/monado/-/archive/%{version}/monado-%{version}.tar.gz

BuildRequires: cmake >= 3.13
BuildRequires: gcc-c++
BuildRequires: python3 >= 3.6
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(eigen3)
BuildRequires: mesa-libGL-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(openhmd) >= 0.3.0
BuildRequires: pkgconfig(opencv)
BuildRequires: pkgconfig(libuvc)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(realsense2)
BuildRequires: pkgconfig(libcjson)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libonnxruntime)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: glslc
BuildRequires: pkgconfig(glslang)
BuildRequires: hidapi-devel
BuildRequires: libv4l-devel
BuildRequires: libsurvive-devel
BuildRequires: pkgconfig(percetto)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(openvr)
BuildRequires: dbus-devel
BuildRequires: libbsd-devel

Requires: opencv-videoio >= 4.11.0
Requires: basalt-monado

%description
Monado is an open source XR runtime delivering immersive experiences such as VR
and AR on on mobile, PC/desktop, and any other device
(because gosh darn people come up with a lot of weird hardware).
Monado aims to be a complete and conforming implementation of the OpenXR API made by Khronos.
The project currently is being developed for GNU/Linux and aims to support other operating
systems in the near future.
"Monado" has no specific meaning and is just a name.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DBUILD_DOC:BOOL=OFF
%cmake_build

%install
%cmake_install


%check


%files
%license
%doc

%dir %{_includedir}/monado
%dir %{_datadir}/openxr
%dir %{_datadir}/steamvr-monado

/usr/lib/systemd/user/monado.service
/usr/lib/systemd/user/monado.socket

%{_bindir}/monado-cli
%{_bindir}/monado-ctl
%{_bindir}/monado-service
%{_bindir}/monado-gui

%{_includedir}/monado/*

%{_libdir}/libmonado.so*
%{_libdir}/libopenxr_monado.so

%{_datadir}/openxr/*
%{_datadir}/steamvr-monado/*


%changelog
%autochangelog
