Name:		kolena
Version:	0.1.1
Release:	2
Summary:	A KDE wrapper around the Olena image library which extracts text from images
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://quickgit.kde.org/?p=kolena.git
Source0:	%{name}-%{version}.tar.bz2
Patch0:		kolena-0.1.1-tesseract-3.01.patch
Patch1:		kolena-0.1.1-gcc4.7.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	tesseract-devel

%description
Kolena is a KDE wrapper around the Olena image library which extracts
text from images.

#-------------------------------------------------------------------------

%define kolena_major 0
%define libkolena %mklibname kolena %{kolena_major}

%package -n %{libkolena}
Summary:	Kolena libbrary
Group:		System/Libraries

%description -n %{libkolena}
Kolena library.

%files -n %{libkolena}
%{_kde_libdir}/libkolena.so.%{kolena_major}*

#-------------------------------------------------------------------------

%package devel
Summary:	Kolena plugin devel headers
Group:		Networking/File transfer
Requires:	%{libkolena} = %{version}

%description devel
Kolena plugin devel headers.

%files devel
%{_kde_datadir}/cmake/Kolena
%{_kde_includedir}/kolena
%{_kde_libdir}/libkolena.so

#-------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

