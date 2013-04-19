%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.20-1
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Kurdish
%define languagecode ku
%define lc_ctype ku_TR

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.20.1
Release:       1
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* 

%files
%doc README* Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-10mdv2011.0
+ Revision: 662843
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-9mdv2011.0
+ Revision: 603410
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-8mdv2010.1
+ Revision: 518936
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-7mdv2010.0
+ Revision: 413079
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.12.0-6mdv2009.1
+ Revision: 350042
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.12.0-5mdv2009.0
+ Revision: 220391
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.12.0-4mdv2008.1
+ Revision: 182479
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.12.0-3mdv2008.1
+ Revision: 148804
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-2mdv2007.0
+ Revision: 123283
- Import aspell-ku

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.12.0-1mdk
- first version

