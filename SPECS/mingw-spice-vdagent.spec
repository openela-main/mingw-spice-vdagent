%{?mingw_package_header}
%global _hardened_build 1

#define _version_suffix -348f

Name:           mingw-spice-vdagent
Version:        0.9.0
Release:        3%{?dist}
Summary:        MinGW Windows SPICE guest agent

License:        GPLv2+
URL:            http://spice-space.org/
Source0:        vdagent-win-%{version}%{?_version_suffix}.tar.xz



Patch1:0001-Make-BitmapCoder-from_bitmap-return-a-BMP-file-forma.patch
Patch2:0002-imagetest-Save-PNG-file-using-a-helper-function.patch
Patch3:0003-imagetest-Save-BMP-file-using-BitmapCoder.patch
Patch4:0004-vdagent-Removed-unused-declaration.patch
Patch5:0005-Avoid-to-use-names-with-reserved-characters.patch
# do not apply patch6 + its revert -- do not touch Makefile.am
#Patch6:0006-Enable-some-security-options-on-output-executables.patch
#Patch7:0007-Revert-Enable-some-security-options-on-output-execut.patch
Patch8:0008-vcproj-Remove-reference-to-CxImage.patch
Patch9:0009-vcproj-Add-some-missing-files.patch
Patch10:0010-Fix-minor-compiler-compatibility.patch
Patch11:0011-Avoid-unused-variable-warning.patch
Patch12:0012-msi-Do-not-generate-deps.txt.patch
Patch13:0013-file_xfer-Remove-FileXferTask-structure-alignment.patch
Patch14:0014-file_xfer-Remove-too-C-syntax-for-C.patch
Patch15:0015-file_xfer-Use-destructor-for-FileXferTask.patch
Patch16:0016-file_xfer-Use-shared_ptr-to-simplify-memory-manageme.patch
Patch17:0017-vdagent-Fix-loss-of-mouse-movement-events.patch
Patch18:0018-Reuse-spice-protocol-macros-instead-of-defining-new-.patch
Patch19:0019-vdservice-Do-not-append-line-terminator-to-log.patch
Patch20:0020-Fix-some-minor-buffer-overflows-reading-registry-inf.patch
Patch21:0021-Use-enumeration-types.patch
Patch22:0022-Minimal-message-size-check.patch
Patch23:0023-Use-proper-type-for-_clipboard_owner.patch
Patch24:0024-Reduce-indentation-returning-earlier.patch
Patch25:0025-Minor-overflow-checks-improvements.patch
Patch26:0026-Replace-an-assert-with-proper-handling-code.patch
Patch27:0027-Use-std-unique_ptr-for-_desktop_layout.patch
Patch28:0028-Use-always-TCHAR-to-read-string-from-registry.patch
Patch29:0029-Factor-out-an-utility-function-to-read-strings-from-.patch
Patch30:0030-Allow-one-more-character-reading-strings-from-regist.patch
Patch31:0031-Allocate-_control_event-and-_stop_event-just-once.patch
Patch32:0032-Avoid-declaring-event_thread_id.patch
Patch33:0033-Avoid-declaring-_system_version-member.patch
Patch34:0034-Avoids-to-call-supported_system_version.patch
Patch35:0035-vdlog-Remove-the-lookup-table-for-log-types.patch
Patch36:0036-vdlog-Factor-our-a-logf-function-to-avoid-long-LOG-m.patch
Patch37:0037-vdlog-Use-GetLocalTime-instead-of-multiple-C-functio.patch
Patch38:0038-Use-proper-invalid-value-for-_vio_serial.patch
Patch39:0039-Introduce-an-helper-to-close-VirtIo-device.patch
Patch40:0040-Use-destructor-instead-of-cleanup-function.patch
Patch41:0041-vdagent-Stop-correctly-helper-thread.patch
Patch42:0042-vdagent-Add-a-comment-around-WinSta0_DesktopSwitch-e.patch
Patch43:0043-Use-GetModuleHandle-to-get-some-functions-from-user3.patch

BuildRequires:  mingw32-filesystem >= 23
BuildRequires:  mingw64-filesystem >= 23
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-libpng-static
BuildRequires:  mingw64-libpng-static
BuildRequires:  mingw32-winpthreads-static
BuildRequires:  mingw64-winpthreads-static
BuildRequires:  mingw32-zlib-static
BuildRequires:  mingw64-zlib-static
BuildRequires:  pkgconfig
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw64-pkg-config
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  autoconf-archive

BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64

%package -n mingw32-spice-vdagent
Summary:        MinGW Windows SPICE guest agent

%package -n mingw64-spice-vdagent
Summary:        MinGW Windows SPICE guest agent

%description
Spice agent for Windows guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput.
* Automatic adjustment of the Windows desktop resolution to the client resolution
* Support of copy and paste (text and images) between the active Windows
  session and the client

%description -n mingw32-spice-vdagent
Spice agent for Windows guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput.
* Automatic adjustment of the Windows desktop resolution to the client resolution
* Support of copy and paste (text and images) between the active Windows
  session and the client

%description -n mingw64-spice-vdagent
Spice agent for Windows guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput.
* Automatic adjustment of the Windows desktop resolution to the client resolution
* Support of copy and paste (text and images) between the active Windows
  session and the client

%{mingw_debug_package}

%prep
%setup -q -n vdagent-win-%{version}%{?_version_suffix}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
#%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1

# --- autoreconf ---
# Without autoreconf it fails.
# Update configure.ac with the version and run autoreconf.
# build-aux/git-version-gen is currently not available in the tarball
# so use sed instead.
sed -i "s/^AC_INIT.*/AC_INIT(vdagent-win, [%{version}])/" configure.ac
sed -i "/m4_esyscmd.*build-aux.git-version-gen .tarball-version/d" configure.ac

autoreconf -fi
# --- autoreconf --- done

%build

%mingw_configure --verbose --enable-debug

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

%files -n mingw32-spice-vdagent
%defattr(-,root,root)
%{mingw32_bindir}/vdagent.exe
%{mingw32_bindir}/vdservice.exe

%files -n mingw64-spice-vdagent
%defattr(-,root,root)
%{mingw64_bindir}/vdagent.exe
%{mingw64_bindir}/vdservice.exe

%changelog
* Tue Aug 22 2017 Uri Lublin <uril@redhat.com> - 0.9.0-3
- First build for RHEL-8.0
  Related: rhbz#1557012
