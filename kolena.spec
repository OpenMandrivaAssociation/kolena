Name:          kolena
Version:       0.1.1
Release:       %mkrel 1
Summary:       Kolena is a KDE wrapper around the Olena image library which extracts text from images
Group:         Networking/File transfer
License:       GPLv2+
Url:           http://quickgit.kde.org/?p=kolena.git
Source0:       %{name}-%{version}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: tesseract-devel

%description
Kolena is a KDE wrapper around the Olena image library which extracts text from images.

#-------------------------------------------------------------------------

%define kolena_major 0
%define libkolena %mklibname kolena %kolena_major

%package -n %libkolena
Summary:    Ktorrent libbrary
Group:      System/Libraries

%description -n %libkolena
KTorrent library.

%files -n %libkolena
%defattr(-,root,root)
%_kde_libdir/libkolena.so.%{kolena_major}*

#-------------------------------------------------------------------------

%package devel
Summary: Ktorrent plugin devel headers
Group: Networking/File transfer
Requires: %{libkolena} = %{version}

%description devel
Ktorrent plugin devel headers.

%files devel
%defattr(-,root,root)
%_kde_datadir/cmake/Kolena
%_kde_includedir/kolena
%_kde_libdir/libkolena.so

#-------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4 
%make
 
%install
rm -rf %buildroot
%makeinstall_std -C build

