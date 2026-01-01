%global commit 816616b
%global datetimever 202601010204816616b

Name: monado-constellation
Version: 202601010204816616b
Release: 1%{?dist}
Summary: Monado - XR Runtime (XRT) with WMR & Rift S controller tracking

License: bsl-1.0
URL: https://gitlab.freedesktop.org/thaytan/monado.git
Source0: https://gitlab.freedesktop.org/thaytan/monado/-/archive/%{commit}/monado-%{commit}.tar.gz

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

Conflicts: monado

%description
Monado is an open source XR runtime delivering immersive experiences such as VR
and AR on on mobile, PC/desktop, and any other device
(because gosh darn people come up with a lot of weird hardware).
Monado aims to be a complete and conforming implementation of the OpenXR API made by Khronos.
The project currently is being developed for GNU/Linux and aims to support other operating
systems in the near future.
"Monado" has no specific meaning and is just a name.
This version enables positional tracking for WMR controllers in full 6dof. Includes Rift S support & controllers.

%prep
%autosetup -n monado-%{commit}

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
* Thu Jan 01 2026 GitHub Actions <actions@github.com> - 202601010204816616b-1
- Auto-update to Monado commit 816616b

* Sun Sep 28 2025 GitHub Actions <actions@github.com> - 202509280146b71ebcd-1
- Auto-update to Monado commit b71ebcd

* Sat Sep 27 2025 GitHub Actions <actions@github.com> - 202509270126d958cd4-1
- Auto-update to Monado commit d958cd4

* Wed Sep 24 2025 GitHub Actions <actions@github.com> - 202509240138cecd026-1
- Auto-update to Monado commit cecd026

* Mon Aug 04 2025 GitHub Actions <actions@github.com> - 2025080402070da47fb-1
- Auto-update to Monado commit 0da47fb

* Sat Aug 02 2025 GitHub Actions <actions@github.com> - 20250802015344e9356-1
- Auto-update to Monado commit 44e9356

* Wed Jul 30 2025 GitHub Actions <actions@github.com> - 202507300159e5c6cd7-1
- Auto-update to Monado commit e5c6cd7

* Fri Jul 18 2025 GitHub Actions <actions@github.com> - 20250718103509ddc28-1
- Auto-update to Monado commit 09ddc28

%autochangelog
