%define	major 0
%define libname %mklibname ilbc %{major}
%define libnamedev %mklibname ilbc -d

Summary:	Internet Low Bitrate Codec (iLBC) library
Name:		libilbc
Version:	1.1.1
Release:	7
License:	BSD-style
Group:		System/Libraries
URL:		https://github.com/dekkers/libilbc
Source0:	libilbc-master.zip
BuildRequires:	autoconf automake libtool

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

%setup -q -n libilbc-master

%build
autoreconf -fi
%configure2_5x \
    --disable-static
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc COPYING README
%{_libdir}/libilbc.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/ilbc.h
%{_libdir}/libilbc.so
%{_libdir}/pkgconfig/libilbc.pc
