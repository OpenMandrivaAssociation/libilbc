%define	major 0
%define libname %mklibname ilbc %{major}
%define develname %mklibname ilbc -d

Summary:	Internet Low Bitrate Codec (iLBC) library
Name:		libilbc
Version:	0.6
Release:	9
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
%makeinstall_std

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


%changelog
* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-8mdv2011.0
+ Revision: 627787
- don't force the usage of automake1.7

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-7mdv2011.0
+ Revision: 620142
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.6-6mdv2010.0
+ Revision: 429766
- rebuild

* Wed Jun 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6-5mdv2009.0
+ Revision: 225555
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 23 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6-4mdv2009.0
+ Revision: 210388
- fix build
- fix devel package naming

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.6-3mdv2008.1
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6-3mdv2007.0
+ Revision: 94085
- don't use autoheader
- Import libilbc

* Thu Aug 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6-1mdv2007.0
- rebuild

* Mon Feb 13 2006 Oden Eriksson <oeriksson@mandrakesoft.com> 0.6-2mdk
- use autofoo from the linphone project, but keep the code generation

* Sun Mar 13 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.6-1mdk
- 0.6 (final rfc3951)
- use the %%mkrel macro
- new S1 and S2

* Mon Sep 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- initial mandrake package

