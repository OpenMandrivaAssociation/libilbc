%define	major 0
%define libname %mklibname ilbc %{major}
%define develname %mklibname ilbc -d

Summary:	Internet Low Bitrate Codec (iLBC) library
Name:		libilbc
Version:	0.6
Release:	%mkrel 8
License:	Freeware
Group:		System/Libraries
URL:		http://www.ilbcfreeware.org/
Source0:	ilbc-rfc3951.tar.bz2
Source1:	http://www.ietf.org/rfc/rfc3951.txt.bz2
Source2:	http://www.ilbcfreeware.org/documentation/extract-cfile.awk.bz2
Source3:	http://www.ilbcfreeware.org/documentation/gips_iLBClicense.pdf.bz2
Patch0:		libilbc-0.6-version.diff
BuildRequires:	gawk
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Static library and header files for the iLBC library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname ilbc -d 0}

%description -n	%{develname}
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for robust
voice communication over IP. The codec is designed for narrow band speech and
results in a payload bit rate of 13.33 kbit/s with an encoding frame length of
30 ms and 15.20 kbps with an encoding length of 20 ms. The iLBC codec enables
graceful speech quality degradation in the case of lost frames, which occurs in
connection with lost or delayed IP packets.

This package contains the static library and header files.

%prep

%setup -q -n ilbc-rfc3951
%patch0 -p0

# we well reconstruct the source instead...
pushd src
    rm -f *.[ch]
    bzcat %{SOURCE1} > rfc3951.txt
    bzcat %{SOURCE2} > extract-cfile.awk
    awk -f extract-cfile.awk rfc3951.txt
    # please teach me indent someday...
    perl -pi -e "s|^\ \ \ ||g" *.[ch]
popd

bzcat %{SOURCE3} > gips_iLBClicense.pdf

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --force --copy; aclocal; automake --add-missing --copy --foreign; autoconf

export CFLAGS="%{optflags} -Wall -fPIC -D_REENTRANT"
export LIBS="-lm"

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc gips_iLBClicense.pdf README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc src/rfc3951.txt src/extract-cfile.awk
%dir %{_includedir}/ilbc
%{_includedir}/ilbc/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
