AutoReqProv: no
%global debug_package %{nil}


Name:           ndi-sdk
Version:        5.0.10.1
Release:        1%{dist}
Summary:        NewTek NDI SDK

License:        Propietary distributable
URL:            https://www.newtek.com/ndi/sdk/
Source0: 	https://slepin.fr/obs-ndi/sdk/ndi-sdk-5.0.10.1-Linux.tar.gz 
#Source:	http://514f211588de67e4fdcf-437b8dd50f60b69cf0974b538e50585b.r63.cf1.rackcdn.com/Utilities/SDK/NDI_SDK_Linux_v2/InstallNDISDK_v4_Linux.tar.gz
Source1:	ndi.pc

BuildRequires:  tar
Requires:	libndi-sdk = %{version}-%{release}

%description
NewTek NDI SDK.

%package -n libndi-sdk
Summary:        Libraries files for %{name}


%description -n libndi-sdk
The libndi-sdk package contains libraries for %{name}.

#------------

%package devel
Summary:        Libraries/include files for %{name}
Requires:       %{name} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -c

_target_line="$(sed -n '/^__NDI_ARCHIVE_BEGIN__$/=' "Install_NDI_SDK_v5_Linux.sh")"
_target_line="$((_target_line + 1))"
tail -n +"$_target_line" "Install_NDI_SDK_v5_Linux.sh" | tar -zxvf -
mv -f "NDI SDK for Linux" NDI_SDK_for_Linux

%build


%install
pushd NDI_SDK_for_Linux
ls
install -dm 755 %{buildroot}/%{_bindir}
install -dm 755 %{buildroot}/%{_libdir}/pkgconfig
install -dm 755 %{buildroot}/%{_includedir}/%{name}
cp -rf bin/x86_64-linux-gnu/* %{buildroot}/%{_bindir}/
cp -rf include/* %{buildroot}/%{_includedir}/%{name}
cp -rf lib/x86_64-linux-gnu/* %{buildroot}/%{_libdir}/
cp -f %{S:1} %{buildroot}/%{_libdir}/pkgconfig/


%files 
%{_bindir}/ndi-*

%files -n libndi-sdk
%{_libdir}/libndi.so.*


%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/ndi.pc

%changelog

* Tue Feb 01 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> 5.0.10.1-1
- Updated to 5.0.10.1

* Tue Sep 01 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.5.1-1
- Initial build
