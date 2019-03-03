%define	major 2
%define libname %mklibname ilbc %{major}
%define libnamedev %mklibname ilbc -d

Summary:	Internet Low Bitrate Codec (iLBC) library
Name:		libilbc
Version:	2.0.2
Release:	2
License:	BSD-style
Group:		System/Libraries
URL:		https://github.com/dekkers/libilbc
Source0:	https://github.com/TimothyGu/libilbc/archive/v%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for robust
voice communication over IP. The codec is designed for narrow band speech and
results in a payload bit rate of 13.33 kbit/s with an encoding frame length of
30 ms and 15.20 kbps with an encoding length of 20 ms. The iLBC codec enables
graceful speech quality degradation in the case of lost frames, which occurs in
connection with lost or delayed IP packets.

%package -n	%{libname}
Summary:	Internet Low Bitrate Codec (iLBC) library
Group:          System/Libraries

%description -n	%{libname}
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for robust
voice communication over IP. The codec is designed for narrow band speech and
results in a payload bit rate of 13.33 kbit/s with an encoding frame length of
30 ms and 15.20 kbps with an encoding length of 20 ms. The iLBC codec enables
graceful speech quality degradation in the case of lost frames, which occurs in
connection with lost or delayed IP packets.

%package -n %{libnamedev}
Summary:	Development and header files for the iLBC library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for robust
voice communication over IP. The codec is designed for narrow band speech and
results in a payload bit rate of 13.33 kbit/s with an encoding frame length of
30 ms and 15.20 kbps with an encoding length of 20 ms. The iLBC codec enables
graceful speech quality degradation in the case of lost frames, which occurs in
connection with lost or delayed IP packets.

%prep

%setup -q
%if "%{_lib}" != "lib64"
# Let's not overreach ;)
sed -i -e 's,lib64,%{_lib},g' CMakeLists.txt
%endif

%build
%cmake -G Ninja
%ninja

%install
%ninja_install -C build

rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc COPYING
%{_libdir}/libilbc.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/ilbc.h
%{_libdir}/libilbc.so
%{_libdir}/pkgconfig/libilbc.pc
